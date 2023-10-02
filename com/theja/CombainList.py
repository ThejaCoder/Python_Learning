#Write a function that combines two lists by alternatingly taking elements,
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

#Function to Combine list
def combineList(l1, l2):
    ans = []
    for i in range (0,len(l1)):
        ans.append(l1[i])
        ans.append(l2[i])

#to print
    print(ans)

#Declare list
lst1 = ["a","b","c"]
lst2 = ["1","2","3"]

#Call the function
combineList(lst1,lst2)