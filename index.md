---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
exclude: true
---

# Ethical Reflection Modules for CS 1

In Fall 2019, I redesigned our CS 1 course to integrate practice-based (coding!) reflection directly with technical concepts. This space acts as a repository of ethical reflection modules that I have created over the past couple of years. The goal of these modules is to:
1. Introduce ethical reflection in CS 1 courses. These are categorized based on [Amy Ko's 21st Century Grand Challenges in Computing Education](https://medium.com/bits-and-behavior/21st-grand-challenges-for-computing-education-f5e937d57155) - _limits of computing_, _social responsibility_, _data literacy_, and _diversity literacy_
2. Develop ethical reflection habits _alongside_ coding (all modules involve programming!)
3. Pair directly with _existing_ CS 1 curriculum (students practice for loops - but instead of practicing on trivial problems, their practice is situated in ethical design scenarios)

What these activies are **not**: 
 
- They do **not** teach students what the _right_ or _best_ design is. They  prompt students to reflect on the human consequences of their decisions.
- They are **not** a replacement for teaching students cultural competency

_Note: If you are looking for the old homepage of this site, [click this link](archive/old-index.html)_

--------------------
## **[Conditionals]** Developers as Decision-Makers
![housing algorithms](img/housing.png)

- Scenario: Develop a scoring algorithm to determine which classmates are prioritized for housing on campus. 
- Material: [Nifty Assignments 2019 Page](http://nifty.stanford.edu/2020/peck-decision-makers/)
- Context: 2 hour lab setting. Small student groups. 
- This assignment appeared as part of [_ACM SIGCSE'S Nifty Assignments_](https://dl.acm.org/doi/abs/10.1145/3328778.3372574) track. You can cite that work with: 
```
Nick Parlante, Julie Zelenski, John DeNero, Christopher Allsman, Tiffany Perumpail, Rahul Arya, Kavi Gupta, Catherine Cang, Paul Bitutsky, Ryan Moughan, David J. Malan, Brian Yu, Evan M. Peck, Carl Albing, Kevin Wayne, and Keith Schwarz. 2020. Nifty Assignments. In Proceedings of the 51st ACM Technical Symposium on Computer Science Education (SIGCSE '20). Association for Computing Machinery, New York, NY, USA, 1270–1271. DOI:https://doi.org/10.1145/3328778.3372574
```

--------------------

## **[Functions & Data-types]** Developers as Gatekeepers
![input validation](img/university.jpg)
_What assumptions do we make about the people using our technology? What are the consequences of those assumptions? - who might we exclude? How do we capture diversity through design?_

--------------------

## **[For Loops & Lists]** Developers as Future Makers
![ethical hiring](img/hiring.jpg)
_What does it mean to design a fair algorithm? What is the human cost of efficiency? What systemic advantages/disadvantages are your algorithms likely to amplify?_
- *Scenario:* Develop an algorithm that filters job applications based on student grades
- *Degree of Integration:* Full assignment
- *Needs improvement:* Need to update associated reading assignments and reflection prompts. 


--------------------

## **[Nested Loops & 2D Lists]** Developers as Media Manipulators
![averaging faces](img/faces.png)
- *Scenario:* Given a series of face images, write code to generate the _average_ face of those images.





------------------------
## **[Intro OOP]** Developers as Moral Arbiters
![rescue](modules/ethicalengine1/img/people.jpg)
_What is 'moral' behavior in the context of a computer? How do we write code that is forced to assign value to people? What are the implications of our representation decisions?_
- *Scenario:* Program a disaster-relief robot to prioritize which distressed people to saves


----------

--------------------
## [Hiring Algorithms: Developers as Decision-Makers](modules/hiring)

![ethical hiring](modules/hiring/img/hiring.jpg)

_What does it mean to design a fair algorithm? What is the human cost of efficiency? What systemic advantages/disadvantages are your algorithms likely to amplify?_
- *Scenario:* Develop an algorithm that filters job applications based on GPA
- [Material](modules/hiring)
- *Practice:* loops, conditionals, python lists
- *Writeup:* [Ethical Design in CS 1: Building Hiring Algorithms in 1 Hour (Evan Peck)](https://medium.com/bucknell-hci/ethical-design-in-cs-1-building-hiring-algorithms-in-1-hour-41d8c913859f)
- *Author:* [Evan Peck (Bucknell University)](http://www.eg.bucknell.edu/~emp017/)

--------------------
## [Input Validation: Developers as Gatekeepers](modules/input)
![university](modules/input/img/university.jpg)

- *Scenario:* Collect and validate personal information of people visiting a university
- [Material](modules/input)
- *Practice:* conditionals, functions, data types
- *Author:* [Justin Li (Occidental College)](https://justinnhli.com/), Adapted by [Evan Peck (Bucknell University)](http://www.eg.bucknell.edu/~emp017/)

--------------------
## [Ethical Engine 1: Developers as Definers of Identity](modules/ethicalengine1)
![rescue](modules/ethicalengine1/img/people.jpg)

_How can we adequately represent people in code? What characteristics of people should we **NOT** include in code? What are the implications of our representation decisions?_

- *Scenario:* In code, represent a person so that autonomous cars can make life-critical decisions
- [Material](modules/ethicalengine1)
- *Practice:* OOP design, data types
- *Author:* [Evan Peck (Bucknell University)](http://www.eg.bucknell.edu/~emp017/)

--------------------
## [Ethical Engine 2: Developers as Moral Arbiters](modules/ethicalengine2)
![rescue](modules/ethicalengine2/img/rescue.jpg)

_What is 'moral' behavior in the context of a computer? How do we write code that is forced to assign value to people?_
- *Scenario:* Program a disaster-relief robot to prioritize which distressed people to saves
- [Material](modules/ethicalengine2)
- *Practice:* conditionals, use of APIs and objects, dictionaries (in optional last part)
- *Write ups:*
  - [The Ethical Engine: Integrating Ethical Design into Intro Computer Science (Evan Peck)](https://medium.com/bucknell-hci/ethical-design-in-cs-1-building-hiring-algorithms-in-1-hour-41d8c913859f)
  - [Write Up the Ethical Engine Lab (Justin Li)](https://howtostartacsdept.wordpress.com/2018/01/13/step-86-write-up-the-ethical-engine-lab/)
- *Author:* [Evan Peck (Bucknell University)](http://www.eg.bucknell.edu/~emp017/), parts of activity by [Vinesh Kannan (Mimir HQ)](https://github.com/vingkan)

---------------------




<!-- ## Other Resources
- [ACM Code of Ethics](https://www.acm.org/code-of-ethics)
- [Ethics in Technology Practice](https://www.scu.edu/ethics-in-technology-practice/) -->
---------------------

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>
