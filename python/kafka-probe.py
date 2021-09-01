from kafka import KafkaProducer, KafkaConsumer
import time
import threading
import sys
import datetime  

def current_milli_time():
  return int(time.time() * 1000)


class Mode():

  def produce():
    threading.Timer(2.0,Mode.produce).start()
    producer = KafkaProducer(bootstrap_servers = 'kafka-service:9092')
    ack = producer.send('input', bytes(str(current_milli_time()),'utf-8'))
    metadata = ack.get()

  def consume():
    consumer = KafkaConsumer('input',bootstrap_servers = 'kafka-service:9092' ,auto_offset_reset = 'earliest', enable_auto_commit=True)
    for message in consumer:
      print ("{},{}".format(str(message.value, encoding='utf-8'),str(message.offset)))
      mytimestamp = datetime.datetime.fromtimestamp( int(str(message.value, encoding='utf-8'))/1000 )  
      datetime_str = mytimestamp.strftime( "%Y-%m-%dT%H:%M:%SZ")  
      
      producer = KafkaProducer(bootstrap_servers = 'kafka-service:9092')
      ack = producer.send('output', bytes(str(datetime_str),'utf-8'))

if __name__ == '__main__':
 select = sys.argv[1]
 while True:
  try: 
    if select == 'producer':
      Mode.produce()
    elif select == 'consumer':
      Mode.consume()
  except:
    continue