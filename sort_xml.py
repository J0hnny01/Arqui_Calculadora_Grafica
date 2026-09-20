import xml.etree.ElementTree as ET

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', ns['lc'])

tag_order = [
    'Project',
    'LogicalCircuit',
    'Pin',
    'Constant',
    'CircuitButton',
    'LedMatrix',
    'Splitter',
    'Gate',
    'CircuitSymbol',
    'Wire',
    'TextNote'
]

# Create a mapping of tag to index
tag_map = {f"{{{ns['lc']}}}{tag}": i for i, tag in enumerate(tag_order)}

# Extract all children
children = list(root)
# Remove all children
for c in children:
    root.remove(c)

# Sort children
def get_order(elem):
    return tag_map.get(elem.tag, 99)

children.sort(key=get_order)

# Re-append in order
for c in children:
    root.append(c)

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', xml_declaration=True, encoding='utf-8')
print("XML sorted.")
