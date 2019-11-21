measured_num = BitVector(size=N, intVal=0)
bases = BitVector(size=N)

for i in range(N):
    # Randomly apply a quarter spin to use the Hadamard basis
    with CQCConnection("Bob") as Bob:
        received_qubit = Bob.recvQubit()
        rand = qubit(Bob)
        rand.H()

        if rand.measure() == 1:
            received_qubit.H()
            # update bitvector of bases
            bases[i] = 1

        # Measure the bit and insert it into the decoded number
        measured_num[i] = received_qubit.measure()
