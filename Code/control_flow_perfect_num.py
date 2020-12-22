# This is my code!
# It's purpose is to demonstrate how a more complex loop can be used in both the main function and a function
# called is_perfect() that calculates all of natural numbers that are equal to the sum of their divisors

def is_perfect(n):
    perfect = True
    i = 1
    sum = 0

    while perfect and i < n:
        if n % i == 0:
            sum += i
            if sum > n:
                perfect = False
        i += 1
    if sum != n:
        perfect = False
    return perfect

def main():
    MAX = 500
    for i in range(1,MAX + 1):
        if is_perfect(i):
            print("%d " %i)

if __name__ == "__main__":
    main()
