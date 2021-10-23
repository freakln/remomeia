import json
import os
import re

fileOfDirectory = os.listdir('.')
pattern = "*.json"
pattern_regex = r"^www"
replacement = ''
file_name = 'urls-para-troca.json'
new_file_name = 'www.json'

new_data = []

with open(file_name, encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        aux = re.search(pattern_regex, str(i['error_link']))

        if aux:
            print(i['error_link'])
            new_data.append(i)

    with open(new_file_name, 'w') as outfile:
        json.dump(new_data, outfile)
