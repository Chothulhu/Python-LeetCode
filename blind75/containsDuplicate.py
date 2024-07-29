def containsDuplicate(numbers):
    hash_set = set()
    for num in numbers:
        if num in hash_set:
            return True
        else: 
            hash_set.add(num)
    return False
    
numbers = []
print(containsDuplicate(numbers))