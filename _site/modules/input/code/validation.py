
def form():
  """The form function that collects info from users"""
  # Get street number
  streetNum = get_street_num()
  # Get the age
  age = get_age()

  # Collect more pieces of information by writing more functions

  # Then, print out all our collected info in a form
  print("=====================")
  print("We've collected the following information:")
  print("- Street Number:", streetNum)
  print("- Age:", age)
  # add more
  print("=====================")


def get_street_num():
  """ EXAMPLE: Gets the user's street number.
  Repeats until a valid street number is given.
  Output:
  - streetNum: an integer representing the user's street number
  """
  streetNum = input("Enter the street number of your address: ")

  # Check to see if it's empty!
  if streetNum == "":
    print("SORRY! You forgot to input your street number!\n")
    return get_street_num()
  # Check to see if it's a number!
  elif streetNum.isdigit() == False:
    print("SORRY! Your street number should be a positive number\n")
    return get_street_num()
  else:
    return streetNum

def get_age():
  """ Gets the user's age
  Repeats until a valid age is given
  """
  age = input("Enter your age: ")
  # WRITE MORE CODE HERE
  return age


# TODO: WRITE MORE FUNCTIONS THAT CHECK INPUT!


# Runs the primary program
form()
