import mysql.connector

con = mysql.connector.connect(host='162.241.61.180',
                              database='dexoveco_wp070',
                              user='dexoveco_daniel', password='@Rocce1102')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL versão , db_info')
    cursor = con.cursor()
    cursor.execute('Select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ', linha)

if con.is_connected:
    cursor.close()
    con.close()
    print('A conexão ao MySQL foi encerrada')