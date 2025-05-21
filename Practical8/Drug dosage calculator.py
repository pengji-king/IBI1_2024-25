
# i need write a function which take two input of body weight and strength of paracetamol 
def drug_culculator (weight, strength):
    if 10<weight<100 and strength == 120:
        volume = 5*15*weight/120
    elif 10<weight<100 and strength == 250:
        volume = 5*15*weight/250
    else:
        print("error")
    return volume

#here is an example 
volume = drug_culculator(80,120)
print(volume)