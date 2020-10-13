import random as r
import sys
from Bot import Bot
import requests
import json
from Comando import Comando

class BotZangado(Bot):
    def __init__(self, urlComandos ):
        self.__urlComandos = urlComandos;
        
        res = requests.get(self.__urlComandos)
        dados = json.loads(res.content)[0]
        self.__nome = dados["nome"]
        comandosJSON = dados["comandos"]

        self.__comandos = self.criaComandos(comandosJSON);


    def criaComandos(self, comandosJSON):
        mapa = {}
        for cmd in comandosJSON:
            c = Comando(cmd["id"], cmd["mensagem"], cmd["respostas"])
            mapa[cmd["id"]] = c
        return mapa

    def nome(self):
        return self.__nome

    def apresentacao(self):
        return f"Grrrrrr. Meu nome é {self.__nome} e eu te odeio!"

    def mostra_comandos(self):
        cmd=""
        for comando in self.__comandos.values(): 
            cmd += f"{comando.id()} - {comando.mensagem()}\n"
        return cmd
    
    def executa_comando(self,cmd):
        try:
            cmd = int(cmd)
        except:
            resposta="Quer me sacanear, espertinho?"
        else:
            if cmd not in self.__comandos.keys():
                resposta="Eu sei lá o que você quer de mim sua besta!"
            else:
                msg = self.__comandos[cmd].mensagem()
                res = self.__comandos[cmd].getRandomResposta()

                resposta=f"Você disse '{msg}' \n --> Eu te respondo: '{res}'"

        return resposta

    def boas_vindas(self):
        return "Eu não posso acreditar que você me escolheu, GRRRRRR!"

    def despedida(self):
        return "FINALMENTE, é o dia mais feliz da minha vida. ADEUS!"
