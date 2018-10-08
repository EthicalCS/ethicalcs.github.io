---
layout: page
title: Ethical Engine Documentation
exclude: true
---

This documentation will help you implement your decision engine for an autonomous robot.

Fill in the `decide` method with a program that analyzes the given scenario and returns a string to indicate which group to save: `"loc1people"` or `"loc2people"`. See below for the data available in each scenario.

## Scenario Information

| Attribute | Details | Type |
|-----------|---------|------|
| `scenario.loc1people` | Access the people who are passengers | list |
| `scenario.loc2people` | Access the people who are pedestrians | list |
| `scenario.youInLoc1` | Check if you are one of the people in location 1 | boolean |
| `scenario.trespassing` | Check if the pedestrians in location 2 are trespassing | boolean |

## Accessing Person Objects

You can loop over all of the people at location 1 or 2 like so:

```python
for person in scenario.loc1people:
    print(person.charType)
```

You can also select a specific person by their index:

```python
if len(scenario.loc2people) >= 1:
    firstped = scenario.loc2people[0]
    print(firstped.charType)
```

## Person Information

| Attribute | Details | Type |
|-----------|---------|------|
| `person.charType` | Check the type of character | string: `"human"`, `"cat"`, or `"dog"` |
| `person.age` | If human, check their age group | string: `"baby"`, `"child"`, `"adult"`, `"elderly"` |
| `person.gender` | If human, check their gender | string: `"male"`, `"female"` |
| `person.profession` | If human adult, check their profession | string: `"doctor"`, `"CEO"`, `"criminal"`, `"homeless"`, `"unemployed"`, `"unknown"` |
| `person.bodyType` | If human adult, check their body type | string: `"overweight"`, `"athletic"`, `"average"` |
| `person.pregnant` | If human female, check if they are pregnant | boolean (`True` or `False`)|
