# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 09:32:12 2014

Recreating Nic Sheens Modeller2 in Python

@author: FPopecarter
"""

import numpy as np
import time
import matplotlib.pyplot as plt
import Image


def r_calc(g,d,a,b,z,strike,i):
    return np.sqrt(np.square(a+b*z) + np.square(g+d*z) + np.square(z))
    
def e_calc(g,d,a,b,z,strike,i):
    return np.sqrt(1.0 + np.square(b) + np.square(d))
    
def calc_f1(g,d,a,b,z,strike,i,r,e):
        
    odsq = np.add(1,np.square(d))
    
    t1 = - np.divide(1,odsq)*np.arctan(np.divide((a*g*d)+((a-(b*g*d)*z)),g*r))
    t2 = np.divide(d,2*odsq)* np.log(np.divide(r+a+(b*z),r-a-(b*z)))
    t3 = - np.divide(b*d,2*e*odsq)* np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z)))
    
    temp = -(t1 + t2 + t3)
    #np.savetxt(str(a[0,0])+'t1.csv',t1,delimiter=',')
    #np.savetxt(str(a[0,0])+'t2.csv',t2,delimiter=',')
    #np.savetxt(str(a[0,0])+'t3.csv',t3,delimiter=',')
    #np.savetxt(str(a[0,0])+'tmp.csv',temp,delimiter=',')
    return - (t1 + t2 + t3)
    #return -(-(1.0/(1.0+d**2))*np.arctan(np.divide((a*g*d)+(a-b*g*d)*z,g*r)) + np.divide(d,2*(1+d**2))*np.log(np.divide(r+a+(b*z),r-a-(b*z))) - np.divide(b*d,2*e*(1+d**2))*np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z))))
    
def calc_f2(g,d,a,b,z,strike,i,r,e):
    
    odsq = np.add(1,np.square(b))
    
    t1 = - np.divide(1,odsq)*np.arctan(np.divide((a*b*g)+((g-(a*b*d)*z)),a*r))
    t2 = np.divide(b,2*odsq)* np.log(np.divide(r+g+(d*z),r-g-(d*z)))
    t3 = - np.divide(b*d,2*e*odsq)* np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z)))
    
    temp = -(t1 + t2 + t3)
    #np.savetxt('t1.csv',t1,delimiter=',')
    #np.savetxt('t2.csv',t2,delimiter=',')
    #np.savetxt('t3.csv',t3,delimiter=',')
    #np.savetxt('tmp.csv',temp,delimiter=',')
    return  -(t1 + t2 + t3)
    #return -(-(1.0/(1.0+b**2))*np.arctan(np.divide((a*g*b)+(g-a*b*d)*z,a*r)) + np.divide(b,2*(1+b**2))*np.log(np.divide(r+g+(d*z),r-g-(d*z))) - np.divide(b*d,2*e*(1+b**2))*np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z))))
    
def calc_f3(g,d,a,b,z,strike,i,r,e):
    return -np.arctan((a+b*z)*(g+d*z)/(z*r))-(np.square(b)/(1.0+np.square(b)))*np.arctan((a*b*g+(g-a*b*d)*z)/(a*r))-(np.square(d)/(1.0+np.square(d)))*np.arctan((a*g*d+(a-b*d*g)*z)/(g*r)) -(b/(2.0*(1.0+np.square(b))))*np.log((r+g+d*z)/(r-g-d*z))-(d/(2.0*(1.0+np.square(d))))*np.log((r+a+b*z)/(r-a-b*z))+(b*d/(2.0*e))*(1.0/(1.0+np.square(b))+1.0/(1.0+np.square(d)))*np.log(abs((e*r+a*b+g*d+e*z)/(e*r-a*b-g*d-e*z)))
    
def calc_f4(g,d,a,b,z,strike,i,r,e):
    return -(np.divide(1,1+b**2)*np.arctan(np.divide((a*b*g)+(g-(a*b*d))*z,a*r)) - np.divide(1,1+d**2)*np.arctan(np.divide((a*g*d)+(a-(b*g*d))*z,g*r)) - np.divide(b,2*(1+b**2))*np.log(np.divide(r+g+(d*z),r-g-(d*z))) + np.divide(d,2*(1+d**2))*np.log(np.divide(r+a+(b*z),r-a-(b*z))) + np.divide(b*d,2*e)*(np.divide(1,1+b**2)-np.divide(1,1+d**2))*np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z))))
    
def calc_f5(g,d,a,b,z,strike,i,r,e):
    return -(np.divide(1,2*e)*np.log(np.divide((e*r)+(a*b)+(g*d)+(e*z),(e*r)-(a*b)-(g*d)-(e*z))))
    
def calc_f6(g,d,a,b,z,strike,i,r,e):
    return -((d/(1.0+np.square(d)))*np.arctan((a*d*g+(a-g*b*d)*z)/(g*r))+(1.0/(2.0*(1.0+np.square(d))))*np.log((r+a+b*z)/(r-a-b*z))-(b/(2.0*e*(1.0+np.square(d))))*np.log(abs((e*r+a*b+g*d+e*z)/(e*r-a*b-g*d-e*z))))
    
def calc_f7(g,d,a,b,z,strike,i,r,e):
    return (b/(1.0+np.square(b)))*np.arctan((a*b*g+(g-a*b*d)*z)/(a*r))+(1.0/(2.0*(1.0+np.square(b))))*np.log((r+g+d*z)/(r-g-d*z))-(d/(2.0*e*(1.0+np.square(b))))*np.log(abs((e*r+a*b+g*d+e*z)/(e*r-a*b-g*d-e*z)))

def calcpoints(g,d,a,b,z,strike,i):
    r = r_calc(g,d,a,b,z,strike,i)
    e = e_calc(g,d,a,b,z,strike,i)
    
    f1 = calc_f1(g,d,a,b,z,strike,i,r,e)
    f2 = calc_f2(g,d,a,b,z,strike,i,r,e)
    f3 = calc_f3(g,d,a,b,z,strike,i,r,e)
    f4 = calc_f4(g,d,a,b,z,strike,i,r,e)
    f5 = calc_f5(g,d,a,b,z,strike,i,r,e)
    f6 = calc_f6(g,d,a,b,z,strike,i,r,e)
    f7 = calc_f7(g,d,a,b,z,strike,i,r,e)
    
    Fx = f1 * np.cos(i)*np.cos(strike)**2 + f2*np.cos(i)*np.sin(strike)**2 + f5*2*np.cos(i)*np.sin(strike)*np.cos(strike) - f6*np.sin(i)*np.cos(strike) - f7*np.sin(i)*np.sin(strike)
    Fy = -f4 * np.cos(i)*np.sin(strike)*np.cos(strike) - f5*np.cos(i)*(np.sin(strike)**2 - np.cos(strike)**2) + f6 * np.sin(i)*np.sin(strike) - f7 * np.sin(i)*np.cos(strike)
    Fz = f3 * np.sin(i) - f6 * np.cos(i)* np.cos(strike) - f7 * np.cos(i)* np.sin(strike)
    Ft = f1 * np.cos(i)**2 * np.cos(strike)**2 + f2 * np.cos(i)**2 * np.sin(strike)**2 + f3 * np.sin(i)**2 + f5 * 2 * np.cos(i)**2 * np.sin(strike)*np.cos(strike) - f6 * 2 * np.sin(i)*np.cos(i)*np.cos(strike) - f7 * 2 * np.sin(i)* np.cos(i) * np.sin(strike)
    
    return Fx, Fy, Fz, Ft
    
#survey dimensions (start, stop, sampling density)
surv_x = (-10.0,10.0,10)
surv_y = (-10.0,10.0,10)

xx = np.linspace(surv_x[0],surv_x[1],(surv_x[1]-surv_x[0])*surv_x[2])
yy = np.linspace(surv_y[0],surv_y[1],(surv_y[1]-surv_y[0])*surv_y[2])

gx,gy = np.meshgrid(xx,yy, indexing='xy')

Fields = np.zeros((4,np.shape(gx)[0],np.shape(gx)[1]))

print np.shape(Fields)
#model bounding coordinates
mx = (-1.01,1.01,-1.01,1.01)
my = (-1.01,1.01,-1.01,1.01)
mz = (0.1,0.5)

sensor_z = (0.5,1.0)

inclination = np.deg2rad(70)
susceptibility = 1
strike = np.deg2rad(0)
theta = np.deg2rad(0) #This doesn't appear in Modeller2 GUI
          #is coded in the backend

#Used in all Grad Calculations
#Independent of Grid Position
mba = np.subtract(mz[1],mz[0])

grad0 = np.divide(np.subtract(np.multiply(my[2],mz[0]),
                              np.multiply(my[0],mz[1])
                              ),mba)                   
grad1 = np.divide(np.subtract(my[0],my[2]),mba)
grad2 = np.divide(np.subtract(np.multiply(my[3],mz[0]),
                              np.multiply(my[1],mz[1])
                              ),mba)                  
grad3 = np.divide(np.subtract(my[1],my[3]),mba)

grad4 = np.divide(np.subtract(np.multiply(mx[0],mz[0]),
                              np.multiply(mx[2],mz[1])
                              ),mba)                         
grad5 = np.divide(np.subtract(mx[2],mx[0]),mba)
grad6 = np.divide(np.subtract(np.multiply(mx[3],mz[0]),
                              np.multiply(mx[1],mz[1])
                              ),mba)                      
grad7 = np.divide(np.subtract(mx[1],mx[3]),mba)


#Dependent on Grid Position
alpha1 = np.add(gy,grad0)
alpha2 = np.add(gy,grad2)

gamma1 = np.add(gx,grad4)
gamma2 = np.add(gx,grad6)

#dependent on model
beta1 = grad1
beta2 = grad3

delta1 = grad5
delta2 = grad7

#Dependent on sensor height
for sens_z in sensor_z:
    z1 = mz[0] + sens_z
    z2 = mz[1] + sens_z
        
    # depth[i], depth[i+1]  = a, b
    # x = gx
    # y = gy,
    # h = sensor height (not distance from sensor to feature)
    
    res1 = calcpoints(gamma1,delta1,alpha1,beta1,z1,strike,inclination)
    res2 = calcpoints(gamma1,delta1,alpha1,beta1,z2,strike,inclination)
    res3 = calcpoints(gamma1,delta1,alpha2,beta2,z1,strike,inclination)
    res4 = calcpoints(gamma1,delta1,alpha2,beta2,z2,strike,inclination)
    res5 = calcpoints(gamma2,delta2,alpha1,beta1,z1,strike,inclination)
    res6 = calcpoints(gamma2,delta2,alpha1,beta1,z2,strike,inclination)
    res7 = calcpoints(gamma2,delta2,alpha2,beta2,z1,strike,inclination)
    res8 = calcpoints(gamma2,delta2,alpha2,beta2,z2,strike,inclination)
    
    #Fz = res1[2] - res2[2] - res3[2] + res4[2] - res5[2] + res6[2] + res7[2] - res8[2]
    #Fz = (-1**-susceptibility)* Fz
    pos = np.add(res1,np.add(res4,np.add(res6,res7)))
    neg = np.add(res2,np.add(res3,np.add(res5,res8)))
    temp = np.subtract(pos,neg)
    #temp = np.subtract(res1,np.subtract(res2,np.add(res3,np.subtract(res4,np.add(res5,np.add(res6,np.subtract(res7,res8)))))))
    #Fields = res1 - res2 - res3 + res4 - res5 + res6 + res7 - res8
    temp = (-1.0**-susceptibility)*temp
    
    Fields = np.subtract(Fields,temp)
    
    
    for i,fname in zip(range(0,5),('Fx.csv','Fy.csv','Fz.csv','Ft.csv')):
        Fi = Fields[i]
        fname2 = fname.split('.')[0] +  str(sens_z) + '.csv'
        np.savetxt(fname2, Fi, delimiter=',')
        fig = plt.figure()
        ax = fig.add_axes([0.05,0.05,0.9,0.9])
        ax.axis('equal')
        im = plt.imshow(np.copy(Fi), vmin=np.percentile(Fi,10), vmax=np.percentile(Fi,90), origin='lower', cmap=plt.cm.Greys)
        plt.colorbar()
        plt.hold()
        print fname
        fname_o = fname.split('.')[0] + str(sens_z) + '.png'
        plt.savefig(fname_o)
        plt.show(block=True)
        plt.cla()
        plt.close()
        
        j=1
        #for res in (res1,res2,res3,res4,res5,res6,res7,res8):
            #fig = plt.figure()
            #ax = fig.add_axes([0.05,0.05,0.9,0.9])
            #ax.axis('equal')
            #im = plt.imshow(np.copy(res[i]), vmin=np.percentile(res[i],10), vmax=np.percentile(res[i],90), origin='lower', cmap=plt.cm.Greys)
            #plt.colorbar()
            #plt.hold()
            #plt.show(block=False)
            
            #fname_o = fname.split('.')[0] + str(j) + '.png'
            #print j
            #plt.savefig(fname_o)
            #plt.close()
            #j+=1
            
