# Scanner Implement 

## The file tree structure
```
.
├── README.md
├── main.py
├── libary
│   ├── reader.py
│   ├── scanner.py
│   └── token.py
```

## File Descriptions
### `reader.py`
這個檔案含有`Reader` 的類別，他提供讀取字串的功能
- `nextChar()`: 把下一個字元傳回
- `retracted(n)`: 反回`n`個字元

### `scanner.py`
這個檔案含有`Scanner` 的類別，他提供掃描字串的功能

### `token.py`
這個檔案含有`Token`, `TokenType` 的類別，他提供建立token的功能
- `TokenType`: 枚舉 Token 類型
- `Token`: 建立 Token 的類別
    - `self.type`: Token 的類型
    - `self.text`: 該 Token 的字串

## Token Types
- Separators and Brackets： `;` | `(` | `)` | `[` | `]` | `{` | `}`
- Binary Operators：`+` | `-` | `*` | `/` | `<=` | `>=` | `<>` | `<` | `>` | `=` | `==`
- Comments: `/\*[\s\S]*\*/`
- Layout: ` ` | `\t` | `\r` | `\n`
- Keyword: `int` | `float` | `bool` | `void` | `while` | `if` | `else` | `for` | `return`
- ID: `[a-zA-Z][a-zA-Z0-9]*(_[a-zA-Z0-9]+)*`
- integer: `[0-9]+`
- float: `[0-9]*.[0-9]+(E(+ |- |ε)[0-9]+|ε)`