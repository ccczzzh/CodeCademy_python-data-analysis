# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.9-1 replay file
# Internal Version: 2009_04_16-15.31.05 92314
# Run by Administrator on Sat Jun 26 10:09:30 2010
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=199.527775615454, 
    height=191.277775704861)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
fields=(('x1:','20'),('y1:','20'),('x2:','-20'),('y2:','-20'),('depth:','20'))
x1,y1,x2,y2,depth=getInputs(fields=fields,label='model:')
x1=float(x1)
x2=float(x2)
y1=float(y1)
y2=float(y2)
depth=float(depth)
fields1=(('E:','2.06E5'),('u:','0.3'),('den:','7.8E-9'))
E,u,den=getInputs(fields=fields1,label='mat:')
E=float(E)
u=float(u)
den=float(den)
Load=getInput('Load:','100')
p1=float(Load)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(x1,y1),point2=(x2,y2))
session.viewports['Viewport: 1'].view.setValues(width=117.055, height=65.8, 
    cameraPosition=(2.32105, -0.969474, 188.562), cameraTarget=(2.32105, 
    -0.969474, 0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=depth)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Density(table=((den, ), ))
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((E, u), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c[0:1]
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1[4:5]
a.Set(faces=faces1, name='Set-1')
#: The set 'Set-1' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.7478, 
    farPlane=161.986, width=80.5953, height=43.3975, cameraPosition=(107.503, 
    32.0811, -48.1714), cameraUpVector=(-0.672275, 0.734182, -0.0949932))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1[5:6]
a.Surface(side1Faces=side1Faces1, name='Surf-1')
#: The surface 'Surf-1' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.8429, 
    farPlane=162.719, width=78.0155, height=42.0083, cameraPosition=(57.9711, 
    94.3402, 68.6218), cameraUpVector=(-0.477988, 0.34537, -0.807618))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    initialInc=0.2, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-1']
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region)
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['Surf-1']
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=p1, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=4.0, deviationFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=70, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', parallelizationMethodExplicit=DOMAIN, 
    multiprocessingMode=DEFAULT, numDomains=1, numCpus=1)
