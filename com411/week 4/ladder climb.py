def ladder_climb (steps_left, steps_crossed):
    if steps_left > steps_crossed:
        return "Still some way to go!"
    else:
        return "We are almost there!"

print (ladder_climb(5, 5))
