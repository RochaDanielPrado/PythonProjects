import json

js = {'tago_date': '2022-09-22 11:51:00.448', 'tago_deviece': '62f7ab826fff7f001a492aaf', 'tago_name': 'teste_dani', 'tago_id_register': '632c4c24e682dc0018e47ee5', 'tago_variable': ('ip',), 'tago_value': '192.168.15.137'}

teste = json.dumps(js)

print(type(teste), teste)