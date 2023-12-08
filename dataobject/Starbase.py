from xml.dom.minidom import Element

from dataobject.GalaxyObject import GalaxyObject


class Starbase(GalaxyObject):
#<Starbase internalID="Origins_Inner Source Starbase" 
# guid="1121-c14738e88" 
# name="Inner Source Starbase" 
# shipDesignName="Precursor_Starbase" 
# shipDesignScale="0.010000" 
# posX="304.899994" posY="187.600006" group=""/>
	
    def __init__(self, element:Element, object_guids):
        super().__init__(element, 'shipDesignName', object_guids)

        self.pos_x = element.attrib['posX']
        self.pos_y = element.attrib['posY']
    
    def print_details(self):
            print(self.name.upper())