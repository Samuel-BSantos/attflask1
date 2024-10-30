class prato:
    def __init__(self, nome='', preco=0.0, desc=''):
        self.__nome = nome
        self.__preco = preco
        self.__desc = desc

    def setNome(self, nome): 
        self.__nome = nome

    def getNome(self): 
        return self.__nome
    
    def setPreco(self, preco): 
        self.__preco = preco

    def getPreco(self): 
        return self.__preco
    
    def setDesc(self, desc): 
        self.__desc = desc

    def getDesc(self): 
        return self.__desc