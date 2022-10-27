class Student:
    
    #Constructor init (it will over ride the whole function.)It takes in self then other sattributes you want to put in
    # like name,age,course e.t.c
    def __init__(self,name,course,access_no) :
        print("I am alive")
        self.name=name
        self.course=course
        self.access_no=access_no
    
    #Methods take in self in the parameters
    def eat(self):
        print("I am eating")
     
      #Methods take in self in the parameters   
    def drink(self):
        print("I am drinking")
        
    #Methods take in self in the parameters     
    def sleep(self):
        print("I am sleeping")
    
    #Methods take in self in the parameters     
    def wake(self):
        print("I am waking up")

    #This functions prints the data on the line (Second Last part)   
    def __str__(self):
         return f"Hey this is {self.name} and my course is {self.course} and my access number {self.access_no}"
        
 #Objects being created of student type.       
jim   = Student("Desire","BSIT","A92401")

#Printing specific data for Jim
print(jim)


#Print out the names after calling the str function(Last part)
jimmy = Student("Mambo","BSCS","A92341")
print(jimmy)
Desire = Student("Desire","BSIT","A92401")
print(Desire)
       
            

        
        
        
        
    