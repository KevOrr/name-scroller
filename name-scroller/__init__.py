from namescroller.dictionaries import PERIODIC_TABLE

def get_name(name, *dicts):
    raise NotImplementedError()

def demo():
    name = input('What\'s your name?')
    combinations = get_name(name, PERIODIC_TABLE[0]) or get_name(name, *PERIODIC_TABLE)
    if not combinations:
        print 'Couldn\'t construct %s using Periodic Table element symbols only'
        return None
    for combination in combinations:
        print combination[0]
