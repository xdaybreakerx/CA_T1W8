# get two numbers from user
# convert to int 
# print outcome 

# try, except, block in py
# try, catch, block in most other languages 

# raise in py for error
# throw in most other languages

class NegativeError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))
    
    if n < 0 or d < 0:
        raise NegativeError

    q = n / d

    print(q)
    
except ValueError:
    print("This isn't a number")
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

except ZeroDivisionError:
    print("You cannot divide by zero")
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))
    
except NegativeError:
    print("Please don't input negative numbers")
    
except Exception:
    print("Something went wrong!")
    
else:
    # whenever the try block is succesfully executed without throwing any exceptions
    # not used that frequently 
    print("I am else block")


finally:
    # this will run at the end whether any error was thrown or not
    print("I am finally block")
    
print("end of program")

# file handling example
# try:
#       open a file
#       try to do something
#       write into the file - it may error
# except:
#       do something with error
# finally:
#       close the file