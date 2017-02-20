#Rachel Katz (rak5ea) lab5 newFile.py
from __future__ import print_function, unicode_literals

from helper import greeting


def addMessage(msg1, msg2):
    return msg1 + msg2

if __name__ == "__main__":
    msg = "hello, "
    greeting(addMessage(msg,"world!"))
