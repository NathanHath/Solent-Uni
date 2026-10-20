def escape_by(plan):
    if plan == "jumping over":
        return "We cannot escape that way! The boulder is too big!"
    elif plan == "running around":
        return  "We cannot escape that way! The boulder is moving too fast!"
    elif plan == "cross bridge ahead":
        return  "That might just work! Let's go!"
    else:
        return "We cannot escape that way! The boulder is in the way!"

plan = input("What do you want to do? ")
print(escape_by(plan))