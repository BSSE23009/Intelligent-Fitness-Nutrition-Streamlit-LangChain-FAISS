


from langchain.tools import tool



@tool("workout_schedule")
def workout_schedule(query: str ="schedule") -> str:
    """Provides a basic weekly workout schedule."""
    return ("Weekly Workout Schedule:\n"
            "Monday: Legs\n"
            "Tuesday: Arms\n"
            "Wednesday: Rest or Light Cardio\n"
            "Thursday: Chest\n"
            "Friday: Back\n"
            "Saturday: Shoulders\n"
            "Sunday: Rest or Yoga/Stretching")

@tool
def workout_recommender(goal: str) ->str:
    """Recommends a workout plan based on the user's preference."""
    goal = goal.lower()
    workouts = {
        "legs": "Leg Workout: Squats, Lunges, Deadlifts (3 sets of 10 reps each).",
        "arms": "Arm Workout: Bicep Curls, Tricep Dips, Push-ups (3 sets of 12 reps).",
        "chest": "Chest Workout: Bench Press, Push-ups, Dumbbell Flys.",
        "back": "Back Workout: Pull-ups, Barbell Rows, Deadlifts.",
        "shoulders": "Shoulder Workout: Overhead Press, Lateral Raises, Arnold Press."
    }
    return workouts.get(goal, "Sorry, I don't have a workout plan for that goal. Please choose from legs, arms, chest, back, or shoulders.")


@tool
def suggest_alternatives(goal: str) -> str:
    """Suggests the alternative exercise if the user cannot perform the recommended one."""

    goal =goal.lower()
    alternatives = {
        "squats": "Try step-ups or leg press.",
        "push-ups": "Try bench press or chest press machine.",
        "pull-ups": "Try lat pull-downs or rows.",
        "deadlifts": "Try hip thrusts or Romanian deadlifts with lighter weight."
    }
    return alternatives.get(goal, "Sorry, I don't have an alternative for that exercise. You can do a light variation of the exercise. ")

@tool
def workout_duration(goal: str) -> str:
    """Tells the user how long should workout for this goal."""
    goal = goal.lower()
    duration ={
        "legs": "Leg day usually takes 45–60 minutes.",
        "arms": "Arm workouts typically last 30–45 minutes.",
        "chest": "Chest workouts take 40–60 minutes.",
        "back": "Back day lasts about 45–70 minutes.",
        "shoulders": "Shoulder workouts are around 30–45 minutes."
    }

    return duration.get(goal, "Sorry, I don't have a duration for that goal. A general workout session lasts between 30 to 60 minutes.")

@tool
def warmup_recommendation(query: str = "warmup") -> str:
    """Recommends a warm-up routine before starting the workout."""
    return ("Warm-up Routine: 5-10 minutes of light cardio (jogging, cycling) followed by dynamic stretches like leg swings, arm circles, and torso twists.")


@tool 
def cooldown_recommendation(query: str = "recoommendation") -> str:
    """Recommends a cool-down routine after finishing the workout."""
    return ("Cool-down Routine: 5-10 minutes of light cardio followed by static stretches focusing on the muscles worked during the session.")