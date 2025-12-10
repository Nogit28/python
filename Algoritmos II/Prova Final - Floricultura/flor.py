class Flor:
  def __init__(self,codigo=None,desc=None,unidade=None,quantidade=None,preco=None):
    self.__codigo = codigo
    self.__desc = desc
    self.__unidade = unidade
    self.__quantidade = quantidade
    self.__preco = preco
  
  def setCodigo(self,codigo):
    self.__codigo = codigo
  def getCodigo(self):
    return self.__codigo
  
  def setDesc(self,desc):
    self.__desc = desc
  def getDesc(self):
    return self.__desc
  
  def setUnidade(self,unidade):
    self.__unidade = unidade
  def getUnidade(self):
    return self.__unidade
  
  def setQuantidade(self,quantidade):
    self.__quantidade = quantidade
  def getQuantidade(self):
    return self.__quantidade
  
  def setPreco(self,preco):
    self.__preco = preco
  def getPreco(self):
    return self.__preco