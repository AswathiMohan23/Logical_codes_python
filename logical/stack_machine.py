# A stack machine processes instructions by pushing and popping values to an internal stack.
# A simple example of this is a calculator.
#
# The argument passed to run(instructions) will always be a string containing a series of instructions.
# The instruction set of the calculator will be this:
#
# +: Pop the last 2 values from the stack, add them, and push the result onto the stack.
# -: Pop the last 2 values from the stack, subtract the lower one from the topmost one,
# and push the result.
# *: Pop the last 2 values, multiply, and push the result.
# /: Pop the last 2 values, divide the topmost one by the lower one, and push the result.
# DUP: Duplicate (not double) the top value on the stack.
# POP: Pop the last value from the stack and discard it.
# PSH: Performed whenever a number appears as an instruction. Push the number to the stack.
# Any other instruction (for example, a letter) should result in the value
# "Invalid instruction: [instruction]"
#
# examples:
# "" ➞ 0
# "5 6 +" ➞ 11
# "3 DUP +" ➞ 6
# "6 5 5 7 * - /" ➞ 5
# "x y +" ➞ Invalid instruction: x

if __name__=="__main__":

    stack_data=[1,2,3,4,5,6,7,8]
    value=[]
    # pop last 2 values, add them and push to stack
    stack_data.append(stack_data.pop()+stack_data.pop())
    print("pop last 2 values, add them and push to stack ----> ",stack_data)

    # pop last 2 values, subtract the lower one from topmost one and push the result
    last=stack_data.pop()
    second_last=stack_data.pop()
    top=stack_data[0]

    if second_last<last:
        result=top-second_last
    else:
        result=top-last
    stack_data.append(result)
    print("pop last 2 values, subtract the lower one from topmost one and push the result ----> ",stack_data)
# "pop last 2 values, multiply and push the result
    stack_data.append(stack_data.pop()*stack_data.pop())
    print("pop last 2 values, multiply and push the result ---> ",stack_data)

# "pop last 2 values, divide the lowest by top most element and push the result
    last = stack_data.pop()
    second_last = stack_data.pop()
    top = stack_data[0]

    if second_last < last:
        result = second_last//top
    else:
        result = last//top
    stack_data.append(result)
    print("pop last 2 values, divide the lowest by top most element and push the result--->",stack_data)

    # duplicate the top value on the stack
    stack_data.insert(0,stack_data[0])
    print("Duplicate (not double) the top value on the stack ----> ",stack_data)

    # Pop the last value from the stack and discard it
    stack_data.pop()
    print("Pop the last value from the stack and discard it ----> ",stack_data)

    # push Performed whenever a number appears as an instruction.Push the number to the stack.
    # Any other instruction (for example, a letter) should result in the value
    # "Invalid instruction: [instruction]"
    # value=10
    value='a'
    if isinstance(value,int):
        stack_data.append(value)
        print("stack_data : ",stack_data)
    else:
        print("Invalid instruction")




















    # for i in range(len(stack_data)-2,-1,-1):
    #     value.append(stack_data[i])
    # print(value)
    # value.pop()
