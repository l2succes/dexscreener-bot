import requests

def send_telegram_message(bot_token, message):
    """Send a message to a Telegram chat via bot."""
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': "6018455628",
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(send_url, data=data)
    return response.json()


def filter_pairs(data, bot_token):
    current_time = datetime.now(pytz.utc)
    recent_pairs = []
    chat_id = "6018455628"

    for pair in data['pairs']:
        creation_time = datetime.fromtimestamp(pair['pairCreatedAt'] / 1000, pytz.utc)
        time_difference = current_time - creation_time

        if time_difference < timedelta(hours=200):  # Adjust as necessary
            coin_name = pair['baseToken']['name']
            pair_address = pair['pairAddress']
            pair_link = pair['url']
            message = f"New pair alert: {coin_name}\nAddress: {pair_address}\nLink: {pair_link}"
            send_telegram_message(bot_token, message)
            recent_pairs.append(pair)

    return recent_pairs


# Usage example
bot_token = '7010866436:AAHdBGnzbf_CeUUu4T6fLM6yy15Ygg_GIBk'
data = fetch_data("BASE WETH")  # Assuming you have defined fetch_data() previously

filtered_pairs = filter_pairs(data, bot_token)