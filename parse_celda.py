import xml.etree.ElementTree as ET

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}

celda_id = "7d203fa8-19dc-4675-9b4f-b14da2be3e1d"

def get_name(cid):
    target = root.find(f".//lc:LogicalCircuit[@LogicalCircuitId='{cid}']", ns)
    if target is not None: return target.get('Name')
    target = root.find(f".//lc:Pin[@CircuitId='{cid}']", ns)
    if target is not None: return target.get('Name')
    if "000000020101" in cid: return "AND2"
    if "000000040200" in cid: return "OR"
    if "000000010000" in cid: return "NOT"
    if "000000040300" in cid: return "AND3"
    return cid

symbols = {}
print("Symbols in Celda:")
for sym in root.findall(f".//lc:CircuitSymbol[@LogicalCircuitId='{celda_id}']", ns):
    sid = sym.get('CircuitSymbolId')
    cid = sym.get('CircuitId')
    name = get_name(cid)
    symbols[sid] = name
    print(f"  {sid}: {name} at ({sym.get('X')}, {sym.get('Y')})")

print("\nWires in Celda:")
for w in root.findall(f".//lc:Wire[@LogicalCircuitId='{celda_id}']", ns):
    print(f"  {w.get('X1')},{w.get('Y1')} -> {w.get('X2')},{w.get('Y2')}")

