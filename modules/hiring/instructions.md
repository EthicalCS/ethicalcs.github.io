---
layout: page
title: Moogle's Hiring Algorithm
exclude: true
---

![ethical hiring](img/hiring.jpg)

## Scenario: Moogle's Hiring Filter
Imagine you are working for _Moogle_, a well-known tech company that receives tens of thousands of job applications from graduating seniors every year.

Since the company receives too many job applications for HR to individually assess in a reasonable amount of time, you are asked to create a program that algorithmically analyzes applications and selects the ones most worth passing onto HR.

### Applicant Data
It's difficult to create these first-pass cuts, so _Moogle_ designs their application forms to get some numerical data about their applicants' education. Job applications must enter the grades they received in 6 core CS courses, as well as their overall GPA. For your convenience, this will be stored in a python `list` that you can access. For example, a student who received the following scores...

- **Intro to CS:** 100
- **Data Structures:** 95
- **Software Engineering:** 80
- **Algorithms:** 89
- **Computer Organization:** 91
- **Operative Systems:** 75
- **Overall GPA:** 83

... would result in the following list: `[100, 95, 80, 89, 91, 75, 83]`. You can assume that index `0` is _always_ Intro to CS, `1` is _always_ Data Structures, and so on.

Because you are processing many applications, your program will receive a _list of lists_. For example, this would be the information for 3 applicants:

`[ [100, 95, 80, 89, 91, 75, 83], [75, 80, 85, 90, 85, 88, 90], [85, 70, 99, 100, 81, 82, 91] ]`

### Your Task
Your job is to:
1. Determine how you are going to select the top applicants to pass onto HR.
2. Given a list of applicant data (a _list of lists_), write a function returns a new list of worthwhile candidates.

### Your Code
To get you started, we're provided some template code:

- [`hiring.py`](code/hiring.py) a template where you will write your applicant-selection algorithm based on a small set of dummy data.
- [`lottaApps.py`](code/lottaApps.py) a module that contains a list of ten-thousands applicants you can try once you have completed your code.

### Questions you should answer:

1. What criteria did you choose to select finalists? How did you choose that criteria?

2. Roughly what percentage of applicants does your algorithm pass on as finalists? Is that enough? If _Moogle_ asked you to take a more aggressive approach with your algorithm, are there any tradeoffs?

<!-- ```python
example_list = [[93, 89, 63, 88, 60, 73, 80], [100, 63, 57, 96, 58, 71, 78], [81, 91, 99, 78, 57, 87, 86], [81, 73, 100, 57, 91, 60, 66], [86, 89, 64, 81, 69, 93, 92], [78, 63, 88, 95, 59, 98, 90], [55, 74, 68, 55, 69, 94, 80], [64, 77, 75, 92, 77, 72, 83], [95, 58, 92, 62, 77, 64, 59], [94, 78, 84, 83, 68, 63, 76]]


def get_best_applicants(app_list):
  """ Given applicant data, return the most qualified applications
  input:
  - app_list: a 2D list containing lists of application data
  output:
  - a 2D list of the best applications
  """
  finalists = list()

  for app in app_list:
    # This will return ALL the applicants as finalist.
    # Your job is to only return a subset.
    finalists += [app]

  return finalists


finalists = get_best_applicants(example_list)
print('')
print("-------------------------")
print("The finalists are...")
for finalist in finalists:
  print(finalist)
``` -->
