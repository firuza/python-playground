def factorial(number):
    if number > 0:
        answer = 1
        for i in range(1, number+1):
            answer = answer * i
        print(answer)
        return(answer)
    print("Cannot compute factorial of a negative number")
    return(None)
