import logging

from jmetal.algorithm.singleobjective.evolutionaryalgorithm import GenerationalGeneticAlgorithm
from jmetal.core.solution import BinarySolution, FloatSolution
from jmetal.operator.crossover import SinglePoint, SBX
from jmetal.operator.mutation import BitFlip, Polynomial
from jmetal.operator.selection import BinaryTournament
from jmetal.problem.singleobjectiveproblem import OneMax, Sphere

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    variables = 10
    problem = Sphere(variables)
    algorithm = GenerationalGeneticAlgorithm[FloatSolution, FloatSolution](
        problem,
        population_size=100,
        max_evaluations=25000,
        mutation=Polynomial(1.0/variables, distribution_index=20),
        crossover=SBX(1.0, distribution_index=20),
        selection=BinaryTournament())

    algorithm.run()
    result = algorithm.get_result()

    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())
    logger.info("Solution: " + str(result.variables))
    logger.info("Fitness:  " + str(result.objectives[0]))

if __name__ == '__main__':
    main()
