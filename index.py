import sqlite3
import funcoes

PASSWORD_iNICIAL = '12345'
funcoes.verificarSenha(PASSWORD_iNICIAL)

conn = sqlite3.connect('password.db')
cursor = conn.cursor()

funcoes.criarTabela(cursor);

while True:
    funcoes.menu()

    op= input('O que deseja fazer? ')
    if(op not in ['1','2','3','4']):
        print('Opcao inválida!')
        continue

    if(op == '1'):
        service = input('Qual o nome do Servico? ')
        username = input('Qual o nome do usuario? ')
        password = input('Qual a senha? ')
        funcoes.insertPassword(service, username, password, cursor, conn)
        print('caiu')

    if(op == '2'):
        funcoes.showServices(cursor)
    
    if(op == '3'):
        service =  input('Qual o servico que deseja recuperar a senha? ')
        funcoes.getPassword(service, cursor)

    if(op == '4'):
        break

conn.close()