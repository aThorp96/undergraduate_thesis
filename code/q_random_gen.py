from BitVector import BitVector
from cqc.pythonLib import CQCConnection, qubit

N = 32
bits = BitVector(intVal=0, size=N)

with CQCConnection("Alice") as Alice:
    for i in range(N):
        q = qubit(Alice)
        # Put qubit in superposition
        q.H()
        bits[i] = q.measure()
