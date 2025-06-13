import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from Scanner import Scanner, ScannerState
from Token import Token, TokenType

END_STATE = [
            ScannerState.INTERGER,
            ScannerState.DECIMAL_POINT,
            ScannerState.EXPONENTIAL,
            ScannerState.IDENTITY,
            ScannerState.IDENTITY_UNDERLINE,
            ScannerState.MORE_THAN_STATE,
            ScannerState.LESS_THAN_STATE,
            ScannerState.DIVISON_STATE,
            ScannerState.DOUBLE_SLASH,
            ScannerState.COMMENT
        ]

class TestScanner(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s = None
    def tearDown(self):
        del self.s
        self.s = None
    def text2tokens(self, text: str):    
        self.s = Scanner(text)
        while not self.s.reader.eof():
            self.s.nextState()
        if self.s.currentState in END_STATE:
            self.s.nextState()
        elif not self.s.currentState == ScannerState.START:
            self.s.nextState()
        return self.s.tokens

    # Test for true condition
    def test_single_separator(self):
        tokens = self.text2tokens(';')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ';')])
        tokens = self.text2tokens('(')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '(')])
        tokens = self.text2tokens(')')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ')')])
        tokens = self.text2tokens('[')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '[')])
        tokens = self.text2tokens(']')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ']')])
        tokens = self.text2tokens('{')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '{')])
        tokens = self.text2tokens('}')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '}')])

    def test_multiple_separator(self):
        tokens = self.text2tokens('(){')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '('), Token(TokenType.SEPARATORS, ')'), Token(TokenType.SEPARATORS, '{')])
        tokens = self.text2tokens('};')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, '}'), Token(TokenType.SEPARATORS, ';')])
        tokens = self.text2tokens('];')
        self.assertEqual(tokens, [Token(TokenType.SEPARATORS, ']'), Token(TokenType.SEPARATORS, ';')])

    def test_binary_operator(self):
        tokens = self.text2tokens('+')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '+')])
        tokens = self.text2tokens('-')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '-')])
        tokens = self.text2tokens('*')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '*')])
        tokens = self.text2tokens('/')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '/')])
        tokens = self.text2tokens('<=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<=')])
        tokens = self.text2tokens('>=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '>=')])
        tokens = self.text2tokens('<>')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<>')])
        tokens = self.text2tokens('<')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '<')])
        tokens = self.text2tokens('>')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '>')])
        tokens = self.text2tokens('=')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '=')])
        tokens = self.text2tokens('==')
        self.assertEqual(tokens, [Token(TokenType.BINARY, '==')])

    def test_keyword(self):
        tokens = self.text2tokens('int')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'int')])
        tokens = self.text2tokens('float')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'float')])
        tokens = self.text2tokens('bool')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'bool')])
        tokens = self.text2tokens('void')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'void')])
        tokens = self.text2tokens('while')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'while')])
        tokens = self.text2tokens('if')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'if')])
        tokens = self.text2tokens('else')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'else')])
        tokens = self.text2tokens('for')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'for')])
        tokens = self.text2tokens('return')
        self.assertEqual(tokens, [Token(TokenType.KEYWORD, 'return')])

    def test_comment(self):
        tokens = self.text2tokens('/* Hello World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello World */')])
        tokens = self.text2tokens('/* Hello World\nBye World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello World\nBye World */')])
        tokens = self.text2tokens('/* Hello /* World */')
        self.assertEqual(tokens, [Token(TokenType.COMMENTS, '/* Hello /* World */')])

    def test_single_layout(self):
        tokens = self.text2tokens(' ')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, ' ')])
        tokens = self.text2tokens('\t')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\t')])
        tokens = self.text2tokens('\r')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\r')])
        tokens = self.text2tokens('\n')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\n')])

    def test_multiple_layout(self):
        tokens = self.text2tokens('   ')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' ')])
        tokens = self.text2tokens('\r\n  \t')
        self.assertEqual(tokens, [Token(TokenType.LAYOUT, '\r'), Token(TokenType.LAYOUT, '\n'), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, ' '), Token(TokenType.LAYOUT, '\t')])

    def test_integer(self):
        tokens = self.text2tokens('0')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '0')])
        tokens = self.text2tokens('1')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '1')])
        tokens = self.text2tokens('2')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '2')])
        tokens = self.text2tokens('3')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '3')])
        tokens = self.text2tokens('4')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '4')])
        tokens = self.text2tokens('5')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '5')])
        tokens = self.text2tokens('6')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '6')])
        tokens = self.text2tokens('7')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '7')])
        tokens = self.text2tokens('8')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '8')])
        tokens = self.text2tokens('9')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '9')])
        tokens = self.text2tokens('9')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '9')])
        tokens = self.text2tokens('12345')
        self.assertEqual(tokens, [Token(TokenType.INTEGER, '12345')])

    def test_float(self):
        tokens = self.text2tokens('0.1')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '0.1')])
        tokens = self.text2tokens('2.34')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '2.34')])
        tokens = self.text2tokens('56.789')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '56.789')])
        tokens = self.text2tokens('.321')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '.321')])
        tokens = self.text2tokens('0.3E7')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '0.3E7')])
        tokens = self.text2tokens('85.92E+50')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '85.92E+50')])
        tokens = self.text2tokens('.001E-109')
        self.assertEqual(tokens, [Token(TokenType.FLOAT, '.001E-109')])

    def test_id(self):
        tokens = self.text2tokens('a')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'a')])
        tokens = self.text2tokens('A0')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'A0')])
        tokens = self.text2tokens('QAZ012wsx987')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'QAZ012wsx987')])
        tokens = self.text2tokens('q_1_W_2_e')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'q_1_W_2_e')])
        tokens = self.text2tokens('TREWQ_1234')
        self.assertEqual(tokens, [Token(TokenType.IDENTITY, 'TREWQ_1234')])
    def test_double_slash(self):
        tokens = self.text2tokens("//this is a test ")
        self.assertEqual(tokens, [
            Token(TokenType.COMMENTS, '//this is a test ')
        ])

        tokens = self.text2tokens('//this is a test \n')
        self.assertEqual(tokens, [
            Token(TokenType.COMMENTS, '//this is a test '),
            Token(TokenType.LAYOUT, '\n')
        ])

    def test_complex(self):
        tokens = self.text2tokens('void test(){ int numbers[16] = {0}; }')
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

        tokens = self.text2tokens('//Hi I wanna sleep\naaa=1')
        self.assertEqual(
            tokens,[
                Token(TokenType.COMMENTS, '//Hi I wanna sleep'),
                Token(TokenType.LAYOUT, '\n'),
                Token(TokenType.IDENTITY, 'aaa'),
                Token(TokenType.BINARY, '='),
                Token(TokenType.INTEGER, '1')
            ]
        )
    # Test for error condition
    def test_start_error(self):
        try:
            tokens = self.text2tokens('\\hi I am error test')
            self.assertFalse(tokens)
        except Exception as e:
            self.assertEqual(self.s.currentState, ScannerState.START)
            self.assertIn("token error", str(e))

    def test_float_dot_error(self):
        try:
            tokens = self.text2tokens('1.')
            self.assertFalse(tokens)
        except Exception as e:
            self.assertEqual(self.s.currentState, ScannerState.float_dot)
            self.assertIn("token error", str(e))
            
    def test_exponential_with_sign_error(self):
        try:
            tokens = self.text2tokens('.2E+-')
            self.assertFalse(tokens)
        except Exception as e:
            self.assertEqual(self.s.currentState, ScannerState.exponential_with_sign)
            self.assertIn("token error", str(e))

    def test_exponential_start_error(self):
        try:
            tokens = self.text2tokens('.2E/')
            self.assertFalse(tokens)
        except Exception as e:
            self.assertEqual(self.s.currentState, ScannerState.exponential_start)
            self.assertIn("token error", str(e))
    
    def test_identity_with_underline(self):
        try:
            tokens = self.text2tokens('eee__')
            self.assertFalse(tokens)
        except Exception as e:
            self.assertEqual(self.s.currentState, ScannerState.identity_with_underline)
            self.assertIn("token error", str(e))

if __name__ == "__main__":
    unittest.main()