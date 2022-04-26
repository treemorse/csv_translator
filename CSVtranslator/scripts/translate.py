import os
import requests
import yc_configure as yc
import csv_reader as rc
import json

def write_to_json(translations, file, row, sub_row, language):
    words = []
    words.append(row[1])
    args = yc.configure(words, language)
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        json = args[0],
        headers = args[1]
    )
    response_dict = json.loads(response.text)
    sub_row[1] = '"' + response_dict['translations'][0]['text'] + '"'
    print(sub_row[1])
    file.write(','.join(sub_row) + '\n')
    translations[row[1]] = sub_row[1][1:-1]
    with open(rc.path + 'translations_to_' + language + '.json', 'w') as outfile:
        json.dump(translations, outfile, indent=4, sort_keys=True)
    words = []

def translate(language):
    translations = {}
    reader = rc.read()
    json_path = rc.path + 'translations_to_' + language + '.json'
    with open(rc.path + language + '.csv', 'w') as file:
        for row in reader[0]:
            sub_row = row.copy()
            if os.path.exists(json_path):
                with open(rc.path + 'translations_to_' + language + '.json') as infile:
                    translations = json.load(infile)
                    if row[1] in translations.keys():
                        sub_row[1] = '"' + translations[row[1]] + '"'
                        file.write(','.join(sub_row) + '\n')
                    else:
                        write_to_json(translations, file, row, sub_row, language)
            else:
                write_to_json(translations, file, row, sub_row, language)
        reader[1].close()