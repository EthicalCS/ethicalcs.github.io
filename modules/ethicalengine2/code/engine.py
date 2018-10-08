from scenario import Scenario

"""
The following set of exercises was developed by Vinesh Kanna (MimirHQ) based
on an activity by Evan Peck (Bucknell University). It was modifed by Evan Peck
to match a disaster-relief scenario.
"""

def ruleset1(scenario: Scenario) -> str:
    """
    Decides whether your robot will save the people location 1 or location 2
    - Save the person in location 1, if and ONLY if they are pregnant.

    Note: in this activity, there will only be one person in each location
    @param scenario: details about the scenario
    @return: "loc1People" or "loc2People" depending on who you want to save
    """
    passenger = scenario.loc1People[0]
    pedestrian = scenario.loc2People[0]
    # TODO: Fill in the method
    return "loc1People"


def ruleset2(scenario: Scenario) -> str:
    """
    Decides whether your robot will save the people location 1 or location 2
    - Save the person in location 2, if they are NOT trespassing or if they are a child.

    Note: in this activity, there will only be one person in each location
    @param scenario: details about the scenario
    @return: "loc1People" or "loc2People" depending on who you want to save
    """
    passenger = scenario.loc1People[0]
    pedestrian = scenario.loc2People[0]
    # TODO: Fill in the method
    return "loc1People"


def ruleset3(scenario: Scenario) -> str:
    """
    Decides whether your robot will save the people location 1 or location 2
    - The first priority is to save the person who is a baby.
    - The second priority is to save athletic people.
    - The third priority is to save people who are either a doctor or a CEO.
    - The fourth priority is to save females.
    - The fifth priority is to save the passenger.

    Note: in this activity, there will only be one person in each location
    @param scenario: details about the scenario
    @return: "loc1People" or "loc2People" depending on who you want to save
    """
    passenger = scenario.loc1People[0]
    pedestrian = scenario.loc2People[0]
    # TODO: Fill in the method
    return "loc1People"


def my_decision(scenario: Scenario) -> str:
    """
    Decides whether your robot will save the people location 1 or location 2
    - Your own decision algorithm.

    Note: in this activity, there will only be one person in each location
    @param scenario: details about the scenario
    @return: "loc1People" or "loc2People" depending on who you want to save
    """
    passenger = scenario.loc1People[0]
    pedestrian = scenario.loc2People[0]
    # TODO: Fill in the method
    return "loc1People"
