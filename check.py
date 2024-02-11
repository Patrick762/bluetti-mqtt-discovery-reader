import base64
import json

logfile = open('discovery.log', 'r')
lines = logfile.readlines()

device_type_data_v1 = bytearray()
device_type_data_v2 = bytearray()

address = 0
for line in lines:
    address = address + 1
    encoded = line.strip()
    lineObj = json.loads(encoded)
    if "error" not in lineObj:
        data = base64.b64decode(lineObj["data"])
        data = bytearray([data[3],data[4]])

        if address in [10,11,12,13,14,15]:
            device_type_data_v1 = device_type_data_v1 + data

        if address in [110,111,112,113,114,115]:
            device_type_data_v2 = device_type_data_v2 + data

def swap_bytes(data: bytes):
    arr = bytearray(data)
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print("Please check which result matches your Powerstation model below")

print("Result V1:", swap_bytes(device_type_data_v1).rstrip(b'\0').decode('ascii'))
print("Result V2:", swap_bytes(device_type_data_v2).rstrip(b'\0').decode('ascii'))
