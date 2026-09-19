import xml.etree.ElementTree as ET
import uuid

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd')

cg_id = '514b56b5-4981-4302-af71-d2bd7ee0e26c'

def delete_wire(x1, y1, x2, y2):
    wires = root.findall(f".//lc:Wire[@LogicalCircuitId='{cg_id}']", ns)
    for w in wires:
        if (w.get('X1') == str(x1) and w.get('Y1') == str(y1) and w.get('X2') == str(x2) and w.get('Y2') == str(y2)) or \
           (w.get('X1') == str(x2) and w.get('Y1') == str(y2) and w.get('X2') == str(x1) and w.get('Y2') == str(y1)):
            root.remove(w)

def delete_sym(x, y):
    syms = root.findall(f".//lc:CircuitSymbol[@LogicalCircuitId='{cg_id}']", ns)
    for sym in syms:
        if sym.get('X') == str(x) and sym.get('Y') == str(y):
            root.remove(sym)

def add_wire(x1, y1, x2, y2):
    w = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}Wire')
    w.set('WireId', str(uuid.uuid4()))
    w.set('LogicalCircuitId', cg_id)
    w.set('X1', str(x1))
    w.set('Y1', str(y1))
    w.set('X2', str(x2))
    w.set('Y2', str(y2))
    root.append(w)

def add_not_gate(x, y):
    sym = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}CircuitSymbol')
    sym.set('CircuitSymbolId', str(uuid.uuid4()))
    sym.set('CircuitId', '00000000-0000-0000-0000-000000020101')
    sym.set('LogicalCircuitId', cg_id)
    sym.set('X', str(x))
    sym.set('Y', str(y))
    root.append(sym)

# Delete old overlapping NOT gates and their wires
delete_sym(31, 10)
delete_wire(24, 11, 31, 11)
delete_wire(34, 11, 37, 11)

delete_sym(31, 11)
delete_wire(24, 12, 31, 12)
delete_wire(34, 12, 37, 12)

# Place NOT gate for Bit 0 (Y=11) at X=26
add_not_gate(26, 10)
add_wire(24, 11, 26, 11)
add_wire(29, 11, 37, 11)

# Place NOT gate for Bit 1 (Y=12) at X=31
add_not_gate(31, 11)
add_wire(24, 12, 31, 12)
add_wire(34, 12, 37, 12)

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', encoding='utf-8', xml_declaration=True)
