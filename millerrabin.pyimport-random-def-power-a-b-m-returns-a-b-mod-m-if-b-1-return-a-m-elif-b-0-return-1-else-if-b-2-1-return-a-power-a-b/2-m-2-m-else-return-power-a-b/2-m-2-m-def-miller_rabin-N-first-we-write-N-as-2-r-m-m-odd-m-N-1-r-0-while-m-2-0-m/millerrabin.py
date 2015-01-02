import random

def power(a,b,m):			#returns a^b mod m
	if b==1:
		return a%m
	elif b==0:
		return 1
	else:
		if b%2==1:
			return (a*(power(a,b/2,m)**2))%m
		else:
			return (power(a,b/2,m)**2)%m


def miller_rabin(N):
	#first we write N as 2^r*m, m odd
	m = N-1
	r = 0
	while m%2==0:
		m /= 2
		r += 1
	#then, we choose a random integer modulo N
	x = random.randint(2, N-1)
	#compute the odd power modulo N
	X = power(x,m,N)
	print "The random value chosen is", x, "and the large odd power is", X
	#vector that will contain the repeated squaring of the odd power
	powers_vector = []
	#a boolean that will tell us whether or not we hit -1 at some point
	isneg1 = False
	#start squaring until we hit the (N-1)st power
	for i in range(r+1):
		powers_vector.append(X)
		if X==N-1:
			isneg1 = True
		#here we square the current power
		X = (X**2)%N
	print powers_vector
	if powers_vector[0]==1:
		return True
	else:
		return isneg1

def main():
	N = input("What's the value of N? ")
	n = input("How many times are you applying the test? ")
	isprime = True
	for i in range(n):
		if not miller_rabin(N):
			print N, "is not prime."
			isprime = False
			break
	if isprime:
		print "It is quite possible that", N, "is prime."




if __name__ == "__main__":
    main()
