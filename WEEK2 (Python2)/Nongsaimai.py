def hbd(age):
    return "saimai is just 20, in base " +str(int(age/2))+"!" if age%2==0 else "saimai is just 21, in base " +str(int(age/2))+"!"


year = input("Enter year : ")

print(hbd(int(year)))