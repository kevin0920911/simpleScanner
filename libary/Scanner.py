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
    float_dot = enum.auto()
    DECIMAL_POINT = enum.auto()
    exponential_start = enum.auto()
    exponential_with_sign = enum.auto()
    EXPONENTIAL = enum.auto()

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
                self.__start()
            case ScannerState.INTERGER:
                self.__interger()
            case ScannerState.float_dot:
                self.__float_dot()
        
    def makeToken(self, type:Token.TokenType) -> None:
        #TODO: generate token
        pass 

    def __start(self):
        c = self.reader.nextChar()
        if c in DIGITAL:
            self.currentState = ScannerState.INTERGER
            self.buffer += c
        elif c in ".":
            self.currentState = ScannerState.float_dot
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
            raise Exception(f'token error unkone <{self.buffer}>')
        
    def __float_dot(self):
        c = self.reader.nextChar()

        if c in DIGITAL:
            self.currentState = ScannerState.DECIMAL_POINT
            self.buffer += c
        else:
            raise Exception(f'token error unkone <{self.buffer}>')
    
    def __decimal_point(self):
        c = self.reader.nextChar()

        if c in "E":
            self.currentState = ScannerState.exponential_start
            self.buffer += c
        elif c in DIGITAL:
            self.currentState = ScannerState.DECIMAL_POINT
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.FLOAT)
            self.currentState = ScannerState.START

    def __interger(self):
        c = self.reader.nextChar()

        if c in DIGITAL:
            self.currentState = ScannerState.INTERGER
            self.buffer += c
        elif c in '.':
            self.currentState = ScannerState.float_dot
            self.buffer += c
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.INTEGER)
            self.currentState = ScannerState.START
    
    def __exponential_start(self):
        c = self.reader.nextChar()

        if c in "+-":
            self.currentState = ScannerState.exponential_with_sign
            self.buffer += c
        elif c in DIGITAL:
            self.currentState = ScannerState.EXPONENTIAL
            self.buffer += c
        else:
           raise Exception(f'token error unkone <{self.buffer}>')
    
    def __exponential_with_sign(self):
        c = self.reader.nextChar()

        if c in DIGITAL:
            self.currentState = ScannerState.EXPONENTIAL
            self.buffer += c
        else:
            raise Exception(f'token error unkone <{self.buffer}>')
    
    def __exponential(self):
        c = self.reader.nextChar()

        if c in DIGITAL:
            self.currentState = ScannerState.EXPONENTIAL
            self.buffer += c
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.FLOAT)
            self.currentState = ScannerState.START
