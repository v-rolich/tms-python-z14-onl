# Реализовать интерфейсы: Feline(), Canine()
from abc import ABC, abstractmethod


class Feline(ABC):
    @abstractmethod
    def __init__(self, f_atr, s_atr):
        self.f_atr = f_atr
        self.s_atr = s_atr
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def __init__(self, f_atr, s_atr):
        self.f_atr = f_atr
        self.s_atr = s_atr
        raise NotImplementedError
