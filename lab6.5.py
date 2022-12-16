# Вариант 4
import os
import random
import numpy as np

dirpath = os.path.dirname(os.path.realpath(__file__))

def readFrom(filename):
    filepath = os.path.join(dirpath, filename)
    if os.path.exists(filepath):
        f = open(filepath, 'r')
        data = f.readlines()
        f.close()
        return data

    print('File not found')

    return []
            
def writeTo(filename, data: list[str]):
    filepath = os.path.join(dirpath, filename)
    f = open(filepath, 'w')
    for line in data:
        f.write(line)
    f.close()

def matrixToWritable(m):
    M = []

    for row in m:
        M.append(", ".join(map(str, row)))

    M = "\t\n".join(M)
    return M

def describeNumber():
    inputLines = readFrom('input.txt')
    if len(inputLines) == 0:
        return

    number = inputLines[0]
    digitCount = len(number)
    digitSum = 0
    digitMul = 1
    for n in number:
        n = int(n)
        digitSum += n
        digitMul *= n

    linesToWrite = [
        f"Number: {number}\n",
        f"Digit count: {digitCount}\n",
        f"Digit sum: {digitSum}\n",
        f"Digit mul: {digitMul}\n"
    ]

    writeTo('output.txt', linesToWrite)
    
def isPrime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True

def primeGenerator():
    inputLines = readFrom('input.txt')
    if len(inputLines) == 0:
        return

    N = int(inputLines[0])

    primes = []

    for i in range(N):
        if isPrime(i):
            primes.append(str(i) + '\n')
    
    writeTo('output.txt', primes)

def matrixGenerator():
    inputLines = readFrom('input.txt')
    if len(inputLines) == 0:
        return
    
    (n, m) = inputLines[0].split()
    if n is None or m is None:
        return

    n, m = int(n), int(m)

    A = np.random.randint(1, 100, (n, m))

    A = A / A.max(axis=1).reshape(n, 1)

    k = random.randint(5, 16)
    B = np.random.randint(1, 100, (m, k))

    C = np.dot(A, B)

    

    matricies = [
        f"Matrix A({n}x{m}):\n",
        matrixToWritable(A),
        f"\nMatrix B({m}x{k}):\n",
        matrixToWritable(B),
        f"\nMatrix A*B({n}x{k}):\n",
        matrixToWritable(C)
    ]

    writeTo('output.txt', matricies)



            



if __name__ == '__main__':
    # Задание 2
    # describeNumber()
    # Задание 3
    # primeGenerator()
    # Задание 5
    matrixGenerator()