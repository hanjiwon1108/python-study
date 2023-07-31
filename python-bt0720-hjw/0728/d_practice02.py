### 리스트 메소드 복습 ###

numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

fruits = ['apple', 'orange', 'grape']
fruits.insert(1, 'banana')
print(fruits)

numbers = [1, 2, 3, 4, 5]
removerd_item = numbers.pop()
print(removerd_item)
print(numbers)