import random
import time

class AdaptiveQuestionManager:

    def __init__(self):

        self.easy = [
            "What is your favorite food?",
            "What do you usually do on weekends?",
            "Do you like watching movies?"
        ]

        self.medium = [
            "What do you think about artificial intelligence?",
            "Describe a memorable moment from your life.",
            "If you could travel anywhere, where would you go?"
        ]

        self.hard = [
            "What makes humans different from machines?",
            "How do emotions influence human decisions?",
            "What do you think is the meaning of life?"
        ]

    def get_question(self, difficulty):

        if difficulty == "easy":
            return random.choice(self.easy)

        elif difficulty == "medium":
            return random.choice(self.medium)

        else:
            return random.choice(self.hard)


class AIAgent:

    def respond(self, question):

        responses = [
            "That is an interesting question. I think it depends on the situation.",
            "I enjoy thinking about such topics.",
            "Humans usually have different perspectives on that.",
            "It can vary depending on personal experience.",
            "I believe it requires deeper understanding."
        ]

        return random.choice(responses)


class ResponseAnalyzer:

    def analyze(self, response, response_time):

        score = 0

        if len(response.split()) > 4:
            score += 1

        if response.endswith("."):
            score += 1

        if response_time > 1:
            score += 1

        return score


class TuringTest:

    def __init__(self):

        self.q_manager = AdaptiveQuestionManager()
        self.ai = AIAgent()
        self.analyzer = ResponseAnalyzer()

    def run(self):

        print("\n------ ADAPTIVE TURING TEST ------")

        participants = ["A", "B"]
        ai_participant = random.choice(participants)

        difficulty = "easy"

        scores = {"A": 0, "B": 0}

        for round_num in range(3):

            print("\nRound", round_num + 1)

            question = self.q_manager.get_question(difficulty)

            print("Judge asks:", question)

            if ai_participant == "A":

                start = time.time()
                time.sleep(random.uniform(1, 2))
                response_A = self.ai.respond(question)
                end = time.time()

                print("Participant A:", response_A)

            else:

                start = time.time()
                response_A = input("Human Participant A: ")
                end = time.time()

            time_A = end - start
            scores["A"] += self.analyzer.analyze(response_A, time_A)

            if ai_participant == "B":

                start = time.time()
                time.sleep(random.uniform(1, 2))
                response_B = self.ai.respond(question)
                end = time.time()

                print("Participant B:", response_B)

            else:

                start = time.time()
                response_B = input("Human Participant B: ")
                end = time.time()

            time_B = end - start
            scores["B"] += self.analyzer.analyze(response_B, time_B)

            avg_score = (scores["A"] + scores["B"]) / 2

            if avg_score < 2:
                difficulty = "easy"
            elif avg_score < 4:
                difficulty = "medium"
            else:
                difficulty = "hard"

        print("\n--- Conversation Finished ---")
        print("Scores:", scores)

        guess = input("Judge: Who is the AI? (A/B): ").upper()

        if guess == ai_participant:
            print("Correct! You identified the AI.")
        else:
            print("Wrong! The AI fooled the judge.")

        print("AI was Participant", ai_participant)


test = TuringTest()
test.run()