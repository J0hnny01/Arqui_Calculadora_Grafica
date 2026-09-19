import xml.etree.ElementTree as ET
tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}

# Unidad de Control
uc_id = "803a0e93-ce4d-44fa-9c53-67c2337f7acc"
# FIN:X PinId in UC
fin_x_pin_id = root.find(f".//lc:Pin[@CircuitId='{uc_id}'][@Name='FIN:X']", ns).get('PinId')
print(f"FIN:X PinId in UC: {fin_x_pin_id}")

# In ALU, what connects to the UC's FIN:X?
# The UC is represented as a CircuitSymbol in ALU.
uc_sym = root.find(f".//lc:CircuitSymbol[@CircuitId='{uc_id}']", ns)
if uc_sym is not None:
    uc_sym_id = uc_sym.get('CircuitSymbolId')
    print(f"UC CircuitSymbolId in ALU: {uc_sym_id}")

# We need to find the wire connected to this pin.
# LogicCircuit connects wires to pins of symbols by matching X/Y coordinates?
# Actually, wires connect to X,Y coordinates. We need to compute the X,Y of the FIN:X pin on the UC symbol.
# Or better, just print all wires in ALU and see what connects to DATAPATH and UC.

