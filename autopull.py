#!/usr/bin/env python3

import glob
import re
import sys
import subprocess

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
    'BLUE': '\033[34m',
}


image_set = set()

for file in glob.iglob("./**/docker-compose.yml", recursive=True): # generator, search immediate subdirectories 
    for line in open(file, 'r'):
        if re.search('image:', line):
            image_name = re.sub(r"^.*image:[ \"]*([^ \"]+).*", r"\1", line)
            image_set.add(image_name.rstrip())
            utf_line = "{GREEN}%s -> %s{END}".format(**formatters) % (file.strip(), image_name.strip())
            print(utf_line, flush=True)

for file in glob.iglob("./**/Dockerfile", recursive=True): # generator, search immediate subdirectories 
    for line in open(file, 'r'):
        if re.search('FROM', line):
           image_name = re.sub(r"^.*FROM[ \"]+([^ \"]+).*", r"\1", line)
           image_set.add(image_name.rstrip())
           utf_line = "{GREEN}%s -> %s{END}".format(**formatters) % (file.strip(), image_name.strip())
           print(utf_line, flush=True)

for image in image_set:
    command = ('docker pull %s' % image).split()
    for line in run_command(command):
        utf_line = line.decode('utf-8')
        if "Downloaded newer image" in utf_line:
            utf_line = "{RED}%s{END}".format(**formatters) % utf_line
        elif "Image is up to date" in utf_line:
            utf_line = "{BLUE}%s{END}".format(**formatters) % utf_line
        print(utf_line, end='', flush=True)

