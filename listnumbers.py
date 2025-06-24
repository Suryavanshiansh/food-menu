numbers_list=[5,10,15,20,25]
print(numbers_list)
numbers_list.append(30)
print(numbers_list)
numbers_list.insert(0,0)
print(numbers_list)
numbers_list.remove(15)
print("Total numbers:",len(numbers_list))
for number in numbers_list:
    print("Number:", number/2)
print("Sum of numbers:", sum(numbers_list))
print("Largest number:", max(numbers_list))
print("Smallest number:", min(numbers_list))
numbers_list.sort(reverse=True)
print("Sorted Numbers in Descending Order:", numbers_list)
for numbers in numbers_list:
    print("Original Number", numbers, "Doubled Number:", numbers * 2)