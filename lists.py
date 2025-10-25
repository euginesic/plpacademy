
#creating an empty list
my_list=[]
#adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting element at specific position
my_list.insert(2,15)
#3xtending the list with multiple elements
my_list.extend([50,60,70])
#removing an element
my_list.remove(70)
#sorting the list
sorted_list=sorted(my_list)
#printing an indext of an element
try:
    index_of_30=my_list.index(30)
    print(f"Index of 30: {index_of_30}")
except ValueError:
    print("30 is not in the list")
