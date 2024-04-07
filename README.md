# easydebugger
a Python debugging tool made by blob2763

![PyPI](https://img.shields.io/pypi/v/easydebugger?label=pypi)

## setting it up
simple stuff for installing any library

### 1. installation
install the library using `pip install easydebugger`

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

you can add a code to each of these to make them easier to find. here's what the messages look like with a code:
```py
import easydebugger as ed

ed.error("error message", "ERROR CODE")
ed.warn("warn message", "WARN CODE")
ed.success("success message", "SUCCESS CODE")
```
![Screenshot 2024-04-07 183136](https://github.com/Blob2763/easydebugger/assets/88489444/2d1402fa-8d3a-4b48-bc34-db482fb64fad)

#### parameters
each message function looks something like this:
```py
# Not a real function, but represents any of the 3 message functions
ed.message(message, code)
```

| parameter | required | default | description                                                 |
|-----------|----------|---------|-------------------------------------------------------------|
| `message` | yes      | N/A     | the message                                                 |
| `code`    | no       | `""`    | the code displayed with the message to easily identify them |

### logs
logs are just `print()` statements but they look better. functionally, they are the basically same as the 3 message functions
```py
import easydebugger as ed

ed.log("some data")
ed.log("some labelled data", "LABEL")
```
![Screenshot 2024-04-07 184015](https://github.com/Blob2763/easydebugger/assets/88489444/e2546f42-ca6c-4f4f-b4f9-f1e502bc11e6)

#### parameters
```py
ed.log(message, label)
```

| parameter | required | default | description                                                  |
|-----------|----------|---------|--------------------------------------------------------------|
| `message` | yes      | N/A     | the message                                                  |
| `label`   | no       | `""`    | the label displayed with the message to easily identify them |

### variables
there is a special function just for logging variables. while you could use `ed.log()` for this, `ed.variable()` stands out more and should be used instead

```py
import easydebugger as ed

my_variable = 12345
ed.variable(my_variable, "my_variable")
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/ef594b43-6eab-4097-9059-c7fe07f445c1)

#### parameters
```py
ed.variable(value, name)
```

| parameter | required | default | description          |
|-----------|----------|---------|----------------------|
| `value`   | yes      | N/A     | the variable's value |
| `name`    | yes      | N/A     | the variable's name  |

### timers
you can time how long code takes to run using `ed.start_timer()` and `ed.end_timer()`

```py
import easydebugger as ed
import time as t

def foo():
    t.sleep(2)
    
ed.start_timer("foo")
foo()
ed.end_timer("foo")
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/bca51d8a-3ddb-4ccc-82ee-fa8aee17e2e2)

you can have multiple timers running at once
```py
import easydebugger as ed
import time as t

ed.start_timer("everything")

def foo():
    t.sleep(2)

ed.start_timer("foo")
foo()
ed.end_timer("foo")
ed.end_timer("everything")
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/58de10ec-0a2c-4819-b1d0-357ff3aaf84b)

if you use `ed.start_timer()` for a timer that is already running, the timer starts again
```py
import easydebugger as ed
import time as t

def foo():
    t.sleep(2)

ed.start_timer("foo")
foo()
ed.start_timer("foo")  # resets timer
ed.end_timer("foo")
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/29ee6b51-8dd5-4963-acc1-08eb3fca6135)

#### parameters
```py
ed.start_timer(code)
```

| parameter | required | default | description      |
|-----------|----------|---------|------------------|
| `code`    | yes      | N/A     | the timer's name |

```py
ed.end_timer(code)
```

| parameter | required | default | description      |
|-----------|----------|---------|------------------|
| `code`    | yes      | N/A     | the timer's name |

#### timer storage
if you ever need to see all active timers, you can use `ed.timers`

```py
import easydebugger as ed
import time as t

def foo():
    t.sleep(2)

ed.start_timer("foo")
ed.start_timer("bar")
foo()
ed.log(ed.timers)
ed.end_timer("bar")
ed.end_timer("foo")
```

![image](https://github.com/Blob2763/easydebugger/assets/88489444/3ffd080e-3f20-4ac5-8a91-21ed1f3d3eeb)

`ed.timers` is a dictionary, each key is the name of the timer and each value is the UNIX time in seconds when the timer started

### trace
you can use `ed.trace()` to show when a function is entered and exited
```py
import easydebugger as ed
import time as t

def foo():
    ed.trace()  # when used the first time, the code sees this as the function being entered
    ...
    ed.trace()  # when used the second time, the code sees this as the function being exited

foo()
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/9aa6252b-6fb9-4030-9f43-791a4dd6b8a0)

`ed.trace()` works best in a function, but won't throw an error if used outside of a function
```py
import easydebugger as ed

ed.trace()
ed.trace()
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/44d19b23-12d7-47b6-9be2-eeae07eb5858)

#### parameters
there are no parameters for `ed.trace()` because the function name is detected automatically

#### trace storage
if you ever need to see any active traces, use `ed.traces`
```py
import easydebugger as ed

def foo():
    ed.trace()
    bar()
    ed.trace()


def bar():
    ed.trace()
    ed.log(ed.traces)
    ed.trace()


foo()
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/d5da34d8-47f7-49ba-a5c7-7514c19a7cf8)

`ed.traces` is a list of all the names of the functions currently being traced

### history
easydebugger keeps a record of any messages, logs, timers, and traces used since the code started. you can display this record using `ed.display_history()`
```py
import easydebugger as ed

ed.error("error")
ed.display_history()
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/b6f27a37-5ce4-4ca0-855e-4365580ca76d)

each history entry is timestamped in milliseconds since the code started

if a history entry is made in a function, the entry is indented
```py
import easydebugger as ed

def foo():
    ed.trace()
    ...
    ed.trace()

ed.error("error")
foo()
ed.display_history()
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/4e637abb-cbdd-4d04-9162-65c38f686e57)

#### parameters
`ed.display_history()` has no parameters

#### history storage
if you ever need to use the history storage, use `ed.history`

`ed.history` is a list of dictionaries, one dictionary for each history log entry

each log entry looks like this:
| key            | description                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `time`         | timestamp of when the log was made in milliseconds since the code started                                                                           |
| `stack`        | the stack when the log was made. if you don't know what this means, you don't need to worry about it                                                |
| `stack_length` | length of the stack when the log was made. used for indentation in `ed.display_history()`                                                           |
| `symbol`       | the symbol used by the message, log, timer, or trace. eg: `"!"` for `ed.error()`                                                                    |
| `colour`       | the [8-bit ANSI colour code](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) of the message, log, timer, or trace. eg: `"9"` for `ed.error()` |
| `message`      | the message, log, variable value, or timer/trace message depending on the function that created the entry                                           |
| `label`        | the code, label, variable name, timer name, or traced function name depending on the function that created the entry                                |
| `line_number`  | the line number that the function that created the entry is on                                                                                      |

#### history export
you can export the history with `ed.export_history()`. this makes a text file in a folder called `debug_logs`, the folder is created if it doesn't exist

#### parameters
```py
ed.export_history(file_name)
```

| parameter   | required | default                       | description                                                                               |
|-------------|----------|-------------------------------|-------------------------------------------------------------------------------------------|
| `file_name` | no       | `str(round(t.time() * 1000))` | the name of the txt file being made. default is the current UNIX milliseconds as a string |

### hiding messages
if you want to hide debug messages for a certain area of code, you can use `ed.DISPLAY`

set `ed.DISPLAY` to `False` to hide the messages and set it to `True` if you want to show the messages again
```py
import easydebugger as ed

ed.error("error")
ed.DISPLAY = False
ed.error("another error")  # this won't be shown
ed.DISPLAY = True
ed.error("error")  # this will be shown
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/f12d9073-c16a-40d6-bfc9-5dc5a2edc55d)

`ed.show_history()` will still work even if `ed.DISPLAY` is set to `False`

### custom messages
if you want to make a custom debug message, use `ed.display_message()`
```py
import easydebugger as ed

ed.display_message("^", "LABEL", "message", 123, "65")
```
![image](https://github.com/Blob2763/easydebugger/assets/88489444/9aa1476e-1bd9-4fe7-bda4-dc64556d2591)

#### parameters
```py
ed.display_message(symbol, label, message, line_number, colour_code, indent)
```

| parameter     | required | default  | description                                                                                                                   |
|---------------|----------|--------- |-------------------------------------------------------------------------------------------------------------------------------|
| `symbol`      | yes      | N/A      | the symbol used by the message. eg: `"!"` for `ed.error()`                                                                    |
| `label`       | yes      | N/A      | the text next to the symbol                                                                                                   |
| `message`     | yes      | N/A      | the main part of the debug message                                                                                            |
| `line_number` | yes      | N/A      | the line number shown after the message                                                                                       |
| `colour_code` | yes      | N/A      | the [8-bit ANSI colour code](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) of the message. eg: `"9"` for `ed.error()` |
| `indent`      | no       | `0`      | the text next to the symbol                                                                                                   |

## plans for the future
im really happy with how this has turned out, but i still want to add more:
- automatically try to detect variable name in `ed.variable()`
- finish writing the documentation (yep, there's more!)
- make some usage examples
- an faq
