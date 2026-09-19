import xml.etree.ElementTree as ET
import uuid

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd')

cg_id = '514b56b5-4981-4302-af71-d2bd7ee0e26c'

def delete_wire(x1, y1, x2, y2):
    for w in root.findall(f".//lc:Wire[@LogicalCircuitId='{cg_id}']", ns):
        if (w.get('X1') == str(x1) and w.get('Y1') == str(y1) and w.get('X2') == str(x2) and w.get('Y2') == str(y2)) or \
           (w.get('X1') == str(x2) and w.get('Y1') == str(y2) and w.get('X2') == str(x1) and w.get('Y2') == str(y1)):
            root.remove(w)
            return

def delete_sym(x, y):
    for sym in root.findall(f".//lc:CircuitSymbol[@LogicalCircuitId='{cg_id}']", ns):
        if sym.get('X') == str(x) and sym.get('Y') == str(y):
            root.remove(sym)
            return

def add_wire(x1, y1, x2, y2):
    w = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}Wire')
    w.set('WireId', str(uuid.uuid4()))
    w.set('LogicalCircuitId', cg_id)
    w.set('X1', str(x1))
    w.set('Y1', str(y1))
    w.set('X2', str(x2))
    w.set('Y2', str(y2))
    root.append(w)


delete_sym(31, 12)
delete_wire(24, 13, 31, 13)
delete_wire(34, 13, 37, 13)
add_wire(24, 13, 37, 13)

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', encoding='utf-8', xml_declaration=True)
