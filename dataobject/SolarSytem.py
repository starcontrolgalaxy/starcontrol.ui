from xml.dom.minidom import Element

from dataobject.GalaxyObject import GalaxyObject
from dataobject.Planetoid import Planetoid


class SolarSystem(GalaxyObject):
#<SolarSystem internalID="Origins_Arcturus" 
# guid="3-100002468" 
# name="Arcturus" 
# posX="189.399994" 
# posY="412.500000" 
# starTemplate="red" 

# radius="55.000000" 
# isArena="false" 
# enabledForSMB="false" 
# canBeWanderedIn="true" 
# background="GreenNebula" 
# starMeleeGravityRadius="10.000000" 
# starMeleeGravityMagnitude="8.500000" 
# factionTemplate="scryve" group="">
	
    def __init__(self, element:Element, object_guids):
        super().__init__(element, 'starTemplate', object_guids)

        self.pos_x = element.attrib['posX']
        self.pos_y = element.attrib['posY']
        
        self.planetoids = []

        for planetoid in element:
            if (planetoid.tag != 'AsteroidBelt'):
                self.planetoids.append(Planetoid(planetoid, 1, object_guids))
     
    
    def print_details(self):
            print(self.name.upper())
 

#<AsteroidBelt internalID="Origins_The Asteroid Belt" 
# guid="89-a44d94944" 
# name="The Asteroid Belt" 
# orbitRadius="60.000000" radius="3.500000" 
# asteroidBeltTemplate="default"/>

#<AsteroidBelt internalID="Origins_The Kuiper Belt" 
# guid="89-a44d94945" 
# name="The Kuiper Belt" 
# orbitRadius="152.000000" radius="3.500000" 
# asteroidBeltTemplate="default"/>

#<AsteroidBelt internalID="Origins_Proxima Centauri Asteroid Belt" 
# guid="3-a00000206" 
# name="Proxima Centauri Asteroid Belt" 
# orbitRadius="21.000000" radius="5.500000" 
# asteroidBeltTemplate="default"/>
	