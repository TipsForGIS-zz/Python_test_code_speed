import time

def execTime(code):
    start = time.clock()
    result = eval(code)
    runningTime = time.clock() - start
    print str(runningTime) + ' seconds.'


def myCode(n):
   i = 0
   while i < n:
      i = i + 1


execTime('myCode(999999)')
