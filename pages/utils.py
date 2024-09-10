import requests
from urllib.parse import quote


def send_telegram_notification(message):
    bot_token = ""
    bot_chat_id = ""

    # escape special characters
    special_characters = [".", "-", "+", "(", ")"]
    for char in special_characters:
        message = message.replace(char, f"\\{char}")

    send_message = (
        f"https://api.telegram.org/bot{bot_token}/sendMessage"
        f"?chat_id={bot_chat_id}&parse_mode=MarkdownV2&text={quote(message)}"
    )

    try:
        response = requests.get(send_message)
        json_response = response.json()
        if response.status_code != 200 or not json_response.get("ok"):
            print("Error sending telegram message: %s", json_response)
            print("Actual message: %s", message)
    except Exception as err:
        print("Error sending telegram message: %s", err)
