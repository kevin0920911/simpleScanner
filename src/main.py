import Scanner
import sys


END_STATE = [
    Scanner.ScannerState.INTERGER,
    Scanner.ScannerState.DECIMAL_POINT,
    Scanner.ScannerState.EXPONENTIAL,
    Scanner.ScannerState.IDENTITY,
    Scanner.ScannerState.IDENTITY_UNDERLINE,
    Scanner.ScannerState.MORE_THAN_STATE,
    Scanner.ScannerState.LESS_THAN_STATE,
    Scanner.ScannerState.DIVISON_STATE,
    Scanner.ScannerState.COMMENT
]
if len(sys.argv) == 2:
    path = sys.argv[1]
    with open(path, mode='r') as f:
        test = f.read()
else:
    test = "1.23 aaa bbb"

scanner = Scanner.Scanner(test)
while not scanner.reader.eof():
    scanner.nextState()

if scanner.currentState in END_STATE:
    scanner.nextState()
elif not scanner.currentState == Scanner.ScannerState.START:
    scanner.nextState()
    
f = open('token.l', mode = 'w')
for token in scanner.tokens:
    f.write(str(token)+'\n')