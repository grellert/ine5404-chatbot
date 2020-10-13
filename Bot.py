from abc import ABC, abstractmethod
import random as r
import sys

class Bot(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
