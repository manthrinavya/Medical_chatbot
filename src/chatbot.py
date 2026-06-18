from load_data import load_dataset
from retriever import Retriever
from entity_recognition import recognize_entities

print("Loading MedQuAD Dataset...")

questions, answers = load_dataset()

print("Dataset Loaded Successfully")

retriever = Retriever(
    questions,
    answers
)

def get_response(query):

    entities = recognize_entities(query)

    answer = retriever.get_answer(query)

    return answer, entities