import csv
import os

class Trata_csv:
    def __init__(self):
        self.file_csv = 'import_tago_csv.csv'
        print('Verificando o arquivo:', self.file_csv)
        self.verifica_csv()
        print('Criando lista à partir do arquivo:', self.file_csv)
        self.readIdMedidasfromCsv()
    def verifica_csv(self):
        if os.path.exists(self.file_csv):
            print('O arquivo existe.... Continua...')
            with open(self.file_csv, mode='r') as csv_file:
                reader_obj = csv.reader(csv_file)  # read the current csv file
        else:
            print('O arquivo não existe.... Criando...')
            with open(self.file_csv, 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['data', 'device', 'nome', 'id',  'variavel', 'valor']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
                writer.writeheader()

            csv_file.close()
    def readIdMedidasfromCsv(self):
        filename = open(self.file_csv, 'r')

        file = csv.DictReader(filename)

        _id_list = []
        # values to empty list
        for col in file:
            _id_list.append(col['id'])
        return _id_list

    def _file(self):
        self.file = self.file_csv
        return self.file

#Trata_csv()