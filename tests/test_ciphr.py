"""Tests for hex and unhex functions."""
import pytest
from ciphr import hex, unhex


def test_hex_basic():
    """Test basic hex encoding with simple ASCII input"""
    input_data = [b'abc']
    result = list(hex(input_data))
    assert result == [b'616263']


def test_hex_empty():
    """Test hex encoding with empty input"""
    input_data = [b'']
    result = list(hex(input_data))
    assert result == [b'']


def test_hex_special_chars():
    """Test hex encoding with special characters"""
    input_data = [b'\x00\xff\x80']
    result = list(hex(input_data))
    assert result == [b'00ff80']


def test_hex_multiple_chunks():
    """Test hex encoding with multiple chunks"""
    input_data = [b'a', b'b', b'c']
    result = list(hex(input_data))
    assert result == [b'61', b'62', b'63']


def test_unhex_basic():
    """Test basic hex decoding with valid input"""
    input_data = [b'616263']
    result = list(unhex(input_data))
    assert result == [b'abc']


def test_unhex_empty():
    """Test hex decoding with empty input"""
    input_data = [b'']
    result = list(unhex(input_data))
    assert result == [b'']


def test_unhex_special_chars():
    """Test hex decoding with special characters"""
    input_data = [b'00ff80']
    result = list(unhex(input_data))
    assert result == [b'\x00\xff\x80']


def test_unhex_multiple_chunks():
    """Test hex decoding with multiple chunks"""
    input_data = [b'61', b'62', b'63']
    result = list(unhex(input_data))
    assert result == [b'a', b'b', b'c']


def test_unhex_invalid_input():
    """Test hex decoding with invalid hex input"""
    input_data = [b'zz']  # invalid hex characters
    with pytest.raises(ValueError):
        list(unhex(input_data))


def test_unhex_odd_length():
    """Test hex decoding with odd-length input"""
    input_data = [b'6']  # single hex digit is invalid
    with pytest.raises(ValueError):
        list(unhex(input_data))