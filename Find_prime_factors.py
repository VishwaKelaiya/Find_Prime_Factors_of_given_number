def find_prime_factor(num):
    if not check_prime(num):
        for i in range(2, num):
            if check_prime(i) and num%i == 0:
                print(i, end = ' ')
    else:
        print('Number is itself prime and does not have factors\n')



def check_prime(num):

    for i in range(2,num):
        if num%i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Enter number to find its prime factors\n'))
    find_prime_factor(n)