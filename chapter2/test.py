#!/bin/env python
import sys
from abc import ABC, abstractmethod
from typing import List


# interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        raise NotImplementedError


# interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, o: Observer):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, o: Observer):
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self):
        raise NotImplementedError


# interface
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
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

    def notify_observers(self):
        for o in self.__observers:
            o.update(self.__temperature, self.__humidity, self.__pressure)

    def set_mesasurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.notify_observers()


class CurrentConditionDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        Observer.__init__(self)
        DisplayElement.__init__(self)

        self.__temperature: float = 0
        self.__humidity: float = 0

        self.__weather_data = weather_data
        self.__weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.display()

    def display(self):
        print(f'temperature: {self.__temperature}, humidity: {self.__humidity}')


def main(argv):
    weather_data = WeatherData()

    CurrentConditionDisplay(weather_data)

    weather_data.set_mesasurements(80, 65, 30.4)
    weather_data.set_mesasurements(82, 70, 29.2)
    weather_data.set_mesasurements(78, 90, 29.2)


if __name__ == '__main__':
    main(sys.argv[1:])
