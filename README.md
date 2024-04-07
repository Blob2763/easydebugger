# easydebugger

a Python debugging tool made by blob2763

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

| parameter | required | default | description                                                  |
|-----------|----------|---------|--------------------------------------------------------------|
| `value`   | yes      | N/A     | the variable's value                                         |
| `name`    | yes      | N/A     | the variable's name                                          |

in the future, i might add functionality to detect the variable name automatically. there will be be a way to override this because the detection is not always accurate

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

| parameter | required | default | description                                                  |
|-----------|----------|---------|--------------------------------------------------------------|
| `code`    | yes      | N/A     | the timer's name                                             |

```py
ed.end_timer(code)
```

| parameter | required | default | description                                                  |
|-----------|----------|---------|--------------------------------------------------------------|
| `code`    | yes      | N/A     | the timer's name                                             |

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
