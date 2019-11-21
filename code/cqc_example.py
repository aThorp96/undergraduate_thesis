from cqc.pythonLib import CQCConnection, qubit

# Encode and measure a qubit
with CQCConnection("Alice") as Alice:
    q = qubit(Alice)

    # Encode 1 in qubit
    q.Z()

    # Send qubit to Bob
    Alice.sendQubit(q, "Bob")

# Recieve and decode qubit
with CQCConnection("Bob") as Bob:
    # Recieve qubit from server
    q = Bob.recvQubit()

    decoded = q.measure()
