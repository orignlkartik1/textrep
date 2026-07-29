"""
TextRep exception types.
"""


class TextRepError(Exception):
    """
    Base exception for TextRep errors.
    """


class UnsupportedFileTypeError(TextRepError, ValueError):
    """
    Raised when TextRep cannot load a file extension.
    """


class MissingDependencyError(TextRepError, ImportError):
    """
    Raised when a loader requires an optional dependency.
    """
