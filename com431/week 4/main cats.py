from cat import Cat

cat1 = Cat("Binnie", 1)
cat2 = Cat("Clyde", 2)
cat3 = Cat("old tom", 6)
cat1.eat()
cat2.eat()
cat3.eat()
cat1.walk()
cat2.walk()
cat3.walk()

print(cat1.getDetails())
print(cat2.getDetails())
print(cat3.getDetails())