# -*- coding: utf-8 -*-
from sqlalchemy import PrimaryKeyConstraint, Column, DateTime, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = "USD_exchange_rates"
    __table_args__ = (
        PrimaryKeyConstraint("date", "provider"),
    )

    date = Column(DateTime)
    provider = Column(String)
    AED = Column(DECIMAL)
    AFN = Column(DECIMAL)
    ALL = Column(DECIMAL)
    AMD = Column(DECIMAL)
    ANG = Column(DECIMAL)
    AOA = Column(DECIMAL)
    ARS = Column(DECIMAL)
    ATS = Column(DECIMAL)
    AUD = Column(DECIMAL)
    AWG = Column(DECIMAL)
    AZN = Column(DECIMAL)
    BAM = Column(DECIMAL)
    BBD = Column(DECIMAL)
    BDT = Column(DECIMAL)
    BEF = Column(DECIMAL)
    BGN = Column(DECIMAL)
    BHD = Column(DECIMAL)
    BIF = Column(DECIMAL)
    BMD = Column(DECIMAL)
    BND = Column(DECIMAL)
    BOB = Column(DECIMAL)
    BRL = Column(DECIMAL)
    BSD = Column(DECIMAL)
    BTC = Column(DECIMAL)
    BTN = Column(DECIMAL)
    BWP = Column(DECIMAL)
    BYR = Column(DECIMAL)
    BZD = Column(DECIMAL)
    CAD = Column(DECIMAL)
    CDF = Column(DECIMAL)
    CHF = Column(DECIMAL)
    CLF = Column(DECIMAL)
    CLP = Column(DECIMAL)
    CNH = Column(DECIMAL)
    CNY = Column(DECIMAL)
    COP = Column(DECIMAL)
    CRC = Column(DECIMAL)
    CUC = Column(DECIMAL)
    CUP = Column(DECIMAL)
    CVE = Column(DECIMAL)
    CYP = Column(DECIMAL)
    CZK = Column(DECIMAL)
    DEM = Column(DECIMAL)
    DJF = Column(DECIMAL)
    DKK = Column(DECIMAL)
    DOP = Column(DECIMAL)
    DZD = Column(DECIMAL)
    EEK = Column(DECIMAL)
    EGP = Column(DECIMAL)
    ERN = Column(DECIMAL)
    ESP = Column(DECIMAL)
    ETB = Column(DECIMAL)
    EUR = Column(DECIMAL)
    FIM = Column(DECIMAL)
    FJD = Column(DECIMAL)
    FKP = Column(DECIMAL)
    FRF = Column(DECIMAL)
    GBP = Column(DECIMAL)
    GEL = Column(DECIMAL)
    GGP = Column(DECIMAL)
    GHS = Column(DECIMAL)
    GIP = Column(DECIMAL)
    GMD = Column(DECIMAL)
    GNF = Column(DECIMAL)
    GRD = Column(DECIMAL)
    GTQ = Column(DECIMAL)
    GYD = Column(DECIMAL)
    HKD = Column(DECIMAL)
    HNL = Column(DECIMAL)
    HRK = Column(DECIMAL)
    HTG = Column(DECIMAL)
    HUF = Column(DECIMAL)
    IDR = Column(DECIMAL)
    IEP = Column(DECIMAL)
    ILS = Column(DECIMAL)
    IMP = Column(DECIMAL)
    INR = Column(DECIMAL)
    IQD = Column(DECIMAL)
    IRR = Column(DECIMAL)
    ISK = Column(DECIMAL)
    ITL = Column(DECIMAL)
    JEP = Column(DECIMAL)
    JMD = Column(DECIMAL)
    JOD = Column(DECIMAL)
    JPY = Column(DECIMAL)
    KES = Column(DECIMAL)
    KGS = Column(DECIMAL)
    KHR = Column(DECIMAL)
    KMF = Column(DECIMAL)
    KPW = Column(DECIMAL)
    KRW = Column(DECIMAL)
    KWD = Column(DECIMAL)
    KYD = Column(DECIMAL)
    KZT = Column(DECIMAL)
    LAK = Column(DECIMAL)
    LBP = Column(DECIMAL)
    LKR = Column(DECIMAL)
    LRD = Column(DECIMAL)
    LSL = Column(DECIMAL)
    LTL = Column(DECIMAL)
    LUF = Column(DECIMAL)
    LVL = Column(DECIMAL)
    LYD = Column(DECIMAL)
    MAD = Column(DECIMAL)
    MCF = Column(DECIMAL)
    MDL = Column(DECIMAL)
    MGA = Column(DECIMAL)
    MKD = Column(DECIMAL)
    MMK = Column(DECIMAL)
    MNT = Column(DECIMAL)
    MOP = Column(DECIMAL)
    MRO = Column(DECIMAL)
    MTL = Column(DECIMAL)
    MUR = Column(DECIMAL)
    MVR = Column(DECIMAL)
    MWK = Column(DECIMAL)
    MXN = Column(DECIMAL)
    MYR = Column(DECIMAL)
    MZN = Column(DECIMAL)
    NAD = Column(DECIMAL)
    NGN = Column(DECIMAL)
    NIO = Column(DECIMAL)
    NLG = Column(DECIMAL)
    NOK = Column(DECIMAL)
    NPR = Column(DECIMAL)
    NZD = Column(DECIMAL)
    OMR = Column(DECIMAL)
    PAB = Column(DECIMAL)
    PEN = Column(DECIMAL)
    PGK = Column(DECIMAL)
    PHP = Column(DECIMAL)
    PKR = Column(DECIMAL)
    PLN = Column(DECIMAL)
    PTE = Column(DECIMAL)
    PYG = Column(DECIMAL)
    QAR = Column(DECIMAL)
    RON = Column(DECIMAL)
    RSD = Column(DECIMAL)
    RUB = Column(DECIMAL)
    RWF = Column(DECIMAL)
    SAR = Column(DECIMAL)
    SBD = Column(DECIMAL)
    SCR = Column(DECIMAL)
    SDG = Column(DECIMAL)
    SEK = Column(DECIMAL)
    SGD = Column(DECIMAL)
    SHP = Column(DECIMAL)
    SIT = Column(DECIMAL)
    SKK = Column(DECIMAL)
    SLL = Column(DECIMAL)
    SML = Column(DECIMAL)
    SOS = Column(DECIMAL)
    SRD = Column(DECIMAL)
    STD = Column(DECIMAL)
    SVC = Column(DECIMAL)
    SYP = Column(DECIMAL)
    SZL = Column(DECIMAL)
    THB = Column(DECIMAL)
    TJS = Column(DECIMAL)
    TMT = Column(DECIMAL)
    TND = Column(DECIMAL)
    TOP = Column(DECIMAL)
    TRY = Column(DECIMAL)
    TTD = Column(DECIMAL)
    TWD = Column(DECIMAL)
    TZS = Column(DECIMAL)
    UAH = Column(DECIMAL)
    UGX = Column(DECIMAL)
    USD = Column(DECIMAL)
    UYU = Column(DECIMAL)
    UZS = Column(DECIMAL)
    VAL = Column(DECIMAL)
    VEB = Column(DECIMAL)
    VEF = Column(DECIMAL)
    VND = Column(DECIMAL)
    VUV = Column(DECIMAL)
    WST = Column(DECIMAL)
    XAF = Column(DECIMAL)
    XAG = Column(DECIMAL)
    XAU = Column(DECIMAL)
    XCD = Column(DECIMAL)
    XCP = Column(DECIMAL)
    XDR = Column(DECIMAL)
    XOF = Column(DECIMAL)
    XPD = Column(DECIMAL)
    XPF = Column(DECIMAL)
    XPT = Column(DECIMAL)
    YER = Column(DECIMAL)
    ZAR = Column(DECIMAL)
    ZMK = Column(DECIMAL)
    ZMW = Column(DECIMAL)
    ZWL = Column(DECIMAL)

    @staticmethod
    def currencies():
        return [a for a in dir(ExchangeRate) if a.isupper()]