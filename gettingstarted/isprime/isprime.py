def isPrime(n):
    #  Check if N is less than or equal to 1
    #     if so, answer no
    #  Count from 2 to N (exclusive), call each number i
    #     Check if N mod i is 0
    #         If so, answer no
    #  Answer yes
    pass  # this is just a placeholder until we write the function


assert not isPrime(0)
assert not isPrime(1)
assert isPrime(2)
assert isPrime(3)
assert not isPrime(4)
assert isPrime(101)
assert not isPrime(13*17)
