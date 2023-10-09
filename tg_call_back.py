import requests
import json


bot_token = 'bot_token'
# У бота должна ОТСУТСВОВАТЬ привязка к webHook
URL = 'https://api.telegram.org/bot'


keyboard = {
    # Не смог починить кнопки. Отрисовываются, но при нажатии нет никакой реакции.
    "inline_keyboard": [
        [{
            "text": "button1",
            "callback_data": "/but1"
        },
            {
                "text": "button2",
                "callback_data": "/but2"
            },
        ]]}




def run():
    update_id = 0
    while True:
        tg_requests = requests.get(f'{URL}{bot_token}/getUpdates?offset={update_id + 1}&timeout=5').json()
        print(*tg_requests)
        if tg_requests['result']:
            for tg_request in tg_requests['result']:
                update_id = tg_request['update_id']
                if 'message' in tg_request:
                    user_message = tg_request['message']
                    print(f"ID пользователя: {user_message['chat']['id']}, Сообщение: {user_message['text']}")
                    if user_message['text'] == '1':
                        text = 'text'
                        chat_id = user_message['chat']['id']
                        keyboard_json = json.dumps(keyboard)
                        data = {
                            'chat_id': chat_id,
                            'text': text,
                            # 'parse_mode': 'HTML',
                            'reply_markup': keyboard_json,
                        }

                        respons = requests.get(f'{URL}{bot_token}/sendMessage', params=data)
                        print(respons.text)
                elif 'callback_query' in tg_request:
                    callback_data = tg_request['callback_query']['data']
                    print(f'Нажата кнопка с callback_data: {callback_data}')


if __name__ == '__main__':
    run()
