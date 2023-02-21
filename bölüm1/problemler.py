
# problem1
value1 = int(input("lütfen değer giriniz"))
value2 = int(input("lütfen değer giriniz"))
value3 = float(input("lütfen değer giriniz"))

output1 = int(value3 * value2 * value1)
print("answer = {} " .format(output1))


#problem2
length = float(input("please enter your length"))
weight = int(input("please enter your weight"))

body_mass_index = weight / (length**2)
print(body_mass_index)


#problem3
value1 = int(input("please write your number"))
value2 = int(input("please write your number"))
print( "value1 = {}, value2 = {}" .format(value1,value2) )

value1,value2 =value2,value1
print( "value1 = {}, value2 = {}" .format(value1,value2) )


#problem4
name = input("please write your name:")
surname = input("please write your last name:")

print("name =  {}\nsurname = {}" .format(name,surname))