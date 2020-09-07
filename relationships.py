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