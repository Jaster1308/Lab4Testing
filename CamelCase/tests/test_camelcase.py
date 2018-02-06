import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentcence(self):

        self.assertEqual('helloWorld', camelcase.camelcase('Hello World'))