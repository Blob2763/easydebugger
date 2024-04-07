# easydebugger

a Python debugging tool made by blob2763

## setting it up
simple stuff for installing any library

### 1. installation
Install the library using `pip install easydebugger`

### 2. importing the library
```py
import easydebugger as ed
```

## functions

### messages
there are 3 types of messages to choose from:
- error
- warn
- success

you can make any of these messages with their corresponding functions:
```py
import easydebugger as ed

ed.error("error message")
ed.warn("warn message")
ed.success("success message")
```
![Screenshot 2024-04-07 182426](https://github.com/Blob2763/easydebugger/assets/88489444/105603f0-efdf-4335-b4e5-557fa5e32764)

each message function looks something like this:
```py
# Not a real function, but represents any of the 3 message functions
ed.message(message, code)
```

| parameter | required | default | description                                                 |
|-----------|----------|---------|-------------------------------------------------------------|
| `message` | yes      | N/A     | the message                                                 |
| `code`    | no       | `""`    | the code displayed with the message to easily identify them |

here's what the messages look like with a code:
```py
import easydebugger as ed

ed.error("error message", "ERROR CODE")
ed.warn("warn message", "WARN CODE")
ed.success("success message", "SUCCESS CODE")
```
![Screenshot 2024-04-07 183136](https://github.com/Blob2763/easydebugger/assets/88489444/2d1402fa-8d3a-4b48-bc34-db482fb64fad)
