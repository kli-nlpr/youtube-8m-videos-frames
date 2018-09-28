# -*- coding: utf-8 -*-
import os
import subprocess
from tqdm import tqdm

lines=open('youtube8mcategories.txt').readlines()
downloaded=open('downloaded_class.txt','w')

for line in tqdm(lines):
    temp=line.strip().split()
    name=" ".join(temp[3:-1])
    file=name+'.txt'

    output=open(file,'w')
    output.write(name+'\n')
    output.close()

    cmd="bash downloadmulticategoryvideos.sh 0 {}".format(file)
    subprocess.call(cmd, shell=True)

    if os.path.isfile(file):
        os.remove(file)

    downloaded.write(line)

downloaded.close()
