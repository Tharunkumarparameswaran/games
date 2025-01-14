Name1 = input("Enter the name1: ").lower()
Name2 = input("Enter the name2: ").lower()
name1 = Name1.replace(" ", "")
name2 = Name2.replace(" ", "")

for i in name1:
    for j in name2:
        if i==j:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(j, "", 1)
            break
count = len(name1+name2)

if count>0:
    list = ["FRIEND", "LOVER", "AFFECTION", "MARRIAGE", "ENEMIES", "SIBILINGS"]
    while len(list) > 1:
        c = count%len(list)
        delete_index = c-1
        if delete_index>=0:
            left = list[:delete_index]
            right = list[delete_index+1:]
            list = right + left 
        else:
            list = list[:len(list)-1]       
    print("The Relationship between ",Name1, " and ",Name2," is: ",list[0])
else:
    print(Name1," and ",Name2," are have same Characters, Please choose different names.")
