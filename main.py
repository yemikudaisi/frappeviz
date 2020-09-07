# main.py
import argparse
import os
import sys

# Create the parser
arg_parser = argparse.ArgumentParser(description='Generates class diagram for Frappe Framewrok app.')

# Add the arguments
arg_parser.add_argument('Directory',
                       metavar='dir',
                       type=str,
                       help='the path to frappe app')

# Execute the parse_args() method
args = arg_parser.parse_args()

input_path = args.Directory

frappe_app_name = ''
app_modules = []

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

def is_frappe_app_folder(path_to_app):
    """Check if a modules.txt file exists within a python module (folder) that shares exactly
    the same name as the frappe app supplied
    """

    global frappe_app_name
    frappe_app_name  = os.path.basename(os.path.normpath(path_to_app))
    module_file_path = os.path.join(path_to_app, frappe_app_name, 'modules.txt') 

    if os.path.isfile(module_file_path):
        return True
    
    return False

if is_frappe_app_folder(input_path):
    print('Frappe App name: ' + frappe_app_name)
else:
    print('Path to directory supplied is not a frappe app folder')
    sys.exit()
