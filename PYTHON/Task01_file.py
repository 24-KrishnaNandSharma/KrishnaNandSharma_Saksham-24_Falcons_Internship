#This is list of Name of Universities.
print("Top 10 Private Universities in India (NIRF 2024):")
Universities=["","Amrita Vishwa Vidyapeetham",
        "Manipal Academy of Higher Education",
        "Vellore Institute of Technology",
        "BITS Pilani",
        "Shiksha 'O' Anusandhan",
        "Thapar Institute of Engineering and Technology",
        "Amity University",
        "KIIT Bhubaneswar",
        "SRM Institute of Science and Technology",
        "Chandigarh University"]
#For print the name of Universities with numbering.
i=1
while i<=10:
    print(i,Universities[i])
    i+=1
#For input in order 1-10.    
University=int(input("Enter Number of your desired University 1-10:"))
#Condition for 1.
if University==1:
    print("University Name:",Universities[1])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["JEE","AEEE"]
        Exam=input("Enter enterance exam name(JEE,AEEE):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=60:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University")#1 is over
        
#Condition for 2.
if University==2:
    print("University Name:",Universities[2])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["MET"]
        Exam=input("Enter enterance exam name(MET):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=50:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #2 is over     
 
#Condition for 3.        
if University==3:
    print("University Name:",Universities[3])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["VITEEE"]
        Exam=input("Enter enterance exam name(VITEEE):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=60:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #3 is over
        
#Condition for 4.
if University==4:
    print("University Name:",Universities[4])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["BITSAT"]
        Exam=input("Enter enterance exam name(BITSAT):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=75:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #4 is over

#Condition for 5.
if University==5:
    print("University Name:",Universities[5])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["SAAT", "JEE Main"]
        Exam=input("Enter enterance exam name(SAAT, JEE Main):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=45:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #5 is over
        
#Condition for 6.
if University==6:
    print("University Name:",Universities[6])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["JEE Main"]
        Exam=input("Enter enterance exam name(JEE Main):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=60:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University")  #6 is over     
      
#Condition for 7.
if University==7:
    print("University Name:",Universities[7])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["Amity JEE", "JEE Main"]
        Exam=input("Enter enterance exam name(Amity JEE, JEE Main):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=60:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #7 is over
      
#Condition for 8.                
if University==8:
    print("University Name:",Universities[8])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["KIITEE"]
        Exam=input("Enter enterance exam name(KIITEE):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=60:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #8 is over

#Condition for 9.        
if University==9:
    print("University Name:",Universities[9])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["SRMJEEE", "JEE Main"]
        Exam=input("Enter enterance exam name(SRMJEEE, JEE Main):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=50:
                print("You are eligible for this University")
            else:
                print("You are not eligible for thisUniversity")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #9 is over       
        
#Condition for 10.
if University==10:
    print("University Name:",Universities[10])
    Marks_12=int(input("Enter your 12th percentage:"))
    if Marks_12>=75:
        Enterance_Exam_Name=["CUCET", "JEE Main"]
        Exam=input("Enter enterance exam name(CUCET, JEE Main):")
        if Exam in Enterance_Exam_Name:
            Enterance_Exam_Marks=int(input("Enter your enterance exam marks:"))
            if Enterance_Exam_Marks>=50:
                print("You are eligible for this University")
            else:
                print("You are not eligible for this University")        
        else:
            print("You are not eligible for this University")               
    else:
        print("You are not eligible for this University") #10 is over                
        
    
    
