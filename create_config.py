from jinja2 import Template
import json



with open('ConfTemplate.txt','r') as fp:
    loadtemplate=fp.read()

with open('Clients.txt') as json_file:
    clients=json.load(json_file)

jinjatemplate=Template(loadtemplate)


for key in clients:
    hostname=key
    ip=clients[key]
    conf=jinjatemplate.render(hostname=hostname,ip=ip)
myfile=open(key+'.conf','w') #to move in the for loop
result=myfile.writelines(conf)#to move in the for loop

