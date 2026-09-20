import xml.etree.ElementTree as ET
import uuid

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
ET.register_namespace('', ns['lc'])

cg_id = '514b56b5-4981-4302-af71-d2bd7ee0e26c'

# Remove existing broken symbols
symbols_to_remove = []
for sym in root.findall(f".//lc:CircuitSymbol[@LogicalCircuitId='{cg_id}']", ns):
    x, y = int(sym.get('X')), int(sym.get('Y'))
    if (x == 31 and y == 2) or (x == 31 and y == 9) or (x == 26 and y == 10):
        symbols_to_remove.append(sym)

for sym in symbols_to_remove:
    root.remove(sym)
    print(f"Removed broken symbol at {sym.get('X')},{sym.get('Y')}")

not_gate_id = str(uuid.uuid4())
gate = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}Gate')
gate.set('GateId', not_gate_id)
gate.set('GateType', 'Not')
root.append(gate)
print("Added NOT gate to Gate table")

for x, y in [(31, 2), (31, 9), (26, 10)]:
    sym = ET.Element('{http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd}CircuitSymbol')
    sym.set('CircuitSymbolId', str(uuid.uuid4()))
    sym.set('LogicalCircuitId', cg_id)
    sym.set('CircuitId', not_gate_id)
    sym.set('X', str(x))
    sym.set('Y', str(y))
    root.append(sym)
    print(f"Added NOT CircuitSymbol at {x},{y}")

tree.write('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject', xml_declaration=True, encoding='utf-8')
print("Consola_Grafica updated.")
