import os
from threading import Thread


def sstr(i):
    res = str(i)
    while len(res) < 3:
        res = '0' + res
    return res


def work(i, k):
    for j in range(900 * i // k, 900 * (i + 1) // k):
        print(j)
        os.system('python3 ~/Traffic-sign-recognition/Code/edge_detection.py ' +
                  '"../FullIJCNN2013/00' + sstr(j) +
                  '.ppm" "../Edge_detect/00' + sstr(j) + '.ppm"')


if __name__ == "__main__":
    k = 8
    threads = []
    for i in range(k):
        t = Thread(target=work, args=(i, k))
        threads.append(t)
    for i in range(k):
        threads[i].start()
    for i in range(k):
        threads[i].join()
