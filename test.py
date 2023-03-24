print('hello world')

def add(a,b):
  return a + b

x, y = 5, 6

add(x, y)


def divide(a,b):
  try:
    x = a / b
  except ZeroDivisionError:
    x = None
  return x
