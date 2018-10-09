import random


def set_seed(seed):
    random.seed(seed);


class Scenario:
    """ Packages all of the information needed to create an ethical scenario.
    Automatically construct a random scenario in which an autonomous robot must
    decide whether to save the people in location 1 vs. location 2

    Args:
        sameNum (bool, optional): if True, enforces that the number of
            people in location1 is the same as location2
    Attributes:
        numLoc1 (int): the number of entities at location 1
        numLoc2 (int): the number of entities at location 2
        loc1people (list): list of entities at location 1
        loc2people (list): list of entities at location 2
        youInLoc1 (bool): True if you are one of the people at location 1
        trespassing (bool): True if loc2people are currently trespassing
    """
    # The minimum/maximum number of people at each location
    MIN_LOCATION1 = 1
    MAX_LOCATION1 = 1
    MIN_LOCATION2 = 1
    MAX_LOCATION2 = 1

    # The following variables are lists that represent the probabilities of
    # each feature happening. For example, in YOU_CHANCE, there is a 1 in 4
    # chance that that 'you' are in the vehicle. Similarly, in TRESPASSING_CHANCE,
    # there is a 2 in 3 chance that the loc2people are crossing the street
    # legally (the walk sign is on)
    YOU_CHANCE = [True, False, False, False]
    TRESPASSING_CHANCE = [True, True, False]

    def __init__(self, loc1people=None, loc2people=None, youInLoc1=None, trespassing=None,
                 sameNum=True):
        # Create a random number of people in location 2
        numLoc2 = random.randint(self.MIN_LOCATION2, self.MAX_LOCATION2)

        # If sameNum is true, create the same number of people in location 1
        # Otherwise, create a random number of people in location 1
        if not sameNum:
            numLoc1 = random.randint(self.MIN_LOCATION1, self.MAX_LOCATION1)
        else:
            numLoc1 = numLoc2

        # DETERMINE THE PEOPLE IN LOCATION 1
        if loc1people is not None:
            self.loc1people = loc1people
        else:
            # Create randomly generated people for location 1
            self.loc1people = [Person() for numPeople in range(numLoc1)]

            # If you are in location 1, replace one of the people there with you.
            if youInLoc1 is not None:
                self.youInLoc1 = youInLoc1
            else:
                self.youInLoc1 = random.choice(self.YOU_CHANCE)

            if self.youInLoc1 is True:
                # Feel free to change these attributes if you'd like.
                youPerson = Person("you")
                if numLoc1 > 0:
                    self.loc1people[0] = youPerson
                else:
                    self.loc1people += [youPerson]

        # DETERMINE THE PEOPLE IN LOCATION 2
        if loc2people is not None:
            self.loc2people = loc2people
        else:
            self.loc2people = [Person() for numPeople in range(numLoc2)]

        # Determine if the people in location 2 are trespassing
        if trespassing is not None:
            self.trespassing = trespassing
        else:
            self.trespassing = random.choice(self.TRESPASSING_CHANCE)


    def __repr__(self):
        """ Method that helps python understand how to print a Scenario
        For example, you can now create a scenario in your code somewhere:
            scenario = Scenario()
        and then print that scenario:
            print(scenario)
        This will print a readable form of the scenario in your program
        """
        readable = 'People at Location 1: \n'
        for entity in self.loc1people:
            readable += '-' + str(entity) + '\n'

        readable += '\n'
        readable += 'People at Location 2: \n'
        for entity in self.loc2people:
            readable += '-' + str(entity) + '\n'
        readable += '\n'

        if self.trespassing:
            readable += 'This group is trespassing\n'

        return readable


class Person:
    """ Packages all the info needed for a person.
    Every scenario is composed of characters - many of which are people. Each
    of those people can contain a variety of characteristics. The Person class
    will automatically create a random person or animal.
    Attributes:
        charType (string): 'human', 'you', 'cat', 'dog'
        age (string): humans can be a 'baby', 'child', or 'adult'
        profession (string): adults are assigned a profession: 'doctor', 'CEO',
            'criminal', 'homeless', 'unemployed', 'unknown'
        gender (string): 'male' or 'female' TODO: add more diverse options
        bodyType (string): adults are classified as 'average', 'athletic',
            or 'overweight'
        pregnant (bool): adult women may also be pregnant. True if pregant.
    """
    # The following variables not only contain the possibilities of different
    # attributes of people/animals, but also the probability with which they
    # appear. For example, CHAR_TYPES contains 'human' 4 times and 'animal'
    # just 1 time. That means that 'human' is 4x more likely to appear.

    # Choose between a human or animal
    CHAR_TYPES = ["human", "human", "human", "animal", "human"]
    # If it's an animal, choose between cat or dog
    ANIMAL_TYPES = ["cat", "dog"]
    # Possible ages of humans
    AGE_TYPES = ["baby", "child", "adult", "adult", "adult", "elderly"]
    # Possible professions of adults
    PROF_TYPES = ["doctor", "CEO", "criminal", "homeless", "unemployed",
                  "unknown", "unknown", "unknown"]
    # Possible genders of humans
    GENDER_TYPES = ["male", "female"]
    # Select whether a female is pregnant (currently 25% chance)
    PREGNANT_CHANCE = [True, False, False, False]
    # Select the bodytype of each non-child.
    BODYWEIGHT_CHANCE = ["overweight", "athletic", "average", "average"]

    def __init__(self, charType=None, age=None, profession=None,
                 gender=None, bodyType=None, pregnant=None):
        ''' Create a person by randomly selecting their attributes
        All of the parameters in this method are OPTIONAL. This means that by
        default, a random person is made if no information is given. For
        example:
            person = Person()
        However, you can also create a custom person by filling in any
        number of those parameters. For example, the following code would
        create an adult woman with an average body type, but still allow
        the program to randomly select her profession:
            person = Person(charType="human", age="adult", gender="female",
                        bodyType="average")
        '''
        self.charType = charType
        self.profession = profession
        self.age = age
        self.gender = gender
        self.bodyType = bodyType
        self.pregnant = pregnant

        # set type of character (human or animal?)
        if charType is None:
            self.charType = random.choice(self.CHAR_TYPES)

        # If it's an animal, choose which type
        if self.charType == "animal":
            self.charType = random.choice(self.ANIMAL_TYPES)
        # If it's a person, set the characteristics
        if self.charType == "human":
            self.age = random.choice(self.AGE_TYPES)
            self.gender = random.choice(self.GENDER_TYPES)

            # Set adult characteristics.
            if self.age == "adult":
                self.bodyType = random.choice(self.BODYWEIGHT_CHANCE)
                if self.gender == "female":
                    self.pregnant = random.choice(self.PREGNANT_CHANCE)
                self.profession = random.choice(self.PROF_TYPES)

    def __repr__(self):
        """ Method that helps python understand how to print a Person
        For example, you can now create a person in your code somewhere:
            person = Person()
        and then print that person to see what charecteristics it has:
            print(person)
        """
        if self.charType == "human":
            readable = '['
            if self.bodyType:
                readable += self.bodyType + ' '
            if self.age:
                readable += self.age
            if self.gender:
                readable += ' ' + self.gender + ']'
            if self.profession:
                readable += ' job:' + self.profession
            if self.pregnant:
                readable += ', pregnant'
        else:
            readable = self.charType
        return readable
