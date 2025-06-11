# Scanner Implement 

## Token Types
- Separators and Brackets：`;` | `(` | `)` | `[` | `]` | `{` | `}`
- Binary Operators：`+` | `-` | `*` | `/` | `<=` | `>=` | `<>` | `<` | `>` | `=` | `==`
- Comments：`/\*[\s\S]*\*/`
- Layout：` ` | `\t` | `\r` | `\n`
- Keyword：`int` | `float` | `bool` | `void` | `while` | `if` | `else` | `for` | `return`
- ID：`[a-zA-Z][a-zA-Z0-9]*(_[a-zA-Z0-9]+)*`
- integer：`[0-9]+`
- float：`[0-9]*.[0-9]+(E(+ |- |ε)[0-9]+|ε)`

## The file tree structure
```
.
├── README.md
├── src
│   ├── reader.py
│   ├── main.py
│   ├── scanner.py
│   └── token.py
```



## Module Descriptions
### `reader.py`
這個檔案含有`Reader` 的類別，他提供讀取字串的功能
- `nextChar()`: 把下一個字元傳回
- `retracted(n)`: 反回`n`個字元

### `scanner.py`
這個檔案含有`Scanner` 的類別，他提供掃描字串的功能
- `makeToken`: 製造新的token，並加入token list 中
- `nextState`: 產生下一個State，如果下一個State 可以製造token 就製造出來

### `token.py`
這個檔案含有`Token`, `TokenType` 的類別，他提供建立token的功能
- `TokenType`: 枚舉 Token 類型
- `Token`: 建立 Token 的類別
    - `self.type`: Token 的類型
    - `self.text`: 該 Token 的字串




## How to use
```bash
python3 src/main.py <testFile>
```
- 接著結果會在`token.l` 之中
