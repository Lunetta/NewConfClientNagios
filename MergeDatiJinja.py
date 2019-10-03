from jinja2 import Template
with open('ConfTemplate.txt','r') as fp:
    line=fp.read()

hostname='LUNA'
ip='123.123.123.123'
print(line)
tm=Template(line)
conf=tm.render(hostname=hostname,ip=ip)

print(conf)
