def iq_test(numbers):
    nums = numbers.split()
    odd = 0
    even = 0
    i = 0
    while i<len(nums):
        if nums[i] % 2 == 0:
            even = even + 1
            i = i + 1
        else:
            odd = odd + 1
            i = i + 1

    if even == 1:
        return even
