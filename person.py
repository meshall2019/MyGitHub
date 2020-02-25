x_=input(('أدخل الرقم الأول :'))
y_=input(('أدخل الرقم الثاني :'))
x=int(x_)
y=int(y_)


print("جمع")
print("طرح")
print("قسمة")
print("ضرب")
z=input(str('أدخل العملية: '))



if z == "جمع":
    print(x+y)

elif  z=="طرح":

    print(x-y)
elif z=="قسمة":

    print(x/y)
elif z=="ضرب":
    print(x*y)
else:
    print('أدخل العملية الصحيحة')

