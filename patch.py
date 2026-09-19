import xml.etree.ElementTree as ET
import uuid

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd')

uc_id = '803a0e93-ce4d-44fa-9c53-67c2337f7acc'

wires_to_delete = [
    'b03c7aa3-3f99-4f21-92ef-900e24bd4a4a',
    '22f8fd90-1bfd-4548-851f-bf6a02caacaa',
    'a8962414-9c47-4968-af26-03f28d81f6ac',
    '9154dc70-ca0a-4607-87e3-3b157dc60cae'
]

for w_id in wires_to_delete:
    w = root.find(f".//lc:Wire[@WireId='{w_id}']", ns)
    if w is not None:
        root.remove(w)

def add_wire(x1, y1, x2, y2, circuit_id):
    w = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}Wire')
    w.set('WireId', str(uuid.uuid4()))
    w.set('LogicalCircuitId', circuit_id)
    w.set('X1', str(x1))
    w.set('Y1', str(y1))
    w.set('X2', str(x2))
    w.set('Y2', str(y2))
    root.append(w)

add_wire(46, 14, 50, 24, uc_id) # D4 to FF-D
add_wire(46, 12, 62, 12, uc_id) # D2 to IN:X
add_wire(62, 12, 62, 21, uc_id) # IN:X routing

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', encoding='utf-8', xml_declaration=True)
