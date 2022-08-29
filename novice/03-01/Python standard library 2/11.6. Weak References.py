import weakref, gc
class A:
    def __init__(self, value):
         self.value = value
    def __repr__(self):
        return str(self.value)
...
a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print(d['primary'])   

del a                       # remove the one reference
print(gc.collect()) 
print(d['primary'])