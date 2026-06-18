from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:

    def __init__(self, questions, answers):

        self.questions = questions
        self.answers = answers

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def get_answer(self, query):

        query_vector = self.vectorizer.transform([query])

        similarity = cosine_similarity(
            query_vector,
            self.question_vectors
        )

        best_match = similarity.argmax()

        return self.answers[best_match]
        """
        if len(self.answers)>0:
            return self.answers[best_match]
        return "No answer found."
         """