def study_schedule(permanence_period, target_time):
    students = 0

    for entrance_time, exit_time in permanence_period:
        try:
            if entrance_time <= target_time <= exit_time:
                students += 1
        except TypeError:
            return None
    return students