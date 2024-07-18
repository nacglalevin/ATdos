"""
========================================
Name:ATdos Author: Lalevin Martin
 Mailbox: rsjdcl@gmail.com                                              
 Github: http://github.com/nacglalevin
Written in 2024-7-17
==================NACG==================
"""
import os, sys, time

if os.name == 'posix':
        c = os.system('which pip'); print "[+] pip is correctly installed"
        if c == 256:
                print "[+] Installing pip installer"; os.system('sudo yum install python-pip')
        else:
                pass
else:
        print '[+] Installing your pip installer'

try:
        import requests,colorama
        from termcolor import colored,cprint
except:
        try:
                if os.name == 'posix':
                        os.system('sudo pip install colorama termcolor requests')
                        sys.exit('[+] Overload has install the nessecary modules to execute program')
                elif os.name == 'nt':
                        os.sytem('c:\python27\scripts\pip.exe install colorama requests termcolor')
                        sys.exit('[+] Overload has install the nessecary modules to execute program')
                else:
                        sys.exit('[+] Download and install all nessecary modules')
        except Exception,e:
                print '[-]',e
if os.name == 'nt':
        colorama.init()