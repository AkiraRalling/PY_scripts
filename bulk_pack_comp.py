import os
import uuid
import requests
import re
import json

from requests import HTTPError

host = 'http://10.3.163.100:14000'
sscc = input('Input SSCC\n')
regexp = re.compile('\d{18}')
global kiz_status


class BulkSscc:

    @staticmethod
    def atchived_sscc(sscc):
        query_id = uuid.uuid4()
        url_host = f'{host}/v3/kiz/sscc_operations/archived/filter'
        headers = {'Content-Type': 'application/json'}
        data = '{"query_id":"' + str(query_id) + '","sscc":"' + str(sscc) + '"}'
        url_query = requests.post(url_host, headers=headers, data=data)
        if url_query.status_code == 200:
            get_info = requests.get(f'{host}/v3/kiz/result/' + str(query_id))
            json_date = get_info.json()
            # print(json_date)
            if 'filtered_records' in json_date:
                for i in json_date['filtered_records']:
                    for v in i['sscc_operations']:
                        with open('test.txt', 'a') as file:
                            if v['operation_type'] == 61:
                                file.write(f'XML DOCUMENT AGGREGATION is ' + v['xml_document_id'] + '\n')
                            elif v['operation_type'] == 63:
                                file.write(f'XML DOCUMENT DISPENSATION is ' + v['xml_document_id'] + '\n')

    @staticmethod
    def kiz_status(kiz):
        resp = requests.get(f'{host}/v3/kiz/' + str(kiz))
        json_data = resp.json()
        if 'errorDescription' in json_data and regexp.match(kiz):
            BulkSscc.atchived_sscc(kiz)
        elif 'errorDescription' not in json_data and regexp.match(kiz):
            status = json_data['internalState']
            return status

    @staticmethod
    def bulk_pack(string):
        array_kiz = []  # This array will contain a data from request
        kiz_status = BulkSscc.kiz_status(string)
        try:
            query_id = uuid.uuid4()
            url = f'http://{host}/v3/kiz/bulk_package_components'
            headers = {'Content-Type': 'application/json'}
            data = '{"query_id":"' + str(query_id) + '","kizs":["' + str(string) + '"]}'
            url_query = requests.post(url, headers=headers, data=data)
            if url_query.status_code == 200:
                get_res = f'http://{host}/v3/reestr/result/'
                result = requests.get(get_res + str(query_id), headers=headers)
                json_data = result.json()
                data = json_data[0]['package_components']['down']['childs']
                for i in data:
                    sign = i['sign']
                    status = i['internal_state']
                    if kiz_status == status:
                        array_kiz.append(f'{sign}: {status}')
                    else:
                        print(f'Data is differ! SSCC state is {kiz_status}, but SGTIN is {status}')
            return array_kiz

        except HTTPError as http_error:
            print(f'HTTP error by: {http_error}')
        except Exception as err:
            print(f'Other error: {err}')

    @staticmethod
    def write_sgtins(string):
        array = BulkSscc.bulk_pack(string)
        i = 0
        if os.path.exists("test.txt"):
            os.remove("test.txt")

            # Print the statement once
            # the file is deleted
            print("File deleted !")
        while i < len(array):
            with open('test.txt', 'a') as file:
                print(array[i])
                file.write(f'{array[i]}\n')
                i += 1
