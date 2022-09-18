#!/bin/env python
from typing import List


class Pizza:
    def __init__(self):
        self._name = ''
        self._dough = ''
        self._sauce = ''
        self._toppings: List[str] = []

    def prepare(self):
        print(f'prepare start {self._name}')
        print(f'roll dough {self._dough}')
        print(f'add sauce {self._sauce}')
        print('put toppings')
        for topping in self._toppings:
            print(f'topping: {topping}')

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
        self._name = 'New York style cheese pizza'
        self._dough = 'thin cust dough'
        self._sauce = 'tomato sauce'
        self._toppings.extend(['cheese', 'olive'])

    def cut(self):
        print('cut in rectangle')
