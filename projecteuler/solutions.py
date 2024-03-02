from pathlib import Path
##### Question 1 multiples of 3 or 5####
# sum1 = 0
# sum = [n for n in range(1000) if (n % 3 == 0) + (n % 5 == 0)]
# for n in range(1000):
#     if n % 3 == 0 or n % 5 == 0:
#         sum1 += n
# print(sum1)

n = 1
n2 = n3 = n4 = 0
numbers = ()
for n in numbers in range(100):
    if n + n2 != 0:
        n3 = n.append(1) + n
        print(n3)

# from car import Car

# car_1 = Car("lexus", "gx460", 2019, "black")
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.drive()
# car_1.stop()


mul_3 = [i for i in range(20) if i % 3 == 0]
mul_5 = [i for i in range(100) if i % 5 == 0]
s1 = s2 = s3 = 0
for i in range(10):
    if i % 3 == 0 and i % 5 == 0:
        s1 += i
for i in range(10):
    if i % 5 == 0:
        s2 += i
for i in range(0, 10, 3 * 5):
    s3 += i
suma = (s1 + s2)
# print(s3)
# print(suma)
# print(s1)
# print(s2)
# print(current)

# print(mul_3 + mul_5)

# path = Path("repos")

# paths = [p for p in path.iterdir()]
# print(paths)

# output = [x % 3 for x in range(10) if x == 0]
# input = [x % 3 for x in output]
# numbers = []

# for x in output:
#     print(output)
