#Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].

data = int(input("Enter a number : "))

#print(data // 1000)

charArray = []
charArray.extend(str(data))

print (charArray)

#def placeVal(data):



