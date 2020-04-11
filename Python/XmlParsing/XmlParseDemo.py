import xml.etree.ElementTree as ET;


catalog = ET.parse('plant_catalog.xml');
catalogRoot = catalog.getroot();

def PrintXmlChild(xmlNode):	
	for childNode in xmlNode.iter(): #retruns depth first iterator for the tree
		print("PrintXmlChild tag: %s, attr: %s, text: %s" %(childNode.tag, childNode.attrib, childNode.text));


PrintXmlChild(catalogRoot)		


#for child in catalogRoot:
#	PrintXmlChild(child);
	#print(child.tag, child.attrib);		
		
#for child in catalogRoot.iter():
	#PrintXmlChild(child);
	#print(child.tag, child.attrib);
	
	
#for country in root.findall('country'):
#     rank = country.find('rank').text
#     name = country.get('name')
#     print(name, rank)
#