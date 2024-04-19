import multiprocessing
import os
import time

from datetime import datetime


@staticmethod
def _subtract(a:int, b:int) -> int:
        if a >= b:
            return a - b
        else:
            return 0 


def run_pointer(speed:float, pointer_char:str, pointer_ref:str) -> None:
    range_pointer_ref = range(1, len(pointer_ref))
    len_pointer_ref = len(pointer_ref)-1
    velocity = 1 - speed
    
    def pointer_forward():
        for index in range_pointer_ref:
            print(f'|{pointer_ref[:index]}{pointer_char}{pointer_ref[index+1:]}|', end='\r', flush=True)
            time.sleep(velocity)
            
    def pointer_backward():
        for i in range_pointer_ref:
            index = len_pointer_ref - i
            print(f'|{pointer_ref[:index]}{pointer_char}{pointer_ref[index+1:]}|', end='\r', flush=True)
            time.sleep(velocity)
    try:
        while True:
            pointer_forward()                
            time.sleep(velocity)      
            pointer_backward()
            time.sleep(velocity)
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
        
        os.makedirs(path, exist_ok=True)
        self.logger_path = os.path.join(self.path, f'{self.software_name}.log')
                    
            
    def custom_logger(self, value:str) -> None:
        try:
            with open(self.logger_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{value}\n")
        except Exception as e:
            self.error(f'While writing to logfile: {e.args[-1]}')
        
        
    def info(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:       
        self.log(bcolors.BG_WHITE, bcolors.BLACK, 'INFO   ', text, write_file_path, Flush)
    
        
    def ok(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:
        self.log(bcolors.BG_GREEN, bcolors.BLACK, 'OK     ', text, write_file_path, Flush)
    
    
    def warning(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:
        self.log(bcolors.BG_YELLOW, bcolors.BLACK, 'WARNING', text, write_file_path, Flush)  
       
        
    def error(self, text:str='', write_file_path: bool=False, Flush: bool=False) -> None:        
        self.log(bcolors.BG_RED, bcolors.WHITE, 'ERROR  ', text, write_file_path, Flush)
    

    def log(self, bg_color:str, fg_color:str, start:str, middle:str, write_file_path:bool, Flush:bool) -> None:
        formatted_date_time = datetime.now().strftime(self.time_format)
        terminal_size = os.get_terminal_size().columns
        self.title_len = range(len(formatted_date_time)+2)
                
        len_starting_text = len(formatted_date_time) + len(start) + 20
        starting_spaces = f"|{'-' * (len_starting_text-5)}|{bcolors.BG_BLUE} "
        real_terminal_size = terminal_size - len_starting_text
        
        def console_flush(starting_text:str, middle:str) -> None:
            if self.onflush:
                self.onflush = False
                print()

            while len(middle) > real_terminal_size:
                print(f'{starting_text}{middle[:real_terminal_size]} {bcolors.BG_BLACK}|')
                middle = middle[real_terminal_size:]
                starting_text = starting_spaces
            else:
                len_full_text = len(middle) + len_starting_text
                print(f'{starting_text}{middle} {" " * _subtract(terminal_size, len_full_text)}{bcolors.BG_BLACK}|')
        
        if self.pointer_run.is_alive():
            self.pointer_run.terminate()
            if not Flush:
                console_flush(f'|{bcolors.BG_WHITE} {bcolors.BLACK}{formatted_date_time}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{start}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} ', middle)
                console.pointer()
            else:
                self.onflush = True
                len_full_text = len(middle) + len_starting_text
                print(f'\r|{bcolors.BG_WHITE} {bcolors.BLACK}{formatted_date_time}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{start}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {middle} {" " * _subtract(terminal_size, len_full_text)}{bcolors.BG_BLACK}|', end='', flush=True)
        else:
            if not Flush:
                console_flush(f'|{bcolors.BG_WHITE} {bcolors.BLACK}{formatted_date_time}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{start}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} ', middle)
            else:
                self.onflush = True
                len_full_text = len(middle) + len_starting_text
                print(f'\r|{bcolors.BG_WHITE} {bcolors.BLACK}{formatted_date_time}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bg_color} {fg_color}{start}{bcolors.WHITE} {bcolors.BG_BLACK}| :: |{bcolors.BG_BLUE} {middle} {" " * _subtract(terminal_size, len_full_text)}{bcolors.BG_BLACK}|', end='', flush=True)          
        
        if write_file_path:
            self.custom_logger(f'| {formatted_date_time} | :: | {start} | :: | {middle}')
            
            
    def wrap_line(self, write_file_path:bool=False):
        print()
        if self.onflush:
            self.onflush = False
            print()
        if write_file_path:
            self.custom_logger('')
            
            
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
    while  i  <=  4:
        console.info(f'Progress: {i}%', Flush  =  True) #print in just one line.
        i+=1
        time.sleep(0.25)

    console.error('Paragraphs are now supported: The French Revolution (1789-1799) was a transformative event in France and the world. It arose from widespread dissatisfaction with absolute monarchy, marked by social, economic, and political inequality. Initiated with the convocation of the Estates-General in 1789, it quickly turned into a popular movement that overthrew the monarchy, executed King Louis XVI, and established the Republic. The Revolution brought about a series of radical changes, including the abolition of the Ancien Régime, the promulgation of the Declaration of the Rights of Man and of the Citizen proclaiming equality before the law and freedom of expression, and the implementation of secular measures like the revolutionary calendar...', write_file_path  =  True) #printing and writing to the log.
    console.warning('Any WARNING... OCCURRED to log file...')
    
    console.pointer()
    time.sleep(3)