#!/usr/bin/env python3
# read data from files and calculate the residuals between 2 set of data

import sys
import os


# functions
def readdata(filename):
    """
    :param filename: filename of data and reference data
    :return: a list contain all coordinates and data and reference data
    """
    lines = []
    with open(filename, 'r') as filelines:
        for line in filelines.readlines():
            line = line.split()
            if line[0] == '#':
                continue
            # print(line)
            # print(x, y, val)
            lines.append(line)
    return lines


def calres(datalists, rfdatalists):
    """
    :param datalists: list of data
    :param rfdatalists: list of reference data
    :return: residual = data - reference data, list.
    """
    residual = []
    for fdatalist in datalists:
        for rfdatalist in rfdatalists:
            if float(fdatalist[0]) == float(rfdatalist[0]) and float(fdatalist[1]) == float(rfdatalist[1]):
                residual.append([fdatalist[0], fdatalist[1], str(round(float(fdatalist[2])-float(rfdatalist[2]), 8))])
    return residual


def write_output(reslist, output_filename):
    with open(output_filename, 'w') as out_file:
        for i in range(len(reslist)):
            for j in range(len(reslist[i])):
                out_file.write(str(reslist[i][j])+' ')
            out_file.write('\n')
    out_file.close()


# main program
# Read command line arguments
if len(sys.argv) == 3:
    data = sys.argv[1]
    reference_data = sys.argv[2]
    output_file = 'stdout'
    # print(data)
    # print(reference_data)
elif len(sys.argv) == 4:
    data = sys.argv[1]
    reference_data = sys.argv[2]
    output_file = sys.argv[3]
    # print(data)
    # print(reference_data)
    # print(output_file)
else:
    print('Correct usage: residual.py data reference_data output_file ')
    sys.exit()

# Check if the file exists
if os.path.isfile(str(data)):
    pass
else:
    print("Cannot find file", data)
    sys.exit()

if os.path.isfile(str(reference_data)):
    pass
else:
    print("Cannot find file", reference_data)
    sys.exit()

if output_file == 'stdout':
    print('Output is printed on your screen')
elif output_file == 'auto':
    pass
else:
    if os.path.isfile(str(output_file)):
        pass
    else:
        print("Cannot find file", output_file)
        print('creat the new output file', output_file)
        os.system('touch ' + str(output_file))

datalist = readdata(str(data))
# print(datalist)
reference_datalist = readdata(str(reference_data))
# print(reference_datalist)
res = calres(datalist, reference_datalist)

if output_file == 'stdout':
    print(res)
elif output_file == 'auto':
    write_output(res, str(data) + '-' + str(reference_data) )
else:
    write_output(res, str(output_file))
