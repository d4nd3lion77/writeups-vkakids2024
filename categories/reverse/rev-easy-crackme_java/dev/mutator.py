#!/usr/bin/env python3

import random
from re import findall, sub
import os

import argparse
import shutil

parser = argparse.ArgumentParser(description='Скрипт для мутации флагов')
parser.add_argument('--mode', dest="mode",required=True, choices=['print', 'file'])
parser.add_argument('--number', dest="number", required=True, type=int, help='Количество генерируемых файлов/флагов')
parser.add_argument('--flag', dest="flag",required=True)
parser.add_argument('--file', dest="file")

args = parser.parse_args()

FLAG = args.flag
FILE = args.file
NUMBER = args.number
MODE = args.mode

# ===== Вносятся изменения в файл ===== #
def change_file(directory, id, file, mf):
    data_to_change = open(FILE, "r").read()

    # ! ...  Далее внести функционал по обработке файла 
    mf_parts = [mf[i:i + 10] for i in range(0, len(mf), 10)]
    data_to_change = data_to_change.replace("java_code_", mf_parts[0])
    data_to_change = data_to_change.replace("is_that_ea", mf_parts[1])
    data_to_change = data_to_change.replace("sy_to_read", mf_parts[2])
    # ... 
    os.mkdir(os.path.join(directory, id))
    with open(os.path.join(directory, id, file), "wb") as f:
        f.write(data_to_change.encode())
    os.system(f"javac /{directory}/{id}/task.java")    
# ===================================== #

substitutionDict = {"a": "aA4", "b": "bB", "c": "cC", "d": "dD", "e": "eE3", "f":"fF", "g": "gG6", "h": "hH", "i": "iI1", "j": "jJ", "k": "kK", "l":"lL", "n": "nN", "o": "oO0", "p": "pP", "q": "qQ", "r": "rR", "s":"sS5", "t": "tT7", "u": "uU", "v": "vV", "w":"wW", "x": "xX", "y": "yY", "z": "zZ"}

leetEncodedSymbols = "4360715"
leetSymbols = "aegotis"
ordinarySymbols = "ibcdfhjklnpqruvwxyz"

def preCalculate(s):
    devidorsSequence = []
    module = 1
    for i in s:
        if i in leetSymbols:
            module *= 3
            devidorsSequence.append(3)
        elif i in ordinarySymbols:
            module *= 2
            devidorsSequence.append(2)
        else:
            devidorsSequence.append(1)
    module -= 1
    return module, devidorsSequence

def mutate(fl):
    payload = findall(r"{(.+)}", fl)
    if len(payload) == 0:
        s = fl
    else:
        s = payload[0]
    enc = ""
    value = 1
    module, devidorsSequence = preCalculate(s)
    secret = random.randint(0, module)
    for counter, i in enumerate(devidorsSequence):
        if value >= module:
            if i ==  1:
                return fl.replace(s, enc + s[counter:])
            return fl.replace(s, enc + s[counter + 1:])
        if i == 1:
            enc += s[counter]
            continue
        el = secret % i
        value *= i
        enc += substitutionDict[s[counter]][el]
        secret = secret // i
        
    return fl.replace(s, enc + s[counter + 1:])

def normalize(s):
    s = s.lower()
    for a, b in zip(leetEncodedSymbols, leetSymbols):
        s = s.replace(a, b)
    return s

if MODE=="file":
    if not FILE:
        print("Specify file!")
        exit()
    if not os.path.isfile(FILE):
        print("No such file")
        exit()
    
    file_name = os.path.basename(os.path.abspath(FILE))
    chunk = os.urandom(4).hex()
    files_dir = file_name + "." + chunk + ".ARCHIVE"
    files_dir_full = os.path.join(os.path.dirname(os.path.abspath(FILE)), files_dir)
    os.mkdir(files_dir_full)

flags = []
for i in range(NUMBER):
    while True:
        mf = mutate(FLAG)
        if mf not in flags:
                break
    assert FLAG == normalize(mf)
    if MODE == "print":
        print(mf)
    else:
        change_file(files_dir_full, str(i+1), file_name, mf)

    # Формируется файл с флагами
    flags.append(mf)

if MODE == "file":
    shutil.make_archive(files_dir_full, 'zip', files_dir_full)
    with open(os.path.join(os.path.dirname(os.path.abspath(FILE)), file_name + "." + chunk + ".FLAGS.txt"), "w") as f:
        f.write("\n".join(flags))