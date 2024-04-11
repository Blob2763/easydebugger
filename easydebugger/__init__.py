import time as t
import inspect
import os


DISPLAY = True

ESCAPE = u"\u001b[0m"

ERROR = "9"
WARN = "220"
SUCCESS = "120"
VARIABLE = "208"
LOG = "15"
TIME = "93"
TRACE = "27"
HISTORY = "57"

timers = {}
traces = []
history = []


def format_text(code, text, is_background=False):
    if is_background:
        return u"\u001b[48;5;" + code + "m" + text + ESCAPE
    else:
        return u"\u001b[38;5;" + code + "m" + text + ESCAPE


def history_log(symbol, colour, message, label, line_number):
    now = t.time()
    seconds_since_start = now - START_TIME
    
    stack = inspect.stack()
    stack_length = len(stack)
    
    history.append({
        "time": seconds_since_start * 1000,
        "stack": stack,
        "stack_length": stack_length,
        "symbol": symbol,
        "colour": colour,
        "message": message,
        "label": label,
        "line_number": line_number
    })


def display_history():
    for entry in history:
        time = entry["time"]
        stack = entry["stack"]
        stack_length = entry["stack_length"]
        symbol = entry["symbol"]
        colour = entry["colour"]
        message = entry["message"]
        label = entry["label"]
        line_number = entry["line_number"]
        
        
        history_label = format_text(HISTORY, f" - {round(time, 6)}ms ", True)
        
        if label:
            log_label = format_text(colour, f" {symbol} {label} ", True)
        else:
            log_label = format_text(colour, f" {symbol} ", True)
        log_message = format_text(colour, f"{message} (line {line_number})")
        
        print("   " * (stack_length - 3) + history_label + log_label, log_message)


def display_message(symbol, label, message, line_number, colour_code, indent=0):
    if DISPLAY:
        message = format_text(colour_code, f"{message} (line {line_number})")
        
        if label:
            print((" " * indent * 3) + format_text(colour_code, f" {symbol} {label} ", True), message)
        else:
            print(format_text(colour_code, f" {symbol} ", True), message)


def error(message, code=""):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "!"
    colour = ERROR
    display_message(symbol, code, message, caller_line_number, colour)
    history_log(symbol, colour, message, code, caller_line_number)


def warn(message, code=""):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "*"
    colour = WARN
    display_message(symbol, code, message, caller_line_number, colour)
    history_log(symbol, colour, message, code, caller_line_number)
        

def success(message, code=""):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "+"
    colour = SUCCESS
    display_message(symbol, code, message, caller_line_number, colour)
    history_log(symbol, colour, message, code, caller_line_number)
        

def variable(value, name):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "$"
    colour = VARIABLE
    display_message(symbol, name, value, caller_line_number, colour)
    history_log(symbol, colour, value, name, caller_line_number)


def log(message, label=""):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "="
    colour = LOG
    display_message(symbol, label, message, caller_line_number, colour)
    history_log(symbol, colour, message, label, caller_line_number)


def start_timer(code):
    caller_line_number = inspect.stack()[1].lineno
    symbol = "#"
    colour = TIME
    
    start_time = t.time()
    timers[code] = start_time
    
    message = "Started timing"
    
    display_message(symbol, code, message, caller_line_number, colour)
    history_log(symbol, colour, message, code, caller_line_number)


def end_timer(code):
    end_time = t.time()
    
    symbol = "#"
    colour = TIME
    
    if code in timers:
        caller_line_number = inspect.stack()[1].lineno
        
        start_time = timers[code]
        timers.pop(code)
        
        duration_in_seconds = end_time - start_time
        duration_in_millis = duration_in_seconds * 1000
        
        message = f"Finished timing, took {round(duration_in_millis, 6)}ms"
        
        display_message(symbol, code, message, caller_line_number, colour)
        history_log(symbol, colour, message, code, caller_line_number)        
    else:
        display_message(symbol, code, "Timer doesn't exist!", caller_line_number, colour)


def trace():
    caller_line_number = inspect.stack()[1].lineno
    symbol = "@"
    colour = TRACE
    
    function_name = inspect.stack()[1].function
    
    if function_name in traces:
        traces.pop(traces.index(function_name))
        
        message = "Exiting function"
    else:
        traces.append(function_name)
        
        message = "Entering function"

    display_message(symbol, function_name, message, caller_line_number, colour)
    history_log(symbol, colour, message, function_name, caller_line_number)
  

def export_history(file_name=str(round(t.time() * 1000))):
    def deep_copy_list(original_list):
        if isinstance(original_list, list):
            return [deep_copy_list(item) for item in original_list]
        elif isinstance(original_list, dict):
            return {key: deep_copy_list(value) for key, value in original_list.items()}
        else:
            return original_list 
    
    
    if not os.path.exists("debug_logs"):
        os.mkdir("debug_logs")
    
    with open("debug_logs/" + file_name + ".txt", "w") as f:
        success(f"Exported history at debug_logs/{file_name}.txt", "EXPORT_HISTORY")
        
        history_copy = deep_copy_list(history)
        for entry in history_copy:
            entry.pop("symbol")
            entry.pop("colour")
            f.write(str(entry) + "\n")


# ! error
# * warn
# + success
# $ variable
# # time
# = log
# @ trace
# - history

START_TIME = t.time()