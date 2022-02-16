"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    file_contents = open(filename)
    animals = []
    for line in file_contents:
        record = line.split('|')
        animals.append(record[1])
    species = set(animals)

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    
    file_contents = open(filename)
    villagers = []
    for line in file_contents:
        record = line.split('|')
        if search_string == "All" or record[1] == search_string:
            villagers.append(record[0])
    print(sorted(villagers))
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    file_contents = open(filename)
    #hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    #for hobby in hobbies:
    #    list(hobby.lower())
    #hobby_dict = {"Fitness": [], "Nature": [], "Education": [], "Music": [], "Fashion": [], "Play":[]}
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    for line in file_contents:
        record = line.split('|')
#        for hobby in hobbies:
#            if record[3] == hobby:
#                hobby_dict[hobby].append(record(0))


        if record[3] == 'Fitness':
            fitness.append(record[0])
        if record[3] == 'Nature':
            nature.append(record[0])
        if record[3] == 'Education':
            education.append(record[0])
        if record[3] == 'Music':
            music.append(record[0])
        if record[3] == 'Fashion':
            fashion.append(record[0])
        if record[3] == 'Play':
            play.append(record[0])

    return [sorted(fitness),sorted(nature),sorted(education),sorted(music),sorted(fashion),sorted(play)]
    result = [hobby_dict.get() for hobby in hobbies]
    return result

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    file_contents = open(filename)
    all_data = []
    for line in file_contents:
        record = line.rstrip('\n').split('|')
        record = tuple(record)
        all_data.append(record)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    file_contents = open(filename)
    result = None
    for line in file_contents:
        record = line.rstrip('\n').split('|')
        if record[0] == villager_name:
           result = record[-1] 
    return result

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    file_contents = open(filename)
    result = []
    for line in file_contents:
        record = line.rstrip('\n').split('|')
        if record[0] == villager_name:
            personality = record[2]
            break
    for line in file_contents:
        record = line.rstrip('\n').split('|')
        if record[2] == personality:
            result.append(record[0])         
    return(set(result))
#all_species("villagers.csv")
#get_villagers_by_species("villagers.csv")
#print(all_names_by_hobby("villagers.csv"))
#print(all_data("villagers.csv"))
#print(find_motto("villagers.csv", "Nate"))
#print(find_likeminded_villagers("villagers.csv", "Nate"))