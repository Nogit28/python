import sqlite3
from flor import Flor

class FlorDao:
  def incluir(self, flor):
    conn = sqlite3.connect('floricultura.db')
    cursor = conn.cursor()
    sql = f"insert into flores values(" \
          f"'{flor.getCodigo()}','{flor.getDesc()}','{flor.getUnidade()}',"\
          f"{flor.getQuantidade()},{flor.getPreco()})"
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True

  def excluir(self, codigo):
    conn = sqlite3.connect('floricultura.db')
    cursor = conn.cursor()
    sql = f"delete from flores where codigo='{codigo}'" 
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True
  
  def atualizar(self, flor):
    conn = sqlite3.connect('floricultura.db')
    cursor = conn.cursor()
    sql = f"update flores " \
          f"set desc='{flor.getDesc()}', unidade='{flor.getUnidade()}', "\
          f"quantidade={flor.getQuantidade()}, preco={flor.getPreco()} "\
          f"where codigo='{flor.getCodigo()}'"
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True
  
  def consultar(self,codigo):
    conn = sqlite3.connect('floricultura.db')
    cursor = conn.cursor()
    sql = f"select * from flores where codigo='{codigo}'" 
    print(sql)
    cursor.execute(sql)
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        flor_encontrada = Flor(*resultado)
        return flor_encontrada
    else:
        return None