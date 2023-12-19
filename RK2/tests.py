import unittest

from main import *

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.constructs = [
            SyntaxConstruction(1, 'if-else', 8, 1),  # Python
            SyntaxConstruction(2, 'for', 5, 1),  # Python
            SyntaxConstruction(3, 'function', 2, 2),  # JavaScript
            SyntaxConstruction(4, 'class', 9, 3),  # Java
            SyntaxConstruction(5, 'while', 6, 4),  # C++
            SyntaxConstruction(6, 'def', 3, 5),  # Ruby
        ]
        self.langs = [
            ProgrammingLanguage(1, 'Python'),
            ProgrammingLanguage(2, 'JavaScript Language'),
            ProgrammingLanguage(3, 'Java Language'),
            ProgrammingLanguage(4, 'C++'),
            ProgrammingLanguage(5, 'Ruby Language'),
        ]
        self.lang_construct = [
            LanguageConstruction(1, 1),  # Python - if-else
            LanguageConstruction(1, 2),  # Python - for
            LanguageConstruction(2, 3),  # JavaScript - function
            LanguageConstruction(3, 4),  # Java - class
            LanguageConstruction(4, 5),  # C++ - while
            LanguageConstruction(5, 6),  # Ruby - def
        ]
        self.test_word = 'Language'
        self.test_letter = 'f'

    def test_part1(self):
        result = part1(self.test_word, one_to_many(self.langs, self.constructs))
        self.assertEqual(result,[('JavaScript Language', 'function', 2), ('Java Language', 'class', 9), ('Ruby Language', 'def', 3)])

    def test_part2(self):
        result = part2(one_to_many(self.langs, self.constructs))
        self.assertEqual(result,[('Java Language', 9.0), ('Python', 6.5), ('C++', 6.0), ('Ruby Language', 3.0), ('JavaScript Language', 2.0)])

    def test_part3(self):
        result = part3(self.test_letter,many_to_many(self.langs, self.lang_construct, self.constructs))
        self.assertEqual(result,[('for', 'Python'), ('function', 'JavaScript Language')])
        input("Press any button...")

if __name__ == '__main__':
    unittest.main()