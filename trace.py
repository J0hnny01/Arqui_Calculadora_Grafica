import xml.etree.ElementTree as ET
tree = ET.parse('/home/andresj21/Documentos/GitHub/Arqui_Calculadora_Grafica/Proyecto_Calc.CircuitProject')
root = tree.getroot()
ns = {'lc': 'http://LogicCircuit.net/2.0.0.14/CircuitProject.xsd'}
circuit_id = "37287e50-ff97-4dc2-b8e7-f31afc931f81"
for w in root.findall(f".//lc:Wire[@LogicalCircuitId='{circuit_id}']", ns):
    x1, y1 = w.get('X1'), w.get('Y1')
    x2, y2 = w.get('X2'), w.get('Y2')
    if (x1 == '48' and y1 == '9') or (x2 == '48' and y2 == '9'):
        print(f"Wire connected to 48,9: ({x1},{y1}) -> ({x2},{y2})")

