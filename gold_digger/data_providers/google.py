from ._provider import Provider
from bs4 import BeautifulSoup
from datetime import date


class Google(Provider):
    """Simple API for currency conversion."""

    BASE_URL = 'https://www.google.com/finance/converter'
    BASE_CURRENCY = "USD"
    name = 'google'

    def get_all_by_date(self, date_of_exchange, currencies):
        if date_of_exchange == date.today():
            rates = {}
            for c in currencies:
                date_str = date_of_exchange.strftime(format="%Y-%m-%d")
                self.logger.debug("Requesting Google for %s (%s)", c, date_str,
                                  extra={"currency": c, "date": date_str})

                rates[c] = self._convert_value(1, c)
            return rates

    def get_by_date(self, date_of_exchange, currency):
        date_str = date_of_exchange.strftime(format="%Y-%m-%d")
        self.logger.debug("Requesting Google for %s (%s)", currency, date_str,
                          extra={"currency": currency, "date": date_str})

        if date_of_exchange == date.today():
            return self._convert_value(1, currency)

    def _convert_value(self, value, currency):
        response = self._get('{}?a={}&from={}&to={}').format(self.BASE_URL, value, self.BASE_CURRENCY, currency)
        if not response:
            self.logger.warning("Google error. Status: %s", response.status_code,
                                extra={"currency": currency, "value": value})
            return None
        parsed_html = BeautifulSoup(response.text)
        res = parsed_html.body.find('span', attrs={'class': 'bld'}).text.split(' ')
        return self._to_decimal(res[0], currency) if value is not None else None

    def get_historical(self, origin_date, currencies):
        return {}

    def __str__(self):
        return self.name