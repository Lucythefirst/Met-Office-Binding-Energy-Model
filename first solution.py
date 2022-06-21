#epsilon = depth of well= dispersion energy
# sigma = van der Waals radius
# r = distance between a pair of particles

# For a system with pairs of objects, el[0] = epsilon_0 = dispersion energy for 1st pair of objects
#                                     sl[0] = sigma_0 = double the van der Waals radius for 1st pair of objects
#                                     r1[0] = r_0 = distance between 1st pair of ojects
#                                     el[0] = epsilon_0 = dispersion energy for 2nd pair of objects etc.

#For 6 objects: 

def total_binding_energy_6():
    el=[1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21,1.65E-21] 
    sl=[3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10,3.41E-10]
    rl=[6.82E-10,1E-10,3.41E-10,6.82E-10,1E-10,3.41E-10,6.82E-10,1E-10,3.41E-10,6.82E-10,1E-10,3.41E-10,6.82E-10,1E-10,3.41E-10]
    list_u = []
    for i in range(len(el)):
        e = el[i]
        s = sl[i]
        r = rl[i]
        u = 4*e*((s/r)**(12) - (s/r)**(6))
        #return(u)
        list_u.append(u)
    total_u = sum(list_u)
    print(total_u,"J for 6 objects")

total_binding_energy_6()
