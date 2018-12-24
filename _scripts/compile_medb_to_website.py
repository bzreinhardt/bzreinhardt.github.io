#! /usr/bin/env python
import sys
import os
from shutil import copyfile
from shutil import rmtree

MEDB_DIR = '/Users/Zaaron/Dropbox/MeDb'
WEBSITE_DIR = '/Users/Zaaron/Code/bzreinhardt.github.io'

if __name__=="__main__":
  rmtree(os.path.join(WEBSITE_DIR,'MeDb'))
  os.mkdir(os.path.join(WEBSITE_DIR,'MeDb'))
  with open(os.path.join(WEBSITE_DIR, "medb.md"), 'w') as f:
    for file in os.listdir(MEDB_DIR):
      if file.endswith(".txt"):
        name = file.split(".")[-2]
        if "IGNORE" in name:
            print("ingoring " + name)
            continue
        filename = name.replace("_","-") + ".md"
        title=" ".join(name.replace("_","-").split("-")).title()
        urlname = name.replace("_","-")
        newpath = os.path.join(os.path.join(WEBSITE_DIR,'MeDb'), filename)
        copyfile(os.path.join(MEDB_DIR,file), newpath)
        print("copying from " + file + " to " + newpath)

        header = '---\n' + \
                'layout: page\n'+\
                'title: %s\n'%title + \
                'permalink: /%s/\n'%urlname + \
                '---\n'

        with open(newpath, 'r') as original:
            data = original.read()
        with open(newpath, 'w') as modified:
            modified.write(header + data)

        f.write("[%s](/%s)\n\n"%( name, name))
