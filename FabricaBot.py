import random as r
import sys

class FabricaBot:
    def __init__(self):
        self.__construtor_bot = {}
        self.__construtor_args = {}

    def registrar_tipo_bot(self,tipo,construtor, url):
        self.__construtor_bot[tipo] = construtor
        self.__construtor_args[tipo] = url
    
    def lista_tipo_bots(self):
        return self.__construtor_bot.keys()
    
    def get_bot(self,tipo):
        construtor = self.__construtor_bot.get(tipo)
        url = self.__construtor_args.get(tipo)
        if not construtor:
            raise ValueError(tipo)
        return construtor(url)

