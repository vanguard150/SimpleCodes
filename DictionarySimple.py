# Input 1234, output One Two Three Four
phone=input("Phone: ")
digits_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output=""
for ch in phone:
    output +=digits_dict.get(ch,"!")+" "
print(output)

#Dictio
