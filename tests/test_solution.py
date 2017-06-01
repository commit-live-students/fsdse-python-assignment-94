from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import numpy as np
        exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        res = solution(exam_data, labels)

        self.assertEqual(res['attempts']['a'], 1)
        self.assertEqual(res['name']['a'], 'Anastasia')
        self.assertEqual(res['qualify']['b'], 'no')
        self.assertEqual(res['score']['c'], 16.5)
