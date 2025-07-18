#Dictionaries are used to store datavalue in "key":value pair
#They are unordered and mutable and don't allow duplicate keys
dict={
     "Name":"Radheshyam",                                #"key":value
     "Subjects":["Python","C","Java","Rust"],
     "Age":20,
     "Topics":("Dictionary","Set"),
     "is_adult":True
}
dict["Age"]=19 
dict["Surname"]="Sharma"             #to assign or add new value  dict["key"]="value"
print(dict)

#Nested dictionary
Student={
    "Name":"Radheshyam Sharma",
    "Subject":{
        "Phy":97,
        "Chemistry":89,
        "Maths":98
    }
}
print(Student["Subject"]["Chemistry"])
print(Student)

#Dictionary methods
# myDict.keys()           #return all keys
# myDict.values()           #return all values
# myDict.items()         #return all (key,value)pair as tuples
# myDict.get(key)         #return key according to value
# myDict.update(newDict)  #insert the specified items to the dictionary

col={
    "Student_name":"Radhe",
    "Branch":"CSE AIML",
    "Sec":"SYBTECH",
    "Skill":"Python"
}

print(col.keys())                 
print((list(col.keys())))          #we typecaste the dictionary to any datatype
print(col.values())
print(col.items())
print(col.get("Branch"))


#differnce between dict["key"] and dict.get("key")
"""print(col["Branch2"])           #error
print(col.get("Branch2")) """      #return none


col.update({"city":"mumbai"})
print(col)