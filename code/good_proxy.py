for _ in range(N):
    # Receive qubits from Alice
    qubit = conn.recvQubit()
    # Forward qubits to Bob
    conn.sendQubit(qubit, "Bob")
