import simpy
import random

# Define a class to represent jobs
class Job:
    def __init__(self, job_type, due_date, other_params):
        self.job_type = job_type
        self.due_date = due_date
        self.other_params = other_params
        self.start_time = None
        self.end_time = None

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_delay(self):
        if self.end_time is None:
            return None  # Job not completed yet
        return self.end_time - self.due_date
