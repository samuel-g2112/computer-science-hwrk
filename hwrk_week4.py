numList = [4, 19, 20, 21, 41, 48, 56, 58, 61, 99, 131, 136, 145, 148, 152, 183, 185, 187, 188, 193, 205, 208, 231, 241, 302, 305, 320, 327, 335, 340, 341, 350, 354, 358, 370, 380, 392, 412, 414, 430, 439, 446, 449, 450, 456, 460, 472, 494, 495, 504, 510, 526, 531, 535, 542, 552, 577, 580, 595, 599, 602, 612, 615, 625, 653, 654, 671, 682, 702, 705, 744, 753, 755, 760, 767, 794, 802, 806, 807, 841, 870, 875, 899, 900, 901, 903, 905, 910, 911, 918, 919, 920, 926, 927, 933, 942, 965, 966, 968, 990]

def selectionsort (mylist):
    n = len(mylist) #set n to the length of the list
    for i in range(n-1): #repeats for i=0 to i=last index
        min_index = i #set min_index to the loop value
        for j in range(i+1, n): #from the value after min_value to the length of the list
            if mylist[j] < mylist[min_index]: #if the value after min_index is higher:
                min_index = j #set min to the lowr value
        min_value = mylist.pop(min_index) #removes smaller number
        mylist.insert(i, min_value) #put the smaller number in th i'th position of the list

    print(mylist)

def selectionsortswap(mylist):
    n = len(mylist) #set n to the length of the list
    for i in range(n): #i loops n times
        min_index = i #min_index is set the first value of the unsorted section
    for j in range(i+1, n): #from the value after min_value to the length of the list
        if mylist[j] < mylist[min_index]: #if the value after min_index is higher:
            min_index = j #set min to the lowr value
    mylist[i], mylist[min_index] = mylist[min_index], mylist[i] #swap first value of the unsorted section with the smallest value.

    print(mylist)

selectionsort(numList)
selectionsortswap(numList)
