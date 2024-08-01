# app.py
import time
import random


def main():
    while True:
        number=random.randint(1,5)
        # if number==2:
        #     raise Exception('custom exception')
        print(f"Hello, Supervisor! {number}")
        with open('a.txt','a') as f:
            f.write(str(time.time())+"\n")
        time.sleep(5)

if __name__ == "__main__":
    main()
