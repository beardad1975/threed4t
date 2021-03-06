import sys
import threading
from queue import Queue, Empty 
import time
import code

from direct.task import Task


import __main__
from __main__ import __dict__ as main_dict

class Repl:
    """  Repl main and readline thread """
    def start_repl(self): 
        self.cmd_queue = Queue()
        self.is_cmd_completed = True

        self.console = code.InteractiveConsole(locals=main_dict,filename='輸入')   
        

        #arcade.schedule(self.handle_repl, 0.2)
        taskMgr.doMethodLater(0.5, self.handle_repl, 'handle_repl')
        
        t = threading.Thread(target=self.readline_thread)
        t.daemon = True
        t.start()  

    def readline_thread(self):
        print('立體模擬開始 ')
        print('\n')
        print('>>> ', end='')
        while True:
             try:
                line = sys.stdin.readline()
                self.cmd_queue.put(line)
                time.sleep(0.2)
             except RuntimeError as e :
                 print('請按上方執行或STOP按鈕')
                 return

    def handle_repl(self, task):
        #print('handling...')
        try:
            line = self.cmd_queue.get(block=False)
        except Empty:
            return task.again

        # strip enter  or  leading white space
        line = line.rstrip()
        if self.is_cmd_completed: line = line.lstrip()


        if self.console.push(line):
            # not complele
            print('... ', end='')
            self.is_cmd_completed = False
        else:
            # complete
            print('>>> ', end='')
            self.is_cmd_completed = True

        return task.again

        # try:
        #     if '=' in line:
        #         #exec(line)
        #         exec(line, main_dict)
        #     else:
        #         #r = eval(line)
        #         r = eval(line, main_dict)
        #         if r:
        #             print(r)
        #     #print('Got: ', line[:-1], '---')
        
        # except Exception as e:
        #     print(e)
        # finally:
        #     print('4t>>> ', end='') 