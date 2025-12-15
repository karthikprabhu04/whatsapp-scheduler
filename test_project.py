import pytest
from unittest.mock import patch
from project import (
    validate_datetime,
    extract_time,
    send_whatsapp_message,
    wait_until
)
from datetime import datetime, timedelta

def test_validate_datetime_valid():
    assert validate_datetime("2025-12-20 09:30") is True

def test_validate_datetime_invalid():
    assert validate_datetime("20-12-2025 09:30") is False

def test_extract_time():
    hour, minute = extract_time("2025-12-20 09:30")
    assert hour == 9
    assert minute == 30

@patch("project.pywhatkit.sendwhatmsg")
def test_send_whatsapp_message(mock_send):
    send_whatsapp_message("+447000000000", "Test message", 9, 30)
    mock_send.assert_called_once_with(
        "+447000000000",
        "Test message",
        9,
        30
    )

@patch("project.time.sleep", return_value=None)
def test_wait_until(mock_sleep):
    future_time = (datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
    wait_until(future_time)
    assert mock_sleep.called
