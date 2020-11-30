from random import randint
class NaiveBayesImplementation():
	def __init__(self):
		self.__arr = []
		self.__testing = []
		self.__insCount = 8124
		self.__atr = []
		self.__atrVal = []
		self.__positive = []
		self.__negative = []
		self.__readFile()
		self.__separateTestingSet()
		self.__separatePosNegData()
		self.__dataEntry()
		self.__countEachVal()
		self.__calProb()

	def __del__(self):
		del self.__arr
		del self.__atr
		del self.__atrVal
		del self.__testing
		del self.__positive
		del self.__negative
	
	def __separateTestingSet(self):
		j = self.__insCount
		for i in range(int(self.__insCount*30/100)):
			self.__testing.append(self.__arr.pop(randint(0, j-1)))
			j-=1
	
	def __readFile(self):
		f = open("agaricus-lepiota.data", "r")
		for i in range(self.__insCount):
			ln = f.readline(45)
			f.readline(45)
			self.__arr.append(ln.split(','))
		f.close()
	
	def __separatePosNegData(self):
		for i in range(len(self.__arr)):
			if self.__arr[i][0] == "e":
				self.__positive.append(self.__arr[i])
			elif self.__arr[i][0] == "p":
				self.__negative.append(self.__arr[i])

	def __dataEntry(self):
		self.__atr = ["cap-shape", "cap-surface", "cap-color", "bruises?", "odor", "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"] 
		self.__atrVal.append([["b", 0, 0, "bell"], ["c", 0, 0, "conical"], ["x", 0, 0, "convex"], ["f", 0, 0, "flat"], ["k", 0, 0, "knobbed"], ["s", 0, 0, "sunken"]])
		self.__atrVal.append([["f", 0, 0, "fibrous"],["g", 0, 0, "grooves"], ["y", 0, 0, "scaly"], ["s", 0, 0, "smooth"]])
		self.__atrVal.append([["n", 0, 0, "brown"],["b", 0, 0, "buff"], ["c", 0, 0, "cinnamon"], ["g", 0, 0, "gray"], ["r", 0, 0, "green"], ["p", 0, 0, "pink"], ["u", 0, 0, "purple"],["e", 0, 0, "red"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["t", 0, 0, "bruises"],["f", 0, 0, "no"]])
		self.__atrVal.append([["a", 0, 0, "almond"],["l", 0, 0, "anise"], ["c", 0, 0, "creosote"], ["y", 0, 0, "fishy"], ["f", 0, 0, "foul"], ["m", 0, 0, "musty"], ["n", 0, 0, "none"],["p", 0, 0, "pungent"], ["s", 0, 0, "spicy"]])
		self.__atrVal.append([["a", 0, 0, "attached"],["d", 0, 0, "descending"], ["f", 0, 0, "free"], ["n", 0, 0, "notched"]])
		self.__atrVal.append([["c", 0, 0, "close"],["w", 0, 0, "crowded"], ["d", 0, 0, "distant"]])
		self.__atrVal.append([["b", 0, 0, "broad"],["n", 0, 0, "narrow"]])
		self.__atrVal.append([["k", 0, 0, "black"],["n", 0, 0, "brown"], ["b", 0, 0, "buff"], ["h", 0, 0, "chocolate"], ["g", 0, 0, "gray"], ["r", 0, 0, "green"], ["o", 0, 0, "orange"],["p", 0, 0, "pink"], ["u", 0, 0, "purple"], ["e", 0, 0, "red"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["e", 0, 0, "enlarging"],["t", 0, 0, "tapering"]])
		self.__atrVal.append([["b", 0, 0, "bulbous"],["c", 0, 0, "club"], ["u", 0, 0, "cup"], ["e", 0, 0, "equal"], ["z", 0, 0, "rhizomorphs"], ["r", 0, 0, "rooted"], ["?", 0, 0, "missing"]])
		self.__atrVal.append([["f", 0, 0, "fibrous"],["y", 0, 0, "scaly"], ["k", 0, 0, "silky"], ["s", 0, 0, "smooth"]])
		self.__atrVal.append([["f", 0, 0, "fibrous"],["y", 0, 0, "scaly"], ["k", 0, 0, "silky"], ["s", 0, 0, "smooth"]])
		self.__atrVal.append([["n", 0, 0, "brown"],["", 0, 0, "buff"], ["c", 0, 0, "cinnamon"], ["g", 0, 0, "gray"], ["o", 0, 0, "orange"], ["p", 0, 0, "pink"], ["e", 0, 0, "red"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["n", 0, 0, "brown"],["", 0, 0, "buff"], ["c", 0, 0, "cinnamon"], ["g", 0, 0, "gray"], ["o", 0, 0, "orange"], ["p", 0, 0, "pink"], ["e", 0, 0, "red"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["p", 0, 0, "partial"],["u", 0, 0, "universal"]])
		self.__atrVal.append([["n", 0, 0, "brown"],["o", 0, 0, "orange"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["n", 0, 0, "none"],["o", 0, 0, "one"], ["t", 0, 0, "two"]])
		self.__atrVal.append([["c", 0, 0, "cobwebby"],["e", 0, 0, "evanescent"], ["f", 0, 0, "flaring"], ["l", 0, 0, "large"], ["n", 0, 0, "none"], ["p", 0, 0, "pendant"], ["s", 0, 0, "sheathing"], ["z", 0, 0, "zone"]])
		self.__atrVal.append([["k", 0, 0, "black"],["n", 0, 0, "brown"], ["b", 0, 0, "buff"], ["h", 0, 0, "chocolate"], ["r", 0, 0, "green"], ["o", 0, 0, "orange"], ["u", 0, 0, "purple"], ["w", 0, 0, "white"], ["y", 0, 0, "yellow"]])
		self.__atrVal.append([["a", 0, 0, "abundant"],["c", 0, 0, "clustered"], ["n", 0, 0, "numerous"], ["s", 0, 0, "scattered"], ["v", 0, 0, "several"], ["y", 0, 0, "solitary"]])
		self.__atrVal.append([["g", 0, 0, "grasses"],["l", 0, 0, "leaves"], ["m", 0, 0, "meadows"], ["p", 0, 0, "paths"], ["u", 0, 0, "urban"], ["w", 0, 0, "waste"], ["d", 0, 0, "woods"]])
	
	def __Prob(self, n, m):
		return n/m
		
	def __calProb(self):
		for n in range(len(self.__atrVal)):
			for val in self.__atrVal[n]:
				val.append(self.__Prob(val[1], len(self.__positive)))
				val.append(self.__Prob(val[2], len(self.__negative)))
	
	def __countEachVal(self):
		for n in range(len(self.__atrVal)):
			for fst in self.__positive:
				for val in self.__atrVal[n]:
					if val[0] == fst[n+1]:
						val[1] += 1
			for fst in self.__negative:
				for val in self.__atrVal[n]:
					if val[0] == fst[n+1]:
						val[2] += 1
	
	def __result(self, test):
		posProd = len(self.__positive)/len(self.__arr)
		negProd = len(self.__negative)/len(self.__arr)
		for n in range(len(self.__atrVal)):
			for val in self.__atrVal[n]:
				if val[0] == test[n+1]:
					posProd *= val[4]
					negProd *= val[5]
		if posProd < negProd:
			result = "p"
		else:
			result = "e"
		return result
		
	def __calculateAccuracy(self):
		count = 0
		for fst in self.__testing:
			if self.__result(fst) == fst[0]:
				count += 1
		return count*100/int(self.__insCount*30/100)
	
	def execution(self):
		for n in range(len(self.__atrVal)):
			print("{}:".format(self.__atr[n]))
			for val in self.__atrVal[n]:
				print(val)
		print("Accuracy of Classifier is {:.2f}%".format(self.__calculateAccuracy()))
		
###################

NaiveBayesImplementation().execution()