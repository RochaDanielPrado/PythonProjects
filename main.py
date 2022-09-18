from tago_data import Tago_Data, ImportTago
from csvfile import Trata_csv
from conversoes import Dtconvert, Bitconvert
import os
import csv
from datetime import datetime, timedelta

class Main:
    def __init__(self):
        self.obj_csv = Trata_csv()
        self.obj_token_devices = Tago_Data()
        self.obj_dados = ImportTago()
        self.variaveis()
        self.main()
    def variaveis(self):
        self.file = self.obj_csv._file()
        self.start_str = '2022-01-01 00:00:01'
        self.end_str = '2022-01-01 23:59:59'
        self.today_str = str(datetime.now())
        self.lista_devices_token = self.obj_token_devices.dev_list #self.obj_token_devices.devices_tupla
        self.compara = self.obj_csv.readIdMedidasfromCsv()

    def main(self):
        start_str = self.start_str
        end_str = self.end_str
        start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
        end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
        print('Importando dados do TagoIo..........')
        while start_str <= self.today_str:
            print(start_str)
            contador = '.'
            for key in self.lista_devices_token:
                item = key['device token']

                try:
                   with open(self.file, 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = ['data', 'device', 'nome', 'id',  'variavel', 'valor']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
                        lista = self.obj_dados.importaDadosTago(item, start_str, end_str)
                        contador = contador + '.'
                        print(contador)
                        for valor in lista:
                            temp = valor
                            i = temp['id']
                            if i not in self.compara:
                               # print('insere', 'i:', i, 'compara:', compara)
                                #print(temp['id'], temp['device'], temp['variable'], temp['value'], Dtconvert(temp['time']))

                                dicionario = {'data': Dtconvert(temp['time']),
                                                'device': key['id'],
                                                'nome': key['nome'],
                                                'id': temp['id'],
                                                'variavel': temp['variable'],
                                                'valor': temp['value']}
                                if temp['variable'] == 'inputs':
                                    dict_temp = Bitconvert.bitand(temp['value'])

                                    for item in dict_temp:
                                        #print(f"key: {key}, value: {dict_temp[key]}")
                                        dicionario = {'data': Dtconvert(temp['time']),
                                                      'device': key['id'],
                                                      'nome': key['nome'],
                                                      'id': temp['id'],
                                                      'variavel': item,
                                                      'valor': dict_temp[item]}
                                        writer.writerow(dicionario)
                                else:
                                   # print('nao entrou ')
                                    writer.writerow(dicionario)
                            else:
                                print('não insere')

                except:
                    pass


            start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            start_str = str(start_object)
            end_str = str(end_object)

        print('Fim...')

Main()
