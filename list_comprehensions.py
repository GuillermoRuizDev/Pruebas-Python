def run():
    """ squares = []
    for i in range(1,101):
        if i%3 !=0 :
            squares.append(i**2)
     """
    #squares = [i**2 for i in range(1,101) if i%3 != 0]
    squares = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0 ]
    print(squares)

def run2():
    """ my_dict = {}

    for i in range(1,101):
        my_dict[i]=i**3
     """
    #my_dict = {i:i**3 for i in range(1,101) if i%3 !=0}
    my_dict = {i:i**(1/2) for i in range(1,1001)}
    print(my_dict)

        


if __name__ == "__main__":
    run2()