def add(first_term, second_term):
    return first_term + second_term

#function to subtract number
def subtract(first_term, second_term):
    return first_term - second_term


#function to test math
def math_test():
    assert add(6,4)==10
    assert subtract(10,4)==6
    print ("Test completed Succesfully")

if __name__ == '__main__':
    math_test()


