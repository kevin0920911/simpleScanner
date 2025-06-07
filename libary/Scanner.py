import Reader
import Token
import enum
import string

DIGITAL = string.digits
LETTER  = string.ascii_letters


class ScannerState(enum.Enum):
    START = enum.auto()

    #NUMBER PART
    INTERGER = enum.auto()
    FLOAT_DOT = enum.auto()
    DECIMAL_POINT = enum.auto()
    EXPONENTIAL_START = enum.auto()
    EXPONENTIAL_WITH_SIGN = enum.auto()
    EXPONENTIAL_PART = enum.auto()

    #IDENTITY PART
    


class Scanner():
    def __init__(self, text:str) -> None:
        self.reader = Reader.Reader(text)
        self.buffer = ""
        self.currentState = ScannerState.START
        self.tokens = []
    
    def nextState(self) -> None:
        #TODO: nextToken
        match self.currentState: 
            case ScannerState.START:
                c = self.reader.nextChar()
                if c in DIGITAL:
                    self.currentState = ScannerState.INTERGER
                    self.buffer += c
                elif c in LETTER:
                    #TODO: ID
                    pass
                elif c in "+-*":
                    #TODO: Binary
                    pass
                elif c in "<":
                    #TODO: Binary
                    pass
                elif c in ">=":
                    #TODO: Binary
                    pass
                elif c in "/":
                    #TODO: maybe comments
                    pass
                elif c in ";()[]\{\}":
                    #TODO: Seperator
                    pass
                elif c in "\t\r\n ":
                    #TODO: Layout
                    pass
                else:
                    raise('token error')
    def makeToken(self, type:Token.TokenType) -> None:
        #TODO: generate token
        pass 