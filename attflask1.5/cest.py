class estoque:
    def __init__ (self, nome='', qtd=0, preco=0, data='', validade=''):
        self.__nome = nome
        self.__qtd = qtd
        self.__preco = preco
        self.__data = data
        self.__validade = validade

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    
    def setQtd(self, qtd):
        self.__qtd = qtd
    def getQtd(self):
        return self.__qtd
    
    def setPreco(self, preco):
        self.__preco = preco
    def getPreco(self):
        return self.__preco
    
    def setData(self, data):
        self.__data = data
    def getData(self):
        return self.__data
    
    def setValidade(self, validade):
        self.__validade = validade
    def getValidade(self):
        return self.__validade