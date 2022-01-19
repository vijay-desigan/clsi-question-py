
jad = "How can mirrors be real if our eyes aren't real"
jad2=""
print(jad)
for i in range(len(jad)):
    if i==0:
        jad2+=jad[i]
    else:
        if jad[i-1]==" ":
            jad2+=jad[i].upper()
        else :
            jad2+=jad[i]
print( jad2)
