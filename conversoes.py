

class Dtconvert:
    def __init__(self, dt):
        self._dt_ = dt

    def __str__(self):
        return f'{self._dt_[0:10]} {self._dt_[11:23]}'

class Bitconvert:
    def bitand(valor):
        bits = (1, 2, 4, 8, 16, 32, 64, 128)
        x = int(valor)
        dicionario = {'bit8': 0,'bit7': 0, 'chave saida acido': 0, 'chave saida alcalino': 0, 'sensor sal': 0, 'sensor acido': 0, 'sensor alcalino': 0, 'enable geral': 'off', }
        for i in bits:
            if i & x > 0:
               # print(i, i & x)
                match i:
                    case 1:
                        dicionario['enable geral'] = 'on'
                    case 2:
                        dicionario['sensor alcalino'] = 1
                    case 4:
                        dicionario['sensor acido'] = 1
                    case 8:
                        dicionario['sensor sal'] = 1
                    case 16:
                        dicionario['chave saida alcalino'] = 1
                    case 32:
                        dicionario['chave saida acido'] = 1
                    case 64:
                        dicionario['bit7'] = 1
                    case 128:
                        dicionario['bit8'] = 1

        return dicionario




