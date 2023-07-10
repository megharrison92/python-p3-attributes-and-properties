#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Guido", job="Sales"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name.title()

    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job
        else:
            print("Job must be in list of approved jobs.")
        
    job = property(get_job, set_job)