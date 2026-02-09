program_dictionary = {
    "Bug" : " An Error",
    "Function" : "A reusable piece of code."
}

print(program_dictionary["Function"])

program_dictionary["Loop"] = "A piece of code that can repeat itself"

#if we want to wipe A dictionary

#empty_dictionary = {}

#program_dictionary = {}

#edit an item in dictionary

program_dictionary["Bug"] = "An insect living in computer"

#print(program_dictionary)

#loop through a dictionary
for key in program_dictionary:
    print(key)