def analyze_scores(records):
    total = 0
    names = ()
    for name, score in records:
        if score >= 50:
            names += (name,)
            total += score
    return names, total

data = (('Alice', 45), ('Bob', 60), ('Charlie', 75))
print(analyze_scores(data))