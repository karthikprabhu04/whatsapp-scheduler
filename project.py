import pywhatkit
from datetime import datetime, timedelta
import time


def main():
    phone = input("Phone number (with country code): ")
    message = input("Message: ")
    time_str = input("Time (YYYY-MM-DD HH:MM): ")

    if not validate_datetime(time_str):
        print("Invalid datetime format.")
        return

    hour, minute = extract_time(time_str)
    wait_until(time_str)
    send_whatsapp_message(phone, message, hour, minute)

    print("Message sent successfully!")


def validate_datetime(time_str):
    try:
        datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False


def extract_time(time_str):
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return dt.hour, dt.minute


def wait_until(time_str):
    target = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    buffer = target - timedelta(minutes=2)

    while datetime.now() < buffer:
        time.sleep(10)


def send_whatsapp_message(phone, message, hour, minute):
    pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=30)


main()