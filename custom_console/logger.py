import multiprocessing
import os
import time

from datetime import datetime


def _subtract(a:int, b:int) -> int:
        if a >= b:
            return a - b
        else:
            return 0 


def run_pointer(speed:float, pointer_char:str, pointer_ref:str) -> None:
    reverse = False
    range_pointer_ref = range(len(pointer_ref))
    len_pointer_ref = len(pointer_ref)-1
    velocity = 1 - speed
    
    try:
        while True:
            for i in range_pointer_ref:                
                if reverse:
                    index = len_pointer_ref - i
                    
                    if index != len_pointer_ref:
                        time.sleep(velocity)      
                else:
                    index = i

                    if index != 0:
                        time.sleep(velocity)
    
                print(f'|{pointer_ref[:index]}{pointer_char}{pointer_ref[index+1:]}|', end='\r', flush=True)     
            if reverse:
                reverse = False
            else:
                reverse = True
    except:
        return


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
    def __init__(self, name:str=__name__, path:str=None, speed:float=0.937, time_format:str="%Y-%m-%d %H:%M:%S", pointer_char:str='⚮') -> None:        
        self.software_name = name
        self.current_software_name = name
        self.path = path
        self.speed = speed
        self.time_format = time_format
        self.pointer_char = pointer_char
        
        self.title_len = range(len(datetime.now().strftime(time_format))+2)
        self.onflush = False
        self.pointer_ref = ''
        self.pointer_run = multiprocessing.Process
        
        self.log_file = open(os.path.join(self.path, f'{self.software_name}.log'), 'a', encoding='utf-8')
                    
            
    def custom_logger(self, value:str) -> None:
        try:
            self.log_file.write(f"{value}\n")
        except Exception as e:
            self.log(e.args[-1])
        
        
    def info(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:       
        self.log(bcolors.BG_WHITE, bcolors.BLACK, 'INFO', text, write_file_path, Flush)
        
    def ok(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:
        self.log(bcolors.BG_GREEN, bcolors.BLACK, 'OK', text, write_file_path, Flush)
    
    def warning(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:
        self.log(bcolors.BG_YELLOW, bcolors.BLACK, 'WARNING', text, write_file_path, Flush)  
        
    def error(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:        
        self.log(bcolors.BG_RED, bcolors.WHITE, 'ERROR', text, write_file_path, Flush)
    

    def log(self, bg_color:str, fg_color:str, start:str, middle:str, write_file_path:bool, Flush:bool) -> None:
        formatted_date_time = datetime.now().strftime(self.time_format)
        terminal_size = os.get_terminal_size().columns
        self.title_len = range(len(formatted_date_time)+2)
    
        values_text = (f'{formatted_date_time}', f'{start.upper()}', middle)
        
        def console_flush() -> None:
            if self.onflush:
                self.onflush = False
                print()

            print(f'|{bcolors.BG_WHITE} {bcolors.BLACK}{values_text[0]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{values_text[1]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {values_text[2]} {" " * _subtract(terminal_size-20, len("".join(values_text)))}{bcolors.BG_BLACK}|')
        
        is_pointer_time = self.pointer_run.is_alive()
        if is_pointer_time:
            self.pointer_run.terminate()
            if not Flush:
                console_flush()
                console.pointer()
            else:
                self.onflush = True
                print(f'\r|{bcolors.BG_WHITE} {bcolors.BLACK}{values_text[0]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{values_text[1]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {values_text[2]} {" " * _subtract(terminal_size-20, len("".join(values_text)))}{bcolors.BG_BLACK}|', end='', flush=True)
        else:
            if not Flush:
                console_flush()
            else:
                self.onflush = True
                print(f'\r|{bcolors.BG_WHITE} {bcolors.BLACK}{values_text[0]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{values_text[1]}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {values_text[2]} {" " * _subtract(terminal_size-20, len("".join(values_text)))}{bcolors.BG_BLACK}|', end='', flush=True)          
        
        if write_file_path:
            self.custom_logger(f'| {values_text[0]} | :: | {values_text[1]} | :: | {values_text[2]} |')
            
            
    def pointer(self) -> None:       
        pointer_ref=''
        for _ in self.title_len:    
            pointer_ref += ' '
                
        self.pointer_run = multiprocessing.Process(target=run_pointer, args=(self.speed, self.pointer_char, pointer_ref, ))
        self.pointer_run.daemon = True
        self.pointer_run.start()
            
            
if __name__ == "__main__": #test
    console  =  type_terminal('program', 'E:/PyProjs/New folder', speed=0.998)
    console.pointer()

    console.ok('Something to show...') #simple print, without writing to the log file and without being on one line.
    time.sleep(1)

    i  =  0
    while  i  <=  5:
        console.info(f'Progress: {i}%', Flush  =  True) #print in just one line.
        i+=1
        time.sleep(0.33)

    console.error('Any ERROR OCCURRED to LOG file...', write_file_path  =  True) #printing and writing to the log.
    console.warning('Any WARNING... OCCURRED to log file...')
    
    console.pointer()
    time.sleep(3)