# main.py
import argparse
import os
import sys
from sys import modules
import json

frappe_app_modules = []

def is_frappe_app_folder(path_to_app):
    """Check if a modules.txt file exists within a python module (folder) that shares exactly
    the same name as the frappe app dir supplied
    """

    global frappe_app_name,frappe_app_modules
    frappe_app_name  = os.path.basename(os.path.normpath(path_to_app))
    module_file_path = os.path.join(path_to_app, frappe_app_name, 'modules.txt') 

    # If a 'modules.txt' file exists
    if os.path.isfile(module_file_path):
       
        # fetch app modules from file content in to a global variable
        with open(module_file_path, "r") as modules:
            for l in modules.readlines():
                frappe_app_modules.append(l.replace('\n',''))
        return True
    
    return False

class Composition:
    """ Python class that represents a class composition relationship
    """
    def __init__(self, class_name):
        self.owner_class_name = class_name

    def has(self, other_class_name, comment = ''):
        """Add a composition relationship between owner class to another class
        """
        self.child_class_name = other_class_name
        self.comment = comment
        return self
    
    def __str__(self):
        """PlantUML string representation of class diagram"""
        output = '"%s" *-- "%s"' % (self.child_class_name,self.owner_class_name)
        
        #check if a comment was supplied
        if not self.comment == '':
            output += ': %s' % (self.comment)

        return output

class Extension:
    """ Python class for extension class relartionship
    """
    def __init__(self, class_name):
        self.child_class_name = class_name

    def extends(self, other_class_name, comment = ''):
        self.parent_class_name = other_class_name
        self.comment = comment
        return self
    
    def __str__(self):
        """PlantUML string representation of class diagram"""
        output = '"%s" <|- "%s" : %s' % (self.parent_class_name,self.child_class_name)
        
         #check if a comment was supplied
        if not self.comment == '':
            output += ': %s' % (self.comment)

class Docfield:
    """ Python representing docfield in a frappe doctype
    """
    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name
    
    def __str__(self):
        return '%s : %s' % (self.name, self.type_name)

class ClassGenerator:
    """Doctype class diagram UML generator
    """
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []
        self.relationships = []
    
    def addField(self, fieldObj):
        """ Adds a docfield to a class"""
        if fieldObj['fieldtype'] == 'Link':
            self.relationships.append(Composition(self.class_name).has(fieldObj['options'],fieldObj['fieldname']))
        self.fields.append(Docfield(fieldObj['fieldname'], fieldObj['fieldtype']))
    
    def to_plantuml(self):
        """ Returns PlantUML class diagram for doctype in text format
        """
        output = ''

        for r in self.relationships:
            output += '\n'+str(r)

        output += '\n  class "%s" {' % (self.class_name)
        for f in self.fields:
            output += '\n    '+str(f)
        output += '\n  }\n'
        return output

def generate_doctype_uml(doctype_name, fields):
    """Generates class diagram for doctype given a list of fields
    """
    gen = ClassGenerator(doctype_name)
    for f in fields:
        gen.addField(f)
    return gen.to_plantuml()

def get_folder_name(module_name):
    """ Basically converts
    'Hello World' to 'hello_word'
    """
    return module_name.lower().replace(' ','_')

def generate_plantuml_graphics():
    """Generate plantuml image for corresponding plantuml files in output folder.
    """
    for filename in os.listdir(output_dir):
        if filename.endswith('.plantuml'):
            command = 'python3 -m plantuml %s' % os.path.join(output_dir,filename)
            os.system(command)
            continue

def write_app_module_output(module_file_name, module_uml):
    """Writes the plantuml uml text for a module to file given a module file name
    """
    if output_dir:
        if not os.path.isdir(output_dir):
            print('output directory does not exist')
        else:
            file = open(os.path.join(output_dir,module_file_name+'.plantuml'),"w")
            file.write(module_uml)
            file.close()

def generate_plantuml_text():
    # Loop through app modules and generate UML packages and classes for respective modules and doctypes    
    for m in frappe_app_modules:
        module_path = os.path.join(frappe_app_dir,frappe_app_name,get_folder_name(m))
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

if __name__ == '__main__':
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

    # Parse arguments
    args = arg_parser.parse_args()

    global frappe_app_dir, output_dir
    frappe_app_dir = args.app_dir
    output_dir = args.output

    if not os.path.isdir(frappe_app_dir):
        print('Frappe app directory does not exist')
        sys.exit()

    # Validate frappe app directory passed as argument
    if is_frappe_app_folder(frappe_app_dir):
        print('Generating UML for ' + frappe_app_name)
    else:
        print('Directory is not a frappe app.')
        sys.exit()

    generate_plantuml_text()
    generate_plantuml_graphics()