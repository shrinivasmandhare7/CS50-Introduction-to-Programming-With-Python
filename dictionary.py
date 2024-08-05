myDict = {"name": "Shrinivas Mandhare", "age": 25}
print(myDict)


#  when you use a for loop in Python to iterate over a dictionary, by design, it iterates over all of
# the keys

for k in myDict:
    print(k)

for k in myDict:
    print(k, myDict[k])
# None Represent absence of value

students = [{"name": "bhushan"}, {"name": "Anmol"}]
for student in students:
    print(student["name"])
