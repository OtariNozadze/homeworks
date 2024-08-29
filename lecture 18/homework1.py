def decoraotor(func):
    def positive_or_negative(num):
        if num < 0:
            raise ValueError("The Number Must Be Positive")
        result = func(num)
        print(result)
        return result
    return positive_or_negative
        
@decoraotor
def return_num(num):
    return num
return_num(10)
return_num(-6)
