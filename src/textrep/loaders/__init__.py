"""
File text extraction loaders.
"""

from .registry import get_loader, supported_extensions

__all__ = [
    "get_loader",
    "supported_extensions",
]
