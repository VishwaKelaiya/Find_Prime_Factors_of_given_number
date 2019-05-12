l1 = [2]

def find_next_prime():
    i=1
    while(True):
        if check_prime(l1[-1]+i):
            print(l1[-1]+i,end = ' ')
            l1.append(l1[-1]+i)
            i += 1
            break
        else:
            i += 1
            continue


def check_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


if __name__ == '__main__':

    while(True):
        ask = input('\nDo you want to find next prime number? y or n\n')
        if ask == 'y':
            find_next_prime()
        else:
            print('Ok Thank you!\n')
            break


