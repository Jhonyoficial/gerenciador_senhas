import sqlite3
import funcoes

PASSWORD_iNICIAL = '12345'

senha = input('Digite a senha para entrar: ')
if(senha != PASSWORD_iNICIAL):
    print('Senha inválida')
    exit()

conn = sqlite3.connect('password.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    usernamve TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

while True:
    funcoes.menu()
    op= input('O que deseja fazer? ')
    if(op not in ['1','2','3','4']):
        print('Opcao inválida!')
        continue
    if(op == '4'):
        break

conn.close()