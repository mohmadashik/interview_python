import threading
import time

def worker (text):
  counter = 1
  while True:
    print(f'counter: {counter} and text : {text}')
    counter+=1
    time.sleep(11)

t1 = threading.Thread(target=worker,daemon=True,args=("HI",))
t2 = threading.Thread(target=worker,daemon=True,args=("BYE",))  # daemon = True means it will run until any other process is working in the program =
t1.start()
t2.start()
stop = input('enter to stop')