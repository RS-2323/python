# binary to dicimal

binaryValue = input("enter your binary value >")

lastDigit = binaryValue % 10
remainedDigit = binaryValue/10

secLastDigit = remainedDigit % 10
remainedDigit = remainedDigit/10

secDigit = remainedDigit % 10
remainedDigit = remainedDigit/10

firstDigit = remainedDigit % 10
remainedDigit = remainedDigit/10

decimalValue = lastDigit*1 + secLastDigit*2 + secDigit*4 + firstDigit*8

print("dicimalValue:")

print(decimalValue)



