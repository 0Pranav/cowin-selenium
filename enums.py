import enum

class VaccineType(enum.Enum):
    Covishield = 1
    Covaxin = 2
    Any = 3

class PaidType(enum.Enum):
    Paid = 1
    Free = 2
    Any = 3

class AgeType(enum.Enum):
    MoreThanFortyFive = 1
    MoreThanEighteen = 2