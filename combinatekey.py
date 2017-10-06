# import sched
# import threading
# import time
import pyHook
import pythoncom

def key_press(event):
    if(pyHook.GetKeyState(pyHook.HookConstants.VKeyToID('VK_CONTROL')) and pyHook.HookConstants.IDToName(event.KeyID) == 'Q'):
        print 'ctrl+Q pressed'
        handler()
    return True

def handler():
    pass

hm = pyHook.HookManager()
hm.KeyDown = key_press
hm.HookKeyboard()
pythoncom.PumpMessages()