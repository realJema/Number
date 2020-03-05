
# A python program to convert digits to letters 
# the number conversion is in english 
import datetime

def converter(value): 
    if(value == 0): return ''
    elif(value == 1): return 'one'
    elif(value == 2): return 'two'
    elif(value == 3): return 'three'
    elif(value == 4): return 'four'
    elif(value == 5): return 'five'
    elif(value == 6): return 'six'
    elif(value == 7): return 'seven'
    elif(value == 8): return 'eight'
    elif(value == 9): return 'nine'
    elif(value == 10): return 'ten'
    elif(value == 11): return 'eleven'
    elif(value == 12): return 'twelve'
    elif(value == 13): return 'thirteen'
    elif(value == 14): return 'fourteen'
    elif(value == 15): return 'fifteen'
    elif(value == 16): return 'sixteen'
    elif(value == 17): return 'seventeen'
    elif(value == 18): return 'eighteen'
    elif(value == 19): return 'nineteen'

    # deals with all the multiples of ten
    elif(value % 10 == 0) and (value < 100): 
        if(value == 20): return 'twenty'
        if(value == 30): return 'thirty'
        if(value == 40): return 'forty'
        if(value == 50): return 'fifty'
        if(value == 60): return 'sixty'
        if(value == 70): return 'seventy'
        if(value == 80): return 'eithy'
        if(value == 90): return 'ninety'
    
    # deals with all values in between multiples of ten
    elif(value > 20) and (value < 100): 
        first_digit = int(value/10) * 10
        last_digit = value % 10
        return str(converter(first_digit)) + ' ' + str(converter(last_digit))

    # deals with all hundreds
    elif(value > 100) and (value < 1000):
        first_digit = int(value/100)
        last_digits = value % 100
        last_digits_value=converter(last_digits)
        if(last_digits_value==''):
            return str(converter(first_digit)) + ' hundred ' + str(last_digits_value)
        else:
            return str(converter(first_digit)) + ' hundred and ' + str(last_digits_value)

    elif (value > 1000) and (value <1000000):
        first_digit = int(value/1000)
        last_digits = value % 1000
        return str(converter(first_digit)) + ' thousands ' + str(converter(last_digits))
    elif (value > 1000000) and (value <1000000000):
        first_digit = int(value/1000000)
        last_digits = value % 1000000
        return str(converter(first_digit)) + ' millions ' + str(converter(last_digits))
    elif (value > 1000000000) and (value <1000000000000):
        first_digit = int(value/1000000000)
        last_digits = value % 1000000000
        return str(converter(first_digit)) + ' billions ' + str(converter(last_digits))



    else: return 'invalid'


if __name__ == "__main__":
    # this section calls the function converter and returns the results
    user_input= int(input('Enter a number: '))
    print('Results: ', converter(user_input))
    # y=1
    # Start_time = datetime.datetime.now()
    # while (y<1000000):
    #     print(str(y) + ' ---> ' + converter(y))
    #     y += 1
    # End_time = datetime.datetime.now()
    # print('Start of program : ',Start_time)
    # print('End of program : ',End_time)

        