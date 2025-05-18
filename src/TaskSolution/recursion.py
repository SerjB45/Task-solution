def recursion_sum():
    lst = initial_data()
    print('check value: ', sum(lst))
    
    def inner_fn(numbers):
        if numbers == []:
            return 0
        return numbers[0] + inner_fn(numbers[1:])
    
    print(inner_fn(lst))
      
    
def recursion_max():
    lst = initial_data()
    print('check value: ', max(lst))
        
    def inner_fn(numbers):
        if len(numbers) == 2:
            return numbers[0] if numbers[0] > numbers[1] else numbers[1]
        tmp_max = inner_fn(numbers[1:])
        return numbers[0] if numbers[0] > tmp_max else tmp_max
    
    print(inner_fn(lst))
    
    
        

def recursion_len():
    lst = initial_data()
    print('check value: ', len(lst))
    
    def inner_fn(numbers):
        if numbers == []:
            return 0
        return 1 + inner_fn(numbers[1:])  
    
    print(inner_fn(lst))

def initial_data():
    return [1, 3, 5, 45 , 4, 6, 2, 9, 3, 3, 10]         