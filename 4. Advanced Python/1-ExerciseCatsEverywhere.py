# Exercise Cats Everywhere

# Given the below class:


class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# SCROLL FOR ANSWERS

# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat("mycat1", 1)
cat2 = Cat("mycat2", 2)
cat3 = Cat("mycat3", 1)


# 2 Create a function that finds the oldest cat.
def find_oldest_cat(*args: Cat):
    return max(cat.age for cat in args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {find_oldest_cat(cat1, cat2, cat3)} years old.")


# region
# # Answers:
# # 1 Instantiate the Cat object with 3 cats.
# cat1 = Cat("cat1", 5)
# cat2 = Cat("Cat2", 7)
# cat3 = Cat("Cat3", 3)


# # 2 Create a function that finds the oldest cat.
# def oldest_cat(*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.".
# # x will be the oldest cat age by using the function in #2
# print(f"Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
# endregion
