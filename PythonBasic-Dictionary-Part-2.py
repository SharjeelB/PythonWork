def main() : 
	#Create a Dictionary
	dicEmployee =	{
	  "EmployeeName": "Sharjeel",
	  "employeeId": "sha-0123",
	  "joiningYear": 2018
	}
	print(dicEmployee)
	
	#Accessing Items : You can access the items of a dictionary by referring to its key name
	employeeName = dicEmployee["EmployeeName"]
	print(employeeName)
	
	#Get the value of the "model" key
	employeeId = dicEmployee.get("employeeId")
	print(employeeId)
	
	#Change the "joiningYear" to 2019
	dicEmployee["joiningYear"] = 2019
	print(dicEmployee)
	
	#Use for loop to iterate in dictionary values : Print all key names in the dictionary, one by one
	for empInfo in dicEmployee:
		print(empInfo)
	
	#Print all values in the dictionary, one by one:
	for x in dicEmployee:
		print(dicEmployee[x])

	#You can also use the values() function to return values of a dictionary:
	for dicValues in dicEmployee.values():
	  print(dicValues)
	  
	#Loop through both keys and values, by using the items() function
	for dicKey, dicValue in dicEmployee.items():
		print(dicKey, dicValue)

	#Dictionary Length : To determine how many items (key-value pairs) a dictionary have, use the len() method.
	print(len(dicEmployee))
	
	#Adding Items : Adding an item to the dictionary is done by using a new index key and assigning a value to it
	dicEmployee["employeeDepartment"] = "Information Technologies"
	print(dicEmployee)
	
	#Removing Items : There are several methods to remove items from a dictionary
	#The del keyword removes the item with the specified key name
	del dicEmployee["joiningYear"]
	print(dicEmployee)
	
	#The pop() method removes the item with the specified key name
	dicEmployee.pop("employeeDepartment")
	print(dicEmployee)
	
	#The clear() keyword empties the dictionary:
	dicEmployee.clear()
	print(dicEmployee)
	
	#The del keyword can also delete the dictionary completely
	del dicEmployee
	
	dicEmployee =	dict(EmployeeName = "Sharjeel", employeeId= "sha-0123", joiningYear = 2018)
	print(dicEmployee)
	
main()
