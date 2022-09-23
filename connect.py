import mysql.connector
from mysql.connector import Error
import json

def db_connect():
    try:
        config_read()
        global con
        con = mysql.connector.connect(host=f'{host}',
                                      database=f'{db}',
                                      user=f'{user}',
                                      password=f'{senha}')

        if con.is_connected():
            db_info = con.get_server_info()
            print('Conectado ao servidor MySQL versão' , db_info)
            cursor = con.cursor()
            cursor.execute('Select database();')
            linha = cursor.fetchone()
            cursor.close()
            print('Conectado ao banco de dados ', linha)
            sql_create = """CREATE TABLE IF NOT EXISTS tago_data (
                           id INT(6) NOT NULL AUTO_INCREMENT,
                           data DATETIME,
                           device VARCHAR(50),
                           nome VARCHAR(50),
                           id_registro VARCHAR(50),
                           variavel VARCHAR(50),
                           valor VARCHAR(50),
                           dt_import DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                           PRIMARY KEY (id)) ENGINE = InnoDB;"""
            db_create_table(sql_create)
    except Error as erro:
        print('Erro ao acessar banco - {}'.format(erro))


def config_read():
    try:
        print('Lendo dados de conexão ao db')
        acesso = open('autentificacao/pass.txt', 'r', encoding='utf-8')

        linhas = acesso.readlines()
        js = ""

        for linha in linhas:
            js = js + linha.rstrip()

        db_par = json.loads(js)['db_connect']

        global host, db, user, senha
        host = db_par['host']
        db = db_par['db']
        user = db_par['user']
        senha = db_par['pass']

        tago_par = json.loads(js)['tago_access']
        global tago_account, tago_profile_id
        tago_account = tago_par['account']
        tago_profile_id = tago_par['profile_id']

    except Error as erro:
        print('Erro ao ler o arquivo de configuração- {}'.format(erro))
    finally:
        acesso.close()

def db_create_table(sql_create):

    try:

        sqlx = """SELECT COUNT(*) FROM information_schema.tables
            WHERE table_schema = '""" + f'{db}' + "'" """
            AND table_name = 'tago_data'
            LIMIT 1;"""
        cursor = con.cursor()
        cursor.execute(sqlx)
        existe = cursor.fetchone()
        existe = existe[0]
        if existe == 1:
            print('Tabela OK')
        else:
            print('A tabela foi criada com exito')
            cursor.execute(sql_create)

    except Error as erro:
        print('Erro ao criar a tabela banco - {}'.format(erro))


def db_query_table():

    try:
        db_connect()
        sql = "SELECT * FROM tago_data;"
        cursor = con.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        return records
    except Error as erro:
        print('Erro ao ler na tabela banco - {}'.format(erro))
    finally:
        cursor.close()
        con.close()
def db_insert_table(sql):

    try:
        db_connect()
        cursor = con.cursor()
        print('Inserindo novos registros....')
        cursor.execute(sql)
        con.commit()

    except Error as erro:
        print('Erro ao inserir registros no banco - {}'.format(erro))
    finally:
        cursor.close()
        con.close()

def readIdMedidasfromDb():

    file = db_query_table()
    #print(file)
    _id_list = []
    # values to empty list
    for col in file:
        _id_list.append(col[4])
    return _id_list

try:
    sql = """INSERT INTO `tago_data`
                (id_oper, data, device, nome, variavel, valor)
                VALUES
                ('xde', '2022-09-28 18:55:16', 'teste', 'texst', 'dfdd', '3456'),
                ('dfdfd', '2022-09-06 18:55:16', 'dfdf', 'dfd', 'ddf', 'dfdf');"""

    #readIdMedidasfromDb()

finally:
    pass
    #if con.is_connected:
     #   cursor.close()
      #  con.close()
       # print('a conexão ao mysql foi encerrada')
