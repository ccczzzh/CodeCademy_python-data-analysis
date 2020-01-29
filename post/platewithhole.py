from abaqus import *
from abaqusConstants import *
from caeModules import *
from abaqus import backwardCompatibility
backwardCompatibility.setValues(reportDeprecated=False)
width=float(getInput('Enter the width of plate:','20'))
height=float(getInput('Enter the height of plate:','20'))
diameter=float(getInput('Enter the diamter of hole:','5'))
spacing=float(getInput('Enter the spacing of hole:','1'))

xstart=-width/2.
ystart=-height/2.

span=diameter+spacing
nx=int((width-spacing)/span)
ny=int((height-spacing)/span)
if (nx<1 or ny<1):
    print("Holes are too big!")
print("creating hole  grid of ", nx, " by", ny)
nhole=nx*ny

myModel=mdb.Model(name='Model-1')

mysheetSize=width
if (height>width):
    mysheetSize=height
s1 = myModel.Sketch(name='__profile__', sheetSize=mysheetSize)
s1.rectangle(point1=(-width/2., -height/2.), point2=(width/2., height/2.))
p1 = myModel.Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p1.BaseShell(sketch=s1)
#p1 = myModel.parts['Part-1']

s2 = myModel.Sketch(name='__profile__', sheetSize=mysheetSize)
r=diameter/2.
xs=spacing+r+xstart
ys=spacing+r+ystart
#xs=0.5*(width-span*(nx-1))+xstart
#ys=0.5*(height-span*(ny-1))+ystart
#r=diameter/2.
for i in range(0,ny):
    y=ys+i*span
    for j in range(0,nx):
        x=xs+j*span
        s2.CircleByCenterPerimeter(center=(x,y), point1=(x,y+r))
p2 = myModel.Part(name='Part-2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p2.BaseShell(sketch=s2)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.1882, 
    farPlane=62.9489, width=36.1069, height=19.8207, viewOffsetX=-0.96285, 
    viewOffsetY=0.158936)
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanCut(name='Part-3', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], 
    cuttingInstances=(a.instances['Part-2-1'], ), originalInstances=SUPPRESS)
p = myModel.parts['Part-3']
myInstance=a.Instance(name='Part-3-1', part=p, dependent=OFF)
a.features['Part-1-1'].suppress()
a.features['Part-2-1'].suppress()

myModel.Material(name='Material-1')
myModel.materials['Material-1'].Elastic(table=((100000000.0,0.3), ))
myModel.HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=1.0)
region = regionToolset.Region(faces=p.faces)
p.SectionAssignment(region=region, sectionName='Section-1')

myModel.StaticStep(name='Step-1', previous='Initial')
side1Edges1=myInstance.edges.findAt(((width/2., 0.,0.),))
region = regionToolset.Region(side1Edges=side1Edges1)
myModel.Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, magnitude=-100.0, amplitude=UNSET)
edges1=myInstance.edges.findAt(((-width/2., 0.,0.),))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC-1', createStepName='Step-1', 
    region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, localCsys=None)
verts1=myInstance.vertices.findAt(((-width/2., -height/2.,0.),))
region = regionToolset.Region(vertices=verts1)
myModel.DisplacementBC(name='BC-2', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, localCsys=None)
    
seedsize=3.14159*diameter/16.
outerEdges=myInstance.edges.findAt(((-width/2.,0.,0.),),((width/2.,0,0.),),
    ((0.,-height/2.,0.),),((0.,height/2.,0.),))
a.seedEdgeBySize(edges=outerEdges, size=seedsize)
seedsize=3.14159*diameter/32.
for i in range(0,ny):
    y=ys+i*span
    for j in range(0,nx):
        x=xs+j*span+r
        innerEdges=myInstance.edges.findAt(((x,y,0.),))
        a.seedEdgeBySize(edges=innerEdges, size=seedsize)

elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=STIFFNESS, distortionControl=OFF)
meshRegions =myInstance.faces
a.setMeshControls(regions=meshRegions, algorithm=ADVANCING_FRONT)

meshRegions =(myInstance.faces, )
a.setElementType(regions=meshRegions, elemTypes=(elemType1,))
a.generateMesh(regions=meshRegions)

mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=60, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', parallelizationMethodExplicit=DOMAIN, 
    multiprocessingMode=DEFAULT, numDomains=1, numCpus=1)
