def revert_number():
    numbers = [100, 201, 48, 4895]
    
    def inner_fn(number: int) -> int:
        return int(str(number)[::-1])
    
    def inner_fn_2(number: int) -> int:
        return int(''.join(list(reversed(str(number)))))
    
    for number in numbers:    
        print(inner_fn(number))
        print(inner_fn_2(number))
        
        print('-' * 15)

def prime_number():
    
    numbers = [1, 2, 3, 4, 5, 100, 201, 48, 4895]
    
    def inner_fn(number: int) ->bool:
        
        for i in range(2, number):
            if number % i == 0:
                return False
            if i > number // 2:
                break
        return True   
    
    for number in numbers:
        print(f'{number} is prime: {inner_fn(number)}')     
            
            
def fibonacci():
    
    length = 14
    
    def get_all_order_iteration(length):
        lst = [0, 1]
        for item, index in enumerate(range(2, length + 1)):
            lst.append(lst[index-2] + lst[index-1])
        return lst
    
    def calculate_next(lst, length):
        if len(lst) < length:
            lst.append(lst[-2] + lst[-1])
            return calculate_next(lst, length)
        else:
            return lst
    
    def get_all_order_recursion(length):
        lst = [0, 1]
        return calculate_next(lst, length + 1)
    
    def specific_number_recursion(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return specific_number_recursion(n - 1) + specific_number_recursion(n - 2)
        
    def specific_number_iterative(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
    print(get_all_order_iteration(length))    
    print(get_all_order_recursion(length))    
    print(specific_number_recursion(length))    
    print(specific_number_iterative(length))    

def max_value():
    def inner_fn(*args):
        maximum = args[0]
        for i in args:
            if i > maximum:
                maximum = i
                
        return maximum        
    
    print(inner_fn(1, 5, 7))       
    print(inner_fn(1, 35, 7, 10))
    lst = [1, 35, 7, 10]       
    print(inner_fn(*lst))       
    print(inner_fn(6))

    
def swap():
    def inner_fn(a, b):
        a, b = b, a
        return a, b
    a = 1
    b = 5
    a, b = inner_fn(a, b)
    print(a, b)           

def factorize():
   
    def inner_fn(number):
        left_portion = number
        factors = []
        index = 2
        while left_portion != 1:
            while left_portion % index == 0:
                factors.append(index)
                left_portion = left_portion / index
            index += 1

        return factors
    
    print(inner_fn(25))
    print(inner_fn(52))
    print(inner_fn(63))

            