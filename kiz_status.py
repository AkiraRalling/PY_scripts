import json
import re
import requests

url = 'http://10.3.163.100:14000/v3/kiz/result/'
query_id = input(str('Input a query id here\n'))
pattern_query = re.compile('^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$')
arr_kiz = []


def status_doc(query_id):
    if pattern_query.match(query_id):
        get_status = requests.get(url + str(query_id))
        json_data = get_status.json() #if get_status.status_code == 200 else None
        if 'broken' in json_data:
            for broken in json_data['broken']:
                error = broken.get('error')
                sign = broken.get('sign')
                if error == 22:
                    arr_kiz.append('This is error ' + sign)
                elif error == 11:
                    arr_kiz.append('Hey! This KIZ is on another status or MD. Check this SGTIN ' + sign)
    else:
        print('No-no, pls give me a queary id, okey?')


status_doc(query_id)
new_arr = sorted(arr_kiz)
print(new_arr)

i = 0
while i < len(new_arr):
    print(new_arr[i])
    i+=1