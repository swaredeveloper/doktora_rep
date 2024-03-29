import logging
from typing import List

from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.core.solution import FloatSolution
from jmetal.operator.crossover import SBX
from jmetal.operator.mutation import Polynomial
from jmetal.operator.selection import BinaryTournament
from jmetal.testfunctions.multiobjectiveproblem import Kursawe, Fonseca, Schaffer, Viennet2
from jmetal.component.observer import WriteFrontToFileObserver, AlgorithmObserver
from jmetal.util.solution_list_output import SolutionListOutput
from jmetal.util.time import get_time_of_execution

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@get_time_of_execution
def main() -> None:
    problem = Kursawe()
    algorithm = NSGAII[FloatSolution, List[FloatSolution]](
        problem,
        population_size=100,
        max_evaluations=25000,
        mutation=Polynomial(1.0/problem.number_of_variables, distribution_index=20),
        crossover=SBX(1.0, distribution_index=20),
        selection=BinaryTournament())

    observer = WriteFrontToFileObserver("output_directory")
    algorithm.observable.register(observer=observer)

    algorithm.run()

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())

if __name__ == '__main__':
    main()
