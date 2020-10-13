from BotZangado import BotZangado
from FabricaBot import FabricaBot
from SistemaChatbot import SistemaChatBot
import random as rand

fabrica = FabricaBot()
fabrica.registrar_tipo_bot("BotZangado", BotZangado, "https://raw.githubusercontent.com/grellert/jsonbin/master/botzangado.json")

lista_bots = []
for tipo_bot in list(fabrica.lista_tipo_bots()):
    lista_bots.append(fabrica.get_bot(tipo_bot))

sys = SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()