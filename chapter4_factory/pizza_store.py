#!/bin/env python
from abc import ABC, abstractmethod
from pizza import NystylePizza, Pizza


class PizzaStore(ABC):
    def orderPizza(self, type: str):
        p = self._createPizza(type)

        p.prepare()
        p.bake()
        p.cut()
        p.box()

        return p

    @abstractmethod
    def _createPizza(self, type: str) -> Pizza:
        raise NotImplementedError


class NyStylePizzaStore(PizzaStore):
    def _createPizza(self, type: str) -> Pizza:
        return NystylePizza()
