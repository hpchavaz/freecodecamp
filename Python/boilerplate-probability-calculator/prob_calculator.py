import copy
import random
# Consider using the modules imported above.

from collections import Counter

class Hat:

	def __init__(self, **kwargs):
		self.contents = []
		for key in kwargs:
			for n in range(kwargs[key]):
				self.contents.append(key)

	def draw(self, nballs):
		if nballs > len(self.contents): 
			ret = copy.deepcopy(self.contents)
			self.contents = []
			return ret
		
		ret = []
		for i in range(nballs):
			rd = random.randrange(0, len(self.contents))
			ret.append(self.contents[rd])
			del self.contents[rd]
		return ret

	def __len__(self):
		  return len(self.contents)
	
	def __str__(self):
		return str(self.contents)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0

  for i in range(num_experiments):
    temphat = copy.deepcopy(hat)
    counter = Counter(temphat.draw(num_balls_drawn))
    for k in expected_balls:
      if expected_balls[k] > counter[k]:
        break
    else:
      success += 1
  return success / num_experiments