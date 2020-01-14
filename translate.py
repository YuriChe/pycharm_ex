import requests

def translate_line(text, lang):
    URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
    res = requests.post(URL,
                        params={'srv': 'tr-text',
                                'id': 'fbee7025.5e1cd488.ddf95e6d-3-0',
                                'lang': lang,
                                'reason': 'auto',
                                'format': 'text'},
                        data={'text': text})

    result_of_trans = res.json()['text'][0]

    return result_of_trans

def translate_ya(url_what, url_result, lang_text, lang_to= 'ru'):

    lang_to_translate = f'{lang_text}-{lang_to}'
    with open(url_what, 'r', encoding= 'utf8') as file_in, open(url_result, 'w', encoding= 'utf8') as file_out:
        for line in file_in:
            line_to_translate = line.strip()
            if line_to_translate != '':
                file_out.write(translate_line(line_to_translate, lang_to_translate) + '\n')
            else:
                file_out.write('' + '\n')
    status_of = True
    return status_of

translate_ya('DE.txt', 'DE-RU.txt', 'de')
translate_ya('ES.txt', 'ES-RU.txt', 'es')
translate_ya('FR.txt', 'FR-RU.txt', 'fr')
