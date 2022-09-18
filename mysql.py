import mysql.connector

con = mysql.connector.connect(host='', database='', user='', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL versão , db_info')
    cursor = con.cursor()
    cursor.execute('Select database();')
    linha = cursor.fechone()
    print('Conectado ao banco de dados ', linha)

if con.is_connected:
    cursor.close()
    con.close()
    print('A conexão ao MySQL foi encerrada')