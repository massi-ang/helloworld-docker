import time
while True:
  print(f"Hello, now is {time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())}")
  time.sleep(5)
