#!/usr/bin/env python3

import random
from re import findall, sub
import os

import argparse
import shutil
import pikepdf

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
    new_values = [89, 68, 78, 84]
    for i in mf:
        new_values.append(ord(i) ^ 47)
    new_values.append(82)
    #print(new_values)
    # ! ...  Далее внести функционал по обработке файла 
    new_encrypted_str = f"var encrypted = {new_values};"
    data_to_change = data_to_change.replace('var encrypted = [89, 68, 78, 84, 95, 71, 28, 88, 112, 70, 91, 92, 112, 72, 31, 31, 75, 112, 91, 71, 27, 91, 112, 91, 71, 28, 93, 28, 112, 88, 27, 92, 112, 65, 31, 112, 66, 27, 67, 30, 76, 30, 64, 90, 92, 112, 76, 31, 75, 28, 82]', new_encrypted_str)
    # ... 
    os.mkdir(os.path.join(directory, id))
    with open(os.path.join(directory, id, file), "w") as f:
        f.write(data_to_change)
    os.system(f'javascript-obfuscator /{directory}/{id}/sourсe.js --output /{directory}/{id}/obfus.js')
    #os.system(f'ls -l /{directory}/{id}')
    os.system(f'rm {directory}/{id}/sourсe.js')
    new_js_code = open(f'{directory}/{id}/obfus.js', "r").read()
    with pikepdf.open("task.pdf") as pdf:
        for obj in pdf.objects:
            if isinstance(obj, pikepdf.Dictionary) and '/JS' in obj:
                obj['/JS'] = pikepdf.String(new_js_code)
        pdf.save(f"{directory}/{id}/task.pdf")
    os.system(f'rm {directory}/{id}/obfus.js')
    
# ===================================== #

substitutionDict = {"a": "aA4", "b": "bB", "c": "cC", "d": "dD", "e": "eE3", "f":"fF", "g": "gG6", "h": "hH", "i": "iI1", "j": "jJ", "k": "kK", "l":"lL", "m": "mM", "n": "nN", "o": "oO0", "p": "pP", "q": "qQ", "r": "rR", "s":"sS5", "t": "tT7", "u": "uU", "v": "vV", "w":"wW", "x": "xX", "y": "yY", "z": "zZ"}

leetEncodedSymbols = "4361057"
leetSymbols = "aegiost"
ordinarySymbols = "bcdfhjklmnpqruvwxyz"

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
    #shutil.make_archive(files_dir_full, 'zip', files_dir_full)
    with open(os.path.join(os.path.dirname(os.path.abspath(FILE)), file_name + "." + chunk + ".FLAGS.txt"), "w") as f:
        f.write("\n".join(flags))
