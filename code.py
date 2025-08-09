import pandas as pd

# Seus 1RMs
lifts_1rm = {
    "Back Squat": 144.2,
    "Bench Press": 89.9,
    "Overhead Press": 29.1,
    "Deadlift": 150.0
}

# Cálculo da Training Max (90% do 1RM)
training_max = {lift: round(weight * 0.9, 1) for lift, weight in lifts_1rm.items()}

# Percentuais por semana
percentages = {
    "Semana 1 (3x5)": [0.65, 0.75, 0.85],
    "Semana 2 (3x3)": [0.70, 0.80, 0.90],
    "Semana 3 (5/3/1)": [0.75, 0.85, 0.95],
    "Semana 4 (Deload)": [0.40, 0.50, 0.60]
}

# Geração das tabelas
tables = {}
for lift, tm in training_max.items():
    rows = []
    for week, percents in percentages.items():
        for i, pct in enumerate(percents):
            if "3x3" in week:
                reps = ["3", "3", "3+"]
            elif "5/3/1" in week:
                reps = ["5", "3", "1+"]
            elif "Deload" in week:
                reps = ["5", "5", "5"]
            else:
                reps = ["5", "5", "5+"]
            rows.append({
                "Semana": week,
                "Série": i + 1,
                "Repetições": reps[i],
                "Carga (kg)": round(tm * pct, 1)
            })
    df = pd.DataFrame(rows)
    tables[lift] = df

# Exibindo as tabelas por lift
for lift, df in tables.items():
    print(f"\n=== {lift} ===")
    print(df.to_string(index=False))
