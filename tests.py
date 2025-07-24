import unittest
from question.Question import Question


class QuestionTest(unittest.TestCase):
    """A set of tests for the Question class"""

    def testStringInputToList(self):
        """Test that this static method takes a string, splits on a comma and returns a list,
        also making sure remove any empty strings from the list"""

        # assert that passing an empty string returns an empty list
        self.assertListEqual(Question.stringInputToList(''), [])

        # assert that empty strings are removed from list.
        # we want to ensure that if two commas are together (,,) the resulting empty string is removed from the list
        s = 'math,add,subtract,,divide'
        self.assertListEqual(Question.stringInputToList(s), ['math', 'add', 'subtract', 'divide'])

        # assert that any trailing or leading whitespace is stripped
        s = '   apple,banana   , pear, melon,     ,,     strawberry   ,'
        self.assertListEqual(Question.stringInputToList(s), ['apple', 'banana', 'pear', 'melon', 'strawberry'])

    def setUp(self):
        # create a question
        self.__question = Question('A test question', 'an answer', ['tag1', 'tag2'], 10, 'ident')

    def testIdent(self):
        # assert ident 'property' is correct
        self.assertEqual(self.__question.ident, 'ident')

    def testQuestion(self):
        # assert question 'property' is correct
        self.assertEqual(self.__question.question, 'A test question')

    def testGetTags(self):
        self.assertListEqual(self.__question.getTags(), ['tag1', 'tag2'])

    def testSetTags(self):
        # assert tags before update
        self.assertListEqual(self.__question.getTags(), ['tag1', 'tag2'])

        # set new tags
        self.__question.setTags(['newTag3', 'newTag4'])

        # assert tags set correctly
        self.assertListEqual(self.__question.getTags(), ['newTag3', 'newTag4'])

    def testGetPoints(self):
        self.assertEqual(self.__question.getPoints(), 10)

    def testSetPoints(self):
        # assert tags before update
        self.assertEqual(self.__question.getPoints(), 10)

        # set new tags
        self.__question.setPoints(20)

        # assert tags set correctly
        self.assertEqual(self.__question.getPoints(), 20)

    def testClone(self):
        # because object is a clone it will have a different 'id' in memory,
        # therefore we can assert that it isn't just the same object being returned
        self.assertNotEqual(self.__question, self.__question.clone())

        # can then use the __dict__ magic methods on the objects to assert that the new object has same properties
        self.assertDictEqual(self.__question.__dict__, self.__question.clone().__dict__)


if __name__ == '__main__':
    unittest.main()
