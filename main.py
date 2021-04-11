import time

from module.task import add

if __name__ == '__main__':
    for i in range(10):
        result = add.delay(i, i)
        print(f'Got result: {result.get()}')
        #time.sleep(2)
    print('Done')