import random

class Comando:
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__msg = msg
        self.__respostas = respostas

    def id(self):
        return self.__id

    def mensagem(self):
        return self.__msg

    def addResposta(self, resposta):
        self.__respostas.append(resposta)
    
    def delResposta(self, resposta):
        self.__respostas.remove(resposta)

    def getRandomResposta(self):
        return random.choice(self.__respostas)