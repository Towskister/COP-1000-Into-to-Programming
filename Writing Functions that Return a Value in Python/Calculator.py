# Calculator.py - This program performs arithmetic, ( +. -, *. / ) on two numbers.
# Input:  Interactive
# Output:  Result of arithmetic operation
# NOTE!! I could also remove all the int & str conversions. because of eval

def performOperation(x, y, z):  # Write performOperation function here
    expression = str(x) + z + str(y)  # simple string concatenation
    a = eval(expression)
    return a


if __name__ == '__main__':
    numberOne = int(input("Enter the first number: "))
    numberTwo = int(input("Enter the second number: "))
    operation = input("Enter an operator (+ - * /): ")

    # Call performOperation method here and store the value in "result"
    result = performOperation(numberOne, numberTwo, operation)
    print(str(numberOne) + " " + operation + " " + str(numberTwo) + " = " + str(result))


'''
https://stackoverflow.com/questions/2983139/assign-operator-to-variable-in-python
You can use the operator module and a dictionary:

        import operator
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.div
        }   
        op_char = input('enter a operand')
        op_func = ops[op_char]
        result = op_func(a, b)

For python 3.x the operator.truediv or operator.floordiv should be used instead docs.python.org/3/library/operator.html – 
    joni jones
     Feb 14, 2017 at 21:20
additionally, using op_func in this way doesn't work. As the edit queue on this answer is full I've fixed these errors in an answer below (assuming this answer remains ACCEPTED w/ 76 upvotes...) – 
    Robert Houghton
     Dec 31, 2021 at 17:12
@RobertHoughton: what do you claim "doesn't work" with this answer? (I don't know what you mean by "the edit queue" either, but that's maybe just something I don't see.) – 
    rici
     Dec 31, 2021 at 20:06
      
-----------------------------------------------------------

I know this is a really old thread, but I believe at the time people didn't know about the eval function (Maybe it came with Python 3). So here's an updated answer to the question

        a = input('enter a value')
        b = input('enter a value') 
        op = input('enter an operand')
        expression = a + op + b # simple string concatenation
        result = eval(expression)
        
If the input is not expected to be valid all the time ast.literal_eval can be used instead. It raises an exception if the input isn't a valid Python datatype, so the code won't be executed if it's not. Eg. if a, b and op are respectively 5, 10, + then result is 15


It should be expression = a + c + b . btw, using eval for user input is a bad idea. ast.literal_eval is better. – 
    SilentGuy
     Oct 23, 2020 at 22:20
@SilentGuy you're very much right! I've updated my answer – 
    Eeshaan
     Oct 24, 2020 at 3:41
eval wasn't new to Python 3. The reason people aren't suggesting it is because it is not safe to use on user input. It can execute any Python expression (with any side effects) that someone types in. Also, literal_eval only evaluates literals. It cannot evaluate an arithmetic expression like '5+10'. – 
    khelwood
     May 16, 2021 at 13:03 
ast.literal_eval cannot do arithmetic in general, or deal with other operators. It can only handle + and - because of a quirk in the Python grammar. – 
    Karl Knechtel
     May 29 at 23:57
'''