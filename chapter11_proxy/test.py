#!/bin/env python

# https://velog.io/@newtownboy/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-%ED%94%84%EB%A1%9D%EC%8B%9C%ED%8C%A8%ED%84%B4Proxy-Pattern
from abc import ABCMeta, abstractmethod


class Image(metaclass=ABCMeta):
    @abstractmethod
    def display_image(self):
        raise NotImplementedError


class RealImage(Image):
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def display_image(self):
        print(f'show {self.__file_name}')


class ProxyImage(Image):
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__real_image: RealImage = None

    def display_image(self):
        if self.__real_image is None:
            self.__real_image = RealImage(self.__file_name)

        self.__real_image.display_image()


def main():
    p = ProxyImage('hoy')
    p.display_image()


if __name__ == '__main__':
    main()
