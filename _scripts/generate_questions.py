#!/usr/bin/env python
import os
from shutil import copyfile

QUESTIONS_LOC = '/Users/Zaaron/Dropbox/MeDb/questions.txt'
ROOT = '/Users/Zaaron/Code/bzreinhardt.github.io/questions.md'
copyfile(QUESTIONS_LOC, ROOT)
