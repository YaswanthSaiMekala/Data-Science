import sys
import os
import unittest
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file_) + '/src')))
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file_) + '/tests')))
from core import main
if _name_ = '_main_':
    f=open('packets/tcp.txt','r')
    g=open('packets/udp.txt','r')
    main(f)
