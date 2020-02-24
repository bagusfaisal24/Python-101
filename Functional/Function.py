def myFunc():
    print("hellow world")


myFunc()


def FuncAddMe(a, b):
    print(a + b)


FuncAddMe(5, 6)


def listFunc(listNumber):
    for i in listNumber:
        print(i)


listFunc([1, 2, 3, 4, 5])

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
