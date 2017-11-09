# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
from core import Banner, gui, Obevilion, Check, Control

check_req  = Check.Check_req()
printer    = Banner.Printer()
looprocess = Control.LoopControl()

action = ''
commands = ['--gui', '--cli', '--help', '--about']

try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()
    looprocess.loop()

def run():
    try:
        assert action in commands, "Action is not one of %s" % ', '.join(map(str, commands))
        if action == '--gui':
            gui.main()
        elif action == '--cli':
            print("Not Working Right Now")
        elif action == '--help':
            printer.help_banner()
        elif action == '--about':
            printer.about()
    except Exception as e:
        try:
            if sys.argv[1] is not commands:
                printer.invalid_input()
            else:
                pass
        except Exception as e:
            pass

def main():

    check_req.check_os() # Checking the required operation system
    check_req.check_py_version() # Check valid python version
    run() # Run

if __name__ == '__main__':
    main()
