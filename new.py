#case 1 - 2 particles
# sigma = 3.41E-10
# epsilon = 1.65E-21
# r = 6.82E-10
# u = 4*epsilon*((sigma/r)**(12) - (sigma/r)**(6))
# #print(u)

#case 2 - 3 particles

# el=[1.65E-21,1.65E-21,1.65E-21] #epsilon_list
# sl=[3.41E-10,3.41E-10,3.41E-10] #sigma_list
# rl=[6.82E-10,1E-10,3.41E-10] #r_list

# u0= 4*el[0]*((sl[0]/rl[0])**(12) - (sl[0]/rl[0])**(6))
# u1= 4*el[1]*((sl[1]/rl[1])**(12) - (sl[1]/rl[1])**(6))
# u2= 4*el[2]*((sl[2]/rl[2])**(12) - (sl[2]/rl[2])**(6))

#u_total_case2 = u0 + u1 + u2

# epsilon = depth of well= dispersion energy
# sigma = van der Waals radius
# r = distance between a pair of particles

# For a system with pairs of objects, el[0] = epsilon_0 = dispersion energy for 1st pair of objects
#                                     sl[0] = sigma_0 = van der Waals radius for 1st pair of objects
#                                     r1[0] = r_0 = distance between 1st pair of ojects
#                                     el[0] = epsilon_0 = dispersion energy for 2nd pair of objects etc.

def total_binding_energy():
    el=[1.65E-21,1.65E-21,1.65E-21] 
    sl=[3.41E-10,3.41E-10,3.41E-10]
    rl=[6.82E-10,1E-10,3.41E-10]
    list_u = []
    for i in range(len(el)):
        e = el[i]
        s = sl[i]
        r = rl[i]
        u = 4*e*((s/r)**(12) - (s/r)**(6))
        #return(u)
        list_u.append(u)
        print(list_u)
    total_u = sum(list_u)
    print(total_u,"J")

total_binding_energy()

# for objects at 

