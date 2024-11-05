import xml.etree.ElementTree as ET

xml_datos = """
<persona>
    <nombre>moises</nombre>
    <edad>33</edad>
    <prop3>
        <prop4><v>Moises</v></prop4>
    </prop3>
</persona>
"""

root = ET.fromstring(xml_datos)
for child in root:
    print (child.tag,child.text)
    print (child.items)
    # mas codigo aca si tiene hijos
#print (root.find('nombre').tag)
#print (root.find('edad').text)


#tree = ET.parse("xmlfile.xml", )
#root = tree.getroot()

#for child in root:
#    print(child.tag, child.text)