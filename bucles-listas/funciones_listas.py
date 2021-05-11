array = ["Lunes", "Martes", 1, 2, 1, [3, 4, 5], True]
array2 = ["Lunes"]
array3 = array+array2
print(len(array))
array.append(66)
print(len(array))
array.insert(1, 88)
print(array)
array.extend([1, 88, True, False])
print(array)
print(array3)


print("Lunes" in array)
print(array.index("Martes"))
print(array)
print(array.count(66))
array.remove("Lunes")
print(array)
array.reverse()
print(array)
array.clear()
print(array)

arr = [33, 1, 2, 3, 4]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
