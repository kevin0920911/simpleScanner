import Reader
import Token
import enum
import string

DIGITAL = string.digits
LETTER  = string.ascii_letters
KEYWORD = ['int' , 'float' , 'bool' , 'void' , 'while' , 'if' , 'else' , 'for' , 'return']

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
    IDENTITY = enum.auto()
    identity_with_underline = enum.auto()
    IDENTITY_UNDERLINE = enum.auto()

    #BINARY PART 
    MORE_THAN_STATE = enum.auto()
    LESS_THAN_STATE = enum.auto()
    DIVISON_STATE = enum.auto()

    #Comment PART
    inside_comment = enum.auto()
    COMMENT = enum.auto()
    DOUBLE_SLASH = enum.auto()
    
class Scanner():
    def __init__(self, text:str) -> None:
        self.reader = Reader.Reader(text)
        self.buffer = ""
        self.currentState = ScannerState.START
        self.tokens = []
    def nextState(self) -> None:
        match self.currentState: 
            case ScannerState.START:
                self.__start()
            case ScannerState.INTERGER:
                self.__interger()
            case ScannerState.float_dot:
                self.__float_dot()
            case ScannerState.DECIMAL_POINT:
                self.__decimal_point()
            case ScannerState.exponential_start:
                self.__exponential_start()
            case ScannerState.exponential_with_sign:
                self.__exponential_with_sign()
            case ScannerState.EXPONENTIAL:
                self.__exponential()
            case ScannerState.LESS_THAN_STATE:
                self.__less_than_state()
            case ScannerState.MORE_THAN_STATE:
                self.__more_than_state()
            case ScannerState.DIVISON_STATE:
                self.__division()
            case ScannerState.inside_comment:
                self.__inside_comment()
            case ScannerState.COMMENT:
                self.__commnet()
            case ScannerState.IDENTITY:
                self.__identuty()
            case ScannerState.identity_with_underline:
                self.__identity_with_underline()
            case ScannerState.IDENTITY_UNDERLINE:
                self.__identity_underline()
            case ScannerState.DOUBLE_SLASH:
                self.__double_slash()
    def makeToken(self, type:Token.TokenType) -> None:
        newToken = Token.Token(type, self.buffer)
        self.buffer = ''
        self.tokens.append(newToken) 
    def __start(self):
        c = self.reader.nextChar()
        if c in DIGITAL:
            self.currentState = ScannerState.INTERGER
            self.buffer += c
        elif c in ".":
            self.currentState = ScannerState.float_dot
            self.buffer += c
        elif c in LETTER:
            self.currentState = ScannerState.IDENTITY
            self.buffer += c
        elif c in "+-*":
            self.buffer += c
            self.makeToken(Token.TokenType.BINARY)
            self.currentState = ScannerState.START
        elif c in "<":
            self.buffer += c 
            self.currentState = ScannerState.LESS_THAN_STATE
        elif c in ">=":
            self.buffer += c  
            self.currentState = ScannerState.MORE_THAN_STATE
        elif c in "/":
            self.buffer += c
            self.currentState = ScannerState.DIVISON_STATE
        elif c in ";()[]{}":
            self.buffer += c
            self.makeToken(Token.TokenType.SEPARATORS)
            self.currentState = ScannerState.START
        elif c in "\t\r\n ":
            self.buffer += c
            self.makeToken(Token.TokenType.LAYOUT)
            self.currentState = ScannerState.START
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
    def __less_than_state(self):
        c = self.reader.nextChar()
        if c in ">=":
            self.buffer += c
            self.makeToken(Token.TokenType.BINARY)
            self.currentState = ScannerState.START
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.BINARY)
            self.currentState = ScannerState.START
    def __more_than_state(self):
        c = self.reader.nextChar()
        if c in "=":
            self.buffer += c
            self.makeToken(Token.TokenType.BINARY)
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.BINARY)
            self.currentState = ScannerState.START
    def __division(self):
        c = self.reader.nextChar()

        if c in '*':
            self.currentState = ScannerState.inside_comment
            self.buffer += c
        elif c in '/':
            self.currentState = ScannerState.DOUBLE_SLASH
            self.buffer += c
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.BINARY)
            self.currentState = ScannerState.START
    def __inside_comment(self):
        c = self.reader.nextChar()

        if c in '*':
            self.buffer += c
            self.currentState = ScannerState.COMMENT
        else:
            self.buffer += c
            self.currentState = ScannerState.inside_comment
    def __commnet(self):
        c = self.reader.nextChar() 
        if c in '/':
            self.buffer += c
            self.makeToken(Token.TokenType.COMMENTS)
            self.currentState = ScannerState.START
        else:
            self.buffer += c
            self.currentState = ScannerState.inside_comment
    def __identuty(self):
        c = self.reader.nextChar()
        if c in LETTER+DIGITAL:
            self.buffer += c
            self.currentState = ScannerState.IDENTITY
        elif c in '_':
            self.buffer += c
            self.currentState = ScannerState.identity_with_underline
        else:
            self.reader.retracted(1)
            self.currentState = ScannerState.START
            
            if self.buffer in KEYWORD:
                self.makeToken(Token.TokenType.KEYWORD)
            else:
                self.makeToken(Token.TokenType.IDENTITY)
    def __identity_with_underline(self):
        c = self.reader.nextChar()

        if c in LETTER+DIGITAL:
            self.buffer += c
            self.currentState = ScannerState.IDENTITY_UNDERLINE
        else:
            raise Exception(f'token error unkone <{self.buffer}>')
    def __identity_underline(self):
        c = self.reader.nextChar()

        if c in LETTER+DIGITAL:
            self.buffer += c
            self.currentState = ScannerState.IDENTITY_UNDERLINE
        elif c in "_":
            self.buffer += c
            self.currentState = ScannerState.identity_with_underline
        else:
            self.reader.retracted(1)
            self.makeToken(Token.TokenType.IDENTITY)
            self.currentState = ScannerState.START
    def __double_slash(self):
        c = self.reader.nextChar()

        if c in '\n':
            self.currentState = ScannerState.START
            self.makeToken(Token.TokenType.COMMENTS)
        else:
            self.currentState = ScannerState.DOUBLE_SLASH
            self.buffer += c


