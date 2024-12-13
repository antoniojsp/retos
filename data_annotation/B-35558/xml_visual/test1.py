import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Access elements
for elem in root:
    print(elem.tag, elem.text)

# Access attributes
for concept in root.find('Concepts'):
    print(concept.attrib['Concept_Sno'], concept.attrib['Concept_name'])

# Access specific elements
description = root.find('sub_topic_description').text
print(description)