from tago import Account, Device

class ImpTago:

    def listadevicesjson():
        _MY_ACCOUNT_TOKEN = '6bc735c7-c9cf-45e3-8d0d-f07a056b601f'
        _my_account = Account(_MY_ACCOUNT_TOKEN)
        json = _my_account.devices.list()
        lista = json['result']
        return lista

    def listadevices():
        lista = ImpTago.listadevicesjson()
        devices = []
        for valor in lista:
            temp = valor
            devices.append(temp['id'])
        return devices

    def importaDadosTago(device, inicio, fim): #colocar variavel de datas
        my_device = Device(device)

        filter = {
            #'variable': 'inputs',
            #'query': 'last_value'
            'start_date': inicio,
            'end_date': fim,
            'qty': 10000
        }

        #filter = {'start_date': inicio, 'end_date': fim }

        q_json = my_device.find(filter)
        return q_json['result']

    def listaTokenDevices():
        listaToken = ('84c1bda6-12c3-4f44-b168-05fbfe17e4ed',
                     '50e2eddb-178f-4150-a44c-db67aa491bdf',
                     '1f207ed5-eeac-4f23-b913-65f6b1ed8ffa',
                     '921d6066-daff-49db-8316-d340c451e35c',
                     'dce8c9e1-6cfc-4d44-992b-78bc4466ff69',
                     'dd0b6125-ca6c-4044-be3e-e4e990dda7d8',
                     'a6a97d83-b14a-42c9-b9dd-5b67f871735f',
                     'a4cba398-e48b-4357-baad-4c23e210c09a',
                     'bfd9a2f2-aeaa-44f2-8c08-2225c4829f0a')

        return listaToken

