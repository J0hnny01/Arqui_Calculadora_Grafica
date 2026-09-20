import xml.etree.ElementTree as ET
import uuid

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', ns['lc'])

dp_id = '37287e50-ff97-4dc2-b8e7-f31afc931f81'

wires_to_delete = []
for w in root.findall(f".//lc:Wire[@LogicalCircuitId='{dp_id}']", ns):
    x1, x2 = int(w.get('X1')), int(w.get('X2'))
    y1, y2 = int(w.get('Y1')), int(w.get('Y2'))
    if (x1 == 4 and y1 == 11 and x2 == 5 and y2 == 11) or (x1 == 5 and y1 == 11 and x2 == 4 and y2 == 11):
        wires_to_delete.append(w)
    elif (x1 == 4 and y1 == 15 and x2 == 6 and y2 == 15) or (x1 == 6 and y1 == 15 and x2 == 4 and y2 == 15):
        wires_to_delete.append(w)

for w in wires_to_delete:
    root.remove(w)
    print(f"Deleted wire {w.get('X1')},{w.get('Y1')} -> {w.get('X2')},{w.get('Y2')}")

# Add new wires
new_wires = [
    # E_m to y input
    (4, 11, 4, 13),
    (4, 13, 6, 13),
    (6, 13, 6, 15),
    # E_b to x input
    (4, 15, 5, 15),
    (5, 15, 5, 11),
]

for x1, y1, x2, y2 in new_wires:
    elem = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}Wire')
    elem.set('WireId', str(uuid.uuid4()))
    elem.set('LogicalCircuitId', dp_id)
    elem.set('X1', str(x1))
    elem.set('Y1', str(y1))
    elem.set('X2', str(x2))
    elem.set('Y2', str(y2))
    root.append(elem)
    print(f"Added wire {x1},{y1} -> {x2},{y2}")

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', xml_declaration=True, encoding='utf-8')
print("File updated successfully.")
