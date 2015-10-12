#function definition for ciger_party
from _ast import Add
def ciger_party(num, is_weekend):
    if is_weekend:
        if num>=40:
            print("true")
            return True
        else:
            print("false")
            return False
    elif num>=40 and num<=60:
        print("true")
        return True
    else:
        print("false")
        return False

#calling function ciger_party
ciger_party(30, False)
ciger_party(50, False)
ciger_party(70, True)


#function definition caught_speeding
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed-5
    if speed <= 60:
        print(0)
        return 0
    elif speed>=61 and speed<=80:
        print(1)
        return 1
    elif speed > 81:
        print(2)
        return 2
    
    
#calling function caught_speeding
caught_speeding(60, False)
caught_speeding(85, False)
caught_speeding(65, True)


#defining function love6
def love6(a, b):
    sub = abs(a-b)
    add = a+b
    if (a==6 or b==6) or add==6 or sub == 6:
        print("true")
        return True
    else:
        print("false")
        return False



#calling function love6
love6(6, 4)
love6(4, 5)
love6(1, 5)
    
#defining function date_fashion
def date_fashion(you, date):
    if you <=2 or date <= 2:
        print(0)
        return 0
    elif you >=8 or date >= 8:
        print(2)
        return 2
    else:
        print(1)
        return 1  
    
#calling function date_fashion
date_fashion(5, 10)
date_fashion(5, 2)
date_fashion(5, 5) 


#defining function sorta_sum
def sorta_sum(a, b):
    add = a+b
    if add >=10 and add <=19:
        print(20)
        return 20
    else:
        print(add)
        return add
    
#calling function sorta_sum
sorta_sum(3, 4)
sorta_sum(9, 4)
sorta_sum(10, 11) 
    
#defining function in1to10
def in1to10(n, outside_mode):
    if outside_mode:
        if n<=1 or n>=10:
            print("true")
            return True
        else:
            print("false")
            return False
    elif n>=1 and n<=10:
        print("true")
        return True
    else:
        print("false")
        return False


#calling function in1to10
in1to10(5, False)
in1to10(11, False)
in1to10(11, True)
        
        
        
        
        
        
        
        
        
        
               
    
    
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    





        