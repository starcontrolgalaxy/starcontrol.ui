from xml.dom.minidom import Element

from dataobject.GalaxyObject import GalaxyObject


class Planetoid(GalaxyObject):
#<Planetoid internalID="Origins_Arcturus I" 
# guid="3-100002469" 
# name="Arcturus I" 
# orbitRadius="225.799988" 
# radius="2.600000" 
# rotationSpeed="1.300000" 
# planetTemplate="Green"

# orbitYaw="-279.621582" 
# axisTilt="0.000000"  
# meleeOrbitSpeed="0.028877" 
# meleeGravityRadius="10.000000" 
# meleeGravityMagnitude="7.250000">

    def __init__(self, element:Element, layer:int, object_guids):
        super().__init__(element, 'planetTemplate', object_guids)

        self.nest_layer = layer
        
        self.orbit_radius = element.attrib['orbitRadius']
        self.radius = element.attrib['radius']
        self.rotation_speed = element.attrib['rotationSpeed']

        self.planetoids = []
        
        for planetoid in element:
            self.planetoids.append(Planetoid(planetoid, layer+1, object_guids))

     
    def print_details(self):
            tab_spaces = '     '*self.nest_layer
            print(f'{tab_spaces}{self.name} [{self.template}]') 

        
