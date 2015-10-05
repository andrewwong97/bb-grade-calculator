from __future__ import division
from bs4 import BeautifulSoup
import os

#############################################################################
#
# Quick script to extract grades from HTML pages downloaded from Blackboard
# Learn.
#
# Needs a folder containing HTML files. 
# For percentage-based grades: Name file such that first character is !
# For grades out of total points: Name file such that first char is not !
#
# Prints out the grade in the course.
#
#############################################################################

path = raw_input('What is the path of your folder? ')

fileList = [file for file in os.listdir(path)]

os.chdir(path)

for file in fileList:
	if file[-5:] == '.html':
		if file[0] != '!': 
			f = open(file).read()
			soup = BeautifulSoup(f)
			gradeList = []
			totalList = []
			for i in soup.find_all('span', class_="grade"):
				gradeList.append(float(i.string))
			for j in soup.find_all('span', class_="pointsPossible clearfloats"):
				totalList.append(float(j.string[1:]))
			course = str(file[0:-5])
			percent = 100 * sum(gradeList)/sum(totalList)
			print "Current grade in %s = %.1f" % (course, percent)
		if file[0] == '!':
			f = open(file).read()
			soup = BeautifulSoup(f)
			gradeList = []
			totalList = []
			for i in soup.find_all('span', class_="grade"):
				if i == '-':
					gradeList.append('')
				else:	
					gradeList.append(float(i.string[0:-1]))
			course = str(file[1:-5])
			percent = sum(gradeList)/len(gradeList)
			print "Approximate grade in %s = %.1f" % (course, percent)

#





