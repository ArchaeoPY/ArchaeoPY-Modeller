import numpy as np

'''2D resistivity modelling of responses over a single buried Sphere. 
Based on Lynam's 1970 equations.'''

def res2D(array, a, a1, a2, x, contrast, z):
    if array == 'wenner_long':   #Wenner Array, Longitudinal Traverse
        #Relative horizontal offset
        c1p1_l = x + 1.5 * a
        c1p2_l = x + 1.5 * a
        p1c2_l = x + 0.5 * a
        p2c2_l = x - 0.5 * a
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = 2.0 * a
        p1c2_p = 2.0 * a
        p2c2_p = a
        
        rel_p = 2.0 #array scaling factor
        s = z #relative depth to centre of sphere
        
    if array == 'wenner_broad': #Wenner array, Broadside Traverse
        #Relative horizontal offset
        c1p1_l = 1.5 * a
        c1p2_l = 1.5 * a
        p1c2_l = 0.5 * a
        p2c2_l = -0.5 * a
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = 2.0 * a
        p1c2_p = 2.0 * a
        p2c2_p = a
        
        rel_p = 2.0 #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
        
    if array == 'tp_long': #Twin Probe Array, Longitudinal Traverse
        #Relative horizontal offset
        c1p1_l = x + 0.5 * a
        c1p2_l = x + 0.5 * a
        p1c2_l = x - 0.5 * a
        p2c2_l = 30.5 * a - x
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = 31.0 * a
        p1c2_p = 31.0 * a
        p2c2_p = a
        
        rel_p = 1.0 #array scaling factor
        s = z #relative depth
        
    if array == 'tp_broad': #Twin Probe Array, Broadside Traverse
        #Relative horizontal offset        
        c1p1_l = 0.5 * a
        c1p2_l = 0.5 * a
        p1c2_l = 0.5 * a
        p2c2_l = -30.5 * a
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = 31.0 * a
        p1c2_p = 31.0 * a
        p2c2_p = a
        
        rel_p = 1.0 #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
        
    if array == 'square_a': #Square Array, Alpha Configuration
        #Relative horizontal offset       
        c1p1_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        c1p2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        p1c2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        p2c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0))   
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = np.sqrt(2.0) * a
        p1c2_p = np.sqrt(2.0) * a
        p2c2_p = a
        
        rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x))  #relative depth to centre of sphere
       
    if array == 'square_b': #Square Array: Beta Config
        #Relative horizontal offset         
        c1p1_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        c1p2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        p1c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0))  
        p2c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0)) 
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = np.sqrt(2.0) * a
        p1c2_p = np.sqrt(2.0) * a
        p2c2_p = a
        
        rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
           
    if array == 'square_g': #Square Array: Beta Config
        #Relative horizontal offset         
        c1p1_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        c1p2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
        p1c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0))  
        p2c2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0)) 
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = a
        p1c2_p = a
        p2c2_p = a
        
        rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
           
           
    if array == 'trap_b': #Trapezoid Array: Longitudinal config
        #Relative horizontal offset  
        c1p1_l = np.sqrt(np.square(a/2.0)+np.square(x-a2/2.0))   
        c1p2_l = np.sqrt(np.square(a/2.0)+np.square(x-a2/2.0))    
        p1c2_l = np.sqrt(np.square(a1/2.0)+np.square(x+a2/2.0))      
        p2c2_l = np.sqrt(np.square(a1/2.0)+np.square(x+a2/2.0))    
        
        #Relative probe separation
        c1p1_p = np.sqrt(np.square(a2) + np.square((a1-a) / 2.0))
        c1p2_p = np.sqrt(np.square(a2) + np.square(a1-(a1-a) / 2.0))
        p1c2_p = np.sqrt(np.square(a2) + np.square(a1-(a1-a) / 2.0))
        p2c2_p = np.sqrt(np.square(a2) + np.square((a1-a) / 2.0))
        
        rel_p = np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 + \
        np.square(a2)))/(np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 + \
        np.square(a2))) - 1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
    
    if array == 'trap_l': #Trapezoid Array: Broadside Config
        #Relative horizontal offset        
        c1p1_l = np.sqrt(np.square(x-(a2/2.0))+np.square(a/2.0))    
        c1p2_l = np.sqrt(np.square(x-(a2/2.0))+np.square(a/2.0))     
        p1c2_l = np.sqrt(np.square(x-(a2/2.0))+np.square(a/2.0))     
        p2c2_l = np.sqrt(np.square(x+(a2/2.0))+np.square(a1/2.0))
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = np.sqrt(np.square(a2) + np.square(a1-(a1-a) / 2.0))
        p1c2_p = np.sqrt(np.square(a2) + np.square(a1-(a1-a) / 2.0))
        p2c2_p = a1
        
        rel_p = np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 + \
        np.square(a2)))/(np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 +\
        np.square(a2))) - 1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
     
    if array == 'trap_t':#Trapezoid Array: Theta config
        #Relative horizontal offset        
        c1p1_l = np.sqrt(np.square(x-(a/2.0))+np.square(a2/2.0))    
        c1p2_l = np.sqrt(np.square(x-(a/2.0))+np.square(a2/2.0))     
        p1c2_l = np.sqrt(np.square(x+(a/2.0))+np.square(a2/2.0))     
        p2c2_l = np.sqrt(np.square(x-(a1/2.0))+np.square(a2/2.0))
        
        #Relative probe separation
        c1p1_p = a
        c1p2_p = np.sqrt(np.square(a2) + np.square((a1-a) / 2.0))
        p1c2_p = np.sqrt(np.square(a2) + np.square((a1-a) / 2.0))
        p2c2_p = a1
        
        rel_p = np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 + \
        np.square(a2)))/(np.sqrt((a1 * a) + np.sqrt(np.square(a1 - a) / 2.0 + \
        np.square(a2))) - 1.0) #array scaling factor
        s = np.sqrt(np.square(z)+np.square(x)) #relative depth to centre of sphere
     
    c1p1_r = np.sqrt(np.square(c1p1_l)+np.square(s)) #distance to centre of sphere
    c1p2_r = np.sqrt(np.square(c1p2_l)+np.square(s)) #distance to centre of sphere
    p1c2_r = np.sqrt(np.square(p1c2_l)+np.square(s)) #distance to centre of sphere
    p2c2_r = np.sqrt(np.square(p2c2_l)+np.square(s)) #distance to centre of sphere
    
    #Geometry Factor Calculations for each probe pair
    c1p1_gf = (c1p1_r / (np.sqrt(np.square(s) * np.square(np.square(c1p1_r) - 1) + \
    np.square((np.square(c1p1_r) * (c1p1_p - c1p1_l)) + c1p1_l)))) - (1 / (c1p1_r * \
    (np.sqrt(np.square(c1p1_r) + np.square(c1p1_p) - 2 * c1p1_l * c1p1_p))))
        
    c1p2_gf = (c1p2_r / (np.sqrt(np.square(s) * np.square(np.square(c1p2_r) - 1) + \
    np.square((np.square(c1p2_r) * (c1p2_p - c1p2_l)) + c1p2_l)))) - (1 / (c1p2_r * \
    (np.sqrt(np.square(c1p2_r) + np.square(c1p2_p) - 2 * c1p2_l * c1p2_p))))
        
    p1c2_gf = (p1c2_r / (np.sqrt(np.square(s) * np.square(np.square(p1c2_r) - 1) + \
    np.square((np.square(p1c2_r) * (p1c2_p - p1c2_l)) + p1c2_l)))) - (1 / (p1c2_r * \
    (np.sqrt(np.square(p1c2_r) + np.square(p1c2_p) - 2 * p1c2_l * p1c2_p))))
        
    p2c2_gf = (p2c2_r / (np.sqrt(np.square(s) * np.square(np.square(p2c2_r) - 1) + \
    np.square((np.square(p2c2_r) * (p2c2_p - p2c2_l)) + p2c2_l)))) - (1 / (p2c2_r * \
    (np.sqrt(np.square(p2c2_r) + np.square(p2c2_p) - 2 * p2c2_l * p2c2_p))))
     
    #Overall Geometry factor calculation
    gf = c1p1_gf - c1p2_gf - p1c2_gf + p2c2_gf
    
    #Return Relative Resistivity Response    
    return rel_p * contrast * a * gf + 1