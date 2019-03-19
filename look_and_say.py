"""
There exists a sequence of numbers that follows the pattern

          1
         11
         21
        1211
       111221
       312211
      13112221
     1113213211
          .
          .
          .
Starting with "1" the following lines are produced by "saying what you see", so that line two is "one one", line three is "two one(s)", line four is "one two one one".

Write a function that given a starting value as a string, returns the appropriate sequence as a list. The starting value can have any number of digits. The termination condition is a defined by the maximum number of iterations, also supplied as an argument.
https://www.codewars.com/kata/look-and-say-numbers/train/python/5c9023822453954583f028b1
"""
def look_and_say(data='1', maxlen=10):
  #TODO populate result list with the look and say numbers
  ''' data:   starting number set
      maxlen: max sequence length
  '''
  array = []
  for i in range(0,maxlen):
      new_res = ''
      j = 0
      while j < len(data):
          count = 1
          while j < len(data)-1 and data[j] == data[j+1]:
              j = j + 1
              count = count + 1
          j = j + 1
          new_res = new_res + str(count) + data[j-1]
      data = new_res
      array.append(data)
  return array
