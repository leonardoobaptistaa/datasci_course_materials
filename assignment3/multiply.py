import MapReduce
import sys

mr = MapReduce.MapReduce()
l = 5
n = 5

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if matrix == 'a':
      for k in range(0,n):
        mr.emit_intermediate( (i,k), (j,value) )

    if matrix == 'b':
      for k in range(0,l):
        mr.emit_intermediate( (k,j), (i,value) )

def reducer(key, list_of_values):
    array_total = [0,0,0,0,0]
    array_a = [0,0,0,0,0]
    array_b = [0,0,0,0,0]
    for value in list_of_values:
      key_m = value[0]
      total = value[1]
      if array_a[key_m] == 0:
        array_a[key_m] = total
      elif array_b[key_m] == 0:
        array_b[key_m] = total;

    for i in range(0, len(array_a) ):
      array_total[i] = array_a[i] * array_b[i]

    mr.emit( (key[0], key[1], sum(array_total) ) )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
