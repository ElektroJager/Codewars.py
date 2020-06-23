from binarytree import Node
from binarytree import build

def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2,number-1,1):
        if number % i == 0:
            return False

    return True

def recbinary(root,total):
    print(total)
    print(root)

    if root.left and not root.right:
        total += root.left.value
        return recbinary(root.left,total)
    if root.right and not root.left:
        total += root.right.value
        return recbinary(root.right,total)

    if root.left and root.right:
        if root.left.value > root.right.value and not isPrime(root.left.value):
            total += root.left.value
            return recbinary(root.left,total)
        elif root.right.value > root.left.value and not isPrime(root.right.value):
            total += root.right.value
            return recbinary(root.right,total)

        elif not isPrime(root.right.value) and isPrime(root.left.value):
            total += root.right.value
            return recbinary(root.right,total)
        elif not isPrime(root.left.value) and isPrime(root.right.value):
            total += root.left.value
            return recbinary(root.left,total)

    return total

values = [
215,
193,124,
117,237,442,
218,935,347,235,
320,804,522,417,345,
229,601,723,835,133,12
248,202,277,433,207,263,257,
359,464,504,528,516,716,871,182,
461,441,426,656,863,560,380,171,923,
381,348,573,533,447,632,387,176,975,449,
223,711,445,645,245,543,931,532,937,541,444,
330,131,333,928,377,733,17,778,839,168,197,197,
131,171,522,137,217,224,291,413,528,520,227,229,928,
223,626,34,683,839,53,627,310,713,999,629,817,410,121,
924,622,911,233,325,139,721,218,253,223,107,233,230,124,233]
root = build(values)

total = root.value
#print(isPrime(433))
x = recbinary(root,total)
print(x)
