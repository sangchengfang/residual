#!/usr/bin/env python3
# read data from files and calculate the residuals between 2 set of data

import sys
import os


def read_file(file):
    """
    :param file: filename of data and reference data
    the first and second columns are the longitude abd latitude, the third column is the data
    :return: a list contain all coordinates and data (GPS rates or model predictions)
    """
    lon = []
    lat = []
    values = []
    with open(file, 'r') as lines:
        for line in lines.readlines():
            line = line.split()
            if line[0] != '#':
                lon.append(line[0])
                lat.append(line[1])
                values.append(line[2])
            else:
                continue
    return lon, lat, values


def calculate_residual(data_lon, data_lat, data_values, model_lon, model_lat, model_values):
    """
    :param data_lon: longitude from data file
    :param data_lat: latitude from data file
    :param data_values: data
    :param model_lon: longitude from model prediction file
    :param model_lat: latitude from model prediction file
    :param model_values: model predictions
    :return: return the residual between model prediction and data
    """
    lon = []
    lat = []
    residual = []
    list_length = [len(data_lon), len(data_lat), len(data_values), len(model_lon), len(model_lat), len(model_values)]
    length = len(list_length)
    for i in range(length-1):
        if list_length[i] == list_length[i+1]:
            element_number_equal = True
        else:
            element_number_equal = False
            print('The data points of the data and the model predictions are different')
            break

    for i in range(len(data_lon)):
        if float(data_lon[i]) == float(model_lon[i]) and float(data_lat[i]) == float(model_lat[i]):
            lon.append('{:.2f}'.format(float(data_lon[i])))
            lat.append('{:.2f}'.format(float(data_lat[i])))
            result = float(data_values[i])-float(model_values[i])
            residual.append('{:.8f}'.format(result))

    return lon, lat, residual


def write_output(lon, lat, residual, file_path, output_filename):

    with open(file_path + '/' + output_filename, 'w') as out_file:
        for i in range(len(lon)):
            out_file.write(str(lon[i]).ljust(10))
            out_file.write(str(lat[i]).ljust(10))
            out_file.write(str(residual[i]))
            out_file.write('\n')


# main()
def main():
    # main program
    # Read command line arguments
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

    Glon, Glat, Gresidual = calculate_residual(Gdata_lon, Gdata_lat, Gdata_values, Gmodel_lon, Gmodel_lat,
                                               Gmodel_values)

    if output_file == 'stdout':
        print(Gresidual)
    else:
        write_output(Glon, Glat, Gresidual, Gfile_path[0], output_file)


if __name__ == "__main__":
    main()