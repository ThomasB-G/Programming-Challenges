def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
if __name__ == "__main__":
    nums = list(map(int, input("Please input a list of numbers separated by spaces: ").split()))
    target = int(input("Please input a target number: "))
    result = twoSum(nums, target)
    print(result)