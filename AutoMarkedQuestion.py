from question.Question import Question


class AutoMarkedQuestion(Question):
    """A Question that can be marked automatically"""

    # Factory style method that determines and creates the correct type of child object from its input
    @staticmethod
    def createFromInput(question, choices, correctAnswer, tags, points):
        # if multiple correct answers then must be a multiple answer question
        if len(correctAnswer) > 1:
            return MultipleAnswerQuestion(question, correctAnswer, tags, points, choices)

        choices = [x.lower() for x in choices.values()]
        if 'true' in choices and 'false' in choices:
            return TrueFalseQuestion(question, correctAnswer, tags, points, choices)

        return MultipleChoiceQuestion(question, correctAnswer, tags, points, choices)


class ArithmeticQuestion(AutoMarkedQuestion):
    """An Arithmetic Question"""
    def __init__(self, question, answer, tags, points):
        super().__init__(question, answer, tags, points)


class ReorderQuestion(AutoMarkedQuestion):
    """A Reorder Question"""
    # Not required for cw1
    pass


class MultipleAnswerQuestion(AutoMarkedQuestion):
    """A Multiple Answer Question"""
    def __init__(self, question, answer, tags, points, choices):
        self.choices = choices
        super().__init__(question, answer, tags, points)

    def getNumCorrectAnswers(self):
        return len(self._answer)


class MultipleChoiceQuestion(MultipleAnswerQuestion):
    """Multiple Choice Question"""
    pass


class TrueFalseQuestion(MultipleAnswerQuestion):
    """True or False Question"""
    pass