#!/usr/bin/env python3
# read data from files and calculate the residuals between 2 set of data

import sys
import os
from Residual import read_file, calculate_residual, write_output

if len(sys.argv) == 3:
    data = sys.argv[1]
    model = sys.argv[2]
    output_file = 'stdout'
    # print(data)
    # print(reference_data)
elif len(sys.argv) == 4:
    data = sys.argv[1]
    model = sys.argv[2]
    output_file = sys.argv[3]
    # print(data)
    # print(reference_data)
    # print(output_file)
else:
    print('Correct usage: residual.py data model output_file')
    sys.exit()

data = str(data)
model = str(model)
output_file = str(output_file)
Gfile_path = os.path.split(os.path.abspath(data))
# Check if the file exists
if os.path.isfile(data):
    pass
else:
    print("Cannot find file", data)
    sys.exit()

if os.path.isfile(model):
    pass
else:
    print("Cannot find file", model)
    sys.exit()

if output_file == 'stdout':
    print('Output will be printed on your screen')
elif os.path.isfile(output_file):
    pass
else:
    print("Cannot find file", output_file, 'create the new output file', output_file)
    os.system('touch ' + output_file)

# read the data (GPS data)
Gdata_lon, Gdata_lat, Gdata_values = read_file(data)
# read the model predictions
Gmodel_lon, Gmodel_lat, Gmodel_values = read_file(model)

Glon, Glat, Gresidual = calculate_residual(Gdata_lon, Gdata_lat, Gdata_values, Gmodel_lon, Gmodel_lat, Gmodel_values)


if output_file == 'stdout':
    print(Gresidual)
else:
    write_output(Glon, Glat, Gresidual, Gfile_path[0], output_file)
