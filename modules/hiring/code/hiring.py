"""
Use this file as a template to develop Moogle's Hiring Filter

0: Intro to CS
1: Data Structures
2: Software Engineering
3: Algorithms
4: Computer Organization
5: Operating Systems
6: Overall College GPA

The list representing a single application would look like this:
[100, 95, 80, 89, 91, 75, 83]
"""

# When you have something working, uncomment this line!
#from lottaApps import *

example_list = [[93, 89, 63, 88, 60, 73, 80], [100, 63, 57, 96, 58, 71, 78], [81, 91, 99, 78, 57, 87, 86], [81, 73, 100, 57, 91, 60, 66], [86, 89, 64, 81, 69, 93, 92], [78, 63, 88, 95, 59, 98, 90], [55, 74, 68, 55, 69, 94, 80], [64, 77, 75, 92, 77, 72, 83], [95, 58, 92, 62, 77, 64, 59], [94, 78, 84, 83, 68, 63, 76]]


def get_best_applicants(app_list):
	"""
	Given applicant data, return the most qualified applications

	@param app_list: a 2D list containing lists of application data
	@return a 2D list of the best applications
	"""
	finalists = list()

	for app in app_list:
		# Where we decide whether to
		if analyze_applicant1(app) == True:
			finalists += [app]

	return finalists

def analyze_applicant1(applicant):
	"""
	Given the GPAs of a single applicant, return True if they are qualified
	Qualification: An applicant is qualified if...
		- their Overall College GPA is above 80

	@param applicant: a list of GPAs (integers)
	@return True if the applicant qualifies
	"""
	return True


def analyze_applicant2(applicant):
	"""
	Given the GPAs of a single applicant, return True if they are qualified
	Qualification: An applicant is qualified if...
		- they have no grade below a 65

	@param applicant: a list of GPAs (integers)
	@return True if the applicant qualifies
	"""
	return True

def analyze_applicant3(applicant):
	"""
	Given the GPAs of a single applicant, return True if they are qualified
	Qualification: An applicant is qualified if...
		- they have at least 4 grades above 85

	@param applicant: a list of GPAs (integers)
	@return True if the applicant qualifies
	"""
	return True

def analyze_applicant4(applicant):
	"""
	Given the GPAs of a single applicant, return True if they are qualified
	Qualification: An applicant is qualified if...
		- the average GPA of their CS courses (all but Overall) is above 85

	@param applicant: a list of GPAs (integers)
	@return True if the applicant qualifies
	"""
	return True

def your_analysis(applicant):
	"""
	Given the GPAs of a single applicant, return True if they are qualified
	Qualification: An applicant is qualified if...
		- YOUR DECISION. WRITE IT HERE.

	@param applicant: a list of GPAs (integers)
	@return True if the applicant qualifies
	"""
	return True


# When you have it working on example_list, uncomment the import above
# and then replace example_list with lottaApps
applicants = example_list
finalists = get_best_applicants(applicants)

print('')
print("-------------------------")
print()
print("The finalists are...")
for finalist in finalists:
  print(finalist)
print("Your algorithm kept", round(len(finalists)/len(applicants)*100), "percent of applicants")
