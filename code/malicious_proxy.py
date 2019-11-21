measured_values = [None] * N
for i in range(N):
    # Intercept qubits from Alice
    qubit = conn.recvQubit()
    # Measure all qubits in standard basis
    measured_values[i] = qubit.measure(inplace=True)
    # Forward qubits to Bob
    conn.sendQubit(qubit, "Bob")
