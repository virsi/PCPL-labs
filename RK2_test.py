import unittest
from RK2_main import (Faculty, University, query_a1, query_a2, query_a3,
                      prepare_one_to_many, prepare_many_to_many)

class TestRK2(unittest.TestCase):

    def setUp(self):
        self.facs = [
            Faculty(1, 'Технический факультет'),
            Faculty(2, 'Другой отдел')
        ]
        self.unis = [
            University(1, 'Университет 1', 100, 1),
            University(2, 'Университет 2', 50, 1)
        ]
        self.o2m = prepare_one_to_many(self.facs, self.unis)

    def test_query_a1_sorting(self):
        """Тест сортировки по количеству студентов (A1)"""
        result = query_a1(self.o2m)
        self.assertEqual(result[0][1], 50)
        self.assertEqual(result[1][1], 100)

    def test_query_a2_sum(self):
        """Тест суммирования студентов по факультетам (A2)"""
        result = query_a2(self.facs, self.o2m)
        self.assertEqual(result[0], ('Технический факультет', 150))

    def test_query_a3_filter(self):
        """Тест фильтрации по слову 'факультет' (A3)"""
        m2m = [('Университет 1', 100, 'Технический факультет'),
               ('Университет 2', 50, 'Другой отдел')]

        result = query_a3(self.facs, m2m)
        self.assertIn('Технический факультет', result)
        self.assertNotIn('Другой отдел', result)
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
