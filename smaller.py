def allSmaller(nums):
    lis = []
    # nums.sort()
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        lis.append(count)
    # return lis
    res = dict(map(lambda x, y: (x, y), nums, lis))
    # res = {}
    # for key in nums:
    #     for val in lis:
    #         res[key] = val
    #         lis.remove(val)
    #         break
    return res


# ctrl +/ to comment multiple in Python

print(allSmaller([8, 4, 5, 2, 1]))
