#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count =10
    while count >0:
        print(count )
        count -=1
        
    print("Happy New Year!")

# happy_new_year()

def square_integers(int_list):
    new_array = [pow(int_list[i], 2) for i in range(len(int_list))]
    return new_array
          
print(square_integers([1,2,3,4,5]))



def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i %3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i %3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i %3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i) 
fizzbuzz()
