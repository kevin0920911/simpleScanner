import Reader
import Token
import enum
import string

DIGITAL = string.digits
LETTER  = string.ascii_letters


class ScannerState(enum.Enum):
    START = enum.auto()

class Scanner():
    def __init__(self, text:str) -> None:
        self.reader = Reader.Reader(text)
        self.currentState = ScannerState.START
        self.tokens = []
    
    def nextState(self) -> None:
        #TODO: nextToken
        pass

    def makeToken(self, type:Token.TokenType) -> None:
        #TODO: generate token
        pass 