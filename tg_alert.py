import requests

TOKEN = 'Token'
URL = 'https://api.telegram.org/bot'

# Просто скопировал из salebot
tg_request = {"update_id":607319979,"callback_query":{"id":"4878463651406889152","from":{"id":1135855831,"is_bot":False,"first_name":"Николай","last_name":"Писарев","username":"Nikolay_Pisarev","language_code":"ru"},"message":{"message_id":409,"from":{"id":6605524695,"is_bot":True,"first_name":"portfolio_pisarev","username":"portfolio_pisarev_bot"},"chat":{"id":1135855831,"first_name":"Николай","last_name":"Писарев","username":"Nikolay_Pisarev","type":"private"},"date":1696796757,"edit_date":1696819446,"text":"Какая красивая елочка\nНиколай, установим звезду?","reply_markup":{"inline_keyboard":[[{"text":"Да","callback_data":"Да"},{"text":"Вернуться в главно меню","callback_data":"\/start"}]]}},"chat_instance":"8274356876315667667","data":"Да"}}


def answer_callback_query_show_alert():
    request_name = 'answerCallbackQuery'
    text = 'text'
    callback_query = tg_request['callback_query']
    callback_query_id = callback_query["id"]
    # callback_query_id = 4878463651406889152

    data = {
        'text': text,
        # 'parse_mode': 'HTML',
        'callback_query_id': callback_query_id,
        'show_alert': True,
    }

    respons = requests.get(f'{URL}{TOKEN}/{request_name}', params=data)
    print(respons.text)
    # {"ok":false,"error_code":400,"description":"Bad Request: query is too old and response timeout expired or query ID is invalid"}
    # Видимо answerCallbackQuery отрабатывает на salebot