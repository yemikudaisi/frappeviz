# main.py
import argparse
import os
import sys
from sys import modules
from umlbuilder import ClassGenerator
import json

#plantuml download link
plantuml_jar_link = r"""https://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fplantuml%2Ffiles%2Fplantuml.jar%2Fdownload&ts=1599539005"""

# Create the parser
arg_parser = argparse.ArgumentParser(description='Generates class diagram for Frappe Framewrok app.')

# Add the arguments
arg_parser.add_argument('app_dir',
                       metavar='dir',
                       type=str,
                       help='the path to frappe app')

arg_parser.add_argument('--output', '-o',
    help="Output directory",
    required=True)

# Execute the parse_args() method
args = arg_parser.parse_args()

input_path = args.app_dir
output_dir = args.output

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
        # read modules
        global app_modules
        with open(module_file_path, "r") as modules:
            for l in modules.readlines():
                app_modules.append(l.replace('\n',''))
        return True
    
    return False

def generate_doctype_uml(doctype_name, fields):
    """Generates class diagram for doctype given a list of fields
    """
    gen = ClassGenerator(doctype_name)
    for f in fields:
        gen.addField(f)
    return gen.to_plantuml()

if is_frappe_app_folder(input_path):
    print('Generating UML for ' + frappe_app_name)
else:
    print('Path to directory supplied is not a frappe app folder')
    sys.exit()

def get_folder_name(module_name):
    module_name = module_name.lower()
    module_name = module_name.replace(' ','_')
    return module_name

def generate_plantuml_graphics():
    """Generate plantuml image for corresponding plantuml files in output folder.
    Usage:
        %java -jar plantuml.jar -tsvg filname
    """
    for filename in os.listdir(output_dir):
        if filename.endswith(".plantuml"):
            command = "java -jar plantuml.jar %s" % os.path.join(output_dir,filename)
            print(command)
            os.system("java -jar plantuml.jar %s" % filename)
        else:
            continue


def write_app_module_output(module_file_name, module_uml):
    """Writes the plantuml uml text for a module to file given a module file name
    """
    if output_dir:
        if not os.path.isdir(output_dir):
            print("output directory does not exist")
        else:
            file = open(os.path.join(output_dir,module_file_name+'.plantuml'),"w")
            file.write(module_uml)
            file.close()
        
for m in app_modules:
    module_doctype_files = []
    module_path = os.path.join(input_path,frappe_app_name,get_folder_name(m))
    if os.path.isdir(module_path):
        module_doctype_dir = os.path.join(module_path, 'doctype')
        if os.path.isdir(module_doctype_dir):
            module_uml = '@startuml\npackage %s.%s <<Folder>> {' % (frappe_app_name,get_folder_name(m))
            for filename in os.listdir(module_doctype_dir):
                doctype_file = os.path.join(module_doctype_dir,filename, filename+'.json')
                if os.path.isfile(doctype_file):
                    with open(doctype_file) as f:
                        data = json.load(f)
                    module_uml += generate_doctype_uml(data['name'], data['fields'])
                    
            module_uml += '}\n@enduml'
            write_app_module_output(get_folder_name(m),module_uml)

generate_plantuml_graphics()

