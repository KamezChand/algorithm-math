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

max_v_1 = max(bug1)
max_i_1 = bug1.index(max_v_1)
max_v_2 = max(bug2)
max_i_2 = bug2.index(max_v_2)

if max_i_1 == max_i_2:
    bug1[max_i_1] = 0
    bug2[max_i_2] = 0
    sec_max_v_1 = max(bug1)
    sec_max_v_2 = max(bug2)
    print(n - max(max_v_1, max_v_2) - max(sec_max_v_1, sec_max_v_2))
else:
    print(n - max_v_1 - max_v_2)