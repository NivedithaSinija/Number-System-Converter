print("Data Converter")
print("1. Binary to Decimal")
print("2. Decimal to Binary")
print("3. Decimal to Octal")
print("4. Decimal to Hexadecimal")
print("5. Binary to Octal")
print("6. Binary to Hexadecimal")
print("7. Octal to Binary")
print("8. Octal to Decimal")
print("9. Exit")
c=int(input("Enter choice:"))
while c!=9:
    if c==1:
        binary_num=int(input("Enter binary number:"))
        decimal_num=0
        a=1
        length=len(str(binary_num))
        for i in range(length):
            reminder=binary_num%10
            decimal_num=decimal_num+(reminder*a)
            a=a*2
            binary_num=int(binary_num//10)
        print(decimal_num)
    elif c==2:
        decimal_num=int(input("Enter decimal number:"))
        binary_num=''
        while decimal_num!=0:
            d=decimal_num%2
            i=str(d)
            binary_num+=i
            decimal_num=decimal_num//2
        binarynum=binary_num[-1:-len(binary_num)-1:-1]
        print(binarynum)
    elif c==3:
        decimal_num=int(input("Enter decimal number:"))
        octal_num=''
        while decimal_num>0:
            d=decimal_num%8
            i=str(d)
            octal_num+=i
            decimal_num=decimal_num//8
        octalnum=octal_num[-1:-len(octal_num)-1:-1]
        print(octalnum)
    elif c==4:
        decimal_num=int(input("Enter decimal number:"))
        hexadecimal=''
        while decimal_num!=0:
            d=decimal_num%16
            i=str(d)
            if d>9:
                if d==10:
                    hexadecimal+='A'
                elif d==11:
                    hexadecimal+='B'
                elif d==12:
                    hexadecimal+='C'
                elif d==13:
                    hexadecimal+='D'
                elif d==14:
                    hexadecimal+='E'
                elif d==15:
                    hexadecimal+='F'
            else:
                hexadecimal+=i
            decimal_num=decimal_num//16
        hexa_decimal=hexadecimal[-1:-len(hexadecimal)-1:-1]
        print(hexa_decimal)
    elif c==5:
        binary_num=int(input("Enter binary number:"))
        octal_num=''
        binary_str=str(binary_num)
        binary=binary_str[-1:-len(binary_str)-1:-1]
        for i in range(0,len(binary),3):
            a=binary[i:i+3]
            if len(a)!=3:
                if len(a)==1:
                    a+='00'
                elif len(a)==2:
                    a+='0'
            a1=a[-1:-4:-1]
            if a1=='000':
                octal_num+='0'
            elif a1=='001':
                octal_num+='1'
            elif a1=='010':
                octal_num+='2'
            elif a1=='011':
                octal_num+='3'
            elif a1=='100':
                octal_num+='4'
            elif a1=='101':
                octal_num+='5'
            elif a1=='110':
                octal_num+='6'
            elif a1=='111':
                octal_num+='7'
        octalnum=octal_num[-1:-len(octal_num)-1:-1]
        print(octalnum)
    elif c==6:
        binary_num=int(input("Enter binary number:"))
        hexadecimal=''
        binary_str=str(binary_num)
        binary=binary_str[-1:-len(binary_str)-1:-1]
        for i in range(0,len(binary),4):
            a=binary[i:i+4]
            if len(a)!=4:
                if len(a)==1:
                    a+='000'
                elif len(a)==2:
                    a+='00'
                elif len(a)==3:
                    a+='0'
            a1=a[-1:-5:-1]
            if a1=='0000':
                hexadecimal+='0'
            elif a1=='0001':
                hexadecimal+='1'
            elif a1=='0010':
                hexadecimal+='2'
            elif a1=='0011':
                hexadecimal+='3'
            elif a1=='0100':
                hexadecimal+='4'
            elif a1=='0101':
                hexadecimal+='5'
            elif a1=='0110':
                hexadecimal+='6'
            elif a1=='0111':
                hexadecimal+='7'
            elif a1=='1000':
                hexadecimal+='8'
            elif a1=='1001':
                hexadecimal+='9'
            elif a1=='1010':
                hexadecimal+='A'
            elif a1=='1011':
                hexadecimal+='B'
            elif a1=='1100':
                hexadecimal+='C'
            elif a1=='1101':
                hexadecimal+='D'
            elif a1=='1110':
                hexadecimal+='E'
            elif a1=='1111':
                hexadecimal+='F'
        hexadecimal_num=hexadecimal[-1:-len(hexadecimal)-1:-1]
        print(hexadecimal_num)
    elif c==7:
        octal_num=int(input("Enter octal number:"))
        binary_num=''
        octal_str=str(octal_num)
        for i in octal_str:
            if i=='0':
                binary_num+='000'
            elif i=='1':
                binary_num+='001'
            elif i=='2':
                binary_num+='010'
            elif i=='3':
                binary_num+='011'
            elif i=='4':
                binary_num+='100'
            elif i=='5':
                binary_num+='101'
            elif i=='6':
                binary_num+='110'
            elif i=='7':
                binary_num+='111'
        print(binary_num)
    elif c==8:
        octal_num=int(input("Enter octal number:"))
        decimal_num=0
        a=1
        length=len(str(octal_num))
        for i in range(length):
            reminder=octal_num%10
            decimal_num=decimal_num+(reminder*a)
            a=a*8
            octal_num=octal_num//10
        print(decimal_num)
    c=int(input("Enter choice:"))
print("Exitting")
