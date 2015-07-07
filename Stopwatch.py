import time
class stopwatch():
	def __init__(self):
		self.startTime = 0
		self.endTime = 0
	def start(self):
		self.startTime = time.time()
	def stop(self):
		self.stopTime = time.time()
	def duration(self):
		return self.stopTime - self.startTime