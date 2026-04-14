@app.route("/fitness")
def fitness_page():
    workouts = [
        {"day": "Dushanba",   "exercise": "Yugurish",    "duration": 30, "calories": 280},
        {"day": "Seshanba",   "exercise": "Suzish",      "duration": 45, "calories": 400},
        {"day": "Chorshanba", "exercise": "Velosiped",   "duration": 60, "calories": 500},
        {"day": "Payshanba",  "exercise": "Dam olish",   "duration": 0,  "calories": 0},
        {"day": "Juma",       "exercise": "Yoga",        "duration": 40, "calories": 180},
        {"day": "Shanba",     "exercise": "Og'irlik",    "duration": 50, "calories": 350},
        {"day": "Yakshanba",  "exercise": "Dam olish",   "duration": 0,  "calories": 0},
    ]

    goal_calories = 2000
    total_calories = sum(w["calories"] for w in workouts)
    remaining = goal_calories - total_calories

    return render_template(
        "fitness.html",
        workouts=workouts,
        total_calories=total_calories,
        remaining=remaining
    )
