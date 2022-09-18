#!/bin/env python
from typing import List
from abc import ABC, abstractmethod
from pizza_ingredient_factory import Dough, NyStylePizzaIngredient


class Pizza(ABC):
    def __init__(self):
        self._name = ''
        self._dough: Dough = None  # type: ignore
        self._sauce = ''
        self._toppings: List[str] = []

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print('bake in 175 degree for 25 minutes')

    def cut(self):
        print('cut in half')

    def box(self):
        print('put that in the box')

    def get_name(self) -> str:
        return self._name


class NystylePizza(Pizza):
    def __init__(self):
        super().__init__()

    def prepare(self):
        f = NyStylePizzaIngredient()
        self._name = 'New York style cheese pizza'
        self._dough = f.create_dough()
        self._sauce = 'tomato sauce'
        self._toppings.extend(['cheese', 'olive'])

    def cut(self):
        print('cut in rectangle')
