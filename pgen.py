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

import argparse, sys, os, shutil

# *********************************************************
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--i",     nargs='?', default='pgen.txt',         metavar='input_file',                 help="text file containing items to back up, default is 'pgen.txt'")
    parser.add_argument("--o",     nargs='?', default="pgen",         metavar='output_dir',                 help="output directory, default is 'pgen'")
    parser.add_argument("--p",     action='store_true',                                                         help="precheck only, don't perform actual pgen")
    
    args = parser.parse_args()
    
#     print ""
#     print "=============================="
#     print "%-15s %s" % ("input file",     args.i)  
#     print "%-15s %s" % ("output dir",     args.o)  
#     print "%-15s %s" % ("precheck",       args.p)  
    
# #     try:
# #         iFile = open(args.i)
# #     except  IOError:
# #         print "ERROR: Input file [%s] does not exist" % (args.i)
# #         sys.exit()

# #     # If dest directory doesn't exist create it.        
# #     if not os.access(args.o, os.F_OK):
# #         os.makedirs(args.o)

# #     for line in iFile:
# #         parseLine(args.o, line)
# #         
# #     iFile.close()

# *********************************************************
def parseLine(out_dir, line):
    # clean version of full path of item to be backed up including drive letter
    full_in_path = str.strip(line)
    
    sp = str.rsplit(full_in_path, "\\", 1)
    in_directory = sp[0]
    fnft = sp[1]
    
    sp = str.split(fnft, ".")
    fn = sp[0]
    ft = sp[1]
    
    sp = str.split(in_directory, "\\", 1)
    out_dir = "\\".join([out_dir, sp[1]])
    
#      print "====================="
    print "%-15s %s" % ("full_in_path", full_in_path)
#      print "%-15s %s" % ("in_directory", in_directory)
#      print "%-15s %s" % ("fnft", fnft)
#      print "%-15s %s" % ("in_drive", in_drive)
#      print "%-15s %s" % ("out_dir", out_dir)
#     print "%-15s %s" % ("fn", fn)
#     print "%-15s %s" % ("ft", ft)
    
    # if backing up an entire directory
    if ft == "*":
        # if out_dir exists delete it
        if os.access(out_dir, os.F_OK):
            shutil.rmtree(out_dir, ignore_errors=True)

        # copy entire tree
        try:
            shutil.copytree(in_directory, out_dir)
        except:
            pass
        
    else:
        # If out_dir doesn't exist create it.        
        if not os.access(out_dir, os.F_OK):
            os.makedirs(out_dir)
            
        if fn == "*":
            fileList = os.listdir(in_directory)
            for f in fileList:
                if os.path.isfile("\\".join([in_directory, f])):
                    sp = str.split(f, ".")
                    if sp[1] == ft:
                        shutil.copy("\\".join([in_directory, f]), out_dir)
        else:
            shutil.copy(full_in_path, out_dir)
    
# *********************************************************        
if __name__ == "__main__":
    main()