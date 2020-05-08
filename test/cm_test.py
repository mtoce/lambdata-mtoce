import unittest

from my_lambdata.cm import c_matrix

# y_actual = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
# y_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]


class TestCM(unittest.TestCase):
    def test_cm(self):
        y_actual = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
        y_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
        cm = c_matrix(y_actual, y_predicted)
        cm1 = cm.confusion_matrix(y_actual, y_predicted)

        # check that #columns==3
        self.assertEqual(len(cm1.columns), 3)

        # check that #rows==3
        self.assertEqual(len(cm1), 3)


if __name__ == "__main__":
    unittest.main()
