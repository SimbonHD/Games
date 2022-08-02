
weight = 23

#Ground Shipping
GS_Flat_Charge = 20.00
GS_Charge = 0.00

#Ground Shipping Premium
GSP_Flat_Charge = 125.00
GSP_Final = GSP_Flat_Charge
#Drone Shipping
DS_Flat_Charge = 0.00
DS_Charge = 0

#General
BPrice = 0.00
FPrice = 0.00
Final_Message = ""
#Ground Shipping
if weight < 2:
  GS_Charge += 1.50
elif weight <= 6:
  GS_Charge += 3.00
elif weight <= 10:
  GS_Charge += 4.00
elif weight > 10:
  GS_Charge += 4.75

GS_Final = (GS_Charge * weight) + GS_Flat_Charge

#Drone Shipping
if weight < 2:
  DS_Charge += 4.50
elif weight <= 6:
  DS_Charge += 9.00
elif weight <= 10:
  DS_Charge += 12.00
elif weight > 10:
  DS_Charge += 14.25

DS_Final = (DS_Charge * weight) + DS_Flat_Charge

#Compare Ground and Drone Shipping
if GS_Final < DS_Final:
  BPrice += GS_Final
else:
  BPrice += DS_Final

#Compare Premium and Winner Drone and normal Ground
if BPrice < GSP_Flat_Charge:
  FPrice += BPrice
else:
  FPrice += GSP_Final


#Final Message IF
if FPrice == GS_Final:
  Final_Message = "Ground Shipping gets you the best price:\n$"
elif FPrice == DS_Final:
  Final_Message = "Drone Shipping gets you the best price:\n$"
elif FPrice == GSP_Final:
  Final_Message = "Ground Shipping Premium gets you the best price:\n$"


#Final Message
print("Result")
print("---------------------")

print("The Ground Shipping Premium Option would have cost you:\n$" + str(GSP_Final) + "\n")

print("The Ground Shipping Option would have cost you:\n$" + str(GS_Final) + "\n")

print("The Drone Shipping Option would have cost you:\n$" + str(DS_Final) + "\n")

print("---------------------")

print(Final_Message + str(FPrice))
