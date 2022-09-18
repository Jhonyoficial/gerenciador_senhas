def verificarSenha(password_inicial):
    senha =  input('digite a seua senha: ')
    if senha != password_inicial:
        print('senha inválida!')
        exit()


def menu():
    print('\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
    print('1 - inserir uma nova senha          #')
    print('2 - Listar servicos salvos          #')
    print('3 - Recuperar uma senha             #')
    print('4 - Sair                            #')
    print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n')

def criarTabela(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')

def insertPassword(service, username, password, cursor, conn):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def showServices(cursor):
    cursor.execute('''
        SELECT service from users;
    ''')
    for service in cursor.fetchall():
        print(service)

def getPassword(service, cursor):
    cursor.execute(f'''
        SELECT username, password FROM users 
            WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print('Serviço nao encontrato! ')
    else:
        for user in cursor.fetchall():
            print(user)