import requests
import yc_configure as yc
import csv_reader as rc
import json

translations = {}
reader = rc.read()

def translate():
    with open(rc.path + '2.csv', 'w') as file:
        for row in reader[0]:
            sub_row = row.copy()
            with open(rc.path + 'translations.json') as infile:
                translations = json.load(infile)
                if row[1] in translations.keys():
                    sub_row[1] = '"' + translations[row[1]] + '"'
                    file.write(','.join(sub_row) + '\n')
                else:
                    words = []
                    words.append(row[1])
                    args = yc.configure(words)
                    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                        json = args[0],
                        headers = args[1]
                    )
                    response_dict = json.loads(response.text)
                    sub_row[1] = '"' + response_dict['translations'][0]['text'] + '"'
                    print(sub_row[1])
                    file.write(','.join(sub_row) + '\n')
                    translations[row[1]] = sub_row[1][1:-1]
                    with open(rc.path + 'translations.json', 'w') as outfile:
                        json.dump(translations, outfile)
                    words = []
        reader[1].close()