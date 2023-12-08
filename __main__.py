from ast import Dict
import sys
import xml.etree.ElementTree as ET
from dataobject.GalaxyObject import GalaxyObject
from dataobject.SolarSytem import SolarSystem
from dataobject.Starbase import Starbase

tree = ET.parse('sco_assets/Galaxies/StarControlGalaxy.xml')
galaxy = tree.getroot()
asdf = 1

# print (galaxy)
# print (galaxy.attrib)
# print (galaxy.tag)

#galaxy_guids = Dict(str, GalaxyObject)
galaxy_guids = {}

for object in galaxy:
    ElementClass = getattr(sys.modules[__name__], object.tag) #xml tag matches class name
    galaxy_object = ElementClass(object, galaxy_guids) #instantiate class for xml tag

for value in galaxy_guids.values():
    value.print_details()




#un = input('username: ')
#pw = input('password: ')

#print(f'{un} {pw}'