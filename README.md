# residual

# Residual.py is a function file, ie, module.

Read data from files and calculate the residuals between 2 set of data

The first and second columns of the file are the longitude abd latitude,
the third column is the data (for example, GPS rate) or model predictions.

The output file also contains the coordinates, but the third column is the residual.

The residual is calculated by data minus model predictions. 

The output file (ie, residual) is in the same path of the input file.


# Usage
use this script in shell command.

`python3 residual.py data reference_data(model predictions) output_file`

The data points in data file and the model prediction need to be equal. 