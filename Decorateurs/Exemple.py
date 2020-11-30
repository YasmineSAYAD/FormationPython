class Player:
    def __init__(self,name):
        self.name=name

    @property
    def get_name(self):
        return self.name

    @property.setter
    def set_name(self,name):
        if len(name)<=25:
            self.name=name
        else:
            print("trop long")
    @staticmethod
    def one_method():
        pass

    @classmethod
    def another_method():
        pass
""" 
    name=property(get_name,set_name)
    one_method=staticmethod(one_method)
    another_method=classmethod(another_method)
"""

"""
@property remplace ça:
name=property()
name.setter(set_name)
"""