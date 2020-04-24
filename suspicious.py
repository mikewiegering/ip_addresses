import requests

api_key = 'd5645a210a5065b0df6a2851db470f2a771ea67ce0975d39db1b3d31'
# ip_address = '190.102.239.207'

# api_url = f'https://api.ipdata.co/{ip_address}?api-key={api_key}'



filename = 'addresses.txt'
file_handle = open(filename, 'r')
file_content = file_handle.read()

file_lines = file_content.split('\n')

for ip in file_lines:
    api_url = f'https://api.ipdata.co/{ip}?api-key={api_key}'
    response = requests.get(api_url)

    if response.ok:
        print(response.json())