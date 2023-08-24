from opentrons import protocol_api
from opentrons import types
import numpy as np
import json

'''Define coordinates of labware'''

alphabets = ['A','B']
numbers = ['2','3','4','6','7','8','10','11','12','14','15','16','18','19','20','22','23','24']

# Custom 3D-Printed grid in Shien PP Box
plate_coord = np.array([])

for alphas in alphabets:
    for nums in numbers:
        coords = alphas + nums
        plate_coord = np.append(plate_coord, coords)

# Custom 3D-Printed 0.5ml Centrifuge tube holder
centri_holder = np.array([])

alphabet = ['A','B','C','D','E','F']
number = ['1','2','3','4','5','6']

for alpha in alphabet:
    for num in number:
        coord = alpha + num
        centri_holder = np.append(centri_holder,coord)

# Remove the last element of the array as we don't want to use the 25th slot on the microcentrifuge tube rack (for now)
# centri_holder = np.delete(,centri_holder-4)


'''Custom declared labware used'''

# Insert the Shien PP Box + 3D Printed grids
LABWARE_DEF_grid_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","L1"],["A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","K2","L2"],["A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","K3","L3"],["A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","K4","L4"],["A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","K5","L5"],["A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","K6","L6"],["A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","K7","L7"],["A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","K8","L8"],["A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","K9","L9"],["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10","K10","L10"],["A11","B11","C11","D11","E11","F11","G11","H11","I11","J11","K11","L11"],["A12","B12","C12","D12","E12","F12","G12","H12","I12","J12","K12","L12"],["A13","B13","C13","D13","E13","F13","G13","H13","I13","J13","K13","L13"],["A14","B14","C14","D14","E14","F14","G14","H14","I14","J14","K14","L14"],["A15","B15","C15","D15","E15","F15","G15","H15","I15","J15","K15","L15"],["A16","B16","C16","D16","E16","F16","G16","H16","I16","J16","K16","L16"],["A17","B17","C17","D17","E17","F17","G17","H17","I17","J17","K17","L17"],["A18","B18","C18","D18","E18","F18","G18","H18","I18","J18","K18","L18"],["A19","B19","C19","D19","E19","F19","G19","H19","I19","J19","K19","L19"],["A20","B20","C20","D20","E20","F20","G20","H20","I20","J20","K20","L20"],["A21","B21","C21","D21","E21","F21","G21","H21","I21","J21","K21","L21"],["A22","B22","C22","D22","E22","F22","G22","H22","I22","J22","K22","L22"],["A23","B23","C23","D23","E23","F23","G23","H23","I23","J23","K23","L23"],["A24","B24","C24","D24","E24","F24","G24","H24","I24","J24","K24","L24"],["A25","B25","C25","D25","E25","F25","G25","H25","I25","J25","K25","L25"]],"brand":{"brand":"CH_grid_box_pp","brandId":[]},"metadata":{"displayName":"CH_grid_box_pp 300 Well Plate 10 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":128,"yDimension":85.6,"zDimension":20.5},"wells":{"A1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":68.1,"z":1.5},"B1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":63.6,"z":1.5},"C1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":59.1,"z":1.5},"D1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":54.6,"z":1.5},"E1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":50.1,"z":1.5},"F1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":45.6,"z":1.5},"G1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":41.1,"z":1.5},"H1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":36.6,"z":1.5},"I1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":32.1,"z":1.5},"J1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":27.6,"z":1.5},"K1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":23.1,"z":1.5},"L1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":18.6,"z":1.5},"A2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":68.1,"z":1.5},"B2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":63.6,"z":1.5},"C2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":59.1,"z":1.5},"D2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":54.6,"z":1.5},"E2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":50.1,"z":1.5},"F2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":45.6,"z":1.5},"G2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":41.1,"z":1.5},"H2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":36.6,"z":1.5},"I2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":32.1,"z":1.5},"J2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":27.6,"z":1.5},"K2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":23.1,"z":1.5},"L2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":18.6,"z":1.5},"A3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":68.1,"z":1.5},"B3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":63.6,"z":1.5},"C3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":59.1,"z":1.5},"D3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":54.6,"z":1.5},"E3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":50.1,"z":1.5},"F3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":45.6,"z":1.5},"G3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":41.1,"z":1.5},"H3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":36.6,"z":1.5},"I3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":32.1,"z":1.5},"J3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":27.6,"z":1.5},"K3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":23.1,"z":1.5},"L3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":18.6,"z":1.5},"A4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":68.1,"z":1.5},"B4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":63.6,"z":1.5},"C4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":59.1,"z":1.5},"D4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":54.6,"z":1.5},"E4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":50.1,"z":1.5},"F4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":45.6,"z":1.5},"G4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":41.1,"z":1.5},"H4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":36.6,"z":1.5},"I4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":32.1,"z":1.5},"J4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":27.6,"z":1.5},"K4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":23.1,"z":1.5},"L4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":18.6,"z":1.5},"A5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":68.1,"z":1.5},"B5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":63.6,"z":1.5},"C5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":59.1,"z":1.5},"D5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":54.6,"z":1.5},"E5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":50.1,"z":1.5},"F5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":45.6,"z":1.5},"G5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":41.1,"z":1.5},"H5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":36.6,"z":1.5},"I5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":32.1,"z":1.5},"J5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":27.6,"z":1.5},"K5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":23.1,"z":1.5},"L5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":18.6,"z":1.5},"A6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":68.1,"z":1.5},"B6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":63.6,"z":1.5},"C6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":59.1,"z":1.5},"D6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":54.6,"z":1.5},"E6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":50.1,"z":1.5},"F6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":45.6,"z":1.5},"G6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":41.1,"z":1.5},"H6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":36.6,"z":1.5},"I6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":32.1,"z":1.5},"J6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":27.6,"z":1.5},"K6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":23.1,"z":1.5},"L6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":18.6,"z":1.5},"A7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":68.1,"z":1.5},"B7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":63.6,"z":1.5},"C7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":59.1,"z":1.5},"D7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":54.6,"z":1.5},"E7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":50.1,"z":1.5},"F7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":45.6,"z":1.5},"G7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":41.1,"z":1.5},"H7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":36.6,"z":1.5},"I7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":32.1,"z":1.5},"J7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":27.6,"z":1.5},"K7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":23.1,"z":1.5},"L7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":18.6,"z":1.5},"A8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":68.1,"z":1.5},"B8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":63.6,"z":1.5},"C8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":59.1,"z":1.5},"D8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":54.6,"z":1.5},"E8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":50.1,"z":1.5},"F8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":45.6,"z":1.5},"G8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":41.1,"z":1.5},"H8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":36.6,"z":1.5},"I8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":32.1,"z":1.5},"J8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":27.6,"z":1.5},"K8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":23.1,"z":1.5},"L8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":18.6,"z":1.5},"A9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":68.1,"z":1.5},"B9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":63.6,"z":1.5},"C9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":59.1,"z":1.5},"D9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":54.6,"z":1.5},"E9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":50.1,"z":1.5},"F9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":45.6,"z":1.5},"G9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":41.1,"z":1.5},"H9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":36.6,"z":1.5},"I9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":32.1,"z":1.5},"J9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":27.6,"z":1.5},"K9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":23.1,"z":1.5},"L9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":18.6,"z":1.5},"A10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":68.1,"z":1.5},"B10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":63.6,"z":1.5},"C10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":59.1,"z":1.5},"D10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":54.6,"z":1.5},"E10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":50.1,"z":1.5},"F10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":45.6,"z":1.5},"G10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":41.1,"z":1.5},"H10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":36.6,"z":1.5},"I10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":32.1,"z":1.5},"J10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":27.6,"z":1.5},"K10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":23.1,"z":1.5},"L10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":18.6,"z":1.5},"A11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":68.1,"z":1.5},"B11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":63.6,"z":1.5},"C11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":59.1,"z":1.5},"D11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":54.6,"z":1.5},"E11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":50.1,"z":1.5},"F11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":45.6,"z":1.5},"G11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":41.1,"z":1.5},"H11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":36.6,"z":1.5},"I11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":32.1,"z":1.5},"J11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":27.6,"z":1.5},"K11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":23.1,"z":1.5},"L11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":18.6,"z":1.5},"A12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":68.1,"z":1.5},"B12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":63.6,"z":1.5},"C12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":59.1,"z":1.5},"D12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":54.6,"z":1.5},"E12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":50.1,"z":1.5},"F12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":45.6,"z":1.5},"G12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":41.1,"z":1.5},"H12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":36.6,"z":1.5},"I12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":32.1,"z":1.5},"J12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":27.6,"z":1.5},"K12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":23.1,"z":1.5},"L12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":18.6,"z":1.5},"A13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":68.1,"z":1.5},"B13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":63.6,"z":1.5},"C13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":59.1,"z":1.5},"D13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":54.6,"z":1.5},"E13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":50.1,"z":1.5},"F13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":45.6,"z":1.5},"G13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":41.1,"z":1.5},"H13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":36.6,"z":1.5},"I13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":32.1,"z":1.5},"J13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":27.6,"z":1.5},"K13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":23.1,"z":1.5},"L13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":18.6,"z":1.5},"A14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":68.1,"z":1.5},"B14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":63.6,"z":1.5},"C14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":59.1,"z":1.5},"D14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":54.6,"z":1.5},"E14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":50.1,"z":1.5},"F14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":45.6,"z":1.5},"G14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":41.1,"z":1.5},"H14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":36.6,"z":1.5},"I14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":32.1,"z":1.5},"J14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":27.6,"z":1.5},"K14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":23.1,"z":1.5},"L14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":18.6,"z":1.5},"A15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":68.1,"z":1.5},"B15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":63.6,"z":1.5},"C15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":59.1,"z":1.5},"D15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":54.6,"z":1.5},"E15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":50.1,"z":1.5},"F15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":45.6,"z":1.5},"G15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":41.1,"z":1.5},"H15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":36.6,"z":1.5},"I15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":32.1,"z":1.5},"J15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":27.6,"z":1.5},"K15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":23.1,"z":1.5},"L15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":18.6,"z":1.5},"A16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":68.1,"z":1.5},"B16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":63.6,"z":1.5},"C16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":59.1,"z":1.5},"D16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":54.6,"z":1.5},"E16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":50.1,"z":1.5},"F16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":45.6,"z":1.5},"G16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":41.1,"z":1.5},"H16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":36.6,"z":1.5},"I16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":32.1,"z":1.5},"J16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":27.6,"z":1.5},"K16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":23.1,"z":1.5},"L16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":18.6,"z":1.5},"A17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":68.1,"z":1.5},"B17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":63.6,"z":1.5},"C17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":59.1,"z":1.5},"D17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":54.6,"z":1.5},"E17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":50.1,"z":1.5},"F17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":45.6,"z":1.5},"G17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":41.1,"z":1.5},"H17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":36.6,"z":1.5},"I17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":32.1,"z":1.5},"J17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":27.6,"z":1.5},"K17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":23.1,"z":1.5},"L17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":18.6,"z":1.5},"A18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":68.1,"z":1.5},"B18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":63.6,"z":1.5},"C18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":59.1,"z":1.5},"D18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":54.6,"z":1.5},"E18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":50.1,"z":1.5},"F18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":45.6,"z":1.5},"G18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":41.1,"z":1.5},"H18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":36.6,"z":1.5},"I18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":32.1,"z":1.5},"J18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":27.6,"z":1.5},"K18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":23.1,"z":1.5},"L18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":18.6,"z":1.5},"A19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":68.1,"z":1.5},"B19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":63.6,"z":1.5},"C19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":59.1,"z":1.5},"D19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":54.6,"z":1.5},"E19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":50.1,"z":1.5},"F19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":45.6,"z":1.5},"G19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":41.1,"z":1.5},"H19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":36.6,"z":1.5},"I19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":32.1,"z":1.5},"J19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":27.6,"z":1.5},"K19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":23.1,"z":1.5},"L19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":18.6,"z":1.5},"A20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":68.1,"z":1.5},"B20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":63.6,"z":1.5},"C20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":59.1,"z":1.5},"D20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":54.6,"z":1.5},"E20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":50.1,"z":1.5},"F20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":45.6,"z":1.5},"G20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":41.1,"z":1.5},"H20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":36.6,"z":1.5},"I20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":32.1,"z":1.5},"J20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":27.6,"z":1.5},"K20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":23.1,"z":1.5},"L20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":18.6,"z":1.5},"A21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":68.1,"z":1.5},"B21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":63.6,"z":1.5},"C21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":59.1,"z":1.5},"D21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":54.6,"z":1.5},"E21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":50.1,"z":1.5},"F21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":45.6,"z":1.5},"G21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":41.1,"z":1.5},"H21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":36.6,"z":1.5},"I21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":32.1,"z":1.5},"J21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":27.6,"z":1.5},"K21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":23.1,"z":1.5},"L21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":18.6,"z":1.5},"A22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":68.1,"z":1.5},"B22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":63.6,"z":1.5},"C22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":59.1,"z":1.5},"D22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":54.6,"z":1.5},"E22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":50.1,"z":1.5},"F22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":45.6,"z":1.5},"G22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":41.1,"z":1.5},"H22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":36.6,"z":1.5},"I22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":32.1,"z":1.5},"J22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":27.6,"z":1.5},"K22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":23.1,"z":1.5},"L22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":18.6,"z":1.5},"A23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":68.1,"z":1.5},"B23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":63.6,"z":1.5},"C23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":59.1,"z":1.5},"D23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":54.6,"z":1.5},"E23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":50.1,"z":1.5},"F23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":45.6,"z":1.5},"G23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":41.1,"z":1.5},"H23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":36.6,"z":1.5},"I23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":32.1,"z":1.5},"J23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":27.6,"z":1.5},"K23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":23.1,"z":1.5},"L23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":18.6,"z":1.5},"A24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":68.1,"z":1.5},"B24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":63.6,"z":1.5},"C24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":59.1,"z":1.5},"D24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":54.6,"z":1.5},"E24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":50.1,"z":1.5},"F24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":45.6,"z":1.5},"G24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":41.1,"z":1.5},"H24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":36.6,"z":1.5},"I24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":32.1,"z":1.5},"J24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":27.6,"z":1.5},"K24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":23.1,"z":1.5},"L24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":18.6,"z":1.5},"A25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":68.1,"z":1.5},"B25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":63.6,"z":1.5},"C25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":59.1,"z":1.5},"D25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":54.6,"z":1.5},"E25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":50.1,"z":1.5},"F25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":45.6,"z":1.5},"G25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":41.1,"z":1.5},"H25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":36.6,"z":1.5},"I25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":32.1,"z":1.5},"J25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":27.6,"z":1.5},"K25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":23.1,"z":1.5},"L25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":18.6,"z":1.5}},"groups":[{"metadata":{"wellBottomShape":"flat"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","L1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","K2","L2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","K3","L3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","K4","L4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","K5","L5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","K6","L6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","K7","L7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","K8","L8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","K9","L9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10","K10","L10","A11","B11","C11","D11","E11","F11","G11","H11","I11","J11","K11","L11","A12","B12","C12","D12","E12","F12","G12","H12","I12","J12","K12","L12","A13","B13","C13","D13","E13","F13","G13","H13","I13","J13","K13","L13","A14","B14","C14","D14","E14","F14","G14","H14","I14","J14","K14","L14","A15","B15","C15","D15","E15","F15","G15","H15","I15","J15","K15","L15","A16","B16","C16","D16","E16","F16","G16","H16","I16","J16","K16","L16","A17","B17","C17","D17","E17","F17","G17","H17","I17","J17","K17","L17","A18","B18","C18","D18","E18","F18","G18","H18","I18","J18","K18","L18","A19","B19","C19","D19","E19","F19","G19","H19","I19","J19","K19","L19","A20","B20","C20","D20","E20","F20","G20","H20","I20","J20","K20","L20","A21","B21","C21","D21","E21","F21","G21","H21","I21","J21","K21","L21","A22","B22","C22","D22","E22","F22","G22","H22","I22","J22","K22","L22","A23","B23","C23","D23","E23","F23","G23","H23","I23","J23","K23","L23","A24","B24","C24","D24","E24","F24","G24","H24","I24","J24","K24","L24","A25","B25","C25","D25","E25","F25","G25","H25","I25","J25","K25","L25"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"chgridboxpp_300_wellplate_10ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""

LABWARE_DEF_grid = json.loads(LABWARE_DEF_grid_JSON)
LABWARE_LABEL_grid = LABWARE_DEF_grid.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF_grid.get('wells', {}).get('A1', {}).get('yDimension')

# Custom-designed 5x5 2ml microtube holder (NOTE: We will be using only 24 of the slots; leave last one empty) -> Needs to be changed
LABWARE_microtube_holder_JSON = LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1"],["A2","B2","C2","D2","E2","F2"],["A3","B3","C3","D3","E3","F3"],["A4","B4","C4","D4","E4","F4"],["A5","B5","C5","D5","E5","F5"],["A6","B6","C6","D6","E6","F6"]],"brand":{"brand":"CH_0.5ml_centrifuge_rack","brandId":[]},"metadata":{"displayName":"CH_0.5ml_centrifuge_rack 36 Tube Rack with 0.5ml_centrifuge_tube 0.5 mL","displayCategory":"tubeRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.6,"zDimension":33},"wells":{"A1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":75.82,"z":5.1},"B1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":62.63,"z":5.1},"C1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":49.44,"z":5.1},"D1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":36.25,"z":5.1},"E1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":23.06,"z":5.1},"F1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":9.87,"z":5.1},"A2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":75.82,"z":5.1},"B2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":62.63,"z":5.1},"C2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":49.44,"z":5.1},"D2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":36.25,"z":5.1},"E2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":23.06,"z":5.1},"F2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":9.87,"z":5.1},"A3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":75.82,"z":5.1},"B3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":62.63,"z":5.1},"C3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":49.44,"z":5.1},"D3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":36.25,"z":5.1},"E3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":23.06,"z":5.1},"F3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":9.87,"z":5.1},"A4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":75.82,"z":5.1},"B4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":62.63,"z":5.1},"C4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":49.44,"z":5.1},"D4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":36.25,"z":5.1},"E4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":23.06,"z":5.1},"F4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":9.87,"z":5.1},"A5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":75.82,"z":5.1},"B5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":62.63,"z":5.1},"C5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":49.44,"z":5.1},"D5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":36.25,"z":5.1},"E5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":23.06,"z":5.1},"F5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":9.87,"z":5.1},"A6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":75.82,"z":5.1},"B6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":62.63,"z":5.1},"C6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":49.44,"z":5.1},"D6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":36.25,"z":5.1},"E6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":23.06,"z":5.1},"F6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":9.87,"z":5.1}},"groups":[{"brand":{"brand":"0.5ml_centrifuge_tube","brandId":[]},"metadata":{"wellBottomShape":"v","displayCategory":"tubeRack"},"wells":["A1","B1","C1","D1","E1","F1","A2","B2","C2","D2","E2","F2","A3","B3","C3","D3","E3","F3","A4","B4","C4","D4","E4","F4","A5","B5","C5","D5","E5","F5","A6","B6","C6","D6","E6","F6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"ch0.5mlcentrifugerack_36_tuberack_500ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF_microtube_holder = json.loads(LABWARE_microtube_holder_JSON)
LABWARE_LABEL_microtube_holder = LABWARE_DEF_microtube_holder.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF_microtube_holder.get('wells', {}).get('A1', {}).get('yDimension')

# Metadata for protocol
metadata = {
'apiLevel': '2.0',
'author': 'Tan_Ching_Hai'}


# User inputs
samples = 48


'''Start of OT-2 Protocol'''
def run(protocol: protocol_api.ProtocolContext):
    
    '''OT-2 Labware Definition'''
    # Boxes holding the grids
    sample_box_1 = protocol.load_labware_from_definition(LABWARE_DEF_grid, '1', LABWARE_LABEL_grid)
    sample_box_2 = protocol.load_labware_from_definition(LABWARE_DEF_grid, '2', LABWARE_LABEL_grid)
    sample_box_3 = protocol.load_labware_from_definition(LABWARE_DEF_grid, '4', LABWARE_LABEL_grid)
    sample_box_4 = protocol.load_labware_from_definition(LABWARE_DEF_grid, '5', LABWARE_LABEL_grid)

    # Racks holding the environmental stock solution at -2 dilution
    rack_env_sample_1 = protocol.load_labware_from_definition(LABWARE_DEF_microtube_holder, '7', LABWARE_LABEL_microtube_holder)
    rack_env_sample_2 = protocol.load_labware_from_definition(LABWARE_DEF_microtube_holder, '10', LABWARE_LABEL_microtube_holder)
    rack_env_sample_3 = protocol.load_labware_from_definition(LABWARE_DEF_microtube_holder, '11', LABWARE_LABEL_microtube_holder)


    # Reservoir holding PBS
    reservoir = protocol.load_labware('nest_12_reservoir_15ml','8')

    # Tip Racks
    tiprack_1a = protocol.load_labware('opentrons_96_tiprack_20ul', '3') # For 8-channel pipette ONLY
    tiprack_1b = protocol.load_labware('opentrons_96_tiprack_20ul', '6') # For 8-channel pipette ONLY
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', '9') # For single channel pipette ONLY
    
    # Pipette heads
    left = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_2])
    right = protocol.load_instrument('p20_multi_gen2','right', tip_racks=[tiprack_1a, tiprack_1b])
    

    ''' Setting OT-2 hardware parameters'''
    # Flow Rate Settings
    left.flow_rate.aspirate = 70
    left.flow_rate.blow_out = 50
    

    # Offset to accommodate for fact that we are using 6 channels on the multi-channel pipette & not 8 (hence need less current so don't damage head and motors)
    num_channels_per_pickup = 1
    # (only pickup tips on front-most channel)    

    per_tip_pickup_current = .075
    # (current required for picking up one tip, do not modify unless
    # you are using a GEN2 P20 8-Channel in which case change it to 
    # 0.075)

    pick_up_current = num_channels_per_pickup*per_tip_pickup_current
    '''protocol._hw_manager.hardware._attached_instruments[
        right._implementation.get_mount()].update_config_item(
        'pick_up_current', pick_up_current)'''
    
    # Control Speed of Axis Movement (Motors)
    left.default_speed = 800  # Speed of Motors



    '''Parameters for aspiration & dispensation'''

    # Volume of PBS to aspirate from reservoir && dispense into each grid
    pbs_vol = 18

    # Air gap volume (stops dripping)
    air_gap_vol = 2

    # Mixing volume
    mix_vol = 3

    # Serial dilution volume 
    serial_vol = 2

    # How much sample to pipette into each grid
    sample_vol = 2

    # Volume that is aspirated from stock solution (use 3ul here so can deposit 1ul into each member of the -3 dilution triplet)
    initial_sample_vol =  sample_vol*3

    '''Positioning offsets'''

    # Offset value from bottom when dispensing pbs into custom grids
    vert_offset = 3.0 
    '''Used for PBS & Serial dilution processes'''
    # Box is 19mm in height. The agar estimated to be 2.8-2.9mm in height.Grids are 5.1 mm in height. Hence offset is 3.0 from bottom of the box (not too low as to pierce agar. Not too high such that it will end up aspirating air) 

    # Microtube offset (we do this so pipette tip doesn't crash into microtubes even if they aren't placed perfectly in the rack_holder)
    tube_offset = 3

    '''Start of Protocol'''

    # Creating sample box list to determine how many && which sample boxes to use
    box_list = [sample_box_1, sample_box_2, sample_box_3, sample_box_4]
    if samples <= 24:
        boxes = box_list[0:1]
    elif 24 < samples <= 48:
        boxes = box_list[0:2]
    elif 48 < samples <= 72:
        boxes = box_list[0:3]
    elif 72 < samples <= 96:
        boxes = box_list[0:4]

    def pbs_pipetting(samples):

        # Calculate no. of iterations based on no. of samples the user inputs
        iterations = (samples-1)//6 + 1

        # Reservoir array used to dynamically adjust which well we pull PBS from (we change PBS aspirating well every 12 samples)
        res = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']

        # Create iterator for detecting when to change well from which we aspirate PBS (every 12 columns we move on to the column of well from reservoir)
        w = 1
        
        # Iterate through each box to fill the pbs solution based on user input 
        # (User_input [sample] affects no. of boxes used as well as iterations, affecting how much of each custom plate is used)
        right.pick_up_tip()
        for box in boxes:
            for i in plate_coord[0:iterations*9]:
                index = (w - 1) // 12
                rese = res[index] 
                right.aspirate(volume=pbs_vol,location=reservoir[rese].bottom(3)) # OR can just use reservoir[res[index]]
                right.move_to(box[i].top())  
                right.dispense(volume=pbs_vol,location=box[i].bottom(vert_offset))
                right.blow_out() 
                right.air_gap(volume = air_gap_vol)
                w += 1
        right.drop_tip()
    

    # Aliquot the stock solution from the respective "rack for stock solutions" into the respective wells
    def aliquot(samples):
        
        # Create an array containing coordinates of each triplet (for env sample pipetting)
        triplet = np.array([])
        alphabet_1 = ['A','C','E','G','I','K','B','D','F','H','J','L']
        number_1 = ['2','3','4','14','15','16']
        for alpha_1 in alphabet_1:
            for num_1 in number_1:
                coordinate = alpha_1 + num_1
                triplet = np.append(triplet,coordinate)
        triplet = triplet.reshape(-1,3)

        
        # Create list containing all the racks to determine which rack to pick sample from (depends on no. of samples the user inputs)
        rack_list = [rack_env_sample_1, rack_env_sample_2, rack_env_sample_3]

        # Create an iterator to determine which sample machine is currently running
        z = 1 # We count z=1 as the 1st iteration
        

        while z <= samples:
            # Determine which sample box to use
            box_list = [sample_box_1, sample_box_2, sample_box_3, sample_box_4]
            '''for i in range(4): # Between samples 1-24 we use sample_box_1, samples 25-48 we use sample_box_2 and so on
                if i*24 < z <= (i+1)*24:
                    box_used = box_list[i] #Possible source of error code here'''
            if z <= 24:
                box_used = box_list[0]
            elif 24 < z <= 48:
                box_used = box_list[1]
            elif 48 < z <= 72:
                box_used = box_list[2]
            elif 72 < z <= 96:
                box_used = box_list[3]
           
           # Choosing which rack the machine picks up the sample from
            if z <= 36:
                rack = rack_list[0]
            elif 36 < z <= 72:
                rack = rack_list[1]
            elif 72 < z <= 96:
                rack = rack_list[2]

            # Choosing which centrifuge tube machine picks up from (for each rack)
            if z <= 36:
                tube = centri_holder[z-1] # As index position of lists start from 0, we take z-1 to pinpoint tube we want to use
            elif z > 36: # No matter how large the value is, it will always pick up from the correct tube (assuming we use 24 tubes per rack)
                div = z % 36
                tube = centri_holder[div-1]

            # Create new counter to manipulate the counter 'z' when it exceeds 24 samples (The 'triplet' array only has 24 samples so need to re-use it) -> Make sample 25 use ['A2','A3','A4'] again and so on
            q = (z-1) % len(triplet)

            triple = triplet[q]
            left.pick_up_tip()
            left.move_to(rack[tube].top(tube_offset))

            # Aspirate 1ul of sample then air gap 1 ul of sample then dispense 2ul of sample to prevent fluid from sticking to tip
            '''for y in range(0,2):
                left.aspirate(volume = initial_sample_vol, location = rack[tube].bottom()) # Insert offset for aspiration
                left.air_gap(volume = air_gap_vol)
            left.move_to(rack[tube].top(tube_offset)) # Offset for pipette head to raise up before moving off'''
            
            left.aspirate(volume = initial_sample_vol, location = rack[tube].bottom())

            # Move toward the PP Box to dispense env sample in triplets (only dispensing to form -3 dilution)
            for element in triple: 
                left.move_to(box_used[element].top())
                left.dispense(volume = sample_vol, location=box_used[element].bottom(vert_offset)) # Avoid touching the pbs in the grid 

                left.move_to(box_used[element].top(-14.3)) 
                # left.dispense(volume = air_gap_vol)
                left.touch_tip(speed = 25, v_offset = -14.3, radius = 0.8) # Touch tip to ensure env sample enters the grid and not adhere to the side of the pipette tip
            left.air_gap(volume = air_gap_vol)   
            # Drop tip after each 'set' of -3 sample triplets is done to minimise contamination risk
            left.drop_tip()
            
            # Increase iterator value to move on to next sample
            z += 1

    def serial_dilution(samples):

        # Initiate a var to check whether we need to conduct full plate or 1/2 plate dilution based on how much sample is leftover from user input
        leftover = samples # Leftover initially is the same as user input (before 1st round of serial dilution)

        # Create dictionaries to assign coordinates (values) to keys
        position_A = {
                # LHS of plate (custom 3D Printed grids) --> Rows: A,C,E,G,I,K
                'A2': 'A6', # -3 to -4 (1st member of triplet)
                'A3': 'A7', # -3 to -4 (2nd member of triplet)
                'A3': 'A8', # -3 to -4 (3rd member of triplet)
                'A6': 'A10', # -4 to -5 (1st member of triplet)
                'A7': 'A11', # -4 to -5 (2nd member of triplet)
                'A8': 'A12' # -4 to -5 (3rd member of triplet)
            }
        
        position_B = {
                # RHS of plate (custom 3D Printed grids) --> Rows: A,C,E,G,I,K
                'A14': 'A18', # -3 to -4 (1st member of triplet)
                'A15': 'A19', # -3 to -4 (2nd member of triplet)
                'A16': 'A20', # -3 to -4 (3rd member of triplet)
                'A18': 'A22', # -4 to -5 (1st member of triplet)
                'A19': 'A23', # -4 to -5 (2nd member of triplet)
                'A20': 'A24' # -4 to -5 (3rd member of triplet)
            }
        
        position_C = {
                # LHS of plate (custom 3D Printed grids) --> Rows: B,D,F,H,J,L
                'B2': 'B6', # -3 to -4 (1st member of triplet)
                'B3': 'B7', # -3 to -4 (2nd member of triplet)
                'B3': 'B8', # -3 to -4 (3rd member of triplet)
                'B6': 'B10', # -4 to -5 (1st member of triplet)
                'B7': 'B11', # -4 to -5 (2nd member of triplet)
                'B8': 'B12' # -4 to -5 (3rd member of triplet)
            }
        
        position_D = {
                # RHS of plate (custom 3D Printed grids) --> Rows: B,D,F,H,J,L
                'B14': 'B18', # -3 to -4 (1st member of triplet)
                'B15': 'B19', # -3 to -4 (2nd member of triplet)
                'B16': 'B20', # -3 to -4 (3rd member of triplet)
                'B18': 'B22', # -4 to -5 (1st member of triplet)
                'B19': 'B23', # -4 to -5 (2nd member of triplet)
                'B20': 'B24' # -4 to -5 (3rd member of triplet)
            }

        def quad_plate():
            right.pick_up_tip()

            # Create for loop to loop the process: Pick up from prev dilution, dispense into next dilution & mix
            for start,end in position_A.items():
                # Move to the start position && aspirate vol for serial dilution
                right.move_to(box[start].top()) 
                right.move_to(box[start].bottom(vert_offset)) # Move to start well top (lower pipette head)
                right.aspirate(volume = serial_vol)
                right.move_to(box[start].top(5)) # Move to start well top (higher than the actual top)

                # Move to end position && dispense
                right.move_to(box[end].top())
                right.move_to(box[end].bottom(vert_offset))
                right.dispense(volume = serial_vol)

                # Mixing to produce homogenous solution
                right.mix(volume = mix_vol)

            right.drop_tip()

        def half_plate():
            quad_plate()
            right.pick_up_tip()
            # Create for loop to loop the process: Pick up from prev dilution, dispense into next dilution & mix
            for start,end in position_B.items():

                # Move to the start position && aspirate vol for serial dilution
                right.move_to(box[start].top()) 
                right.move_to(box[start].bottom(vert_offset)) # Move to start well top (lower pipette head)
                right.aspirate(volume = serial_vol)
                right.move_to(box[start].top(5)) # Move to start well top (higher than the actual top)

                # Move to end position && dispense
                right.move_to(box[end].top())
                right.move_to(box[end].bottom(vert_offset))
                right.dispense(volume = serial_vol)

                # Mixing to produce homogenous solution
                right.mix(volume = mix_vol)
                
            right.drop_tip()

        def three_quads():
            half_plate()
            right.pick_up_tip()
            # Create for loop to loop the process: Pick up from prev dilution, dispense into next dilution & mix
            for start,end in position_C.items():

                # Move to the start position && aspirate vol for serial dilution
                right.move_to(box[start].top()) 
                right.move_to(box[start].bottom(vert_offset)) # Move to start well top (lower pipette head)
                right.aspirate(volume = serial_vol)
                right.move_to(box[start].top(5)) # Move to start well top (higher than the actual top)

                # Move to end position && dispense
                right.move_to(box[end].top())
                right.move_to(box[end].bottom(vert_offset))
                right.dispense(volume = serial_vol)

                # Mixing to produce homogenous solution
                right.mix(volume = mix_vol)
                
            right.drop_tip()

        def full_plate():
            three_quads()
            right.pick_up_tip()
            # Create for loop to loop the process: Pick up from prev dilution, dispense into next dilution & mix
            for start,end in position_D.items():

                # Move to the start position && aspirate vol for serial dilution
                right.move_to(box[start].top()) 
                right.move_to(box[start].bottom(vert_offset)) # Move to start well top (lower pipette head)
                right.aspirate(volume = serial_vol)
                right.move_to(box[start].top(5)) # Move to start well top (higher than the actual top)

                # Move to end position && dispense
                right.move_to(box[end].top())
                right.move_to(box[end].bottom(vert_offset))
                right.dispense(volume = serial_vol)

                # Mixing to produce homogenous solution
                right.mix(volume = mix_vol)
                
            right.drop_tip()
        
        for box in boxes:
            if leftover <= 24:

                if leftover == 1:
                    for box in boxes:
                        quad_plate()
                        
                    
                if 2 < leftover <= 12:
                    for box in boxes:
                        half_plate()
 

                if leftover == 13:
                    for box in boxes:
                        three_quads()
                
                if 13 < leftover <= 24:
                    for box in boxes:
                        full_plate()
                    
            elif leftover > 12:
                full_plate()
                leftover = leftover - 12
    pbs_pipetting(samples)
    aliquot(samples)
    serial_dilution(samples)

        
                

           
            



    



                




        


        





    
     

    
        


    

   



