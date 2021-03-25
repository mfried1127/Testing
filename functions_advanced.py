def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount



# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ',' + first_name + " " + last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


# Write your dog_years function here:
def dog_years(name, age):
  return name+", you are "+ str(age * 7) +" years old in dog years "

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 2))
# should print "Baby, you are 0 years old in dog years"


# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth
  
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
