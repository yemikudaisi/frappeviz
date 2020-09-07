import json
from umlbuilder import ClassGenerator

with open('test.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(data['name'])

def generate_doctype_uml(doctype_name, fields):
    """Generates class diagram for doctype given a list of fields
    """
    gen = ClassGenerator(doctype_name)
    for f in fields:
        gen.addField(f)
    
    print(gen.to_plantuml())

generate_doctype_uml(data['name'], data['fields'])