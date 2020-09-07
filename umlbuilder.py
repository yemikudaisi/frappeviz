
from relationships import Composition

class Docfield:

    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name
    
    def __str__(self):
        return '%s : %s' % (self.name, self.type_name)

class ClassGenerator:
    fields = []
    relationships = []
    def __init__(self, class_name):
        self.class_name = class_name
    
    def addField(self, fieldObj):
        if fieldObj['fieldtype'] == 'Link':
            self.relationships.append(Composition(self.class_name).has(fieldObj['options'],fieldObj['fieldname']))
        self.fields.append(Docfield(fieldObj['fieldname'], fieldObj['fieldtype']))
    
    def to_plantuml(self):
        output = ''

        for r in self.relationships:
            output += str(r)+'\n'

        output += 'class "%s" {' % (self.class_name)
        for f in self.fields:
            output += '\n  '+str(f)
        output += '\n}'
        return output
