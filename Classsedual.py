print("Enter routine timing of Day")
print("Manual of program, First of all enter the day and time ")
day=input("Enter Day :- ")
match day:
    case 'Monday' :
        time=int(input("Enter timeing :- "))
        if(time==10):
            print("C.N.D.C 6th Semester in Electronic Branch")
        elif(time==11 or time==12):
            print("No Class any Branch")    
        elif(time==1 or time==2):
            print("Python program Lab civil Engering 2th Semester")
        else:
            print("No Class")
    case 'Tuesday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("C.N.D.C 6th Semester in Electronic Branch")
        elif(time==11 or time==12):
            print("Data Structure Algrorithem in 4th Semester")
        elif(time==2):
            print("Python Programing in 4th Semster")
        elif(time==3 or time==4):
            print("Python program Lab civil Engering 2th Semester")
        else:
            print("Rest and personal work")    
    
    case 'Wednesday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("C.N.D.C 6th Semester in Electronic Branch")
        elif(time==11):
            print("Python program Lab civil Engering 2th Semeste")
        elif(time==12 or time==1.00):
            print("Lunch")
        elif(time==2):
            print("Data Structure Algrorithem in 4th Semester")
        elif(time==3 or time==4):
            print("Python program Lab Computer Engneering 4th Semest")
        else:
            print("No Routine")

    case 'Thrusday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("Data Structure Algrorithem in 4th Semester")
        elif(time==11):
            print("Python program Computer Science & Engering 4th Semester")
        elif(time==2):
            print("python programming 2th semester civil branch")
        elif(time==3 or time==4):
            print("Data Structure Algrorithem Lab in 4th Semester")
        else:
            print("Rest Time") 
    case 'Friday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("No Class")
        elif(time==11 or time==12):
            print("Data Structure Algrorithem Lab in 4th Semester")
        elif(time==1 or time==2):
            print("python programming 2th semester civil branch")
        elif(time==3 or time==4):
            print("python programming 2th semester civil branch(11)")
        else:
            print("Rest Time")

    case 'Saturday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("Python program Lab Computer Science & Engering 4th Semester")
        elif(time==11 or time==12):
            print("Python program Lab Computer Science & Engering 4th Semester")
        elif(time==1 or time==2):
            print("C.N.D.C 6th Semester in Electronic Branch")
        elif(time==3 or time==4):
            print("Rest Time")
        else:
            print("REST TIME")
    case 'Sunday' :
        time=int(input("Enter timing :- "))
        if(time==10):
            print("FULL Time REST ") 
        else:
            print("Invalide Day & Timeing")
    


        
            