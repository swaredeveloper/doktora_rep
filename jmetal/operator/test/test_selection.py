import unittest

from hamcrest import *

from jmetal.core.solution import Solution
from jmetal.operator.selection import BinaryTournament, BestSolution, RandomSolution, NaryRandomSolution, \
    RankingAndCrowdingDistanceSelection

__author__ = "Antonio J. Nebro"


class BinaryTournamentTestCases(unittest.TestCase):
    def setUp(self):
        self.selection = BinaryTournament[Solution]()

    def test_should_constructor_create_a_non_null_object(self):
        self.assertIsNotNone(self.selection)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_none(self):
        solution_list = None
        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_empty(self):
        solution_list = []
        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_return_the_solution_in_a_list_with_one_solution(self):
        solution = Solution(3,2)
        solution_list = [solution]

        self.assertEqual(solution, self.selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_two_non_dominated_solutions(self):
        solution1 = Solution(2,2)
        solution1.variables = [1.0, 2.0]
        solution2 = Solution(2,2)
        solution2.variables = [0.0, 3.0]

        solution_list = [solution1, solution2]

        assert_that(any_of(solution1 , solution2), self.selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_two_solutions_and_one_them_is_dominated(self):
        solution1 = Solution(2,2)
        solution1.variables = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.variables = [0.0, 3.0]

        solution_list = [solution1, solution2]

        assert_that(solution2, self.selection.execute(solution_list))


class BestSolutionSelectionTestCases(unittest.TestCase):
    def setUp(self):
        self.selection = BestSolution[Solution]()

    def test_should_constructor_create_a_non_null_object(self):
        self.assertIsNotNone(self.selection)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_none(self):
        solution_list = None

        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_empty(self):
        solution_list = []
        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_return_the_solution_in_a_list_with_one_solution(self):
        solution = Solution(3,2)
        solution_list = [solution]

        self.assertEqual(solution, self.selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_two_non_dominated_solutions(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 2.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]

        solution_list = [solution1, solution2]

        self.assertTrue(self.selection.execute(solution_list) in solution_list)

    def test_should_execute_work_if_the_solution_list_contains_two_solutions_and_one_them_is_dominated(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]

        solution_list = [solution1, solution2]

        self.assertEqual(solution2, self.selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_five_solutions_and_one_them_is_dominated(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]
        solution3 = Solution(2,2)
        solution3.objectives = [0.0, 4.0]
        solution4 = Solution(2,2)
        solution4.objectives = [1.0, 3.0]
        solution5 = Solution(2,2)
        solution5.objectives = [0.2, 4.4]

        solution_list = [solution1, solution2, solution3, solution4, solution5]

        self.assertEqual(solution2, self.selection.execute(solution_list))


class RandomSolutionSelectionTestCases(unittest.TestCase):

    def setUp(self):
        self.selection = RandomSolution[Solution]()

    def test_should_constructor_create_a_non_null_object(self):
        self.assertIsNotNone(self.selection)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_none(self):
        solution_list = None
        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_empty(self):
        solution_list = []
        with self.assertRaises(Exception):
            self.selection.execute(solution_list)

    def test_should_execute_return_the_solution_in_a_list_with_one_solution(self):
        solution = Solution(3,2)
        solution_list = [solution]

        self.assertEqual(solution, self.selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_two_non_dominated_solutions(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 2.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]

        solution_list = [solution1, solution2]

        self.assertTrue(self.selection.execute(solution_list) in solution_list)

    def test_should_execute_work_if_the_solution_list_contains_two_solutions_and_one_them_is_dominated(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]

        solution_list = [solution1, solution2]

        self.assertTrue(self.selection.execute(solution_list) in solution_list)

    def test_should_execute_work_if_the_solution_list_contains_five_solutions_and_one_them_is_dominated(self):
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]
        solution3 = Solution(2,2)
        solution3.objectives = [0.0, 4.0]
        solution4 = Solution(2,2)
        solution4.objectives = [1.0, 3.0]
        solution5 = Solution(2,2)
        solution5.objectives = [0.2, 4.4]

        solution_list = [solution1, solution2, solution3, solution4, solution5]
        self.assertTrue(self.selection.execute(solution_list) in solution_list)


class NaryRandomSolutionSelectionTestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_constructor_create_a_non_null_object(self):
        selection = NaryRandomSolution[Solution]()
        self.assertIsNotNone(selection)

    def test_should_constructor_create_a_non_null_object_and_check_number_of_elements(self):
        selection = NaryRandomSolution[Solution](3)
        self.assertEqual(selection.number_of_solutions_to_be_returned, 3)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_none(self):
        selection = NaryRandomSolution[Solution]()
        solution_list = None
        with self.assertRaises(Exception):
            selection.execute(solution_list)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_empty(self):
        selection = NaryRandomSolution[Solution]()
        solution_list = []
        with self.assertRaises(Exception):
           selection.execute(solution_list)

    def test_should_execute_raise_an_exception_if_the_list_of_solutions_is_smaller_than_required(self):
        selection = NaryRandomSolution[Solution](4)
        solution_list = [Solution(1,1), Solution(1,1)]
        with self.assertRaises(Exception):
           selection.execute(solution_list)

    def test_should_execute_return_the_solution_in_a_list_with_one_solution(self):
        selection = NaryRandomSolution[Solution](1)
        solution = Solution(3,2)
        solution_list = [solution]

        self.assertEqual([solution], selection.execute(solution_list))

    def test_should_execute_work_if_the_solution_list_contains_two_non_dominated_solutions(self):
        selection = NaryRandomSolution[Solution](2)
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 2.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]

        solution_list = [solution1, solution2]

        selection_result = selection.execute(solution_list)
        self.assertTrue(selection_result[0] in solution_list)
        self.assertTrue(selection_result[1] in solution_list)

    def test_should_execute_work_if_the_solution_list_contains_five_solutions_and_one_them_is_dominated(self):
        selection = NaryRandomSolution[Solution](1)
        solution1 = Solution(2,2)
        solution1.objectives = [1.0, 4.0]
        solution2 = Solution(2,2)
        solution2.objectives = [0.0, 3.0]
        solution3 = Solution(2,2)
        solution3.objectives = [0.0, 4.0]
        solution4 = Solution(2,2)
        solution4.objectives = [1.0, 3.0]
        solution5 = Solution(2,2)
        solution5.objectives = [0.2, 4.4]

        solution_list = [solution1, solution2, solution3, solution4, solution5]

        self.assertTrue(selection.execute(solution_list)[0] in solution_list)


class DominanceRankingTestCases(unittest.TestCase):
    def setUp(self):
        self.ranking_and_crowding_selection = RankingAndCrowdingDistanceSelection(5)

    def test_should_len_of_nsgaii_execute_be_5(self):
        solution1 = Solution(2, 2)
        solution2 = Solution(2, 2)
        solution3 = Solution(2, 2)
        solution4 = Solution(2, 2)
        solution5 = Solution(2, 2)
        solution6 = Solution(2, 2)

        solution1.objectives[0] = 1.0
        solution1.objectives[1] = 0.0
        solution2.objectives[0] = 0.6
        solution2.objectives[1] = 0.6
        solution3.objectives[0] = 0.5
        solution3.objectives[1] = 0.5
        solution4.objectives[0] = 1.1
        solution4.objectives[1] = 0.0
        solution5.objectives[0] = 0.0
        solution5.objectives[1] = 1.0
        solution6.objectives[0] = 1.05
        solution6.objectives[1] = 0.1

        solution_list = [solution1, solution2, solution3, solution4, solution5, solution6]

        list_of_crowding_and_rankings = self.ranking_and_crowding_selection.execute(solution_list)

        self.assertEqual(len(list_of_crowding_and_rankings), 5)
        self.assertEqual(solution1, list_of_crowding_and_rankings[0])
        self.assertEqual(solution3, list_of_crowding_and_rankings[1])
        self.assertEqual(solution5, list_of_crowding_and_rankings[2])
        self.assertEqual(solution4, list_of_crowding_and_rankings[3])
        self.assertEqual(solution2, list_of_crowding_and_rankings[4])

if __name__ == '__main__':
    unittest.main()
