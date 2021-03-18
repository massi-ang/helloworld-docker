import time
while True:
  print(f"Hello world, now is {time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())}")
  time.sleep(5)
