a, b, c= map(int, input().split())

if(a>=b and b>=c): print("{}\n{}\n{}\n".format(c,b,a))
elif(a>=b and c>=b and a>=c): print("{}\n{}\n{}\n".format(b,c,a))
elif(b>=a and a>=c): print("{}\n{}\n{}\n".format(c,a,b))
elif(b>=a and c>=a and b>=c): print("{}\n{}\n{}\n".format(a,c,b))
elif(c>=a and a>=b): print("{}\n{}\n{}\n".format(b,a,c))
elif(c>=a and b>=a and c>=b): print("{}\n{}\n{}\n".format(a,b,c))

print("{}\n{}\n{}".format(a,b,c))