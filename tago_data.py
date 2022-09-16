from tago import Account, Device

class Tago_Data:
    def __init__(self):
        self._my_account = Account('c9159d98-2f00-4e9a-a8ba-7370e7584283')
        self._profile_id = '626438b6cce7b90011bdf271'
        self.token_profile_list_json = self._my_account.profiles.tokenList(self._profile_id)

        if self.token_profile_list_json['status'] == True:
            pass
            #print(self.token_profile_list_json)
        else:
            raise ValueError ('Não foi possível acessessar! Check o Token!')

        print('Criando lista devices_id, nome, tags, token....')
        self.device_list_json = self.devices_list_js()
        self.devices_tupla = ()
        if self.device_list_json['status'] == True:
            self.dev_list = self.devices_list()['lista']
            self.dev_dict = self.devices_list()['dict']

            temp = []
            for key1 in self.dev_dict:

                for key, value in list(key1.items()):
                    try:
                        if key == 'id':
                            try:
                                token = self.token_list(key1['id'])
                                self.devices_tupla = self.devices_tupla + (key1['id'],)
                                key1['device token'] = token
                                temp.append(key1)

                            except:
                                pass
                            self.dev_list = temp

                    except:
                        pass

        else:
            raise ValueError ('Não foi possível acessessar! Check o Token!')


    def devices_list_js(self):
        my_devices = self._my_account.devices.list()
        return my_devices

    def devices_list(self):
        lista = self.device_list_json['result']

        devices = []
        dicionario = {}
        list_dict = []
        for valor in lista:
            temp = valor
            devices.append(temp['id'])
            dicionario['id'] = temp['id']
            dicionario['nome'] = temp['name']
            dicionario['tags'] = temp['tags']
            list_dict.append(dicionario)
            dicionario = {}

        return {'lista': devices, 'dict': list_dict}

    def token_list(self, dispositivo_id):
        device_token_list_json = self._my_account.devices.tokenList(dispositivo_id)#device_id
        if device_token_list_json['status'] == True:
            dev_token_list = device_token_list_json['result'][0]

            token_vl = dev_token_list['token']

        else:
            pass
        return token_vl


    def listadevicesjson(self):
        #_MY_ACCOUNT_TOKEN = '6bc735c7-c9cf-45e3-8d0d-f07a056b601f'
        #_my_account = Account(_MY_ACCOUNT_TOKEN)
        json = self._my_account.devices.list()
        lista = json['result']
        return lista

    def listadevices(self):
        lista = self.listadevicesjson()
        devices = []
        for valor in lista:
            temp = valor
            devices.append(temp['id'])
        return devices

    def listaTokenDevices(self):
        listaToken = self.devices_tupla

        return listaToken

class ImportTago:
    def importaDadosTago(self, device, inicio, fim): #colocar variavel de datas
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




#my_account = Account('c9159d98-2f00-4e9a-a8ba-7370e7584283')

#result = my_account.profiles.tokenList('626438b6cce7b90011bdf271')
#print(result)

#my_devices = my_account.devices.list()
#print(my_devices)

#device_info = my_account.devices.info('631b3097b9d0fa001800a01c')#device_id
#print(device_info)

