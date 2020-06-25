from SortingAlgorithms.bubble_sort import bubble_sort
from SortingAlgorithms.insertion_sort import insertion_sort
from SortingAlgorithms.merge_sort import merge_sort

file = open("test_array/array.txt", "r")
array = [int(x) for x in file.read()[1:-1].split(", ")]
file.close()
file = open("test_array/sorted.txt", "r")
sorted_array = [int(x) for x in file.read()[1:-1].split(", ")]
file.close()

print("BUBBLE SORT:")
if bubble_sort(array.copy()) == sorted_array:
    print("SUCCESS!")
else:
    print("FAILURE!")
    print(bubble_sort(array.copy()))

print("INSERTION SORT:")
if insertion_sort(array.copy()) == sorted_array:
    print("SUCCESS!")
else:
    print("FAILURE!")
    print(insertion_sort(array.copy()))


def quick_sort(array_to_sort):
    pass


print("QUICK SORT:")
if quick_sort(array.copy()) == sorted_array:
    print("SUCCESS!")
else:
    print("FAILURE!")
    print(quick_sort(array.copy()))


print("MERGE SORT:")
if merge_sort(array.copy()) == sorted_array:
    print("SUCCESS!")
else:
    print("FAILURE!")
    print(merge_sort(array.copy()))
