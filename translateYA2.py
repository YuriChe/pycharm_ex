import requests

def translate_line(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    req_line = f'{URL}?key=trnsl.1.1.20200113T220016Z.35e595bb4a95f4bb.dbfbb76e4d8dd77d50f2f3b8a06ee20500c10b54&text={text}&lang={lang}'

    res = requests.post(req_line)
    result_of_trans = res.json()['text'][0]

    return result_of_trans

def translate_ya(url_what, url_result, lang_text, lang_to= 'ru'):

    lang_to_translate = f'{lang_text}-{lang_to}'
    with open(url_what, 'r', encoding= 'utf8') as file_in, open(url_result, 'w', encoding= 'utf8') as file_out:
            to_translate = file_in.read()
            file_out.write(translate_line(to_translate, lang_to_translate))

translate_ya('DE.txt', 'DE-RU.txt', 'de')
translate_ya('ES.txt', 'ES-RU.txt', 'es')
translate_ya('FR.txt', 'FR-RU.txt', 'fr')


