import numpy as np

def res2Dpseudo(array, array_range, x, contrast, z):
    first = True
    for a in array_range:
        if array == 'wenner_long':   
            c1p1_l = x + 1.5 * a
            c1p2_l = x + 1.5 * a
            p1c2_l = x + 0.5 * a 
            p2c2_l = x - 0.5 * a
            
            c1p1_p = a
            c1p2_p = 2.0 * a
            p1c2_p = 2.0 * a
            p2c2_p = a
            
            rel_p = 2.0 #array scaling factor1
            s = z   
            
        if array == 'wenner_broad':
            c1p1_l = 1.5 * a
            c1p2_l = 1.5 * a
            p1c2_l = 0.5 * a
            p2c2_l = -0.5 * a
            
            c1p1_p = a
            c1p2_p = 2.0 * a
            p1c2_p = 2.0 * a
            p2c2_p = a
            
            rel_p = 2.0 #array scaling factor1
            s = np.sqrt(np.square(z)+np.square(x))    
            
        if array == 'tp_long':
            c1p1_l = x + 0.5 * a
            c1p2_l = x + 0.5 * a
            p1c2_l = x - 0.5 * a
            p2c2_l = 30.5 * a - x
                
            c1p1_p = a
            c1p2_p = 31.0 * a
            p1c2_p = 31.0 * a
            p2c2_p = a
            
            rel_p = 1.0 #array scaling factor1
            s = z
            
        if array == 'tp_broad':         
            c1p1_l = 0.5 * a
            c1p2_l = 0.5 * a
            p1c2_l = 0.5 * a
            p2c2_l = -30.5 * a
            
            c1p1_p = a
            c1p2_p = 31.0 * a
            p1c2_p = 31.0 * a
            p2c2_p = a
            
            rel_p = 1.0 #array scaling factor1
            s = np.sqrt(np.square(z)+np.square(x)) 
            
        if array == 'square_a':
            c1p1_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
            c1p2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
            p1c2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
            p2c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0))   
            
            c1p1_p = a
            c1p2_p = np.sqrt(2.0) * a
            p1c2_p = np.sqrt(2.0) * a
            p2c2_p = a
            
            rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1
            s = np.sqrt(np.square(z)+np.square(x))  
           
        if array == 'square_b': #Square Array: Beta Config       
            c1p1_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
            c1p2_l = np.sqrt(np.square(a/2.0)+ np.square(x-a/2.0))
            p1c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0))  
            p2c2_l = np.sqrt(np.square(a/2.0)+ np.square(x+a/2.0)) 
            
            c1p1_p = a
            c1p2_p = np.sqrt(2.0) * a
            p1c2_p = np.sqrt(2.0) * a
            p2c2_p = a
            
            rel_p = np.sqrt(2.0)/(np.sqrt(2.0)-1.0) #array scaling factor1
            s = np.sqrt(np.square(z)+np.square(x))
            
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

    
        c1p1_r = np.sqrt(np.square(c1p1_l)+np.square(s))
        c1p2_r = np.sqrt(np.square(c1p2_l)+np.square(s))
        p1c2_r = np.sqrt(np.square(p1c2_l)+np.square(s))
        p2c2_r = np.sqrt(np.square(p2c2_l)+np.square(s)) 
        
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
            
        gf = c1p1_gf - c1p2_gf - p1c2_gf + p2c2_gf
            
        resistivity = rel_p * contrast * a * gf + 1.0
        
        
        if first:
            pseudo = resistivity
            first = False
        else:
            pseudo = np.vstack((pseudo,resistivity))

    return pseudo