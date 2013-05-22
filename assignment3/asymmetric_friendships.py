import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    name = record[0]
    friend = record[1]
    mr.emit_intermediate((name, friend),1)
    mr.emit_intermediate((friend, name),1)

def reducer(key, list_of_values):
    total = sum(list_of_values)
    if total == 1:
        mr.emit(key)
        

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)