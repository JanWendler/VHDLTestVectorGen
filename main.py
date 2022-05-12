# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:07:16 2022

@author: andreas.senn
"""

import struct


def double_to_hex(f):
    if f == 0:
        return "0x0000000000000000"
    return hex(struct.unpack('<Q', struct.pack('<d', f))[0])


def genTestVector(inputFilePath):
    output = ""
    with open(inputFilePath, "r") as file:
        data = file.read().splitlines()
    info = data[:4]
    data = data[4:]
    output = "constant " + info[0] + " : " + info[1] + "(0 to " + info[2] + " - 1)(" + info[3] + " - 1 downto 0) := (\n"
    for line in data:
        if line == (len(data))-1:
            output += "\tX\"" + double_to_hex(float(line))[2:] + "\""
        else:
            output += "\tX\"" + double_to_hex(float(line))[2:] + "\",\n"
    output = output[:-2]
    output += ");"
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputFilePath = "input.txt"
    outputFilePath = "output.txt"
    output = genTestVector(inputFilePath)
    with open(outputFilePath, "w") as file:
        file.write(output)
