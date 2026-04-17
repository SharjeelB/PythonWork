
def employeeInformation():
    employeeName = "Aravind Kumar"
    print("employee name of class is : " + employeeName  )


    #NumericTypes = [int, float, complex]
    employeeAge= 28
    employeeSalary = 50000.50
    employeeID = "AED987565DF87"

    print("employee age is : ", employeeAge)
    print("employee salary is : ", employeeSalary)
    print("employee ID is : ", employeeID)

    #SequenceTypes = [list, tuple, range]
    employeeQualification = ["B.Tech", "M.Tech", "PhD"]
    employeeDepartment = ("IT", "HR", "Finance")
    employeeIDRange = range(1, 100)

    print("employee qualification is : ", employeeQualification)
    print("employee qualification is : ", employeeQualification[1])
    print("employee department is : ", employeeDepartment)
    print("employee ID range is : ", employeeIDRange)

    

    #Difference between list and touple
    #List is mutable, while tuple is immutable
    employeeProjects = ["Project A", "Project B", "Project C"]
    employeeRoles = ("Developer", "Manager", "Analyst")
    print("employee projects before modification : ", employeeProjects)
    employeeProjects[0] = "Project X"  # This is allowed, as lists are mutable
    print("employee projects after modification : ", employeeProjects)



    #tuple is immutable, so the following line would raise an error if uncommented
    #print("employee roles before modification : ", employeeRoles)
    #employeeRoles[0] = "Lead"  # This will raise a TypeError,

    #Ditionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
    employeeDetails = {
        "name": "Aravind Kumar",
        "age": 28,
        "salary": 50000.50,
        "department": "IT"
    }

    print("employee details : ", employeeDetails["name"])
    print("employee details : ", employeeDetails["age"])
    print("employee details : ", employeeDetails["salary"])
    print("employee details : ", employeeDetails["department"])

    employeeMobileNo = input("Enter employee mobile number : ")
    print("employee mobile number is : ", employeeMobileNo)


    empPinCode = int(input("Enter employee pin code : "))
    print("employee pin code is : ", empPinCode)
    



employeeInformation()