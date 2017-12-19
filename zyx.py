def test1(number):
	if number <=0:
		return None
	elif number == 1:	
		print number
	else: 
		a= range(2,number)
		for n in a[::-1]:
#			print n
			x=divmod(number,n)
			if (x[1]>0) :
				a.remove(n)	
	if len(a) > 0:
		return a
	else:
		print '%d is Perime' %(number)
			


def m(n):
    ret = []
    while n > 1:
    for i in range(n-1):
        k = i+2
        if n % k == 0:
            ret.append(k)
            n = int(n / k)
            break
    print(ret)

