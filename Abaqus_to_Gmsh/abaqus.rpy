# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-4 replay file
# Internal Version: 2015_06_11-16.41.13 135079
# Run by lzhaok6 on Tue Aug 21 09:51:57 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=206.888885498047, 
    height=101.333335876465)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('FSP_canopy_sym_fluidmodel.cae')
#: The model database "C:\Users\lzhaok6\OneDrive\UNDEX research\Abaqus\input files\FSP_canopy_sym_fluidmodel.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
del a.features['WHOLEFLUID-1']
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
a.resumeFeatures(('A-1', 'B-1', 'C-1', 'D-1', ))
p1 = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
s = p.features['Solid extrude-1'].sketch
mdb.models['FSP_canopy_sym_fluidmodel'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
d[0].setValues(value=6.4008, )
s1.unsetPrimaryObject()
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
p.features['Solid extrude-1'].setValues(sketch=s1)
del mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
p.regenerate()
p1 = mdb.models['FSP_canopy_sym_fluidmodel'].parts['B']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['B']
s = p.features['Solid extrude-1'].sketch
mdb.models['FSP_canopy_sym_fluidmodel'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
d[0].setValues(value=2.1336, )
s2.unsetPrimaryObject()
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['B']
p.features['Solid extrude-1'].setValues(sketch=s2)
del mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['B']
p.regenerate()
p1 = mdb.models['FSP_canopy_sym_fluidmodel'].parts['C']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['C']
s = p.features['Solid extrude-1'].sketch
mdb.models['FSP_canopy_sym_fluidmodel'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
d[0].setValues(value=6.4008, )
s1.unsetPrimaryObject()
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['C']
p.features['Solid extrude-1'].setValues(sketch=s1)
del mdb.models['FSP_canopy_sym_fluidmodel'].sketches['__edit__']
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['C']
p.regenerate()
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3232, 
    farPlane=28.0022, width=9.53925, height=6.23842, cameraPosition=(5.81707, 
    11.5987, 14.4218), cameraUpVector=(-0.658252, 0.483726, -0.576813), 
    cameraTarget=(-2.80863, -2.17596, 0.253856))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5095, 
    farPlane=28.4384, width=9.65525, height=6.31428, cameraPosition=(10.3601, 
    0.350941, 17.1595), cameraUpVector=(-0.173237, 0.887882, -0.426209), 
    cameraTarget=(-2.78729, -2.22879, 0.266715))
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.0224, 
    farPlane=27.681, width=9.97456, height=6.5231, cameraPosition=(0.203185, 
    2.17205, 21.2161), cameraUpVector=(-0.324442, 0.822611, -0.466956), 
    cameraTarget=(-2.97818, -2.19456, 0.342956))
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.8574, 
    farPlane=26.1205, width=10.4944, height=6.86304, cameraPosition=(0.588166, 
    18.6806, 5.18379), cameraUpVector=(-0.271149, -0.0662352, -0.960256), 
    cameraTarget=(-2.97306, -1.97494, 0.129671))
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.0779, 
    farPlane=26.9997, width=10.0091, height=6.5457, cameraPosition=(2.02571, 
    16.925, 9.21872), cameraUpVector=(-0.185548, 0.1375, -0.972968), 
    cameraTarget=(-2.97788, -1.96905, 0.116138))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.4871, 
    farPlane=27.7313, width=9.64129, height=6.30516, cameraPosition=(2.35775, 
    11.8311, 15.7971), cameraUpVector=(-0.195269, 0.508349, -0.83872), 
    cameraTarget=(-2.97822, -1.96379, 0.109348))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.776, 
    farPlane=27.3968, width=9.82114, height=6.42278, cameraPosition=(
    -0.0041101, 12.0097, 16.2582), cameraUpVector=(-0.178197, 0.501812, 
    -0.846422), cameraTarget=(-2.98349, -1.96339, 0.110376))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.7478, 
    farPlane=27.425, width=9.82963, height=6.42832, viewOffsetX=0.00187564, 
    viewOffsetY=-0.00125507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5385, 
    farPlane=27.6827, width=9.699, height=6.3429, cameraPosition=(1.72905, 
    11.1971, 16.5264), cameraUpVector=(-0.184215, 0.542296, -0.819744), 
    cameraTarget=(-2.98138, -1.96414, 0.110873), viewOffsetX=0.00185071, 
    viewOffsetY=-0.00123839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.6235, 
    farPlane=27.5733, width=9.75203, height=6.37758, cameraPosition=(1.55348, 
    12.204, 15.7177), cameraUpVector=(-0.188106, 0.490466, -0.850917), 
    cameraTarget=(-2.9818, -1.96188, 0.108925), viewOffsetX=0.00186083, 
    viewOffsetY=-0.00124516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.663, 
    farPlane=28.0149, width=9.77669, height=6.39371, cameraPosition=(5.04837, 
    -16.9649, 13.4095), cameraUpVector=(0.128689, 0.906818, 0.401397), 
    cameraTarget=(-2.97486, -2.01282, 0.107685), viewOffsetX=0.00186554, 
    viewOffsetY=-0.00124831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2172, 
    farPlane=28.5078, width=9.49842, height=6.21173, cameraPosition=(9.32959, 
    5.63744, 16.2863), cameraUpVector=(-0.185395, 0.742868, -0.643254), 
    cameraTarget=(-2.92065, -1.72398, 0.142638), viewOffsetX=0.00181244, 
    viewOffsetY=-0.00121278)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.3663, 
    farPlane=27.4265, width=10.2157, height=6.68081, cameraPosition=(8.09118, 
    16.0271, 5.7567), cameraUpVector=(-0.429309, 0.151981, -0.890278), 
    cameraTarget=(-2.93818, -1.58118, -0.00347066), viewOffsetX=0.00194931, 
    viewOffsetY=-0.00130436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.7982, 
    farPlane=26.9307, width=10.4853, height=6.8571, cameraPosition=(2.0039, 
    18.3954, 6.4781), cameraUpVector=(-0.302918, 0.0252316, -0.952683), 
    cameraTarget=(-3.03168, -1.54564, 0.0070973), viewOffsetX=0.00200075, 
    viewOffsetY=-0.00133878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.251, 
    farPlane=25.4706, width=11.3921, height=7.45014, cameraPosition=(-3.32782, 
    20.0094, 0.993484), cameraUpVector=(-0.177723, -0.289161, -0.940638), 
    cameraTarget=(-3.1057, -1.52417, -0.0694445), viewOffsetX=0.00217379, 
    viewOffsetY=-0.00145457)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5938, 
    farPlane=28.0845, width=9.73348, height=6.36545, cameraPosition=(2.95193, 
    13.8309, 13.9244), cameraUpVector=(-0.120319, 0.395769, -0.910434), 
    cameraTarget=(-3.01923, -1.60732, 0.108386), viewOffsetX=0.0018573, 
    viewOffsetY=-0.00124279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3771, 
    farPlane=28.3079, width=9.59822, height=6.27699, cameraPosition=(5.94857, 
    9.57663, 16.2273), cameraUpVector=(-0.301201, 0.627587, -0.717922), 
    cameraTarget=(-2.98114, -1.66148, 0.138736), viewOffsetX=0.00183149, 
    viewOffsetY=-0.00122552)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'B-1', 'C-1', 'D-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8642, 
    farPlane=28.5502, width=11.1506, height=7.31778, viewOffsetX=2.18144, 
    viewOffsetY=1.13612)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1794, 
    farPlane=27.8574, width=11.9715, height=7.85652, cameraPosition=(-0.495156, 
    20.7537, 4.23759), cameraUpVector=(-0.180874, -0.0807799, -0.980183), 
    cameraTarget=(-3.70951, 0.0359559, -0.794237), viewOffsetX=2.34204, 
    viewOffsetY=1.21976)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3831, 
    farPlane=28.0012, width=11.4745, height=7.53035, cameraPosition=(1.44144, 
    16.8413, 11.2721), cameraUpVector=(-0.670108, 0.166627, -0.723319), 
    cameraTarget=(-2.21778, -1.47736, 0.505888), viewOffsetX=2.24481, 
    viewOffsetY=1.16912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.1019, 
    farPlane=29.4465, width=11.299, height=7.41518, cameraPosition=(10.5811, 
    11.0034, 12.7922), cameraUpVector=(-0.617707, 0.558042, -0.5541), 
    cameraTarget=(-1.70075, -1.83804, 0.58038), viewOffsetX=2.21048, 
    viewOffsetY=1.15124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.1989, 
    farPlane=31.4942, width=12.6079, height=8.27417, cameraPosition=(20.0195, 
    3.33686, -12.272), cameraUpVector=(-0.723326, 0.58079, -0.373474), 
    cameraTarget=(1.61374, -0.40224, -1.68324), viewOffsetX=2.46655, 
    viewOffsetY=1.2846)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['A-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#c50 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.21336, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.6994, 
    farPlane=30.2289, width=12.2962, height=8.06956, cameraPosition=(1.04563, 
    17.9635, 13.1996), cameraUpVector=(-0.0136111, 0.255147, -0.966807), 
    cameraTarget=(-5.41194, 1.10712, 1.40812), viewOffsetX=2.40556, 
    viewOffsetY=1.25283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7039, 
    farPlane=30.2785, width=12.299, height=8.07142, cameraPosition=(-13.9098, 
    11.0816, 17.0133), cameraUpVector=(0.0121551, 0.520121, -0.854006), 
    cameraTarget=(-7.17928, -1.63025, 0.951388), viewOffsetX=2.40611, 
    viewOffsetY=1.25312)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1891, 
    farPlane=31.0895, width=11.9777, height=7.86056, cameraPosition=(-24.5263, 
    8.41383, 7.34254), cameraUpVector=(0.331832, 0.48162, -0.811128), 
    cameraTarget=(-8.08426, -2.53783, -1.29432), viewOffsetX=2.34325, 
    viewOffsetY=1.22038)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['A-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#12a ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.24384, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4745, 
    farPlane=31.2471, width=12.1558, height=7.97745, cameraPosition=(-23.4256, 
    8.8495, -13.3752), cameraUpVector=(0.753532, 0.644354, 0.130376), 
    cameraTarget=(-6.05674, -1.75095, -6.2459), viewOffsetX=2.3781, 
    viewOffsetY=1.23853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9622, 
    farPlane=30.1459, width=13.0844, height=8.58687, cameraPosition=(-4.52934, 
    3.75653, -26.9887), cameraUpVector=(0.349051, 0.760488, 0.547559), 
    cameraTarget=(-1.26295, -2.87522, -6.73469), viewOffsetX=2.55977, 
    viewOffsetY=1.33314)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['A-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#285 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.24384, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
partInstances =(a.instances['A-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.6122, 
    farPlane=31.74, width=12.2418, height=8.03387, cameraPosition=(18.6693, 
    5.58994, -13.6034), cameraUpVector=(-0.158039, 0.478802, 0.863581), 
    cameraTarget=(1.795, -3.22435, -3.48208), viewOffsetX=2.39492, 
    viewOffsetY=1.24728)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7994, 
    farPlane=31.4664, width=12.3586, height=8.11054, cameraPosition=(-19.1755, 
    14.8094, -13.5483), cameraUpVector=(0.483958, 0.406262, 0.775071), 
    cameraTarget=(-4.3321, 0.960634, -6.2848), viewOffsetX=2.41777, 
    viewOffsetY=1.25918)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7879, 
    farPlane=31.4888, width=12.3514, height=8.10583, cameraPosition=(-24.932, 
    -9.26414, 10.0897), cameraUpVector=(0.126406, 0.991967, 0.00487957), 
    cameraTarget=(-8.04651, -4.10967, -2.28711), viewOffsetX=2.41637, 
    viewOffsetY=1.25845)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.701, 
    farPlane=31.5898, width=12.2971, height=8.07022, cameraPosition=(-26.5488, 
    6.03478, 6.107), cameraUpVector=(0.620217, 0.759434, -0.196446), 
    cameraTarget=(-8.47696, -1.57868, -2.85504), viewOffsetX=2.40576, 
    viewOffsetY=1.25292)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9001, 
    farPlane=31.3682, width=12.4214, height=8.15179, cameraPosition=(-26.9182, 
    5.74658, -8.86378), cameraUpVector=(0.651597, 0.756993, 0.0488185), 
    cameraTarget=(-7.09077, -2.0409, -5.5317), viewOffsetX=2.43008, 
    viewOffsetY=1.26558)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.0889, 
    farPlane=31.1646, width=12.5393, height=8.22915, cameraPosition=(-27.3014, 
    -2.17875, -11.2126), cameraUpVector=(0.408867, 0.912517, -0.0118211), 
    cameraTarget=(-6.50296, -3.55022, -5.6972), viewOffsetX=2.45314, 
    viewOffsetY=1.27759)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'A-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'B-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7348, 
    farPlane=31.2468, width=11.6941, height=7.67447, cameraPosition=(-22.2198, 
    11.9091, 9.63396), cameraUpVector=(0.66069, 0.580522, -0.475902), 
    cameraTarget=(-8.37989, -0.457131, -1.33918), viewOffsetX=2.28779, 
    viewOffsetY=1.19147)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6385, 
    farPlane=30.9765, width=11.634, height=7.63504, cameraPosition=(-24.07, 
    6.52841, 11.3489), cameraUpVector=(0.534777, 0.755709, -0.378043), 
    cameraTarget=(-8.44174, -1.3269, -1.25783), viewOffsetX=2.27604, 
    viewOffsetY=1.18535)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6467, 
    farPlane=30.9684, width=11.6392, height=7.63842, cameraPosition=(-23.0118, 
    4.73098, 13.7808), cameraUpVector=(-0.0743534, 0.401855, -0.91268), 
    cameraTarget=(-7.3835, -3.12433, 1.17403), viewOffsetX=2.27705, 
    viewOffsetY=1.18587)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9236, 
    farPlane=30.5665, width=11.812, height=7.75184, cameraPosition=(-16.0249, 
    12.1105, 16.2379), cameraUpVector=(-0.164657, 0.326501, -0.930744), 
    cameraTarget=(-7.15164, -1.58167, 2.14296), viewOffsetX=2.31086, 
    viewOffsetY=1.20348)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8234, 
    farPlane=30.1902, width=11.1253, height=7.30115, cameraPosition=(13.8615, 
    6.25888, 15.0463), cameraUpVector=(-0.527136, 0.761394, -0.377369), 
    cameraTarget=(-2.61992, -1.44658, 3.47629), viewOffsetX=2.17651, 
    viewOffsetY=1.13351)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.9246, 
    farPlane=29.4871, width=11.1885, height=7.34259, cameraPosition=(8.21211, 
    1.94999, 20.6103), cameraUpVector=(-0.278622, 0.867232, -0.412648), 
    cameraTarget=(-4.09325, -1.93488, 3.33717), viewOffsetX=2.18886, 
    viewOffsetY=1.13994)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8818, 
    farPlane=29.5784, width=11.1618, height=7.32504, cameraPosition=(8.92532, 
    2.37073, 20.1459), cameraUpVector=(-0.287512, 0.859001, -0.42362), 
    cameraTarget=(-3.97647, -1.84254, 3.39274), viewOffsetX=2.18363, 
    viewOffsetY=1.13722)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.2164, 
    farPlane=30.0679, width=11.3707, height=7.46219, cameraPosition=(19.1401, 
    3.78536, -7.85785), cameraUpVector=(-0.617201, 0.780355, -0.100542), 
    cameraTarget=(0.298291, -0.685432, 1.62241), viewOffsetX=2.22449, 
    viewOffsetY=1.1585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.156, 
    farPlane=29.8239, width=11.9572, height=7.84711, cameraPosition=(5.98014, 
    5.50054, -21.6801), cameraUpVector=(-0.356513, 0.77748, 0.518096), 
    cameraTarget=(0.33625, -1.01317, -1.91659), viewOffsetX=2.33923, 
    viewOffsetY=1.21826)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['B-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#c50 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.21336, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0508, 
    farPlane=30.6815, width=11.8915, height=7.80401, cameraPosition=(-25.1795, 
    -2.63066, -11.883), cameraUpVector=(0.553236, 0.779856, -0.292838), 
    cameraTarget=(-5.69505, -3.79804, -2.7248), viewOffsetX=2.32638, 
    viewOffsetY=1.21157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.0108, 
    farPlane=30.5085, width=12.4908, height=8.19727, cameraPosition=(-14.0764, 
    -0.732472, 22.9851), cameraUpVector=(0.1115, 0.913865, -0.390408), 
    cameraTarget=(-7.23893, -2.40823, 2.60573), viewOffsetX=2.44361, 
    viewOffsetY=1.27262)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.2114, 
    farPlane=30.248, width=12.616, height=8.27943, cameraPosition=(-11.6602, 
    -1.88828, 23.9718), cameraUpVector=(0.0547594, 0.9309, -0.361147), 
    cameraTarget=(-6.92083, -2.60177, 2.95024), viewOffsetX=2.4681, 
    viewOffsetY=1.28538)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['B-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#3af ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.24384, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
partInstances =(a.instances['B-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'B-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'C-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9067, 
    farPlane=29.7715, width=11.8016, height=7.74501, cameraPosition=(-21.072, 
    14.9963, 0.717982), cameraUpVector=(0.911012, 0.402657, -0.0890169), 
    cameraTarget=(-6.39842, -0.715879, -0.922602), viewOffsetX=2.30878, 
    viewOffsetY=1.20241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7117, 
    farPlane=29.8902, width=11.6799, height=7.66512, cameraPosition=(-24.1642, 
    10.8722, 0.737476), cameraUpVector=(0.806361, 0.591288, 0.0126707), 
    cameraTarget=(-6.38148, -1.18478, -1.074), viewOffsetX=2.28497, 
    viewOffsetY=1.19001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3969, 
    farPlane=30.0616, width=11.4834, height=7.53617, cameraPosition=(-23.2661, 
    6.7934, 12.8425), cameraUpVector=(0.667283, 0.718023, -0.19793), 
    cameraTarget=(-7.32822, -1.32699, 0.804249), viewOffsetX=2.24653, 
    viewOffsetY=1.16999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6396, 
    farPlane=29.8329, width=11.6349, height=7.6356, cameraPosition=(-19.184, 
    8.9942, 16.8606), cameraUpVector=(0.672599, 0.640832, -0.370062), 
    cameraTarget=(-7.37806, -0.895312, 1.77109), viewOffsetX=2.27617, 
    viewOffsetY=1.18543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1112, 
    farPlane=29.6668, width=11.9293, height=7.82878, cameraPosition=(-12.7135, 
    17.5537, -10.005), cameraUpVector=(0.779773, 0.243732, 0.576671), 
    cameraTarget=(-3.56974, -0.396122, -2.31937), viewOffsetX=2.33376, 
    viewOffsetY=1.21542)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6858, 
    farPlane=30.0332, width=11.6638, height=7.65453, cameraPosition=(-15.174, 
    6.60193, -17.9344), cameraUpVector=(0.308166, 0.73159, 0.60812), 
    cameraTarget=(-2.56252, -1.68637, -2.53544), viewOffsetX=2.28182, 
    viewOffsetY=1.18837)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0896, 
    farPlane=29.6082, width=11.9159, height=7.81995, cameraPosition=(-14.5974, 
    -0.429411, -19.9123), cameraUpVector=(0.127059, 0.893979, 0.429718), 
    cameraTarget=(-2.20292, -2.56915, -2.40021), viewOffsetX=2.33113, 
    viewOffsetY=1.21405)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['C-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#c50 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.21336, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.8158, 
    farPlane=29.9078, width=11.745, height=7.70786, cameraPosition=(-15.7508, 
    16.6945, -8.39532), cameraUpVector=(0.645041, 0.307771, 0.699428), 
    cameraTarget=(-3.48553, 0.105353, -2.13123), viewOffsetX=2.2977, 
    viewOffsetY=1.19664)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4223, 
    farPlane=29.4513, width=12.1236, height=7.95629, cameraPosition=(8.85399, 
    18.7115, -4.62017), cameraUpVector=(-0.141841, -0.0758469, 0.986979), 
    cameraTarget=(0.713985, -0.712063, -0.000597), viewOffsetX=2.37176, 
    viewOffsetY=1.23521)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9017, 
    farPlane=29.993, width=11.7986, height=7.74301, cameraPosition=(12.5692, 
    15.2029, -6.57058), cameraUpVector=(-0.135543, 0.0478244, 0.989617), 
    cameraTarget=(0.827959, -1.68344, -0.100035), viewOffsetX=2.30818, 
    viewOffsetY=1.2021)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.8815, 
    farPlane=29.9714, width=11.786, height=7.73475, cameraPosition=(-23.6962, 
    -0.683753, -11.8311), cameraUpVector=(-0.138443, 0.312489, 0.939779), 
    cameraTarget=(-4.67873, 0.346298, -1.72425), viewOffsetX=2.30571, 
    viewOffsetY=1.20082)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['C-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#3af ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.24384, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
partInstances =(a.instances['C-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'C-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'D-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.557, 
    farPlane=29.4634, width=12.2076, height=8.01145, viewOffsetX=3.4795, 
    viewOffsetY=-0.733409)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.1229, 
    farPlane=28.3983, width=11.3124, height=7.42396, cameraPosition=(-17.8387, 
    14.5472, 5.86365), cameraUpVector=(0.553041, -0.174637, 0.814646), 
    cameraTarget=(-1.56137, 1.34348, 0.80547), viewOffsetX=3.22434, 
    viewOffsetY=-0.679627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4719, 
    farPlane=25.7274, width=11.5303, height=7.56694, cameraPosition=(1.60506, 
    20.1874, 1.50848), cameraUpVector=(0.114048, -0.362013, 0.92517), 
    cameraTarget=(1.3113, -1.36242, 0.880979), viewOffsetX=3.28644, 
    viewOffsetY=-0.692716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.052, 
    farPlane=26.2048, width=10.644, height=6.98527, cameraPosition=(18.183, 
    6.36078, 1.64288), cameraUpVector=(-0.262577, -0.259516, 0.929357), 
    cameraTarget=(-0.158895, -4.95639, 1.03397), viewOffsetX=3.03381, 
    viewOffsetY=-0.639467)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.8155, 
    farPlane=26.9055, width=10.4964, height=6.88838, cameraPosition=(13.7016, 
    10.7592, 9.18545), cameraUpVector=(-0.523158, -0.377275, 0.764179), 
    cameraTarget=(0.231915, -4.40925, 1.88063), viewOffsetX=2.99173, 
    viewOffsetY=-0.630597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.8697, 
    farPlane=26.631, width=10.5302, height=6.91063, cameraPosition=(15.4223, 
    -12.4988, 8.25098), cameraUpVector=(-0.628552, 0.119151, 0.768586), 
    cameraTarget=(-3.63851, -5.56355, 0.939141), viewOffsetX=3.00137, 
    viewOffsetY=-0.632629)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.8739, 
    farPlane=26.2309, width=10.5328, height=6.91235, cameraPosition=(10.8314, 
    -19.5108, -1.33146), cameraUpVector=(-0.130158, 0.168073, 0.977144), 
    cameraTarget=(-4.74157, -4.85694, 1.42904), viewOffsetX=3.00212, 
    viewOffsetY=-0.632787)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['D-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#c50 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.21336, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.444, 
    farPlane=26.3416, width=10.8887, height=7.14588, cameraPosition=(-9.93564, 
    -21.6312, 6.43297), cameraUpVector=(-0.294959, 0.654193, 0.696442), 
    cameraTarget=(-6.00149, -1.57169, -0.423482), viewOffsetX=3.10354, 
    viewOffsetY=-0.654165)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2757, 
    farPlane=26.2958, width=10.7836, height=7.07693, cameraPosition=(-19.5893, 
    -15.412, -0.631168), cameraUpVector=(-0.189295, 0.662861, 0.724419), 
    cameraTarget=(-4.97421, 0.421869, -1.37913), viewOffsetX=3.07359, 
    viewOffsetY=-0.647853)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
e1 = a.instances['D-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#3af ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=0.24384, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
partInstances =(a.instances['D-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'A-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'B-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'C-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2539, 
    farPlane=28.0037, width=9.52157, height=6.24869, cameraPosition=(2.72481, 
    -5.17129, 20.8423), cameraUpVector=(-0.234793, 0.966431, -0.104326), 
    cameraTarget=(-6.42093, -2.03672, 1.57052), viewOffsetX=2.71388, 
    viewOffsetY=-0.572032)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.8924, 
    farPlane=27.5397, width=9.92012, height=6.51025, cameraPosition=(12.31, 
    13.4956, -2.88591), cameraUpVector=(-0.797594, 0.271057, -0.538861), 
    cameraTarget=(-4.3648, 0.74773, 2.04502), viewOffsetX=2.82748, 
    viewOffsetY=-0.595976)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.0329, 
    farPlane=27.0775, width=10.0078, height=6.5678, cameraPosition=(4.65135, 
    18.1997, -3.76301), cameraUpVector=(-0.908217, -0.050996, -0.41538), 
    cameraTarget=(-5.05205, -0.0445498, 2.39027), viewOffsetX=2.85247, 
    viewOffsetY=-0.601244)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.9064, 
    farPlane=27.9681, width=9.30465, height=6.10634, cameraPosition=(4.57805, 
    10.5904, 16.0438), cameraUpVector=(-0.561114, 0.581477, -0.589097), 
    cameraTarget=(-6.16321, -1.6926, 1.9503), viewOffsetX=2.65205, 
    viewOffsetY=-0.559)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.862, 
    farPlane=27.0527, width=9.90112, height=6.49778, cameraPosition=(0.494082, 
    13.3286, -15.2494), cameraUpVector=(-0.674527, 0.365094, 0.641654), 
    cameraTarget=(-0.704615, 0.46393, 2.01148), viewOffsetX=2.82206, 
    viewOffsetY=-0.594834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3953, 
    farPlane=27.838, width=9.60983, height=6.30661, cameraPosition=(12.9728, 
    12.2334, -4.79743), cameraUpVector=(-0.782422, 0.529828, 0.327258), 
    cameraTarget=(-1.76738, -1.11516, 3.53432), viewOffsetX=2.73903, 
    viewOffsetY=-0.577334)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5971, 
    farPlane=27.7213, width=9.73579, height=6.38927, cameraPosition=(15.0456, 
    10.1234, -2.8863), cameraUpVector=(-0.742327, 0.624272, 0.243384), 
    cameraTarget=(-2.06042, -1.25487, 3.65546), viewOffsetX=2.77493, 
    viewOffsetY=-0.584901)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5029, 
    farPlane=27.7848, width=9.677, height=6.35069, cameraPosition=(14.2959, 
    10.9727, -3.66513), cameraUpVector=(-0.762646, 0.589142, 0.266988), 
    cameraTarget=(-1.96496, -1.17404, 3.60932), viewOffsetX=2.75817, 
    viewOffsetY=-0.581369)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a1 = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
a1.InstanceFromBooleanMerge(name='WHOLE_FLUID', instances=(a1.instances['C-1'], 
    a1.instances['B-1'], a1.instances['D-1'], a1.instances['A-1'], ), 
    mergeNodes=ALL, nodeMergingTolerance=0.001, domain=MESH, 
    originalInstances=SUPPRESS)
p1 = mdb.models['FSP_canopy_sym_fluidmodel'].parts['WHOLEFLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['FSP_canopy_sym_fluidmodel'].parts['WHOLEFLUID']
p = mdb.models['FSP_canopy_sym_fluidmodel'].parts['A']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1276, 
    farPlane=28.1384, width=9.47585, height=6.19696, cameraPosition=(11.1818, 
    6.23767, 14.5161), cameraUpVector=(-0.719868, 0.681441, -0.132012), 
    cameraTarget=(-5.02211, -2.50609, 3.29752), viewOffsetX=2.6914, 
    viewOffsetY=-0.567296)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1607, 
    farPlane=28.1053, width=9.49659, height=6.21052, cameraPosition=(11.1306, 
    6.35731, 14.4968), cameraUpVector=(-0.705959, 0.690192, -0.158923), 
    cameraTarget=(-5.07328, -2.38645, 3.27818), viewOffsetX=2.69729, 
    viewOffsetY=-0.568537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2452, 
    farPlane=27.9953, width=9.5495, height=6.24512, cameraPosition=(11.3742, 
    7.81861, 13.2838), cameraUpVector=(-0.736586, 0.653175, -0.175509), 
    cameraTarget=(-4.92831, -2.22519, 3.37278), viewOffsetX=2.71232, 
    viewOffsetY=-0.571704)
mdb.Job(name='Job-1', model='FSP_canopy_sym_fluidmodel', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, 
    numDomains=1, activateLoadBalancing=False, multiprocessingMode=DEFAULT, 
    numCpus=1)
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.4044, 
    farPlane=27.9223, width=9.64924, height=6.31035, cameraPosition=(14.3372, 
    10.3548, -5.25234), cameraUpVector=(-0.804687, 0.593307, -0.0215925), 
    cameraTarget=(-2.50525, -0.0639135, 3.27183), viewOffsetX=2.74065, 
    viewOffsetY=-0.577675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2907, 
    farPlane=28.0344, width=9.57802, height=6.26377, cameraPosition=(12.5281, 
    6.14438, 13.1576), cameraUpVector=(-0.690074, 0.713237, -0.122845), 
    cameraTarget=(-4.81863, -2.23036, 3.47096), viewOffsetX=2.72042, 
    viewOffsetY=-0.573411)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.8616, 
    farPlane=27.0935, width=9.93561, height=6.49762, cameraPosition=(-5.96893, 
    7.90448, 19.3362), cameraUpVector=(-0.527475, 0.511688, -0.678193), 
    cameraTarget=(-6.69561, -3.24162, 0.894064), viewOffsetX=2.82199, 
    viewOffsetY=-0.594819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.681, 
    farPlane=27.2712, width=9.82249, height=6.42364, cameraPosition=(14.9422, 
    10.2692, -0.811101), cameraUpVector=(-0.760516, 0.567818, -0.314958), 
    cameraTarget=(-3.69485, 0.215443, 3.24574), viewOffsetX=2.78986, 
    viewOffsetY=-0.588047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.8577, 
    farPlane=27.1129, width=9.93315, height=6.49601, cameraPosition=(12.4506, 
    12.0286, 6.28461), cameraUpVector=(-0.714072, 0.531419, -0.455735), 
    cameraTarget=(-4.88208, -0.410541, 3.1666), viewOffsetX=2.82129, 
    viewOffsetY=-0.594672)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1237, 
    farPlane=27.8322, width=9.47337, height=6.19534, cameraPosition=(4.6918, 
    12.4473, 14.4942), cameraUpVector=(-0.628643, 0.491758, -0.60248), 
    cameraTarget=(-6.21318, -1.68829, 2.40528), viewOffsetX=2.6907, 
    viewOffsetY=-0.567146)
session.viewports['Viewport: 1'].view.setValues(width=8.94458, height=5.84952, 
    viewOffsetX=2.80414, viewOffsetY=-0.476923)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.0977, 
    farPlane=28.0772, width=8.88968, height=5.81362, cameraPosition=(14.143, 
    7.05819, -10.1227), cameraUpVector=(-0.675029, 0.723671, 0.143651), 
    cameraTarget=(-1.3273, -0.0648937, 3.0988), viewOffsetX=2.78693, 
    viewOffsetY=-0.473996)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
f1 = a.instances['WHOLE_FLUID-1'].elements
face1Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:155 #c00f801f #f003e007 #7c00f801 #1f003e00 #7c00f80 #1f003e0', 
    ' #7c00f8 #801f003e #e007c00f #3 ]', ), )
face3Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:312 #7c000000 #0:2 #3e0 #0 #1f0000 #0', 
    ' #f8000000 #0:2 #7c0 #0 #3e0000 #0 #f0000000', 
    ' #1 #0 #f80 #0 #7c0000 #0 #e0000000', 
    ' #3 #0 #1f00 #0 #f80000 #0 #c0000000', 
    ' #7 #0 #3e00 #0 #1f00000 #0 #80000000', 
    ' #f #0 #7c00 #0 #3e00000 #0:2 #1f', ' #0 #f800 ]', ), )
face4Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:164 #80200800 #20080200 #8020080 #2008020 #802008 #80200802', 
    ' #20080200 #8020080 #2008020 #802008 #80200802 #20080200 #8020080', 
    ' #2008020 #802008 #80200802 #20080200 #8020080 #2008020 #802008', 
    ' #80200802 #20080200 #8020080 #2008020 #802008 #80200802 #20080200', 
    ' #8020080 #2008020 #802008 #80200802 #20080200 #8020080 #2008020', 
    ' #802008 #80200802 #20080200 #8020080 #2008020 #802008 #80200802', 
    ' #20080200 #8020080 #2008020 #802008 #80200802 #20080200 #8020080', 
    ' #2008020 #802008 #80200802 #20080200 #8020080 #2008020 #802008', 
    ' #80200802 #20080200 #8020080 #2008020 #802008 #80200802 #20080200', 
    ' #8020080 #2008020 #802008 #80200802 #20080200 #8020080 #2008020', 
    ' #802008 #80200802 #20080200 #8020080 #2008020 #802008 #80200802', 
    ' #20080200 #8020080 #2008020 #802008 #80200802 #20080200 #8020080', 
    ' #2008020 #802008 #80200802 #20080200 #8020080 #2008020 #802008', 
    ' #80200802 #20080200 #8020080 #2008020 #802008 #80200802 #20080200', 
    ' #8020080 #2008020 #802008 #80200802 #20080200 #8020080 #2008020', 
    ' #802008 #80200802 #20080200 #8020080 #2008020 #802008 #80200802', 
    ' #20080200 #8020080 #2008020 #802008 #80200802 #20080200 #8020080', 
    ' #2008020 #802008 #80200802 #20080200 #8020080 #2008020 #802008', ' #2 ]', 
    ), )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:25 #1f00000 #0 #80000000 #f #0 #7c00', 
    ' #0 #3e00000 #0:2 #1f #0 #f800 #0', 
    ' #7c00000 #0:2 #3e #0 #1f000 #0 #f800000', 
    ' #0:2 #7c #0 #3e000 #0 #1f000000 #0:2', 
    ' #f8 #0 #7c000 #0 #3e000000 #0:2 #1f0', 
    ' #0 #f8000 #0 #7c000000 #0:2 #3e0 ]', ), )
a.Surface(face1Elements=face1Elements1, face3Elements=face3Elements1, 
    face4Elements=face4Elements1, face5Elements=face5Elements1, 
    name='FSI_Fluid')
#: The surface 'FSI_Fluid' has been edited (700 mesh faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.6802, 
    farPlane=27.5082, width=9.23266, height=6.03792, cameraPosition=(13.0317, 
    9.35077, 9.67996), cameraUpVector=(-0.655354, 0.662959, -0.361934), 
    cameraTarget=(-4.89206, -0.907912, 3.48509), viewOffsetX=2.89445, 
    viewOffsetY=-0.492284)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2294, 
    farPlane=28.1366, width=8.96725, height=5.86434, cameraPosition=(7.1566, 
    -7.12169, -18.7123), cameraUpVector=(-0.925026, 0.296008, -0.238129), 
    cameraTarget=(-2.2456, 1.68596, -1.42348), viewOffsetX=2.81124, 
    viewOffsetY=-0.478132)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.221, 
    farPlane=27.9255, width=8.96231, height=5.86111, cameraPosition=(10.6606, 
    12.6681, -8.93057), cameraUpVector=(-0.860447, 0.475375, 0.18344), 
    cameraTarget=(-1.96877, 0.202164, 3.31603), viewOffsetX=2.80969, 
    viewOffsetY=-0.477869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.6547, 
    farPlane=27.7071, width=9.2177, height=6.02813, cameraPosition=(15.8269, 
    -12.3877, -3.68046), cameraUpVector=(0.169363, 0.976699, -0.131817), 
    cameraTarget=(-1.10539, -1.1256, 3.48487), viewOffsetX=2.88976, 
    viewOffsetY=-0.491486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1685, 
    farPlane=28.3054, width=8.93141, height=5.84091, cameraPosition=(7.24228, 
    4.92805, 18.2906), cameraUpVector=(-0.602656, 0.742438, -0.292561), 
    cameraTarget=(-6.05522, -2.24608, 2.90924), viewOffsetX=2.80001, 
    viewOffsetY=-0.476221)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3152, 
    farPlane=28.1897, width=9.01777, height=5.89739, cameraPosition=(-19.6763, 
    -0.0468819, 14.6691), cameraUpVector=(-0.160531, 0.67999, -0.715433), 
    cameraTarget=(-6.31729, -3.70756, -1.85402), viewOffsetX=2.82708, 
    viewOffsetY=-0.480826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.7034, 
    farPlane=26.7926, width=9.83519, height=6.43196, cameraPosition=(-25.279, 
    -3.08357, -0.770637), cameraUpVector=(0.285201, 0.683134, -0.672301), 
    cameraTarget=(-3.89591, -4.04131, -3.36354), viewOffsetX=3.08334, 
    viewOffsetY=-0.524411)
a = mdb.models['FSP_canopy_sym_fluidmodel'].rootAssembly
f1 = a.instances['WHOLE_FLUID-1'].elements
face2Elements1 = f1.getSequenceFromMask(mask=(
    '[#ffffffff:2 #7ff #0:67 #fffffc00 #ffffffff:8 #3fffff #0:209', 
    ' #fffffffc #ffffffff #1fff ]', ), )
face3Elements1 = f1.getSequenceFromMask(mask=(
    '[#7fff #0 #3fff800 #0 #ffc00000 #1f #0', 
    ' #fffe #0 #7fff000 #0 #ff800000 #3f #0', 
    ' #1fffc #0 #fffe000 #0 #ff000000 #7f #0', 
    ' #3fff8 #0 #1fffc000 #0 #fe000000 #ff #0', 
    ' #7fff0 #0 #3fff8000 #0 #fc000000 #1ff #0', 
    ' #fffe0 #0 #7fff0000 #0 #f8000000 #3ff #0', 
    ' #1fffc0 #0 #fffe0000 #0 #f0000000 #7ff #0', 
    ' #3fff80 #0 #fffc0000 #1 #e0000000 #fff #0', 
    ' #7fff00 #0 #fff80000 #3 #c0000000 #1fff #0', 
    ' #fffe00 #0 #fff00000 #7 #80000000 #3fff ]', ), )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:290 #c0000000 #1fff #0 #fffe00 #0 #fff00000', 
    ' #7 #80000000 #3fff #0 #1fffc00 #0 #ffe00000', 
    ' #f #0 #7fff #0 #3fff800 #0 #ffc00000', 
    ' #1f #0 #fffe #0 #7fff000 #0 #ff800000', 
    ' #3f #0 #1fffc #0 #fffe000 #0 #ff000000', 
    ' #7f #0 #3fff8 #0 #1fffc000 #0 #fe000000', 
    ' #ff #0 #7fff0 #0 #3fff8000 #0 #fc000000', 
    ' #1ff #0 #fffe0 #0 #7fff0000 #0 #f8000000', 
    ' #3ff #0 #1fffc0 #0 #fffe0000 #0 #f0000000', 
    ' #7ff #0 #3fff80 #0 #fffc0000 #1 #e0000000', ' #fff ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=(
    '[#40008001 #10002000 #4000800 #1000200 #400080 #100020 #40008', 
    ' #80010002 #20004000 #8001000 #2000400 #800100 #200040 #80010', 
    ' #20004 #40008001 #10002000 #4000800 #1000200 #400080 #100020', 
    ' #40008 #80010002 #20004000 #8001000 #2000400 #800100 #200040', 
    ' #80010 #20004 #40008001 #10002000 #4000800 #1000200 #400080', 
    ' #100020 #40008 #80010002 #20004000 #8001000 #2000400 #800100', 
    ' #200040 #80010 #20004 #40008001 #10002000 #4000800 #1000200', 
    ' #400080 #100020 #40008 #80010002 #20004000 #8001000 #2000400', 
    ' #800100 #200040 #80010 #20004 #40008001 #10002000 #4000800', 
    ' #1000200 #400080 #100020 #40008 #80010002 #20004000 #8001000', 
    ' #2000400 #800100 #200040 #80010 #20004 #40008001 #10002000', 
    ' #4000800 #1000200 #400080 #100020 #40008 #80010002 #20004000', 
    ' #8001000 #2000400 #800100 #200040 #80010 #20004 #40008001', 
    ' #10002000 #4000800 #1000200 #400080 #100020 #40008 #80010002', 
    ' #20004000 #8001000 #2000400 #800100 #200040 #80010 #20004', 
    ' #40008001 #10002000 #4000800 #1000200 #400080 #100020 #40008', 
    ' #80010002 #20004000 #8001000 #2000400 #800100 #200040 #80010', 
    ' #20004 #40008001 #10002000 #4000800 #1000200 #400080 #100020', 
    ' #40008 #80010002 #20004000 #8001000 #2000400 #800100 #200040', 
    ' #80010 #20004 #40008001 #10002000 #4000800 #1000200 #400080', 
    ' #100020 #40008 #80010002 #20004000 #8001000 #2000400 #800100', 
    ' #200040 #80010 #20004 #40008001 #10002000 #4000800 #1000200', 
    ' #400080 #100020 #40008 #80010002 #20004000 #8001000 #2000400', 
    ' #800100 #200040 #80010 #401004 #40100401 #10040100 #4010040', 
    ' #1004010 #401004 #40100401 #10040100 #4010040 #1004010 #401004', 
    ' #40100401 #10040100 #4010040 #1004010 #401004 #40100401 #10040100', 
    ' #4010040 #1004010 #401004 #40100401 #10040100 #4010040 #1004010', 
    ' #401004 #40100401 #10040100 #4010040 #1004010 #401004 #40100401', 
    ' #10040100 #4010040 #1004010 #401004 #40100401 #10040100 #4010040', 
    ' #1004010 #401004 #40100401 #10040100 #4010040 #1004010 #401004', 
    ' #40100401 #10040100 #4010040 #1004010 #401004 #40100401 #10040100', 
    ' #4010040 #1004010 #401004 #40100401 #10040100 #4010040 #1004010', 
    ' #401004 #40100401 #10040100 #4010040 #1004010 #401004 #40100401', 
    ' #10040100 #4010040 #1004010 #401004 #40100401 #10040100 #4010040', 
    ' #1004010 #401004 #40100401 #10040100 #4010040 #1004010 #401004', 
    ' #40100401 #10040100 #4010040 #1004010 #401004 #40100401 #10040100', 
    ' #4010040 #1004010 #401004 #40100401 #10040100 #4010040 #1004010', 
    ' #401004 #40100401 #10040100 #4010040 #1004010 #401004 #40100401', 
    ' #10040100 #4010040 #1004010 #401004 #40100401 #10040100 #4010040', 
    ' #1004010 #401004 #40100401 #10040100 #4010040 #1004010 #401004', 
    ' #40100401 #10040100 #4010040 #1004010 #401004 #40100401 #10040100', 
    ' #4010040 #1004010 #20004 #40008001 #10002000 #4000800 #1000200', 
    ' #400080 #100020 #40008 #80010002 #20004000 #8001000 #2000400', 
    ' #800100 #200040 #80010 #20004 #40008001 #10002000 #4000800', 
    ' #1000200 #400080 #100020 #40008 #80010002 #20004000 #8001000', 
    ' #2000400 #800100 #200040 #80010 #20004 #40008001 #10002000', 
    ' #4000800 #1000200 #400080 #100020 #40008 #80010002 #20004000', 
    ' #8001000 #2000400 #800100 #200040 #80010 #20004 #40008001', 
    ' #10002000 #4000800 #1000200 #400080 #100020 #40008 #80010002', 
    ' #20004000 #8001000 #2000400 #800100 #200040 #80010 #20004', 
    ' #40008001 #10002000 #4000800 #1000200 #400080 #100020 #40008', 
    ' #80010002 #20004000 ]', ), )
a.Surface(face2Elements=face2Elements1, face3Elements=face3Elements1, 
    face5Elements=face5Elements1, face6Elements=face6Elements1, name='NRB')
#: The surface 'NRB' has been edited (2250 mesh faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8295, 
    farPlane=25.6, width=10.4983, height=6.86559, cameraPosition=(-3.91197, 
    20.2517, -0.179689), cameraUpVector=(-0.349464, -0.317558, -0.881494), 
    cameraTarget=(-7.14809, -1.04994, 0.623467), viewOffsetX=3.29121, 
    viewOffsetY=-0.559766)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.9723, 
    farPlane=27.4588, width=9.40477, height=6.15045, cameraPosition=(17.0004, 
    -4.78932, 8.44646), cameraUpVector=(-0.139461, 0.984942, -0.102179), 
    cameraTarget=(-3.7206, -0.893839, 3.93632), viewOffsetX=2.94839, 
    viewOffsetY=-0.501459)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1577, 
    farPlane=28.2826, width=8.9251, height=5.83676, cameraPosition=(8.58042, 
    -10.3284, 16.6535), cameraUpVector=(0.131031, 0.99123, 0.017162), 
    cameraTarget=(-5.49868, -0.984363, 3.26158), viewOffsetX=2.79801, 
    viewOffsetY=-0.475883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.315, 
    farPlane=28.1285, width=9.01774, height=5.89735, cameraPosition=(9.50502, 
    3.72917, 17.2082), cameraUpVector=(-0.0697215, 0.803311, -0.591465), 
    cameraTarget=(-5.72235, 0.388361, 2.31381), viewOffsetX=2.82705, 
    viewOffsetY=-0.480823)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2041, 
    farPlane=28.2426, width=8.95244, height=5.85466, cameraPosition=(5.48326, 
    9.04415, 17.1721), cameraUpVector=(-0.170591, 0.670138, -0.722366), 
    cameraTarget=(-6.44642, 0.00420392, 1.6531), viewOffsetX=2.80658, 
    viewOffsetY=-0.477341)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.3507, 
    farPlane=27.0857, width=9.62759, height=6.29619, cameraPosition=(17.2587, 
    -1.09706, 8.31594), cameraUpVector=(-0.208362, 0.909096, -0.360735), 
    cameraTarget=(-3.73397, 0.105533, 3.54754), viewOffsetX=3.01824, 
    viewOffsetY=-0.51334)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.2496, 
    farPlane=27.1867, width=9.56805, height=6.25725, cameraPosition=(17.0763, 
    -2.55215, 8.75215), cameraUpVector=(-0.283444, 0.958826, -0.0176482), 
    cameraTarget=(-3.91641, -1.34955, 3.98375), viewOffsetX=2.99957, 
    viewOffsetY=-0.510165)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5946, 
    farPlane=27.8447, width=9.18239, height=6.00504, cameraPosition=(14.3148, 
    5.35444, 11.3995), cameraUpVector=(-0.640899, 0.76393, -0.0752261), 
    cameraTarget=(-4.56158, -1.81758, 3.84163), viewOffsetX=2.87867, 
    viewOffsetY=-0.489602)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.8826, 
    farPlane=27.5559, width=9.35197, height=6.11594, cameraPosition=(14.5681, 
    7.52147, 9.22849), cameraUpVector=(-0.722643, 0.690831, -0.0232239), 
    cameraTarget=(-4.13848, -1.8193, 3.96613), viewOffsetX=2.93183, 
    viewOffsetY=-0.498644)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.1951, 
    farPlane=27.2428, width=9.53596, height=6.23627, cameraPosition=(13.6028, 
    10.8309, 6.75891), cameraUpVector=(-0.789433, 0.598833, -0.134892), 
    cameraTarget=(-4.09997, -1.1444, 3.91581), viewOffsetX=2.98951, 
    viewOffsetY=-0.508454)
del mdb.jobs['Job-1']
mdb.Job(name='Job-1', model='FSP_canopy_sym_fluidmodel', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, 
    numDomains=1, activateLoadBalancing=False, multiprocessingMode=DEFAULT, 
    numCpus=1)
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
