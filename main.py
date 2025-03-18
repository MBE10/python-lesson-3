# collections

lista = [1,2,3,4,4]

tuples = (1,2,3,4)

dictionaries = { "Klasa8" : 10,
 "Klasa 10" : 20}



 #sets

my_set = {1,2,3}

print(my_set)

your_set = set([1,2,3,3,2])
print(your_set)

set1 = {1,2,3}
set2 = {4,5,6}

# set1.update(set2)

unionsets = set1.union(set2)

intersection = set1.intersection(set2)

differencesets = set2.difference(set1)

print(unionsets)
print(intersection)
print(differencesets)

darsejSet = {"Milan", "Chelsea", "Liverpool", "Real Madrid"}

darsejSet.add("Real Betis")

print(darsejSet)

darsejSet.remove("Liverpool")
print(darsejSet)

print(len(darsejSet))
darsejSet.clear()

LisaList = [1,2,3,4,5,6,6,6]

uniqe_list = set(LisaList)

print(uniqe_list)

# Conditionals

# if kushti:
#     print()
# elif kushti:
#     print()

# else: 

# age = 18

# if age >= 18:
#     print("Ti je i rritun")

# else:
#     print ("Ti je i vogel")   


age = 18

if age < 18:
    print("SKI te drejt vote!")

elif age < 65:
    print("Mundesh me votu")   

else:
    print("Je plak tash")     

# in 

setEmra = {"Medina", "Joni", "Andi", "Leoni"}

found = "Joni" in setEmra

print(found)
    