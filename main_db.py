from tago_data import Tago_Data, ImportTago
import connect
from conversoes import Dtconvert, Bitconvert
import os
from datetime import datetime, timedelta

class Main:
    def __init__(self):
        self.obj_token_devices = Tago_Data()
        self.obj_dados = ImportTago()
        self.variaveis()
        self.main()
    def variaveis(self):

        self.start_str = '2022-01-01 00:00:01'
        self.end_str = '2022-01-01 23:59:59'
        self.today_str = str(datetime.now())
        self.lista_devices_token = self.obj_token_devices.dev_list #self.obj_token_devices.devices_tupla
        self.compara = connect.readIdMedidasfromDb()

    def main(self):
        start_str = self.start_str
        end_str = self.end_str
        start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
        end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
        dados = []
        print('Importando dados do TagoIo..........')

        while start_str <= self.today_str:
            print(start_str)
            contador = ''
            for key in self.lista_devices_token:
                item = key['device token']

                try:

                    lista = self.obj_dados.importaDadosTago(item, start_str, end_str)

                    contador = contador + '.'
                    print(contador)
                    for valor in lista:
                        temp = valor
                        i = temp['id']
                        #print('compara', i, self.compara)
                        if i not in self.compara:
                           # print('insere', 'i:', i, 'compara:', compara)
                            #print(temp['id'], temp['device'], temp['variable'], temp['value'], Dtconvert(temp['time']))
                            tupla = ()
                            tupla = (str(Dtconvert(temp['time'])),
                                    key['id'],
                                    key['nome'],
                                    temp['id'],
                                    temp['variable'],
                                    str(temp['value']))
                            dados.append(tupla)
                            #print('dados', dados)
                            if temp['variable'] == 'inputs':
                                dict_temp = Bitconvert.bitand(temp['value'])

                                for item in dict_temp:
                                    #print(f"key: {key}, value: {dict_temp[key]}")
                                    tupla=()
                                    tupla = ( str(Dtconvert(temp['time'])),
                                            key['id'],
                                            key['nome'],
                                            temp['id'],
                                            item,
                                            str(dict_temp[item]))
                                    #writer.writerow(dicionario)
                                    dados.append(tupla)
                                #print('tupla', tupla)

                            else:
                               pass
                               #print('nao entrou ')
                               # writer.writerow(dicionario)

                        else:
                            pass
                            #print('não insere')

                except:
                    pass


                dados_sql = ""
                if len(dados) > 0:
                    ultimo = dados[-1]
                    for y in dados:
                        if y == ultimo:
                            dados_sql = dados_sql + f"{y}"
                        else:
                            dados_sql = dados_sql + f"{y}" + ",\n"

                    sql = f"""INSERT INTO tago_data
                                (data, device, nome, id_registro, variavel, valor)
                                VALUES
                                {dados_sql};"""
                    # print(sql)
                    try:
                        connect.db_insert_table(sql)
                    except:
                        print('Não havia dados a inserir ou houve erro na inserção --')



            start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            start_str = str(start_object)
            end_str = str(end_object)
            dados = []
            #print('dados', dados)


        print('Fim...')

Main()
