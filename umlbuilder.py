class Composition:

    def __init__(self, class_name):
        self.owner_class_name = class_name

    def has(self, other_class_name, comment = ''):
        self.child_class_name = other_class_name
        self.comment = comment
        return self
    
    def __str__(self):
        output = '"%s" *-- "%s"' % (self.child_class_name,self.owner_class_name)
        if not self.comment == '':
            output += ': %s' % (self.comment)

        return output

class Extension:

    def __init__(self, class_name):
        self.child_class_name = class_name

    def extends(self, other_class_name, comment = ''):
        self.parent_class_name = other_class_name
        self.comment = comment
        return self
    
    def __str__(self):
        return '"%s" <|- "%s" : %s' % (self.parent_class_name,self.child_class_name, self.comment)

class Docfield:

    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name
    
    def __str__(self):
        return '%s : %s' % (self.name, self.type_name)

class ClassGenerator:

    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []
        self.relationships = []
    
    def addField(self, fieldObj):
        if fieldObj['fieldtype'] == 'Link':
            self.relationships.append(Composition(self.class_name).has(fieldObj['options'],fieldObj['fieldname']))
        self.fields.append(Docfield(fieldObj['fieldname'], fieldObj['fieldtype']))
    
    def to_plantuml(self):
        output = ''

        for r in self.relationships:
            output += '\n'+str(r)

        output += '\n  class "%s" {' % (self.class_name)
        for f in self.fields:
            output += '\n    '+str(f)
        output += '\n  }\n'
        return output
