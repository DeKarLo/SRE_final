from gpa import get_gpa_by_grade
import unittest

class TestMyModule(unittest.TestCase):
    def test_my_method_to_test_95(self):
        self.assertEqual(get_gpa_by_grade(95), 4)

    def test_my_method_to_test_90(self):
        self.assertEqual(get_gpa_by_grade(90), 3.67)

    def test_my_method_to_test_85(self):
        self.assertEqual(get_gpa_by_grade(85), 3.33)

    def test_my_method_to_test_80(self):
        self.assertEqual(get_gpa_by_grade(80), 3.0)

    def test_my_method_to_test_75(self):
        self.assertEqual(get_gpa_by_grade(75), 2.67)

    def test_my_method_to_test_70(self):
        self.assertEqual(get_gpa_by_grade(70), 2.33)

    def test_my_method_to_test_65(self):
        self.assertEqual(get_gpa_by_grade(65), 2.0)

    def test_my_method_to_test_60(self):
        self.assertEqual(get_gpa_by_grade(60), 1.67)

    def test_my_method_to_test_55(self):
        self.assertEqual(get_gpa_by_grade(55), 1.33)

    def test_my_method_to_test_50(self):
        self.assertEqual(get_gpa_by_grade(50), 1.0)

if __name__ == '__main__':
    unittest.main()
