import enum


class TokenType(enum.Enum):
    SEPARATORS = enum.auto()
    BINARY     = enum.auto()
    COMMENTS   = enum.auto()
    LAYOUT     = enum.auto()
    KEYWORD    = enum.auto()
    IDENTITY   = enum.auto()
    INTEGER    = enum.auto()
    FLOAT      = enum.auto()  


class Token:
    def __init__(self, type: TokenType, text: str):
        self.type = type
        self.text = text

    def __eq__(self, other: 'Token'):
        return isinstance(other, Token) and self.type == other.type and self.text == other.text

    def __repr__(self):
        return f"<{self.type.name}, '{self.text.encode("unicode_escape").decode()}'>"
