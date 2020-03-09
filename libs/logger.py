import time
import datetime

class Logger:
    def __init__(self):
        self.colors = {
            "info" : "\033[32m",
            "silly" : "\033[35m",
            "debug" : "\033[36m",
            "warn" : "\033[33m",
            "error" : "\033[31m", 
            "end" : "\033[0m",
            
        }
        self.debugFile = open("./logs/debug.log", "a")
        self.errorFile = open("./logs/error.log", "a")
    def info(self, msg):
        t = datetime.datetime.now()
        t = t.strftime("%d/%b/%Y %H:%M:%S")
        textShow = "[%s] %s[INFO]%s   %s" %(t, self.colors['info'],self.colors['end'],str(msg))
        print(textShow)
        self.debugFile.write(textShow+"/n")
    def debug(self, msg):
        t = datetime.datetime.now()
        t = t.strftime("%d/%b/%Y %H:%M:%S")
        textShow = "[%s] %s[DEBUG]%s  %s" %(t, self.colors['debug'],self.colors['end'],str(msg))
        print(textShow)
        self.debugFile.write(textShow+"/n")

    def silly(self, msg):
        t = datetime.datetime.now()
        t = t.strftime("%d/%b/%Y %H:%M:%S")
        textShow = "[%s] %s[SILLY]%s  %s" %(t, self.colors['silly'],self.colors['end'],str(msg))
        print(textShow)
        self.debugFile.write(textShow+"/n")
    
    def warn(self, msg):
        t = datetime.datetime.now()
        t = t.strftime("%d/%b/%Y %H:%M:%S")
        textShow = "[%s] %s[WARN]%s   %s" %(t, self.colors['warn'],self.colors['end'],str(msg))
        print(textShow)
        self.errorFile.write(textShow+"/n")
    
    def error(self, msg):
        t = datetime.datetime.now()
        t = t.strftime("%d/%b/%Y %H:%M:%S")
        textShow = "[%s] %s[ERROR]%s  %s" %(t, self.colors['error'],self.colors['end'],str(msg))
        print(textShow)
        self.errorFile.write(textShow+"/n")
