from abaqus import *
from abaqusConstants import *
import regionToolset
session.viewports['Viewport: 1'].setValues(displayedObject=None)
FrameModel = mdb.models['Model-1']
import sketch
import part
from abaqus import getInputs
Ac=(('X','0,6000,12000'),('Y','0,6000,12000'),('Z','0,3000,6000'))
a,b,c =getInputs(fields=Ac,label='Axis coordinates',dialogTitle='Creat axis net',)
a,b,c=eval(a),eval(b),eval(c)
Na, Nb, Nc = len(a),len(b),len(c)
point1 =()
for k in range(1,Nc):
    for i in range(Na):
        point2 = (((a[i],b[0],c[k]),(a[i],b[Nb-1],c[k])),)
        point1 = point1 + point2
    for j in range(Nb):
        point2 = (((a[0],b[j],c[k]),(a[Na-1],b[j],c[k])),)
        point1 = point1 + point2
for i in range(Na):
    for j in range(Nb):
        point2 = (((a[i],b[j],c[0]),(a[i],b[j],c[Nc-1])),)
        point1 = point1 + point2
framePart = FrameModel.Part(name='Frame',dimensionality=THREE_D,type=DEFORMABLE_BODY)
framePart.WirePolyLine(mergeType=MERGE, meshable=ON, points=point1)