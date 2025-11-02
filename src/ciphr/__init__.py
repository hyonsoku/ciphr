"""
Ciphr - A Python CLI tool for cryptographic and encoding operations on data streams
"""
from typing import Iterator


def hex(data: Iterator[bytes]) -> Iterator[bytes]:
    """
    Encode bytes to hexadecimal.

    Args:
        data: Input bytes iterator

    Returns:
        Iterator of hex-encoded bytes

    Example:
        >>> list(hex([b'abc']))
        [b'616263']
    """
    for chunk in data:
        yield chunk.hex().encode('ascii')


def unhex(data: Iterator[bytes]) -> Iterator[bytes]:
    """
    Decode hexadecimal to bytes.

    Args:
        data: Input hex string iterator

    Returns:
        Iterator of decoded bytes

    Example:
        >>> list(unhex([b'616263']))
        [b'abc']
    """
    for chunk in data:
        yield bytes.fromhex(chunk.decode('ascii'))
