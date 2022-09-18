#!/bin/env python
from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class CrustDough(Dough):
    def name(self) -> str:
        return 'crust dough'


# interface
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        raise NotImplementedError


class NyStylePizzaIngredient(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return CrustDough()
