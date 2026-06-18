import os
import xml.etree.ElementTree as ET

def load_dataset():
    questions = []
    answers = []

    dataset_path = "data/MedQuAD-master"

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".xml"):

                file_path = os.path.join(root, file)

                try:
                    tree = ET.parse(file_path)
                    xml_root = tree.getroot()

                    for qa in xml_root.iter("QAPair"):

                        question = qa.find("Question")
                        answer = qa.find("Answer")

                        if question is not None and answer is not None:

                            q_text = "".join(question.itertext()).strip()
                            a_text = "".join(answer.itertext()).strip()

                            if q_text and a_text:
                                questions.append(q_text)
                                answers.append(a_text)

                except Exception as e:
                    print("Error:", file, e)

    return questions, answers