import os
import threading
import time
import atexit

from datetime import datetime 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    WHITE = '\033[39m'
    ORIGINAL = '\033[39;49m' 
    BLACK = '\033[30m'
    
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    

class type_terminal(object):
    def __init__(self, name, path:str=None, speed:float=0.937, time_format:str="%Y-%m-%d %H:%M:%S", pointer_char:str='⚮'):
        atexit.register(self.exit_handler)            
        self.software_name = name
        self.current_software_name = name
        self.path = path
        self.speed = speed
        self.time_format = time_format
        self.pointer_runtime = False
        self.pointer_char = pointer_char
        
        self.onflush = False
        self.pointer_ref = ''
                    
            
    def custom_logger(self, value):
        try:
            with open(os.path.join(self.path, f'{self.software_name}.log'), 'a', encoding='utf-8') as log_file:               
                log_file.write(f"{value}\n")
            
        except Exception as e:
            self.log('error writing to log file', e)
    
            
    def fit_line_from_flush(self):
        print()
        
        
    def _subtract(self, a, b):
        if a >= b:
            return a - b
        else:
            return 0
        

    def str_starting_type(self, start:str):
        match start.lower():
            case 'info':
                return bcolors.BG_WHITE, bcolors.BLACK
            case 'ok':
                return bcolors.BG_GREEN, bcolors.BLACK
            case 'warning':
                return bcolors.BG_YELLOW, bcolors.BLACK
            case 'error':
                return bcolors.BG_RED, bcolors.WHITE
            case _:
                return bcolors.BG_WHITE, bcolors.BLACK
            

    def log(self, start: str="info", middle: str="", write_file_path: bool=False, Flush: bool=False):
        current_datetime = datetime.now()
        formatted_date_time = current_datetime.strftime(self.time_format)
        terminal_size = os.get_terminal_size().columns
        
        key_divisor:str =''
        pointer_ref:str =''
        
        title_len = len(formatted_date_time)
        title_len_a = range(title_len+4)
        title_len_b = title_len+2
        
        for index in title_len_a:    
            if index < title_len_b:
                pointer_ref += ' '
        
        self.key_divisor, self.pointer_ref = key_divisor, pointer_ref
    
        bg_color, fg_color = self.str_starting_type(start)
        values_text = (f'{formatted_date_time}', f'{start.upper()}', middle)
        
        if not Flush:
            is_pointer_time = self.pointer_runtime
            self.pointer_runtime = False
            
            if self.onflush:
                self.fit_line_from_flush()
                self.onflush = False

            print(f'|{bcolors.BG_WHITE} {bcolors.BLACK}{values_text[0]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{values_text[1]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {values_text[2]} {" " * self._subtract(terminal_size-20, len("".join(values_text)))}{bcolors.BG_BLACK}|')
                        
            if is_pointer_time:
                console.pointer()
        else:
            self.pointer_runtime = False
            self.onflush = True
            
            print(f'\r|{bcolors.BG_WHITE} {bcolors.BLACK}{values_text[0]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{values_text[1]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {values_text[2]} {" " * self._subtract(terminal_size-20, len("".join(values_text)))}{bcolors.BG_BLACK}|', end='', flush=True)            
        
        if write_file_path:
            self.custom_logger(f'| {values_text[0]} | :: | {values_text[1]} | :: | {values_text[2]} |')
            
            
    def run_pointer(self):
        self.pointer_runtime = True
        reverse = False
        range_pointer_ref = range(len(self.pointer_ref))
        
        while self.pointer_runtime:
            try:
                for i in range_pointer_ref:
                    if not self.pointer_runtime:
                        break
                    
                    if reverse:
                        index = len(self.pointer_ref)-1 - i
                        
                        if index != len(self.pointer_ref)-1:
                            time.sleep(1 - self.speed)      
                    else:
                        index = i
                        
                        if index != 0:
                            time.sleep(1 - self.speed)
                    
                    if self.pointer_runtime:
                        print(f'|{self.pointer_ref[:index]}{self.pointer_char}{self.pointer_ref[index+1:]}|', end='\r', flush=True)
                    else:
                        break
                        
                if reverse:
                    reverse = False
                else:
                    reverse = True
            except:
                break
            
            
    def pointer(self): 
        pointer_run = threading.Thread(target=self.run_pointer)
        pointer_run.daemon = True
        pointer_run.start()


    def exit_handler(self):
        if self.pointer_runtime:
            self.pointer_runtime = False
            time.sleep(1 - self.speed)
            print('', end='\r', flush=True)
            
            
if __name__ == "__main__":
    console  =  type_terminal('program', 'E:/PyProjs/New folder', speed=0.998)
    console.pointer()

    console.log('ok', 'Something to show...') #simple print, without writing to the log file and without being on one line.
    time.sleep(1)

    i  =  0
    while  i  <=  5:
        console.log('info', f'Progress: {i}%', Flush  =  True) #print in just one line.
        i+=1
        time.sleep(0.33)

    console.log('error', 'Any ERROR OCCURRED to LOG file...', write_file_path  =  True) #printing and writing to the log.
    console.log('warning', 'Any WARNING... OCCURRED to log file...')
    
    console.pointer()
    time.sleep(3)