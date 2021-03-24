###solution to exercise 95 from ben stephenson's "the python workbook".

import random

def plate():
  format_ = random.randint(0,1)
  result = ''
  if format_:
    for i in range(4):
      result = result + chr(random.randint(48,57))
    for i in range(3):
      result = result + chr(random.randint(65,90))
  else:
    for i in range(3):
      result = result + chr(random.randint(65,90))
    for i in range(3):
      result = result + chr(random.randint(48,57))

  return result

print(plate())      
