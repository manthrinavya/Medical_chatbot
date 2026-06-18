def recognize_entities(text):

    symptoms = [
        "fever",
        "cough",
        "headache",
        "fatigue",
        "pain"
    ]

    diseases = [
        "diabetes",
        "cancer",
        "asthma",
        "leukemia"
    ]

    treatments = [
        "surgery",
        "therapy",
        "insulin",
        "chemotherapy"
    ]

    entities = []

    words = text.lower().split()

    for word in words:

        if word in symptoms:
            entities.append(("Symptom", word))

        elif word in diseases:
            entities.append(("Disease", word))

        elif word in treatments:
            entities.append(("Treatment", word))

    return entities