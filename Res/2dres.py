import numpy as np
from matplotlib import pyplot as plt
import time

start = time.time()
# Parameters (This can/will be streamlined with a GUI.. For now, copy + paste desired array into array = in array info)
# <p>'tp_long' : twin-probe array, longitudinal traverse
# <p>'tp_broad' : twin-probe array, broadside traverse
# <p>'wenner_long' : wenner array, longitudinal traverse
# <p>'wenner_broad' : wenner array, broadside traverse
# <p>'square_a' : square array, alpha
# <p>'square_b' : square array, beta
# <p>'square_g' : square array, gamma
# <p>'trap_l' : trapezoid array, longitudinal
# <p>'trap_b' : trapezoid array, broadside
# <p>'trap_t' : trapezoid array, theta

#Array Info
array = 'wenner_long' #Select from one of the array's above
ps = 1.0 #for twin-probe, wenner, square, and trapezoid (side 1) arrays. From 0.1 to 5
ps1 = 3 #for trapezoid array (side 2). From 0.1 to 5
ps2 = 3 #for trapezoid array (separation of sides) From 0.1 to 5

#Line Info
x_start = -10 #Min -10
x_stop = 10 #Max +10
x_step = 0.1 #Min 0.1
x = np.arange(x_start, x_stop + x_step, x_step)

#Sphere Info
insulating = 1.0e+6
conducting = 1.0e-6
rho_sphere = insulating #resistivity of sphere: insulating or conducting
z = 1.1 #depth of sphere from 0.1 to 10

#Other
rho_background = 1.0
contrast = (rho_sphere - rho_background) / (2 * rho_sphere + rho_background)


if array == 'wenner_long':   
    c1p1_l = x + 1.5 * ps
    c1p2_l = x + 1.5 * ps
    p1c2_l = x + 0.5 * ps
    p2c2_l = x - 0.5 * ps
    
    c1p1_p = ps
    c1p2_p = 2.0 * ps
    p1c2_p = 2.0 * ps
    p2c2_p = ps
    
    rel_p = 2.0 #array scaling factor1
    s = z   
    
if array == 'wenner_broad':
    c1p1_l = 1.5 * ps
    c1p2_l = 1.5 * ps
    p1c2_l = 0.5 * ps
    p2c2_l = -0.5 * ps
    
    c1p1_p = ps
    c1p2_p = 2.0 * ps
    p1c2_p = 2.0 * ps
    p2c2_p = ps
    
    rel_p = 2.0 #array scaling factor1
    s = np.sqrt(np.square(z)+np.square(x))    
    
if array == 'tp_long':
    c1p1_l = x + 0.5 * ps
    c1p2_l = x + 0.5 * ps
    p1c2_l = x - 0.5 * ps
    p2c2_l = 30.5 * ps - x
        
    c1p1_p = ps
    c1p2_p = 31.0 * ps
    p1c2_p = 31.0 * ps
    p2c2_p = ps
    
    rel_p = 1.0 #array scaling factor1
    s = z
    
if array == 'tp_broad':         
    c1p1_l = 0.5 * ps
    c1p2_l = 0.5 * ps
    p1c2_l = 0.5 * ps
    p2c2_l = -30.5 * ps
    
    c1p1_p = ps
    c1p2_p = 31.0 * ps
    p1c2_p = 31.0 * ps
    p2c2_p = ps
    
    rel_p = 1.0 #array scaling factor1
    s = np.sqrt(np.square(z)+np.square(x)) 
    
if array == 'square_a':
    c1p1_l = np.sqrt(np.square(ps/2.0)+ np.square(x-ps/2.0))
    c1p2_l = np.sqrt(np.square(ps/2.0)+ np.square(x-ps/2.0))
    p1c2_l = np.sqrt(np.square(ps/2.0)+ np.square(x-ps/2.0))
    p2c2_l = np.sqrt(np.square(ps/2.0)+ np.square(x+ps/2.0))   
    
    c1p1_p = ps
    c1p2_p = np.sqrt(2.0) * ps
    p1c2_p = np.sqrt(2.0) * ps
    p2c2_p = ps
    
    rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1
    s = np.sqrt(np.square(z)+np.square(x))  
   
if array == 'square_b': #Square Array: Beta Config       
    c1p1_l = np.sqrt(np.square(ps/2.0)+ np.square(x-ps/2.0))
    c1p1_l = np.sqrt(np.square(ps/2.0)+ np.square(x-ps/2.0))
    p1c2_l = np.sqrt(np.square(ps/2.0)+ np.square(x+ps/2.0))  
    p2c2_l = np.sqrt(np.square(ps/2.0)+ np.square(x+ps/2.0)) 
    
    c1p1_p = ps
    c1p2_p = np.sqrt(2.0) * ps
    p1c2_p = np.sqrt(2.0) * ps
    p2c2_p = ps
    
    rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1
    s = np.sqrt(np.square(z)+np.square(x))
       
if array == 'trap_b': #Trapezoid Array: Longitudinal config
    c1p1_l = np.sqrt(np.square(ps/2.0)+np.square(x-ps2/2.0))   
    c1p2_l = np.sqrt(np.square(ps/2.0)+np.square(x-ps2/2.0))    
    p1c2_l = np.sqrt(np.square(ps1/2.0)+np.square(x+ps2/2.0))      
    p2c2_l = np.sqrt(np.square(ps1/2.0)+np.square(x+ps2/2.0))    
    
    c1p1_p = np.sqrt(np.square(ps2) + np.square((ps1-ps) / 2.0))
    c1p2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2.0))
    p1c2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2.0))
    p2c2_p = np.sqrt(np.square(ps2) + np.square((ps1-ps) / 2.0))
    
    rel_p = np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 +     np.square(ps2)))/(np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 +     np.square(ps2))) - 1.0)
    s = np.sqrt(np.square(z)+np.square(x)) 

if array == 'trap_l': #Trapezoid Array: Broadside Config       
    c1p1_l = np.sqrt(np.square(x-(ps2/2.0))+np.square(ps/2.0))    
    c1p2_l = np.sqrt(np.square(x-(ps2/2.0))+np.square(ps/2.0))     
    p1c2_l = np.sqrt(np.square(x-(ps2/2.0))+np.square(ps/2.0))     
    p2c2_l = np.sqrt(np.square(x+(ps2/2.0))+np.square(ps1/2.0))
    
    c1p1_p = ps
    c1p2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2.0))
    p1c2_p = np.sqrt(np.square(ps2) + np.square(ps1-(ps1-ps) / 2.0))
    p2c2_p = ps1
    
    rel_p = np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 +     np.square(ps2)))/(np.sqrt((ps1 * ps) + np.sqrt(np.square(ps1 - ps) / 2.0 +     np.square(ps2))) - 1.0)
    s = np.sqrt(np.square(z)+np.square(x))




c1p1_r = np.sqrt(np.square(c1p1_l)+np.square(s))
c1p2_r = np.sqrt(np.square(c1p2_l)+np.square(s))
p1c2_r = np.sqrt(np.square(p1c2_l)+np.square(s))
p2c2_r = np.sqrt(np.square(p2c2_l)+np.square(s)) 

c1p1_gf = (c1p1_r / (np.sqrt(np.square(s) * np.square(np.square(c1p1_r) - 1) + np.square((np.square(c1p1_r) * (c1p1_p - c1p1_l)) + c1p1_l)))) - (1 / (c1p1_r * (np.sqrt(np.square(c1p1_r) + np.square(c1p1_p) - 2 * c1p1_l * c1p1_p))))

c1p2_gf = (c1p2_r / (np.sqrt(np.square(s) * np.square(np.square(c1p2_r) - 1) + np.square((np.square(c1p2_r) * (c1p2_p - c1p2_l)) + c1p2_l)))) - (1 / (c1p2_r * (np.sqrt(np.square(c1p2_r) + np.square(c1p2_p) - 2 * c1p2_l * c1p2_p))))

p1c2_gf = (p1c2_r / (np.sqrt(np.square(s) * np.square(np.square(p1c2_r) - 1) + np.square((np.square(p1c2_r) * (p1c2_p - p1c2_l)) + p1c2_l)))) - (1 / (p1c2_r * (np.sqrt(np.square(p1c2_r) + np.square(p1c2_p) - 2 * p1c2_l * p1c2_p))))

p2c2_gf = (p2c2_r / (np.sqrt(np.square(s) * np.square(np.square(p2c2_r) - 1) + np.square((np.square(p2c2_r) * (p2c2_p - p2c2_l)) + p2c2_l)))) - (1 / (p2c2_r * (np.sqrt(np.square(p2c2_r) + np.square(p2c2_p) - 2 * p2c2_l * p2c2_p))))

gf = c1p1_gf - c1p2_gf - p1c2_gf + p2c2_gf

resistivity = rel_p * contrast * ps * gf + 1.0



# In[17]:

line, = plt.plot(x, resistivity)
plt.show(block=False)

print time.time()-start

 




