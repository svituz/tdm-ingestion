from abc import ABC, abstractmethod
from typing import List, Dict

from tdm_ingestion.models import SensorType, Sensor, TimeSeries


class Client(ABC):
    class NotFound(Exception):
        pass

    @abstractmethod
    def create_entity_types(self,
                            sensor_types: List[SensorType]) -> List[str]:
        pass

    @abstractmethod
    def create_sources(self, sensors: List[Sensor]) -> List[str]:
        pass

    @abstractmethod
    def create_time_series(self, time_series: List[TimeSeries]):
        pass

    @abstractmethod
    def get_entity_types(self, _id: str = None,
                         query: Dict = None) -> SensorType:
        pass

    @abstractmethod
    def get_sources(self, _id: str = None, query: Dict = None) -> Sensor:
        pass

    @abstractmethod
    def sources_count(self, query: Dict) -> int:
        pass

    @abstractmethod
    def entity_types_count(self, query: Dict) -> int:
        pass
