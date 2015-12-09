from __future__ import division
from bs4 import BeautifulSoup

class GradeCalculator(list):

	def __init__(self, weightList):
		# declaring starting percentages
		self.hw = 100 # contains hw, assignments
		self.tests = 100 # contains tests, exams, midterms
		self.clicker = 100 # contains iclicker, participation
		self.quizzes = 100 # contains quizzes
		self.essay = 100 # contains essays
		self.hwWeight = weightList[0]
		self.testWeight = weightList[1]
		self.clickerWeight = weightList[2]
		self.quizzesWeight = weightList[3]
		self.essayWeight = weightList[4]

		self.calcHW()
		self.calcTest()
		self.calcClicker()
		self.calcQuiz()
		self.calcEssay()

	def calcHW(self):
		# Pseudocode:
		# if div item cat contains homework, assignments and
		# if grade != '-' then add num to numList, denom to denomlist
		# else skip
		# finally, calculate total percentage and store it self.hw
		# return void
	def calcTest(self):
		# 
	def calcClicker(self):
		# 
	def calcQuiz(self):
		# 
	def calcEssay(self):
		# 
	
	def calcOverall(self):
		return self.hw * self.hwWeight + self.tests * self.testWeight + self.clicker + self.clickerWeight + self.quizzes * self.quizzesWeight + self.essay * self.essayWeight

# Tester

# This asks for the weights of each class. Not advanced enough to parse syllabuses yet
def main():
	categories = ['hw', 'tests', 'clicker', 'quizzes', 'essays']
	weightList = []
	for i in categories:
		if raw_input("Does class have " + i + "? (Y/N): ").upper() == 'Y':
			weight = float(raw_input("Enter weight: "))
			weightList.append(weight)
		else:
			weightList.append(0)
	return weightList

weightList = main()
gc = GradeCalculator(weightList)
gc.calcOverall()
