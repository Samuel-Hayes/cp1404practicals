

print('Hello World')


nums1 = [1, -5, 2, 0, 4, 2, -3]
nums2 = [1, -5, 2, 4, 4, 2, 7]
result = 0
j = 0
while j < len(nums1):
    if nums1[j] != nums2[j]:
        result = result + 1
    j = j + 1
print(result)

x = 5
for i in range(x):
    x = x + i
    print(x, end=" ")

a = 5
b = 10
c = 0.5

a == b * c or c * 10 >= a
