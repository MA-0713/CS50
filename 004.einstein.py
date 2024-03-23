#Energy-Mass eq

C = 300000000  #m/s

# reminder for user
print("reminder: " , "Energy in Joules , "
      , "mass in Kg and " 
      , " C is speed of light in m/s" )

# define the eq
def energy_mass(mass) :
    energy = mass * C**2
    return energy
#Ast for values (if Energy)
def Energy():
    mass = int(input("mass = ? "))
    Energy = energy_mass(mass)
    print("calculation was completed  and ", "Energy = " , Energy )

# define eq 2
def mass_energy(Energy):
    mass = Energy /C**2
    return mass 
# ask for values(if mass)
def mass() :
    Energy = int(input("Energy = ? "))
    mass = mass_energy
    print("calculation was completed, and " , " mass = " , mass )
    
print ("what you wish to calculate?" , "Enter: Energy() or mass()" , sep='\n') 
if __name__ == "__energy__":
    Energy()
    
if __name__ == "__mass__" :
   mass()
