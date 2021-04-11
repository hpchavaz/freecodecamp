import re

sep = " " * 4

def arithmetic_arranger(problems, compute = False ):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  nlines = 4 if compute else 3
  lines = [""] * nlines
  for np, problem in enumerate(problems):
    match = re.search(r'^\s*(?P<left>\S+)\s*(?P<operator>\S+)\s*(?P<right>\S+)\s*$', problem)
    
    if not (match) :
      return "Error: Wrongly formed problem."
    
    left = match.group('left')
    operator= match.group('operator')
    right = match.group('right')
    
    if not((operator =='+') | (operator == '-')):
      return "Error: Operator must be '+' or '-'."
    if not((left.isdigit()) & (right.isdigit())):
      return "Error: Numbers must only contain digits."
    
    length = max(len(left), len(right))
    
    if length > 4:
      return "Error: Numbers cannot be more than four digits."

    if np > 0: 
      for l in range(nlines): 
        lines[l] += sep
        
    lines[0] = lines[0]            + " " * (2 + length - len(left))  + left
    lines[1] = lines[1] + operator + " " * (1 + length - len(right)) + right
    lines[2] = lines[2]            + "-" * (2 + length)

    if compute :
      result = str(eval(problem))
      lines[3] = lines[3] + " " * (2 + length - len(result)) + result

  return "\n".join(lines)
 