from xml.dom.minidom import Element


class GalaxyObject:
        'Base class for common attributes of things found on the galaxy map'
        def __init__(self, element:Element, template_key:str, object_guids):
            self.element = element
            
            self.guid = element.attrib['guid']
            self.name = element.attrib['name']
            self.template = element.attrib[template_key]
        
            object_guids[self.guid] = self

        #def print_details():
            #an interface/abstract for inheritors to implement
