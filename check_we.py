import xml.etree.ElementTree as ET
tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}

pan_id = '18a5ebd5-8124-420b-92c5-0ee70b10f8b6'
celda_id = '7d203fa8-19dc-4675-9b4f-b14da2be3e1d'

# WE_ln is pin ffb371ad-067f-4fa5-9056-71e1804d643a
# It's a pin of Celda. So in Pantalla 8x8, it's a Pin of the CircuitSymbol of Celda.
# But LogicCircuit just uses coordinates to connect wires to symbols.
# We need to know where WE_ln is on the Celda symbol.
# From earlier, WE_ln is PinType Input, PinSide Left.
# Let's find one Celda in Pantalla 8x8 and trace its WE_ln.

# Find a Celda
celdas = root.findall(f".//lc:CircuitSymbol[@CircuitId='{celda_id}'][@LogicalCircuitId='{pan_id}']", ns)
print(f"Found {len(celdas)} Celdas in Pantalla 8x8")
if len(celdas) > 0:
    c = celdas[0]
    x, y = int(c.get('X')), int(c.get('Y'))
    print(f"First Celda at {x}, {y}")
    # Pins on left side are at X.
    # We need to find which Y is WE_ln.
    # Usually they are ordered top to bottom.
    # Fila_ln, Col_ln, WE_ln, Pixel_In, Reset_in.
    
    # Let's just find all wires touching X of this Celda.
    wires = root.findall(f".//lc:Wire[@LogicalCircuitId='{pan_id}']", ns)
    for w in wires:
        x1, y1 = int(w.get('X1')), int(w.get('Y1'))
        x2, y2 = int(w.get('X2')), int(w.get('Y2'))
        if x1 == x and y <= y1 <= y+10:
            print(f"Wire connected to left side: {x1},{y1} -> {x2},{y2}")
        elif x2 == x and y <= y2 <= y+10:
            print(f"Wire connected to left side: {x2},{y2} -> {x1},{y1}")

