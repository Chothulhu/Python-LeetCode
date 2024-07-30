def productExceptSelf(nums):
    
    nums_length = len(nums)
    answer = [1] * len(nums)
    
    for i in range(1, nums_length):
        answer[i] = answer[i-1] * nums[i-1]
        print(answer)
        
    multiplier = 1
    for i in range(nums_length-1, -1, -1):
        answer[i] *= multiplier
        multiplier *= nums[i]
         
    return answer