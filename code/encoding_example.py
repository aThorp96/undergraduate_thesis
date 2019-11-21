with CQCConnection("Alice") as Alice:
    qubits = [None] * N
    for i in range(bits):
        qubits[i] = qubit(Alice)

        # Encode value
        if bits[i] == 1:
            qubits[i].Z()

        # Change basis
        if bases[i] == 1:
            qubits[i].H()
