import sys
sys.path.append('D:\PyProjects\pythonProject1\.venv\bobik.py')# да это соседняя папка на моем компе, не спрашивайте

from bobik import GOST34112012

def main():
    iterations = 50
    m = GOST34112012(digest_size=32)
    m.update("cvetok")
    d = m.hexdigest()
    counter = 0
    temp = d
    for i in range(iterations-1):
        m = GOST34112012(digest_size=32)
        m.update(d)
        d = m.hexdigest()
        if (i+2)%5 == 0:
            for j in range(len(d)):
                if d[j] != temp[j]:
                    counter +=1
            print(i+2 ,"______", counter)
            counter = 0
    print(m.hexdigest())

if __name__ == "__main__":
    main()
