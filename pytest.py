#CODINGBAT LOGIC 1 PROBLEMS

#function definition for ciger_party
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
        

#defining function squirrel_play
def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >=60 and temp <=100:
            print("true")
            return True
        else:
            print("false")
            return False
    elif temp >= 60 and temp <=90:
        print("true")
        return True
    else:
        print("false")
        return False
        
        
#calling function squirrel_play
squirrel_play(70, False)
squirrel_play(95, False)
squirrel_play(95, True)        
        
        
#defining function alarm_clock
def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            print("off")
            return "off"
        else:
            print("10:00")
            return "10:00"
    elif day == 0 or day == 6:
        print("10:00")
        return "10:00"
    else:
        print("7:00")
        return "7:00"        
        
        
        
#calling function alarm_clock       
alarm_clock(1, False)
alarm_clock(5, False)
alarm_clock(0, False)
        
        
#defining function near_ten
def near_ten(num):
    if num%10 == 1 or num%10 == 2 or num%10 == 8 or num%10 == 9 or num%10 == 0:
        print("true")
        return True
    else:
        print("false")
        return False
    
    
#calling function near_ten    
near_ten(12)
near_ten(17)
near_ten(19)
    
            
#CODINGBAT WARMUP 1

#defining function sleep_in
def sleep_in(weekday, vacation):
    if vacation or not weekday:
        print("true")
        return True
    else:
        print("false")
        return False
                 
    
    
#calling function sleep_in    
sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)     
    
#defining function diff21
def diff21(n):
    if n> 21:
        return (abs(n-21)*2)
    else:
        return abs(n-21)

    
#defining function near   
    
    
    
    
    
    
        
       
    
    
    
    
    
    
    
    
    
    





        