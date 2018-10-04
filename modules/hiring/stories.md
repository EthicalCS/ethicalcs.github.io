---
layout: page
title: Moogle's Hiring Algorithm: Stories
exclude: true
---

Now that you feel good about your algorithm, let's highlight some of those applicant and reveal the stories between them. For each of the following, reflect on whether you think that your algorithm _does the right thing._ If not, how could you change it?

#### **Story 1:** Misread the Instructions
What if an excellent applicant thinks they should put in letter grades?

`[‘A’, ‘A’, ‘A’, ‘A’, ‘A’, ‘A’, ‘A’]`

... or how about their grades on 4-point scale?

`[4, 3.9, 4, 4, 3.95, 4, 3.9]`

#### **Story 2:** Bad Assumptions
What if one of your applicants skipped _Intro to Computer Science_? When they saw your form, they froze, and decided that putting `-1` in the input field would make it obvious...

`[-1, 95, 99, 94, 96, 98, 95]`


#### **Story 3:** Mistake in the Input
What if one of your applicants accidentally put in a number > 100?

`[681, 68, 73, 70, 81, 91, 59]`

That might seem easy enough for a program to catch, but what if they accidentally dropped a `0`?

`[100, 100, 100, 100, 100, 100, 10]`

A person would catch that mistake easily, does your algorithm?


#### **Story 4:** The Awful Semester
What if your applicant had a medical emergency one semester? Or a personal tragedy?

`[95, 93, 50, 91, 98, 90, 90]`


#### **Story 5:** Inverse Trajectories
What if one of your applicants came from an underprivileged background and really struggled at the beginning of college... but showed extraordinary growth by the end?

`[65, 75, 85, 95, 100, 100, 80]`

What if one of your applicants came to college with extraordinary potential? They easily aced their first few classes and then gradually grew apathetic about their education - getting nothing but barely-passing grades by the time they were a senior?

`[100, 100, 95, 85, 75, 65, 80]`

_Does your algorithm treat them equally?_

## Reflection Questions
There are often no easy answers to these questions... but we need to reflect on the tradeoffs of our decisions.

- What systemic advantages/disadvantages are your algorithms likely to amplify?
- What does it mean to design a _fair_ algorithm?
- What is the human cost of efficiency? More permissive algorithms may capture more interesting candidates, but it also means more costly, human work. What is the ideal balance?
