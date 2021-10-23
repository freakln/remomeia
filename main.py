import csv
import os
import re

folder = './entrada/'
fileOfDirectory = os.listdir(folder)
pattern = "*.json"
pattern_regex = r"xml:lang"
replacement = ''
file_name = 'urls-para-troca.json'
new_file_name = 'saida.csv'

new_data = [['Unnamed: 0','site_id','article_id','wordpress_id','article_url','tag','position_in_text']]

print(fileOfDirectory)

for file in fileOfDirectory:
    with open(folder + file, newline='', encoding='utf-8') as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spamreader:
            aux = re.search(pattern_regex, (', '.join(row)))
            if aux:
                print(row)
                new_data.append(row)
    csv_file.close()

with open(new_file_name, 'w', newline='',  encoding='utf-8') as csv_file:
    spamwriter = csv.writer(csv_file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in new_data:
        spamwriter.writerow(row)


