import os
import json
from jinja2 import Template

output_dir = "output_configs"

with open('ConfTemplate.j2', 'r') as fp:
    loadtemplate = fp.read()

with open('clients.json', 'r') as json_file:
    clients = json.load(json_file)

jinjatemplate = Template(loadtemplate)

os.makedirs(output_dir, exist_ok=True)
for hostname, ip in clients.items():
    conf = jinjatemplate.render(hostname=hostname, ip=ip)
    with open(os.path.join(output_dir, hostname + '.conf'), 'w') as myfile:
        result = myfile.writelines(conf)


