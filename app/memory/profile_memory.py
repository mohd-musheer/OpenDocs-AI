profile_memory = {}


def save_fact(key, value):
    profile_memory[key] = value


def get_profile():
    return profile_memory