#Tuples and unpacking
Coordinates=(1,2,3)
x,y,z=Coordinates
print(x,y,z,x*y)
#a,b=Coordinates
#above statement gives error..needs same number
a,b,c=Coordinates
print(a,b)

#Dicttionary
member = {
    "name":"Hari",
    "age":30,
    3: 20
}
print(member[3])
print(member.get("NoKey"))
#Default value
print(member.get("NoKey","There's key"))