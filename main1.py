num = int(input("Enter the number : "))
length = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp = temp // 10

print("Number is {} sum is {}".format(num, sum))
if sum == num:
    print("Is an Armstrong number")
else:
    print("Is not an Armstrong number")