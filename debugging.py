def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num%i == 0 :
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un número: "))
    print(divisor(num))

if __name__ == "__main__":
    run()
