import re
import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Search the file system for ESE database.")
parser.add_argument("START_PATH", help ="Where to begin the recursive search")
parser.add_argument("--OUTPUT_FOLDER","-o", help="Path to a directory where you write templates ")
parser.add_argument("--PATH_TO_ESE_TEMPLATE","-p", help="Path to a ese_template executable")
parser.add_argument("--create_templates","-c",help = "Launch ese_template to create templates",action="store_true")

options = parser.parse_args()

filecount=0
print "Searching for ESE files . . .",
for cwd,dirs,files in os.walk(options.START_PATH):
    for each_file in files:
        filecount+=1
        if (filecount % 250) == 0:
            print ".",
        try:
            first8 = open( os.path.join(cwd,each_file) ).read(8)
        except:
            continue
        if re.match(r"....\xef\xcd\xab\x89",first8):
            print "\nESE FOUND: ", os.path.join(cwd,each_file),"\n"
            if options.create_templates:
                cli = "%s --XLS_OUTFILE \"%s\%s.xlsx\" \"%s\"" % (options.PATH_TO_ESE_TEMPLATE,options.OUTPUT_FOLDER, each_file, os.path.join(cwd,each_file))
                print "Launching ",cli
                os.system(cli)
            

