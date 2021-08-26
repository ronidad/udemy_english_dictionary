import pandas as pd
import numpy as np
import json
import sys
import codecs

if sys.stdout.encoding != 'cp850':
      sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')




data = json.load(open("data.json"))
print(data)

def translate(word):
    return data(word)



word = "rain"

print(translate(word))
