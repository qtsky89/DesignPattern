#!/bin/env python
import sys
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(temperature: float, humidity: float, pressure: float):
        raise NotImplementedError

class Subject(ABC):
    @abstractmethod
    def register_observer(self, o :Observer):
        raise NotImplementedError
    
    @abstractmethod
    def remove_observer(self, o: Observer):
        raise NotImplementedError
    
    @abstractmethod
    def notify_observers():
        raise NotImplementedError

class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self.__observers: List[Observer] = []
        self.__temperature: float = 0
        self.__humidity: float = 0
        self.__pressure: float = 0
        
    
    def register_observer(self, o: Observer):
        self.__observers.append(o)
    
    def remove_observer(self, o: Observer):
        self.__observers.remove(o)
    
    def notify_observer(self):
        for o in self.__observers:
            o.update(self.__temperature, self.__humidity, self.__pressure)
    
    def set_mesasurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.notify_observers()

def main(argv):
    print('hello world')
    

if __name__ == '__main__':
    main(sys.argv[1:])
