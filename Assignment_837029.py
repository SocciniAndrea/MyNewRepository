import wallCalculation
from wallCalculation import wallHeatTransfer
# create dictionary with different values of k for the brick object
#input dictionary  
glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cement ={"name":"cement", "k": 1.5}
length_list =[0.20,0.35,0.95]
material_list = [ glassProp,brickProp,cement]

Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}
 
parallelSet = [R3,R4,R5]
serieSet= [R1,R2,R6]
 
Ti =20
To= -10

def MultipleMaterialSensitivity(mat_list, size_list,resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
    HTresults={}
    HTresults2={}
    HTresults3={}
    i=0
    for material in mat_list:
        R4["k"]=material["k"]
        for length in size_list:            
            R4["length"]=length
            heatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,Ti,To)
            stringInput = "material = "+material["name"]+" length = "+str(length)
            listInput = (material["name"],length)
            HTresults[stringInput]  = heatTransfer
            HTresults2  [listInput] = heatTransfer
            HTresults3[i]={"name":material["name"],"length":length,"HeatTransfer":heatTransfer}
            i=i+1       
    return HTresults3
    # you need to import wallHeatTransfer from wallCalculation Script
HeatTransferSensitivity=MultipleMaterialSensitivity(material_list,length_list,serieSet,parallelSet,Ri,Ro,Ti,To)
print(HeatTransferSensitivity)
#out put should be like this: result_sensitivity=  {"glass":253,"brick": 350,... } 
# the ouput can also be a list of dictionaries [{"name":"glass","HeatTransfer" : 253},{"name":"brick","HeatTransfer" : 352}]   