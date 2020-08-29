from cliente import Cliente
from agendamento import Agendamento

import mysql.connector
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")


def cria_cliente(cliente):
    # cria cliente
    cpf = input('CPF: ')
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    endereco = input('Endereço: ')
    renda = float(input('Renda: '))
    cliente[cpf] = Cliente(cpf, nome, telefone, endereco, renda)
    return cliente

def imprime_cliente(cliente):
    # imprime cliente
    cpf = input('CPF do cliente: ')
    return cliente[cpf].print_cliente()

def cria_agendamento(agendamento):
    # cria agendamento
    id = int(input('ID: '))
    descricao = input('Descrição: ')
    data = input('data: ')
    hora = input('hora: ')
    cliente = int(input('Cliente: '))
    status = input('Status: ')
    agendamento[id] = Agendamento(descricao, data, hora, cliente, status)
    return agendamento

def imprime_agendamento(agendamento):
    # imprime agendamento
    id = int(input('ID do agendamento: '))
    return agendamento[id].print_agendamento()

def main():
    cliente = {}
    agendamento = {}
    while True:
        print('1 - Criar cliente')
        print('2 - Imprime cliente')
        print('3 - Criar agendamento')
        print('4 - Imprime agendamento')
        e = input(': ')
        if e == '1':
            print('----------CRIANDO CLIENTE----------')
            cria_cliente(cliente)
        elif e == '2':
            print('----------IMPRIMINDO CLIENTE----------')
            imprime_cliente(cliente)
        elif e == '3':
            print('----------CRIANDO AGENDAMENTO----------')
            cria_agendamento(agendamento)
        elif e == '4':
            print('----------IMPRIMINDO AGENDAMENTO----------')
            imprime_agendamento(agendamento)
        else:
            print('SAINDO....')
            break

if __name__ == "__main__":
    main()