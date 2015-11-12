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
			notRecorded = 0
			for i in soup.find_all('span', class_="grade"):
				if i.string == '-':
					gradeList.append(0)
					notRecorded += 1
				else:
					gradeList.append(float(i.string))
			step = 0
			for j in soup.find_all('span', class_="pointsPossible clearfloats"):
				if gradeList[step] == 0:
					totalList.append(0)
				else: 
					totalList.append(float(j.string[1:]))
				step += 1
			course = str(file[0:-5])
			percent = 100 * sum(gradeList)/sum(totalList)
			print "Current grade in %s = %.1f" % (course, percent)
			print "# of grades not recorded: %d" % (notRecorded)
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

# TODO:
# Want to write algorithm to extract from blackboard
# Post to jhu login page
# Get from bb





