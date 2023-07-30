# list
# add and remove elements of list
people = ["John", 'Jack', 'Tom']
people.append("Ann")
people += ['Olga']
people.insert(2, 'Sam')
people += 'Iren'
print(people)

people.remove('e')
if 'n' in people:
  i = people.index('n')
  del people[i]
people += 'a'
print(people)

# sort list
sort = sorted(people) #not change list
print(sort)

people.sort() # change source list
print(people)

print("max:", max(people))
print("min:", min(people))

rev = reversed(people)  #not change list
print("reversed:", people)

people.reverse()  # change source list
print("reverse:", people)

people[::-1]
print("reverse using slising:", people)
