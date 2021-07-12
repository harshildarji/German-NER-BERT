# If, for some holy reason, "data/court_data.csv" is removed from this plane of existence, 
# use this python script to generate a new one. Just make sure the ".conll" files are in place.

import os
import pandas as pd

data = open(f"./data/court_data.csv", "w")
data.write("sentence_number|word|tag\n")

sentence = 0
for file in os.listdir("./data/conll"):
    print(f"[+] Converting ./data/conll/{file}...")

    f = open(f"./data/conll/{file}", "r")

    for line in f.readlines():
        if line == "\n":
            sentence += 1
        else:
            w, t = line.split() if len(line.split()) == 2 else [" ", line.strip()]
            data.write(f"{str(sentence)}|{w}|{t}\n")

    f.close()

data.close()
