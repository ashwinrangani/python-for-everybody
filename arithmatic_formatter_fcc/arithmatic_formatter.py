def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    leftoperands = []
    operators = []
    rightoperands = []
    result = []
    max_width = []

    for problem in problems:
        formattedproblems = problem.split()
        leftoperand, operator, rightoperand = formattedproblems

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        if not (leftoperand.isdigit() and rightoperand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        leftoperand = int(leftoperand)
        rightoperand = int(rightoperand)
        

        if len(str(leftoperand)) > 4 or len(str(rightoperand)) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator == "+":
            total = leftoperand + rightoperand
            
        else:
            total = leftoperand - rightoperand
        
        leftoperands.append(str(leftoperand))
        operators.append(operator)
        rightoperands.append(str(rightoperand))
        result.append(str(total))

        width = max(len(str(leftoperand)), len(str(rightoperand))) + 2
        print(width)
        max_width.append(width)
        
        first_line = ""
        second_line = ""
        dashes = ""
        result_line = ""

    for i in range(len(problems)):
        first_line += leftoperands[i].rjust(max_width[i]) + '    '
        second_line += operators[i] + rightoperands[i].rjust(max_width[i]-1) + '    '
        dashes += "-" * max_width[i] + "    "
        if show_answers:
            result_line += result[i].rjust(max_width[i]) + "    "
    
    if show_answers:
       answer =  f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}\n{result_line.rstrip()}"
    else:
        answer =  f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}"

    return answer

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')

