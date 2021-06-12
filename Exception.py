def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num%i == 0 :
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisor(num))
    except ValueError:
        print("Error de valor inválido")

if __name__ == "__main__":
    run()
    
