name=[]
age=[]
clas=[]

while True:
    #input for name list
    print('Enter the nameof the student' + str(len(name)+1) + 'Or enter nothing to stop')
    Name= input()
        #name list concatenation
        #stopping the program if there is no input

    #input for age list 
    print('Enter the age of the student' + str(int(len(age)+1)) + 'Or enter nothing to stop')
    Age= input()
        
    print('Enter the class of the student' + str(int(len(clas)+1)) + 'Or enter nothing to stop')
    Clas= input()
    name=name+[Name]
    age=age+[Age]
    clas=clas+[Clas]

    if Name=='':
        break

    #creating a list to hold name,age and class in a single list(lidt in list)


studentprofile=[[name],[age],[clas]]

print('The profiles are:')

for studentprofile in studentprofile:
    print(''+str(studentprofile))



