#def res3D(array, a, a1, a2, x, contrast, )


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from itertools import izip, product

#Array Info
array = 'tp_broad' #Select from one of the array's above
ps = 1 #for twin-probe, wenner, square, and trapezoid (side 1) arrays. From 0.1 to 5
ps1 = 3 #for trapezoid array (side 2). From 0.1 to 5
ps2 = 3 #for trapezoid array (separation of sides) From 0.1 to 5

#Grid Info
x_length = 20
x_step = 0.25
y_length = 20
y_step = 0.25

#Sphere Info
insulating = 1.0e+6
conducting = 1.0e-6
rho_sphere = insulating #resistivity of sphere: insulating or conducting
radius = 0.25 * ps #relative radius
diameter = 2 * radius #relative sphere diameter
sphere_x = 10
sphere_y = 10 
sphere_z = 2 

#Other
rho_background = 1.0
contrast = (rho_sphere - rho_background) / (2 * rho_sphere + rho_background)
sphere_xyz = np.array([sphere_x, sphere_y, sphere_z])
#print sphere_xyz[0]

'''Grid Computations'''
#Creates a grid of (x, y) measurements positions
#assuming level surface, z = 0
x_grid_pos = np.arange(np.divide(x_step,2.0), x_length, x_step)
y_grid_pos = np.arange(np.divide(y_step,2.0), y_length, y_step)
xgrid, ygrid = np.meshgrid(x_grid_pos, y_grid_pos)

if array == 'wenner_long':
    C1_x = xgrid #X Grid positions of C1 electrode
    C1_y = np.add(ygrid, 1.5 * ps)
    C1_z = np.zeros(C1_x.shape)

    P1_x = xgrid
    P1_y = np.add(ygrid, 0.5 * ps)
    P1_z = np.zeros(P1_x.shape)

    P2_x = xgrid
    P2_y = np.subtract(ygrid, 0.5 * ps)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = 2.0 * ps
    p1c2_p = 2.0 * ps
    p2c2_p = ps
    
    rel_p = 2.0 #array scaling factor1
    
if array == 'wenner_broad':
    C1_x = np.add(xgrid, 1.5 * ps)
    C1_y = ygrid
    C1_z = np.zeros(C1_x.shape)

    P1_x = np.add(xgrid, 0.5 * ps)
    P1_y = ygrid
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.subtract(xgrid, 0.5 * ps)
    P2_y = ygrid
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = 2.0 * ps
    p1c2_p = 2.0 * ps
    p2c2_p = ps
    
    rel_p = 2.0 #array scaling factor1

if array == 'tp_long':
    C1_x = xgrid
    C1_y = np.add(ygrid, ps / 2.0)
    C1_z = np.zeros(C1_x.shape)

    P1_x = xgrid
    P1_y = np.subtract(ygrid, ps / 2.0)
    P1_z = np.zeros(P1_x.shape)

    P2_x = xgrid
    P2_y = np.subtract(100.5 * ps, ygrid)
    P2_z = np.zeros(P2_x.shape)
        
    c1p1_p = ps
    c1p2_p = 101 * ps
    p1c2_p = 101 * ps
    p2c2_p = ps
    
    rel_p = 1.0 #array scaling factor1

if array == 'tp_broad':         
    C1_x = np.add(xgrid, ps / 2.0)
    C1_y = ygrid
    C1_z = np.zeros(C1_x.shape)

    P1_x = np.add(xgrid, ps / 2.0)
    P1_y = ygrid
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.subtract(100.5 * ps, xgrid)
    P2_y = ygrid
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = 101 * ps
    p1c2_p = 101 * ps
    p2c2_p = ps
    
    rel_p = 1.0 #array scaling factor1
        
if array == 'square_a':
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps / 2.0)
    C1_z = np.zeros(C1_x.shape)

    P1_x = np.add(xgrid, ps / 2.0)
    P1_y = np.add(ygrid, ps / 2.0)
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.add(xgrid, ps / 2.0)
    P2_y = np.subtract(ygrid, ps / 2.0)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = np.sqrt(2) * ps
    p1c2_p = np.sqrt(2) * ps
    p2c2_p = ps
    
    rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1

if array == 'square_b': #Square Array: Beta Config       
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps / 2.0)
    C1_z = np.zeros(C1_x.shape)
        
    P1_x = np.subtract(xgrid, ps / 2.0)
    P1_y = np.subtract(ygrid, ps / 2.0)
    P1_z = np.zeros(P1_x.shape)
        
    P2_x = np.add(xgrid, ps / 2.0)
    P2_y = np.subtract(ygrid, ps / 2.0)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = np.sqrt(2) * ps
    p1c2_p = np.sqrt(2) * ps
    p2c2_p = ps
    
    rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1

if array == 'square_g': #Square Array: Gamma Config
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps / 2.0)
    C1_z = np.zeros(C1_x.shape)
        
    P1_x = np.add(xgrid, ps / 2.0)
    P1_y = np.add(ygrid, ps / 2.0)
    P1_z = np.zeros(P1_x.shape)
        
    P2_x = np.subtract(xgrid, ps / 2.0)
    P2_y = np.subtract(ygrid, ps / 2.0)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = ps
    p1c2_p = ps
    p2c2_p = ps
    
    rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1
       
if array == 'trap_l': #Trapezoid Array: Longitudinal config     
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps2 / 2.0)
    C1_z = np.zeros(C1_x.shape)

    P1_x = np.add(xgrid, ps / 2.0)
    P1_y = np.add(ygrid, ps2 / 2.0)
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.add(xgrid, ps1 / 2.0)
    P2_y = np.subtract(ygrid, ps2 / 2.0)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p1c2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p2c2_p = ps1
    
    rel_p = np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2)))/(np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2))) - 1.0)
   
if array == 'trap_b': #Trapezoid Array: Broadside Config       
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps2 / 2.0)
    C1_z = np.zeros(C1_x.shape)

    P1_x = np.subtract(xgrid, ps1 / 2.0)
    P1_y = np.subtract(ygrid, ps2 / 2.0)
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.add(xgrid, ps1 / 2.0)
    P2_y = np.subtract(ygrid, ps2 / 2.0)
    P2_z = np.zeros(P2_x.shape)
    
    c1p1_p = ps
    c1p2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p1c2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p2c2_p = ps1
    
    rel_p = np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2)))/(np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2))) - 1.0)
    
if array == 'trap_t':#Trapezoid Array: Theta config
    C1_x = np.subtract(xgrid, ps / 2.0)
    C1_y = np.add(ygrid, ps2 / 2.0)
    C1_z = np.zeros(C1_x.shape)
        
    P1_x = np.add(xgrid, ps / 2.0)
    P1_y = np.add(ygrid, ps2 / 2.0)
    P1_z = np.zeros(P1_x.shape)

    P2_x = np.subtract(xgrid, ps1 / 2.0)
    P2_y = np.subtract(ygrid, ps2 / 2.0)
    P2_z = np.zeros(P1_x.shape)
        
    c1p1_p = ps
    c1p2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p1c2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2))
    p2c2_p = ps1
    
    rel_p = np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2)))/(np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 + \
    np.square(ps2))) - 1.0)


resistivity_sum = np.ones(C1_x.shape)

for xyz in sphere_xyz:

    c1_x_delta = np.subtract(C1_x,sphere_x) #change in x-between C1(x) and sphere(x)
    c1_y_delta = np.subtract(C1_y,sphere_y) #change in y-between C1(y) and sphere(y)
    c1_z_delta = np.add(C1_z,sphere_z) #change in z-between C1(z) and sphere(z)
    c1_l = np.sqrt(np.square(c1_x_delta)+ np.square(c1_y_delta)) #horizontal (x,y) distance between C1 and centre of sphere
    c1_s = np.sqrt(np.square(c1_z_delta) + np.square(c1_x_delta) + np.square(c1_y_delta)) #relative depth of sphere
    c1_r = np.sqrt(np.square(c1_l)+np.square(c1_s)) #distance to sphere
    
    p1_x_delta = np.subtract(P1_x,sphere_x) #same as previous, but for P1
    p1_y_delta = np.subtract(P1_y,sphere_y)
    p1_z_delta = np.add(P1_z,sphere_z)
    p1_l = np.sqrt(np.square(p1_x_delta)+ np.square(p1_y_delta)) #horizontal (x,y) distance between P1 and centre of sphere
    p1_s = np.sqrt(np.square(p1_z_delta) + np.square(p1_x_delta) + np.square(p1_y_delta)) #relative depth of sphere
    p1_r = np.sqrt(np.square(p1_l)+np.square(p1_s)) #distance to sphere
    
    p2_x_delta = np.subtract(P2_x,sphere_x)
    p2_y_delta = np.subtract(P2_y,sphere_y)
    p2_z_delta = np.add(P2_z,sphere_z)
    p2_l = np.sqrt(np.square(p2_x_delta)+ np.square(p2_y_delta)) #horizontal (x,y) distance between P2 and centre of sphere
    p2_s = np.sqrt(np.square(p2_z_delta) + np.square(p2_x_delta) + np.square(p2_y_delta)) #relative depth of sphere
    p2_r = np.sqrt(np.square(p2_l)+np.square(p2_s))
         
    #Calculating the geometry factors for the probe pairs: 
    
    c1p1_gf = (c1_r/(np.sqrt(np.square(c1_s)*np.square(np.square(c1_r)-1.0)+ \
    np.square((np.square(c1_r)*(c1p1_p-c1_l))+c1_l))))-(1.0/(c1_r*(np.sqrt(np.square(c1_r)\
    +np.square(c1p1_p)-2.0*c1_l*c1p1_p))))
    
    c1p2_gf =(c1_r/(np.sqrt(np.square(c1_s)*np.square(np.square(c1_r)-1.0)+ \
    np.square((np.square(c1_r)*(c1p2_p-c1_l))+c1_l))))-(1.0/(c1_r*(np.sqrt(np.square(c1_r)\
    +np.square(c1p2_p)-2.0*c1_l*c1p2_p))))
    
    p1c2_gf = (p1_r/(np.sqrt(np.square(p1_s)*np.square(np.square(p1_r)-1.0)+\
    np.square((np.square(p1_r)*(p1c2_p-p1_l))+p1_l))))-(1.0/(p1_r*(np.sqrt(np.square(p1_r)\
    +np.square(p1c2_p)-2.0*p1_l*p1c2_p))))
    
    p2c2_gf = (p2_r/(np.sqrt(np.square(p2_s)*np.square(np.square(p2_r)-1.0)+\
    np.square((np.square(p2_r)*(p2c2_p-p2_l))+p2_l))))-(1.0/(p2_r*(np.sqrt(np.square(p2_r)\
    +np.square(p2c2_p-2.0*p2_l*p2c2_p)))))
    
    #Calculating the probe pairs resistivity responses: 
    gf = c1p1_gf - c1p2_gf - p1c2_gf + p2c2_gf
    resistivity = contrast * rel_p * gf * ps
    response = np.add(resistivity_sum, resistivity)


'''Plot Results: 2D'''
fig, ax = plt.subplots()

p = ax.pcolor(xgrid, ygrid, response, cmap=plt.cm.Greys)
cb = fig.colorbar(p, ax=ax)
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
plt.title(array+': Insulating Feature')

'''Plot Results: Wireframe'''
fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection='3d')
surf = ax.plot_wireframe(xgrid, ygrid, response, rstride=4, cstride=4, color='b', alpha=0.7)
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Response')
plt.title('Twin-Probe Broadside: Insulating Feature')
plt.show()






