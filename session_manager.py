# session_manager.py

import json
import time

class SessionManager:

    def __init__(self):
        self.start_time = time.time()
        self.vulnerability = None
        self.attempts = 0
        self.correct = False

    def set_vulnerability(self, vuln):
        self.vulnerability = vuln

    def increment_attempt(self):
        self.attempts += 1

    def mark_correct(self):
        self.correct = True

    def end_session(self):

        duration = round(time.time() - self.start_time, 2)

        log_entry = {
            "vulnerability": self.vulnerability,
            "attempts": self.attempts,
            "correct": self.correct,
            "time_taken_seconds": duration
        }

        with open("logs.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")