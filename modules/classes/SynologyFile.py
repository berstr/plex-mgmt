import os

import config 

class SynologyFile:

    def __init__(self,path):
       self.path = path
       temp = os.path.splitext(os.path.basename(path))
       self.name = temp[0]
       self.ext = temp[1][1:]
       self.dir = os.path.dirname(path)
       self.filename = os.path.basename(path)

    def __str__(self):
        return f'{self.filename}  [{self.dir}]'