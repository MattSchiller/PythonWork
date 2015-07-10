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
		if self.startTime is 0:
			return self.endTime
		elif self.endTime is 0:
			return time.time() - self.startTime
		else
			return self.stopTime - self.startTime