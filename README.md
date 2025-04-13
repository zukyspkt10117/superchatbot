# SuperChatbox

SuperChatbox is an intelligent chatbot application designed to provide seamless interactions and valuable insights. The project includes the following key components:

- **`app.py`**: The main application file that handles the chatbot's core functionality, including user interaction and response generation.
- **`get_gas_price.py`**: A utility module that fetches real-time gas price data, integrating external information into the chatbot's responses.

SuperChatbox combines conversational AI with real-time data integration to deliver a dynamic and engaging user experience.

## SETUP NGROK

NGROK token:
```bash {cmd}
ngrok config add-authtoken 2vduGmrFswcvVJ9trfCw54ByndA_3AdQh9Lp4KprvU66CE9cN
```

- Bước 1: Tạo một tunnel với ngrok
Tạo một tunnel với ngrok
Chạy ngrok để chuyển tiếp lưu lượng HTTP từ Internet đến máy local của bạn.
Giả sử Flask API của bạn đang chạy trên cổng 5000, bạn mở terminal và chạy:
```bash {cmd}
ngrok http 5000
```

- Bước 2: Cập nhật Webhook cho Telegram Bot

```bash {cmd}
curl -F "url=http://1234abcd.ngrok.io/webhook" https://api.telegram.org/bot7313717335:AAEmTTF3lhsrow2bupSJB1ZdYXo6bgD2y9k/setWebhook
```

## DEPLOY APP

Open terminal then run:
```bash {cmd}
python3 ./app.py
```