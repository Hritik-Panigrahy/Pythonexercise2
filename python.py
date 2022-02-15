from json2html import *
import json
with open('test_status.json','r') as f:
    data = json.load(f)

file=json2html.convert(json = data)
f = open('GFG.html', 'w')
f.write(file)

#close the file
f.close()
print("Task Completed")