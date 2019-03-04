def main() : 
	#iF and else cases with and or conditions
	
	EmployeeAge=22
	StudentAge=23
	WorkerAge=25
	
	if EmployeeAge > StudentAge : 
		print("Employee is Older")
	else :
		print("Student is Older")
	
	
	if EmployeeAge > StudentAge and StudentAge > WorkerAge :
		print("Employee is older")
	elif StudentAge > EmployeeAge and EmployeeAge > WorkerAge :
		print("Student is Older")
	elif WorkerAge > EmployeeAge and EmployeeAge > StudentAge :
		print("Worker is Older")
	elif StudentAge == EmployeeAge : 
		print("Student and Employee have same age")
	elif EmployeeAge > StudentAge or EmployeeAge > WorkerAge :
		print("Employee is older then Student or Worker")
	else : 
		print("Sharjeel is older")
	
	
	#While loop with continue and break
	StudentAge = 1
	EmployeeAge = 2
	
	while StudentAge < 6 or StudentAge < 8:
	  print("Student Age Is",  StudentAge)
	  StudentAge += 1
	
	while EmployeeAge <= 19 : 
		print("Employee Age is", EmployeeAge)
		EmployeeAge +=2
	
	#loop with break	
	while EmployeeAge <= 19 : 
		print("Employee Age is", EmployeeAge)
		if EmployeeAge == 8 :
			break
		EmployeeAge +=2	
	
	#loop with continue
	EmployeeAge=1	
	while EmployeeAge <= 19 : 
		EmployeeAge +=2
		if EmployeeAge == 8 :
			continue
		print("Employee Age is", EmployeeAge)
	

	#foor loop
	for x in "Ankur Jasoria" :
		print(x)
	
	friendList = ["Ankur Jasoria", "Gopesh", "Nandu", "Kaku", "Affan"]
	for x in friendList:
	  print(x) 
	  if x == "Nandu":
		break
	
	#for loop with range
	for x in range(4):
	  print(x)
	else:
	  print("Task Done!")
	  
	#nested for loop	
	schoolFriends = ["nahsit", "fahad", "ikhlas"]
	collegeFriends = ["gopesh", "saffan", "raj"]

	for x in schoolFriends:
	  for y in collegeFriends:
		print(x, y)
	
	
	
main()
