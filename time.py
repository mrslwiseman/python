import time

def timing(original):
  def wrapper():
    start = time.time()
    original()
    end = time.time()
    return 'Time to run function: ' + str((end - start)) + '\n'
  return wrapper

def someFunction():
  return print('did stuff')

x = timing(someFunction())

print(x.type())