import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from Scanner import Scanner, ScannerState
from Token import Token, TokenType


class TestScanner(unittest.TestCase):
    @staticmethod
    def text2tokens(text: str):
        END_STATE = [
            ScannerState.INTERGER,
            ScannerState.DECIMAL_POINT,
            ScannerState.EXPONENTIAL,
            ScannerState.IDENTITY,
            ScannerState.IDENTITY_UNDERLINE,
            ScannerState.MORE_THAN_STATE,
            ScannerState.LESS_THAN_STATE,
            ScannerState.DIVISON_STATE,
            ScannerState.COMMENT
        ]
        s = Scanner(text)
        while not s.reader.eof():
            s.nextState()
        if s.currentState in END_STATE:
            s.nextState()
        elif not s.currentState == ScannerState.START:
            s.nextState()
        return s.tokens

    def test_single_separator(self):
        tokens = TestScanner.text2tokens(';')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ';')])
        tokens = TestScanner.text2tokens('(')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '(')])
        tokens = TestScanner.text2tokens(')')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ')')])
        tokens = TestScanner.text2tokens('[')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '[')])
        tokens = TestScanner.text2tokens(']')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ']')])
        tokens = TestScanner.text2tokens('{')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '{')])
        tokens = TestScanner.text2tokens('}')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '}')])

    def test_multiple_separator(self):
        tokens = TestScanner.text2tokens('(){')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '('), Token(TokenType.SEPARATORS, ')'), Token(TokenType.SEPARATORS, '{')])
        tokens = TestScanner.text2tokens('};')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '}'), Token(TokenType.SEPARATORS, ';')])
        tokens = TestScanner.text2tokens('];')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ']'), Token(TokenType.SEPARATORS, ';')])

    def test_binary_operator(self):
        tokens = TestScanner.text2tokens('+')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '+')])
        tokens = TestScanner.text2tokens('-')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '-')])
        tokens = TestScanner.text2tokens('*')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '*')])
        tokens = TestScanner.text2tokens('/')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '/')])
        tokens = TestScanner.text2tokens('<=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<=')])
        tokens = TestScanner.text2tokens('>=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '>=')])
        tokens = TestScanner.text2tokens('<>')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<>')])
        tokens = TestScanner.text2tokens('<')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<')])
        tokens = TestScanner.text2tokens('>')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '>')])
        tokens = TestScanner.text2tokens('=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '=')])
        tokens = TestScanner.text2tokens('==')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '==')])

    def test_keyword(self):
        tokens = TestScanner.text2tokens('int')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'int')])
        tokens = TestScanner.text2tokens('float')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'float')])
        tokens = TestScanner.text2tokens('bool')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'bool')])
        tokens = TestScanner.text2tokens('void')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'void')])
        tokens = TestScanner.text2tokens('while')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'while')])
        tokens = TestScanner.text2tokens('if')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'if')])
        tokens = TestScanner.text2tokens('else')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'else')])
        tokens = TestScanner.text2tokens('for')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'for')])
        tokens = TestScanner.text2tokens('return')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'return')])

    def test_comment(self):
        tokens = TestScanner.text2tokens('/* Hello World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello World */')])
        tokens = TestScanner.text2tokens('/* Hello World\nBye World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello World\nBye World */')])
        tokens = TestScanner.text2tokens('/* Hello /* World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello /* World */')])

    def test_single_layout(self):
        tokens = TestScanner.text2tokens(' ')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, ' ')])
        tokens = TestScanner.text2tokens('\t')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\t')])
        tokens = TestScanner.text2tokens('\r')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\r')])
        tokens = TestScanner.text2tokens('\n')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\n')])

    def test_multiple_layout(self):
        tokens = TestScanner.text2tokens('   ')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' ')])
        tokens = TestScanner.text2tokens('\r\n  \t')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\r'), Token(TokenType.LAYOUT, '\n'), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, '\t')])

    def test_integer(self):
        tokens = TestScanner.text2tokens('0')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '0')])
        tokens = TestScanner.text2tokens('1')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '1')])
        tokens = TestScanner.text2tokens('2')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '2')])
        tokens = TestScanner.text2tokens('3')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '3')])
        tokens = TestScanner.text2tokens('4')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '4')])
        tokens = TestScanner.text2tokens('5')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '5')])
        tokens = TestScanner.text2tokens('6')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '6')])
        tokens = TestScanner.text2tokens('7')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '7')])
        tokens = TestScanner.text2tokens('8')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '8')])
        tokens = TestScanner.text2tokens('9')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '9')])
        tokens = TestScanner.text2tokens('9')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '9')])
        tokens = TestScanner.text2tokens('12345')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '12345')])

    def test_float(self):
        tokens = TestScanner.text2tokens('0.1')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '0.1')])
        tokens = TestScanner.text2tokens('2.34')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '2.34')])
        tokens = TestScanner.text2tokens('56.789')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '56.789')])
        tokens = TestScanner.text2tokens('.321')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '.321')])
        tokens = TestScanner.text2tokens('0.3E7')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '0.3E7')])
        tokens = TestScanner.text2tokens('85.92E+50')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '85.92E+50')])
        tokens = TestScanner.text2tokens('.001E-109')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '.001E-109')])

    def test_id(self):
        tokens = TestScanner.text2tokens('a')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'a')])
        tokens = TestScanner.text2tokens('A0')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'A0')])
        tokens = TestScanner.text2tokens('QAZ012wsx987')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'QAZ012wsx987')])
        tokens = TestScanner.text2tokens('q_1_W_2_e')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'q_1_W_2_e')])
        tokens = TestScanner.text2tokens('TREWQ_1234')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'TREWQ_1234')])

    def test_complex(self):
        tokens = TestScanner.text2tokens(r'void test(){ int numbers[16] = {0}; }')
        self.assertEqual(tokens, [
            Token(TokenType.KEYWORD, 'void'),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.IDENTITY, 'test'),
            Token(TokenType.SEPARATORS, '('),
            Token(TokenType.SEPARATORS, ')'),
            Token(TokenType.SEPARATORS, '{'),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.KEYWORD, 'int'),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.IDENTITY, 'numbers'),
            Token(TokenType.SEPARATORS, '['),
            Token(TokenType.INTEGER, '16'),
            Token(TokenType.SEPARATORS, ']'),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.BINARY, '='),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.SEPARATORS, '{'),
            Token(TokenType.INTEGER, '0'),
            Token(TokenType.SEPARATORS, '}'),
            Token(TokenType.SEPARATORS, ';'),
            Token(TokenType.LAYOUT, ' '),
            Token(TokenType.SEPARATORS, '}')
        ])
