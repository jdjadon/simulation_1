
class Sink:
    def __init__(self):
        self.record = []

    def receive(self, job_type, quantity, timestamp):
        self.record.append({"Job Type": job_type, "Quantity": quantity, "Time": timestamp})

# Create a sink component
sink = Sink()