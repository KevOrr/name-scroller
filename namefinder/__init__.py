from namefinder.dictionaries import PERIODIC_TABLE

def get_choices(name, parts):
    name = name.lower()
    paths = {}
    found = False
    for part in parts:
        if name.startswith(part.lower()):
            if len(name) > len(part):
                path = get_choices(name[len(part):], parts)
                if path != None:
                    paths[part] = path
                    found = True
            else:
                paths[part] = None
                found = True
    return paths if paths else None

def format_choice_tree(choices, leading='    ', delimiter='\n'):
    def inner(inner_choices, level):
        formatted = []
        for choice in inner_choices:
            formatted.append(leading * level + str(choice))
            if inner_choices[choice] != None:
                formatted.extend(inner(inner_choices[choice], level + 1))
        return formatted
    return delimiter.join(inner(choices, 0))

def flatten_choices(choices):
    flat_choices = []
    for choice in choices:
        if choices[choice] != None:
            flat_choices.extend((choice,) + branch for branch in get_flattened_choices(choices[choice]))
        else:
            flat_choices.append((choice,))
    return flat_choices

def demo():
    name = input('What\'s your name: ')
    choices = get_choices(name, PERIODIC_TABLE.keys())
    if not choices:
        print('Couldn\'t construct %s using Periodic Table element symbols only' % repr(name))
        return
    for choice in get_flattened_choices(choices):
        print(' '.join(PERIODIC_TABLE[part] for part in choice))
