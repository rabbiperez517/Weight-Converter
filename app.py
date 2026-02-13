

weight = int(input("Enter your weight: "))
weight_unit = input('(L)bs or (K)g: ')
if weight_unit == 'L':
    print(str(weight * 0.453592) + ' kilograms')
else:
    print(str(weight/0.453592) + ' pounds ')
