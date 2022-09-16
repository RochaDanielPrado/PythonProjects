from csvfile import Trata_csv
from datetime import datetime, timedelta

start_str = '2022-01-01 00:00:01'
end_str = '2022-01-01 23:59:59'
today_str = str(datetime.now())

start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
# datetime_object = str(datetime_object)
print(type(start_object))
print(start_object)  # printed in default format


while start_str <= today_str:
    # print(start_object)
    start_object = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
    end_object = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
    start_str = str(start_object)

import tago

my_account = tago.Account('c9159d98-2f00-4e9a-a8ba-7370e7584283')

result = my_account.profiles.tokenList('626438b6cce7b90011bdf271')
print(result)

my_devices = my_account.devices.list()
print(my_devices)

device_info = my_account.devices.info('631b3097b9d0fa001800a01c') # device_id
print(device_info)

device_token_list = my_account.devices.tokenList('631b3097b9d0fa001800a01c') # device_id
print(device_token_list)
