import Reader
import Token
import enum

class ScannerState(enum.Enum):
    START = enum.auto()

class Scanner():
    def __init__(self, text:str) -> None:
        self.reader = Reader.Reader(text)
        self.currentState = ScannerState.START
        self.tokens = []
    
    def nextToken(self) -> Token.TokenType:
        #TODO: nextToken
        pass

    def generateToken(self) -> None:
        #TODO: generate token
        pass 