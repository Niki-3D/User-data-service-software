from unittest.mock import patch
import pytest
from src.main import ping

def test_ping_exists():
    assert ping

def test_ping_returns_right_value():
    actual = ping()
    assert actual == "pong"
