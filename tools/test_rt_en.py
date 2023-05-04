#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.parse import quote
import requests
import sys
import time
#curl "http://127.0.0.1:12003/xr" -X POST -d
#root_url = 'http://11.186.201.234:32474/xr?'
#root_url = 'http://11.1.23.10:31957/xr?'
#11.1.23.10:31957
#root_url = 'http://11.0.138.144:12002/xr?'
# root_url = 'http://11.28.110.163:54078/bin/tranx?'
root_url = 'http://33.27.233.24:54078/bin/tranx?'

in_file = sys.argv[1]
out_file = sys.argv[2]
sum_time = 0.0
num = 0
start = time.time()
with open(out_file, 'w', encoding='UTF-8') as f_write:
    with open(in_file, 'r', encoding='UTF-8') as f_read:
        for line in f_read:
            line = line.strip()
            if len(line) == 0:
                continue
            # line_decode = quote(line_arr[0], 'utf-8')

            query = root_url + line
            #print(query)
            try:
                #print('jjjjjjjjjjj')
                output = requests.get(query)
                #print(output)
                json_str = requests.get(query).json()
                #print(json_str)
                #result = json_str["result"]["result"]
                result = json_str["result"]
                ti = json_str["time"]
                sum_time += float(json_str["time"])
                num += 1
                #f_write.write(line + '\t' + result + '\t'+ "{:.3}".format(float(json_str["time"])) + '\n')
                f_write.write(result + '\n')
            except Exception as e:
                #print(e)
                f_write.write(line + '\t' + "" + '\t' + "{:.3}".format(0.0) + '\n')


use_time = time.time() - start
print("system time: {}, avg: {}".format(use_time, use_time/max(1, num)))
print("server time: {}, avg: {}".format(sum_time, sum_time/max(1, num)))
