# pretty-logger
### A simple, custom print and file logger for any project.
![Alt text](https://github.com/Suundumused/pretty-logger/blob/main/README_assets/111460.png?raw=true)
---
### Requirements
**Minimum Version**: `python 3.3... ...`

---
### Usage
**Importing**

    from  custom_console.logger  import  type_terminal
---
**Instancing**

    console  =  type_terminal('SOFTWARE NAME', 'Log Output Folder', speed=0.998, time_format="%Y-%m-%d %H:%M:%S")
 - You can instantiate it at the beginning of the file after import and use it in any class/function.

---
**Starting Pointer**

    console.pointer()

 - It's the animated pointer that is shown in the console while your program is still running, it doesn't interfere with the code functioning.
 - Your project must have somewhat latent code or have recursion to be displayed.
---
### Print
    console.log('info', 'Process terminated by machine user.')
**Available colour options:** 
 - '`ok`': GREEN, 
 - '`info`': WHITE, 
 - '`warning`': YELLOW
 - '`error`': RED
---

    console.log('error', 'some error....', write_file_path = True)
    console.log('info', f'single_line_{i}%', Flush = True)

 - `write_file_path = True` It will write a new line to the log file with exactly the same information as the print except the colors.
 - `Flush = True`  It will print in just one line for every hit.
---
### Example

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
        #anything else...
---
### Log File result
    [program] ERROR: any error to log file -- 2024-02-06  22:36:28
    ---------
    [program] ERROR: any error to log file -- 2024-02-06  22:42:11 
    ---------
---
## 💖 Support Me

If you find my work valuable and want to support me, consider making a donation. Your contribution goes a long way in helping me continue my open-source contributions and creating awesome content!

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-Donate-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=A2S5G97QM7XCJ)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=A2S5G97QM7XCJ)

#### Bitcoin :: **bc1qa0xzyhcmcsuvppttmylzygwwfaken5jturhgek**

#### Ethereum :: **0x2fA70716D1Ae2f4994Be8e249b609056D72Ce80a** 

---