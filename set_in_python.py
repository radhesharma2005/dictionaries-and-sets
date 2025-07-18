#Set is a collection of the unordered items each element in the set must be unique and immutable

#syntax
"""nums={1,2,3,4}
set={1,2,2,2}           #repeated elements stored only once,so it resolved to {1,2}
#null_set=set() """        #empty set syntax

#acceptable datatypes in set like (int,float,string,boolean,tuple)#(not acceptable datatype are list and dictionary)
"""collection={1,2,3,4,5,6,6,6,6,"hello","world","world"} #duplicates values will be ignored
print(collection)
print(type(collection))    #to check the type of datatype used
print(len(collection))"""


#set methods
"""set.add(el)   #adds an element
set.remove(el)   #removes an element
set.clear()      #empties the set
set.pop()        #removes a random value
set.union(set2)  #combines both the set value and return new 
set.intersection(set2)      #combine common value and return new"""

#sets->element->immutable
#set->mutable

# coll=set()
# coll.add(4)     #add 4 in null set
# coll.add(5)     
# coll.add(2)     
# coll.remove(2)  #remove 2 from set
# coll.add("hello")
# coll.add((1,2,3))
# coll.clear()
# print(len(coll))         #len=0 since coll is clear

Me={"radhe","prabhu","nikhil","rahul","shubham"}
You={"shubham","radhe","sahil","rohit","cyril"}
# print(Me.pop())             #printing random values
# print(Me.union(You))        #print union of two sets and give new set combine
# print(Me.intersection(You))   #print intersection of sets and return common values from both 



