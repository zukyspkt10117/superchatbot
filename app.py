from flask import Flask, request
import requests
import get_gas_price

app = Flask(__name__)

BOT_TOKEN = '7313717335:AAEmTTF3lhsrow2bupSJB1ZdYXo6bgD2y9k'  # Thay bằng token bot của bạn
# chat_id = '7043128381'

# Dữ liệu danh sách gas và location
gas_list = [
    "Station 1: 15,19 SEK",
    "Station 2: 15,21 SEK",
    "Station 3: 15,29 SEK"
]

location_list = [
    "Location 1: 12.34, 56.78",
    "Location 2: 23.45, 67.89",
    "Location 3: 34.56, 78.90"
]

# Route nhận dữ liệu từ Telegram (Webhook)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        # Kiểm tra xem có lệnh /price hay không
        if text == '/qprice':
            # Gọi hàm get_gas_price để lấy dữ liệu
            result = get_gas_price.get_gas_price_st1()
            full_text = ""
            for i, (name, address, price, date, gg_address) in enumerate(result, start=1):
                maps_url = f"https://www.google.com/maps?q={gg_address.replace(' ', '+')}"
                full_text += f"{i}. Station: {name}\nAddress: <a href='{maps_url}'> {address}</a>\n95 (E10): <b>{price}</b> (updated: {date})\n\n"
            send_message(chat_id, full_text)  # Gửi lại dữ liệu cho người dùng

        elif text == '/price10':
            # Gọi hàm get_gas_price để lấy dữ liệu
            result = get_gas_price.get_gas_price_10()
            full_text = ""
            for i, (name, address, price, date, gg_address) in enumerate(result, start=1):
                maps_url = f"https://www.google.com/maps?q={gg_address.replace(' ', '+')}"
                full_text += f"{i}. Station: {name}\nAddress: <a href='{maps_url}'> {address}</a>\n95 (E10): <b>{price}</b> (updated: {date})\n\n"
            send_message(chat_id, full_text)  # Gửi lại dữ liệu cho người dùng

        elif text == '/location':
            send_location_list(chat_id)

        elif text == '/gaslist':
            send_location_list(chat_id)
        
        elif text == '/help':
            send_message(chat_id, "Gõ /qprice để xem giá xăng ở Gustaf Dalénsgatan 21\nGõ /price10 để xem top giá xăng ở các thấp nhất \n" \
                        "Gõ /location để xem danh sách các địa điểm\nGõ /gaslist để xem danh sách các trạm xăng\nGõ /help để xem tất cả các lệnh được hỗ trợ")
        elif text == '/start':
            send_message(chat_id, "Chào bạn! Chào mừng đến với Chatbox của Zuky\nGõ /help để xem tất cả các lệnh được hỗ trợ.")
        elif text.startswith('/'):  # Xử lý các lệnh con (subcommands) như /1, /2
            handle_subcommand(chat_id, text)
        else:
            send_message(chat_id, "Không hiểu lệnh. Gõ /help để xem tất cả các lệnh được hỗ trợ.")

    return {'ok': True}

def send_gas_list(chat_id):
    """ Gửi danh sách gas cho người dùng """
    message = "Here are the available gas stations:\n"
    for idx, gas in enumerate(gas_list, start=1):
        message += f"/{idx} - {gas}\n"
    
    send_message(chat_id, message)

def send_location_list(chat_id):
    """ Gửi danh sách locations cho người dùng """
    message = "Here are the available locations:\n"
    for idx, location in enumerate(location_list, start=1):
        message += f"/{idx} - {location}\n"
    
    send_message(chat_id, message)

def handle_subcommand(chat_id, text):
    """ Xử lý lựa chọn của người dùng (subcommand) dựa trên lệnh chính """
    try:
        # Lấy lệnh con (ví dụ /1, /2) và xử lý
        choice = int(text[1:])  # Lấy lựa chọn sau dấu "/"
        
        # Kiểm tra lệnh chính từ lựa chọn (gaslist hoặc location)
        if text.startswith('/gaslist/'):
            if 1 <= choice <= len(gas_list):
                selected_gas = gas_list[choice - 1]
                message = f"You selected: {selected_gas}"
                send_message(chat_id, message)
            else:
                send_message(chat_id, "Invalid selection! Please choose a number between 1 and 3.")
        
        elif text.startswith('/location/'):
            if 1 <= choice <= len(location_list):
                selected_location = location_list[choice - 1]
                message = f"You selected: {selected_location}"
                send_message(chat_id, message)
            else:
                send_message(chat_id, "Invalid selection! Please choose a number between 1 and 3.")

        else:
            send_message(chat_id, "Invalid command! Please choose a valid option.")
    
    except ValueError:
        send_message(chat_id, "Invalid command! Please choose a valid option.")

# Hàm gửi tin nhắn về Telegram bot
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'  # Đảm bảo rằng parse_mode là 'HTML'
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)