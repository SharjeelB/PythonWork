def main() : 
	lstEmployee = ["sharjeel", "GOPESH PANDEY", "Rupak"]
	print(lstEmployee)
	
	#You access the list items by referring to the index number
	print(lstEmployee[1])
	
	#To change the value of a specific item, refer to the index number:
	lstEmployee[0] = "AFFAN"
	print(lstEmployee)
	
	#Print all items in the list, one by one
	for employee in lstEmployee:
		print(employee)
	
	#Print the number of items in the list
	print(len(lstEmployee))
	
	#To add an item to the end of the list, use the append() method
	lstEmployee.append("Adyan")
	print(lstEmployee)
	
	#To add an item at the specified index, use the insert() method
	lstEmployee.insert(1, "shaghil")
	print(lstEmployee)
	
	#The remove() method removes the specified item
	lstEmployee.remove("shaghil")
	print(lstEmployee)
	
	#The pop() method removes the specified index, (or the last item if index is not specified)
	lstEmployee.pop()
	print(lstEmployee)
	
	#The del keyword removes the specified index
	del lstEmployee[0]
	print(lstEmployee)
	
	#The del keyword can also delete the list completely
	del lstEmployee
	
	#Using the list() constructor to make a List
	lstEmployee = list(("bilali", "affan", "adyan")) # note the double round-brackets
	print(lstEmployee)
	
main()
