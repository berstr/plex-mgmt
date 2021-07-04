import re

def parse_filename(filename):
    result = None
    pattern = '^(.*) \- (.*) \((.*)\)$'
    m = re.match(pattern,filename)
    #print(m)
    if (m != None) and (m.group() == filename) and (len(m.groups()) == 3):
        result = {'artist':m.group(1),'title':m.group(2),'year':m.group(3)}
    return result
