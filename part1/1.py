def house(size = 5):
  if(size % 2 == 0):
    size += 1
  if(size > 1):
    roof(size)
    walls(size)
    floor(size)

def roof(size):
  for i in range(size+1):
    if(i % 2==0):
      continue
    space = (size - i)//2
    print(" " * space, "X"*i, sep="")

def walls(size):
  for i in range(size//2):
    print("|","|", sep=" "*(size-2))

def floor(size):
  print("-"*size)

house()
