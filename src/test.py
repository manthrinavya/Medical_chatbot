from src.load_data import load_dataset

questions, answers = load_dataset()

print("Questions:", len(questions))
print("Answers:", len(answers))

if questions:
    print(questions[0])