import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    table_name = record[0]
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    
    order_record = []
    for record in list_of_values:
      if record[0] == 'order':
        order_record = record;

    list_of_values.remove(order_record)

    for record in list_of_values:
      array = []
      for field in order_record:
        array.append(field)
      for field in record:
        array.append(field)

      mr.emit( array )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
