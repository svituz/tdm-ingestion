import importlib
import logging
from abc import abstractmethod, ABC
from datetime import timedelta, datetime
from enum import Enum
from typing import Tuple


logger = logging.getLogger(__name__)


def import_class(class_path: str):
    class_path_splitted = class_path.split('.')
    module = '.'.join(class_path_splitted[:-1])
    cls = class_path_splitted[-1]

    logger.debug('importing  class %s  from %s', cls, module)
    return getattr(importlib.import_module(module), cls)


class TimeDelta(Enum):
    one_hour = timedelta(hours=1)
    one_day = timedelta(days=1)

    def get_before_after(self, time: datetime = None) -> Tuple[
        datetime, datetime]:
        now = time or datetime.utcnow()
        if self == TimeDelta.one_hour:
            after = (now - TimeDelta.one_hour.value).replace(
                minute=0,
                second=0,
                microsecond=0)
            before = after + timedelta(minutes=59, seconds=59,
                                       microseconds=999999)
        else:
            after = (now - TimeDelta.one_day.value).replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0)
            before = after + timedelta(
                hours=23, minutes=59, seconds=59,
                microseconds=999999)
        return before, after


class Formatter(ABC):
    @abstractmethod
    def format(self, name):
        pass


class DateTimeFormatter(Formatter):
    def __init__(self, time_delta: timedelta = None):
        self.time_delta = time_delta or timedelta()

    def format(self, name):
        return (datetime.now() - self.time_delta).strftime(name)
