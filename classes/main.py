from cliente import Cliente
from agendamento import Agendamento

import mysql.connector
db_connection = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='ExameFinal')

cursor = db_connection.cursor()

def cria_cliente():
  # cria cliente
  cpf = input('CPF: ')
  nome = input('Nome: ')
  telefone = int(input('Telefone: '))
  endereco = input('Endereço: ')
  renda = float(input('Renda: '))
  # insere cliente no banco
  sql = "INSERT INTO Cliente (cpf, nome, telefone, endereco, renda) VALUES (%s, %s, %s, %s, %s)"
  values = (cpf,nome,telefone,endereco,renda)
  cursor.execute(sql, values)  

  db_connection.commit()
  

def cria_agendamento():
  # cria agendamento
  descricao = input('Descriçao: ')
  data = input('Data/hora 0000-00-00 00:00: ')
  status = input('Status: ')
  id_cliente = int(input('Id do cliente: '))
  # insere cliente no banco
  sql = "INSERT INTO Agendamento (descricao, data, status, id_cliente) VALUES (%s, %s, %s, %s)"
  values = (descricao, data, status, id_cliente)
  cursor.execute(sql, values)  
  
# imprime o cliente de acordo com o ID
def imprime_cliente(id):

  id_cliente = id #input('Digite o id do cliente: ')
  sql = ("SELECT id_cliente, cpf, nome, telefone, endereco, renda FROM cliente WHERE id_cliente={}".format(id_cliente))
  cursor.execute(sql)

  for (id_cliente, cpf, nome, telefone, endereco, renda) in cursor:
    print(id_cliente, cpf, nome, telefone, endereco, renda)
  print("\n")

# imprime o agendamento de acordo com o ID
def imprime_agendamento():

  id_agendamento = input('Digite o id do agendamento: ')
  sql = ("SELECT id_agendamento, descricao, data, status, id_cliente FROM Agendamento WHERE id_agendamento={}".format(id_agendamento))
  cursor.execute(sql)

  for (id_agendamento, descricao, data, status, id_cliente) in cursor:
    print(id_agendamento, descricao, data, status, id_cliente)

def update_cliente():
  a = {1: 'cpf', 2: 'nome', 3: 'telefone', 4: 'endereco', 5: 'renda'}

  id_cliente = input('Digite o id do cliente a ser atualizado: ')
  e = int(input('Escolha: \n1 - CPF \n2 - Nome \n3 - Telefone \n4 - Endereço \n5 - Renda'))
  setar = input('{} = '.format(a[e]))

  sql = ("UPDATE cliente SET {} = '{}' WHERE id_cliente = {}".format(a[e], setar, id_cliente))
  cursor.execute(sql)

  db_connection.commit()

def delete_cliente():
  id_cliente = input('Digite o id do cliente a ser deletado: ')
  print('Tem certeaz que deseja deletar')
  imprime_cliente(id_cliente)
  e = input('s/n')
  if e == 's':
    sql = ("DELETE FROM cliente WHERE id_cliente = {}".format(id_cliente))
    cursor.execute(sql)

    db_connection.commit()
    print('Cliente deletado!')
  else:
    print('ok')

def list_tudo():
  op = input('1 - Cliente / 2 - Agendamento: ')
  if op == '1':
    cliente = ("SELECT * from Cliente")
    cursor.execute(cliente)
  elif op =='2':
    agendamento = ("SELECT * from Agendamento")
    cursor.execute(agendamento)
  else:
    print('opção invalida')

  for a in cursor:
    print(a)
  print('\n')

def main():
  while True:
    print('0 - Listar tudo')
    print('1 - Criar cliente')
    print('2 - Imprime cliente')
    print('3 - Criar agendamento')
    print('4 - Imprime agendamento')
    print('5 - Atualizar dados do cliente')
    print('6 - Deletar cliente')
    e = input(': ')
    if e=='0':
      print('----------LISTANDO TUDO----------')
      list_tudo()
    elif e == '1':
      print('----------CRIANDO CLIENTE----------')
      cria_cliente()
    elif e == '2':
      print('----------IMPRIMINDO CLIENTE----------')
      id = int(input('Id do cliente: '))
      imprime_cliente(id)
    elif e == '3':
      print('----------CRIANDO AGENDAMENTO----------')
      cria_agendamento()
    elif e == '4':
      print('----------IMPRIMINDO AGENDAMENTO----------')
      imprime_agendamento()
    elif e == '5':
      print('----------ATUALIZAR DADOS DO CLIENTE-----------')
      update_cliente()
    elif e == '6':
      print('----------DELETANDO CLIENTE-----------')
      delete_cliente()
    else:
      print('SAINDO....')
      break

if __name__ == "__main__":
    main()