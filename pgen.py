#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    pgen.py
#
#    Copyright 2013 Mike Harley <VestedSkeptic@gmail.comm>
#         
#    pgen is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pgen is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    with these source files.  If not, see <http://www.gnu.org/licenses/>.

# import sys, os, shutil
import random, string, argparse
from Tkinter import Tk

# *********************************************************
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--l",     default=24,                 metavar='password_length',        help="password length, default is 24")
    parser.add_argument("--p",     action='store_true',                                          help="use punctuation")
    
    args = parser.parse_args()
#     print args.l
#     print args.p

    # Assemble base alphabet and generate password
    myrg = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits
    if args.p:
        alphabet += string.punctuation
    pw = str().join(myrg.choice(alphabet) for _ in range(int(args.l)))
    
    print pw

    # put password in clipboard    
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(pw)
    r.destroy()

# *********************************************************        
if __name__ == "__main__":
    main()