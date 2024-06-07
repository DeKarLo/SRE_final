import unittest

def get_final_grade_info(term_grade):
    if term_grade < 50:
        return ""

    scholarship: float = round(((70 - term_grade * 0.6) / 0.4), 2)
    retake: float = round(((50 - term_grade * 0.6) / 0.4), 2)
    answer: str = ""

    if retake <= 50:
        answer += "🔴 To avoid retake: *final exam > 50*\n"
    else:
        answer += "🔴 To avoid retake: *final exam > " + str(retake) + "*\n"

    if scholarship <= 50:
        answer += "🟢 To save scholarship: *final exam > 50*\n"
    else:
        answer += "🟢 To save scholarship: *final exam > " + str(scholarship) + "*\n"

    return answer

class TestGetFinalGradeInfo(unittest.TestCase):
    def test_final_grade_info_above_50(self):
        expected_output = "🔴 To avoid retake: *final exam > 50*\n🟢 To save scholarship: *final exam > 85.0*\n"
        self.assertEqual(get_final_grade_info(60), expected_output)
        
if __name__ == '__main__':
    unittest.main()

