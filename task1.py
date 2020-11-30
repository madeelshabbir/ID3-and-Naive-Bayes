from math import log
from random import randint
class TreeNode():
	def __init__(self,s):
		self.data = s
		self.child = []
		self.edge = []

class Tree():
	def __init__(self, s):
		self.__root = TreeNode(s)
	
	def __del__(self):
		del self.__root
	
	def __appendR(self, p, c, e, n):
		if n.data == p:
			n.child.append(TreeNode(c))
			n.edge.append(TreeNode(e))
			return
		for cld in n.child:
			self.__appendR(p, c, e, cld)
	
	def append(self, p, c, e):
		self.__appendR(p, c, e, self.__root)
	
	def __showR(self, n, sp, ln):
		print(n.data)
		if ln != 0:
			sp += "  "
		for i in range(len(n.data) + ln):
			sp += " "
		i = 0
		for cld in n.child:
			print(sp[:-1],n.edge[i].data,end = ': ')
			self.__showR(cld, sp, len(n.edge[i].data))
			i+=1
	
	def show(self):
		sp = ""
		self.__showR(self.__root, sp, 0)
	
	def __isMatchedR(self, n, test, atr, atrVal):
		t = atr.index(n.data)
		index = 0
		for i in range(len(atrVal)):
			if test[t+1] == atrVal[t][i][0]:
				index = i
				break
		for i in range(len(n.edge)):
			if n.edge[i].data == atrVal[t][index][3]:
				r = ""
				if n.child[i].data == "edible":
					r = "e"
				elif n.child[i].data == "poisonous":
					r = "p"
				if test[0] == r:
					return True
				else:
					return self.__isMatchedR(n.child[i], test, atr, atrVal)
		return False
	
	def isMatched(self, test, atr, atrVal):
		return self.__isMatchedR(self.__root, test, atr, atrVal)
	
class ID3Implementaton():
	def __init__(self):	
		self.__arr = []
		self.__testing = []
		self.__pos = 0
		self.__neg = 0
		self.__insCount = 8124
		self.__atr = []
		self.__atrVal = []
		self.__readFile()
		self.__separateTestingSet()
		self.__calVal(self.__arr)
		self.__dataEntry()
	
	def __del__(self):
		del self.__arr
		del self.__atr
		del self.__atrVal
		del self.__testing
	
	def __separateTestingSet(self):
		j = self.__insCount
		for i in range(int(self.__insCount*30/100)):
			self.__testing.append(self.__arr.pop(randint(0, j-1)))
			j-=1
		
	def __calVal(self, a):
		self.__pos = 0
		self.__neg = 0
		for fst in a:
			if fst[0] == "e":
				self.__pos += 1
			elif fst[0] == "p":
				self.__neg += 1
	
	def __entropy(self, p, n):
		if p == 0 or n == 0:
			return 0.0
		if p == n:
			return 1.0
		tmp1 = p/(p+n)
		tmp2 = n/(p+n)
		return -1*tmp1*log(tmp1,2)-tmp2*log(tmp2,2)
	
	def __avgEntropy(self, ar, n, a):
		for val in ar:
			val[1] = 0
			val[2] = 0
		for fst in a:
			for val in ar:
				if val[0] == fst[n]:
					if fst[0] == "e":
						val[1] += 1
					elif fst[0] == "p":
						val[2] += 1
		avgEnt = 0.0
		for val in ar:
			avgEnt += self.__entropy(val[1], val[2])*(val[1]+val[2])/(self.__pos + self.__neg)
		return avgEnt

	def __calculateAccurracy(self, tree, atr, atrVal):
		count = 0
		for i in range(len(self.__testing)):
			if tree.isMatched(self.__testing[i], atr, atrVal):
				count += 1
		return count*100/int(self.__insCount*30/100)
		
	def __readFile(self):
		f = open("agaricus-lepiota.data", "r")
		for i in range(self.__insCount):
			ln = f.readline(45)
			f.readline(45)
			self.__arr.append(ln.split(','))
		f.close()
	
	def __dataDivision(self, ar, n, tar):
		tmp = []
		for i in range(len(ar)):
			tmp.append([])
			for fst in tar:
				if ar[i][0] == fst[n]:
					tmp[i].append(fst)
		for fst in tmp:
			for scd in fst:
				scd.pop(n)
		return tmp
		
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
	
	def __childRecursion(self, root, decTree, tar):
		nar = self.__dataDivision(self.__atrVal[root], root+1, tar)
		rem = self.__atrVal.pop(root)
		npar = self.__atr.pop(root)
		itr = 0
		for fst in nar:
			self.__calVal(fst)
			ent = self.__entropy(self.__pos, self.__neg)
			if ent == 0:
				if self.__pos != 0:
					decTree.append(npar, "edible", rem[itr][3])
				elif self.__neg != 0:
					decTree.append(npar, "poisonous", rem[itr][3])
				itr += 1
				continue
			max = 0
			root = -1
			for i in range(len(self.__atrVal)):
				tmp = ent - self.__avgEntropy(self.__atrVal[i], i+1, fst)
				if tmp >= max:
					max = tmp
					root = i
			decTree.append(npar, self.__atr[root], rem[itr][3])
			self.__childRecursion(root, decTree, fst)
			itr += 1
	
	def execution(self):
		tmpAtr = []
		tmpAtrVal = []
		for i in range(len(self.__atrVal)):
			tmpAtr.append(self.__atr[i])
			tmpAtrVal.append(self.__atrVal[i])
		ent = self.__entropy(self.__pos, self.__neg)
		max = 0
		root = -1
		for i in range(len(self.__atrVal)):
			tmp = ent - self.__avgEntropy(self.__atrVal[i], i+1, self.__arr)
			if tmp >= max:
				max = tmp
				root = i
		decTree = Tree(self.__atr[root])
		self.__childRecursion(root, decTree, self.__arr)
		decTree.show()
		print("Accuracy of Classifier is {:.2f}%".format(self.__calculateAccurracy(decTree, tmpAtr, tmpAtrVal)))
		
##########

ID3Implementaton().execution()