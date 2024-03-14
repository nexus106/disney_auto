from selenium import webdriver
import chromedriver_binary
import time
import datetime
import random
import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://reserve.tokyodisneyresort.jp/ticket/search/"


def str_date():
    datetime_format = datetime.datetime.now()
    datetime_str = datetime_format.strftime("%Y/%m/%d %H:%M:%S")
    return datetime_str


def send_line_notify(notification_message):
    line_notify_token = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)

    while True:
        x = random.randint(0, 2)
        driver.get(URL)
        time.sleep(10)
        busy_text = driver.find_elements_by_xpath("/html/body/div/div[1]/div/div/p[1]")
        if len(busy_text) > 0 and busy_text[0].text.find("つながりにくい"):
            print("エラーページ")
            print(str(x) + "秒待つ")
            time.sleep(x)
        else:
            print("アクセス成功")
            break
