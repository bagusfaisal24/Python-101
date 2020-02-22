## mencetak kata i love python
### While Loop
i = 0
while (i < 5):
    print("I Love Python Versi While")
    i += 1

for i in range(0, 5):
    print("I Love Python Versi For")

list = ("List 1", "List 2", "List 3")
for x in list:
    if x == "List 1" or x == "List 3":
        print(x)

i = 1
while True:
    print("I Love Python Versi Do While")
    i += 1
    if i > 5:
        break
