import Scanner
import sys

if len(sys.argv) == 2:
    path = sys.argv[1]
    with open(path, mode='r') as f:
        test = f.read()
else:
    test = "1.23 aaa bbb"

scanner = Scanner.Scanner(test)
while not scanner.reader.eof():
    scanner.nextState()

for token in scanner.tokens:
    print(token)