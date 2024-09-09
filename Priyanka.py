list1 =[]
names = input('Enter Names:')
while names!= 'Exit':
    list1.append(names)
    names = input('Enter Names')
    print(list1)
n = input ('Do you want to remove an element from the list?: Y or N').upper()
if n == 'Y':
    rn = input('which name would you like to remove?')
    if rn in list1:
        list1.remove(rn)
    else:
        print('Nope! The name you entered is not in the list.')
    else:
    print('Have a nice day!')
    print('The updated list is:',list1)


