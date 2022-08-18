from datetime import datetime
from dataclasses import dataclass


@dataclass
class Fcast:
    timestamp: datetime = None
    fcast_date: datetime = None
    origin_date: datetime = None
    bound: str = ""
    temp: float = 0

    def date_diff(self):
        return (self.fcast_date - self.origin_date).days


@dataclass
class Actual:
    timestamp: datetime = None
    actual_date: datetime = None
    high_temp: float = 0
    low_temp: float = 0

    def mk_data_str(self):
        data_str = []
        data_str.append(self.actual_date)
        data_str.append(self.high_temp)
        data_str.append(self.low_temp)
        return data_str
