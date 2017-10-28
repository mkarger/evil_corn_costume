#!/usr/bin/env python

# Plays a random audio file when a button is pushed.

import os
import random

def randomSound():
    randomFile = random.choice(os.listdir ("./audio"))
    os.system('mpg123 ' + randomFile)

randomSound()