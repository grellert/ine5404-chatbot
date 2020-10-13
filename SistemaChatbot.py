from Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise ValueError(f"Objeto {bot} na lista de bots fornecida não é do tipo Bot")
        self.__lista_bots=lista_bots
        self.__bot = None
        self.__sair = False

    @property
    def bot(self):
        return self.__bot
    
    def boas_vindas(self):
        print(f"Olá, esse é o sistema de chatbots da empresa {self.__empresa}")

    def mostra_menu(self):
        print("\nOs chat bots os disponíveis no momento são:")
        for key,bot in enumerate(self.__lista_bots):
            print(f"{key} - Bot: {bot.nome()} - Mensagem de apresentação:  {bot.apresentacao()}") 
    
    def escolhe_bot(self):
        bot_index = int(input("\nDigite o número do chat bot desejado:"))
        if bot_index >= len(self.__lista_bots):
            raise IndexError(bot_index)
        bot = self.__lista_bots[bot_index]    

        self.__bot = bot 

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())

    def le_envia_comando(self):
        cmd = input("\nDigite o comando desejado (ou -1 fechar o programa sair):")
        if cmd=="-1":
            self.sair()
        else:
            self.mostra_msg_bot(self.__bot.executa_comando(cmd))

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.__bot = self.__lista_bots[0] 

        while self.bot is None:
            try:
                self.escolhe_bot()
            except IndexError:
                print("Opção inválida! Escolha novamente")
            except ValueError:
                print("Objeto escolhido não é do tipo Bot")

        self.mostra_msg_bot(self.bot.boas_vindas())
        while not self.__sair:
            self.mostra_comandos_bot()
            self.le_envia_comando()

    
    def mostra_msg_bot(self,msg):
        print(f"\n--> {self.__bot.nome()} diz: {msg}")
    
    def sair(self):
        self.mostra_msg_bot(self.__bot.despedida())
        self.__sair = True
