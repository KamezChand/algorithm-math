n = int(input())
nums = list(map(int, input().split()))

nums1 = nums[0::2]
nums2 = nums[1::2]

bug1 = [0] * 100001
bug2 = [0] * 100001

for num in nums1:
    bug1[num] += 1

for num in nums2:
    bug2[num] += 1
