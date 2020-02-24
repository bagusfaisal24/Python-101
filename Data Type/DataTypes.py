x1 = int(20)  # int
x2 = float(20.5)  # float
x3 = complex(1j)  # complex
x4 = list(("apple", "mango", "banana"))  # list
x5 = tuple(("apple", "mango", "banana"))  # tuple
x6 = bool(0)
y = 35656222554887711
y1 = 2.35
print(x1), print(x2), print(x3), print(x4), print(x5), print(x6)
print(type(y))  # untuk mengetahui type data nya menggunaka type
print(type(y1))
print(type(x6))
print(type(x5))
print(type(x4))

## Casting data type
print(int(1))
print(float(2.8))
print(str(2.8) + str(2.8))

## boolean logical
a = 300
b = 200

if a > b:
    print("true")
else:
    print("false")

##type set
thisset = {"Value 1", "Value 2"}
print(thisset)
##type list
list = ("value 1", "value 2")
print(list)

## Python Dictionaries
thisDict = {
    "key 1": "value 1",
    "key 2": "value 2"
}
print(thisDict)

## Accessing key in dictionaries
print(thisDict["key 1"])

## apend data python
data = [1, 2, 3, 4, 5]
newArray = [6, 7, 8]
data.append(newArray)
newArray.append(9)
print(data)

## extend data in python
data1 = [1,2,3,4]
data2 = [4,5,6]
data1.extend(data2)
print(newArray)
print(data1)

