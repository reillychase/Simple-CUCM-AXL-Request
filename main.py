from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
wsdl = 'file:///C:/Users/you/PyCharmProjects/project/network-stats/AXLAPI.wsdl'
location = 'https://cucm:8443/axl/'
username = 'user'
password = 'password'

tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/',
             'http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)

client = Client(wsdl,location=location,faults=False,plugins=[ImportDoctor(imp)],
                username=username,password=password)
resp = client.service.listPhone({'name': '%'}, returnedTags={'name': '', 'description': ''})
print resp
