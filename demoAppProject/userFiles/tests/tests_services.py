from django.test import TestCase
from userFiles.services import get_number_of_lines_in_file


class GetNumberOfLinesInfile(TestCase):
    def test_file_5_lines(self):
        result = get_number_of_lines_in_file('userFiles/tests/test_text_files/file_5_line.txt')
        TestCase.assertEqual(self, result, 5)

    def test_file_0_lines(self):
        result = get_number_of_lines_in_file('userFiles/tests/test_text_files/file_0_line.txt')
        TestCase.assertEqual(self, result, 0)
