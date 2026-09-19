import xml.etree.ElementTree as ET

tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}

def get_name(el):
    if el is None: return "Unknown"
    return el.get('Name', el.get('JamNotation', el.get('Notation', el.get('CircuitId', "Unknown"))))

uc_id = "803a0e93-ce4d-44fa-9c53-67c2337f7acc"
print("Symbols in UC:")
for sym in root.findall(f".//lc:CircuitSymbol[@LogicalCircuitId='{uc_id}']", ns):
    cid = sym.get('CircuitId')
    x = sym.get('X')
    y = sym.get('Y')
    target = root.find(f".//lc:LogicalCircuit[@LogicalCircuitId='{cid}']", ns)
    if target is None:
        target = root.find(f".//lc:Pin[@CircuitId='{cid}']", ns)
    if target is None:
        # Check standard gates
        if "000000020101" in cid: target_name = "AND"
        elif "000000040200" in cid: target_name = "OR"
        elif "000000010000" in cid: target_name = "NOT"
        elif "000000040300" in cid: target_name = "OR3"
        elif "000000020102" in cid: target_name = "AND3"
        else: target_name = cid
    else:
        target_name = get_name(target)
    
    print(f"  {target_name} at ({x}, {y})")

