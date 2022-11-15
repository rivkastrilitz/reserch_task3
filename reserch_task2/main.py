import function
import re
from doctest import testmod

from List import List


################# Q1 ######################

# todo recive a file to function
def check_mail():
    valid_mail = []
    invalid_mail = []
    try:
        with open('mails.txt', 'r') as f:
            lines = f.readlines()
            regex='([A-Za-z0-9]+[.-_%+-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

            for mail_line in lines:
                mail_line = mail_line.strip('\n')
                mail_line = mail_line.strip(' ')
                if re.fullmatch(regex, mail_line):
                    valid_mail.append(mail_line)
                else:
                    invalid_mail.append(mail_line)
        print("valid mails", valid_mail)
        print("invalid mails", invalid_mail)

        f.close()
    except:
        pass


################# Q2 ######################
prev_var = {}

def lastcall(func: function):
    def wrapper(*args, **kwargs):
        '''
                   This function return the ans of func on the argument only if the argument did not
                   apear in privious calls.
                   returns the func call on arguments or print a massage.
                   Define input and expected output:
                    >>> f(3)
                    9
                    >>> f(3)
                    i alredy told you that the enswer is  9
                    >>> f1(x=2)
                    4



               '''
        global prev_var
        args_var = None
        kwargs_var = None
        check_word = None
        for n in args:
            args_var = n
        for key, val in kwargs.items():
            kwargs_var = val
        if args_var is None:
            check_word = kwargs_var
        if kwargs_var is None:
            check_word = args_var
        if check_word in prev_var:
            print("i alredy told you that the enswer is ", prev_var[check_word])
        else:
            prev_var[check_word] = func(check_word)
            return func(*args, **kwargs)

    return wrapper

@lastcall
def f(x: int):
    return x**2

@lastcall
def f1(x: int):
    return x+2

################# Q3 ######################



if __name__ == '__main__':
   print(f(2))
   print(f(x=2))
   print(f(9))
   print(f1(3))
   print(f(x=2))
   testmod(name='f', verbose=True)
   check_mail()
   myList = List([[[1,8,9,33],[4,5,6,66]],
                  [[2,2,2,2],[3,3,3,3]]])
   print(myList[0,1,3])
   print(myList[0, 1, 3])  # 66
   print(myList[0, 0, 3])  # 33
   print(myList[1, 0, 3])  # 2

