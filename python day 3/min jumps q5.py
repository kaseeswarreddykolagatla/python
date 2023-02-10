def minJumps(nums):
    jumps = 0
    current_jump_end = 0
    far = 0
    for i in range(len(nums) -1):
        far = max(far, i + nums[i])
        if i == current_jump_end:
            jumps += 1
            current_jump_end = far
        return jumps

nums1=[1, 3, 5, 8, 9, 2, 6, 7, 6, 7, 6, 8, 9]
print(minJumps(nums1))
