from src.quizGenerator import files, formatting
from src.quizGenerator.constants import *

import random
from os.path import splitext
from time import sleep

from typing import List, Tuple


def main() -> int:
  printProgramHeader()
  topic, worksheet = promptWorksheetSelection()
  runGame(topic, worksheet)

  return 0

def promptWorksheetSelection() -> Tuple[str, str]:
  topicSelection = promptTopicSelection()

  worksheetOptions = files.getWorksheetOptions(topicSelection)
  worksheetOptionsNoFileExt = [ splitext(path)[0] for path in worksheetOptions ]

  print(f'\nWorksheets:\n{formatting.formatMenuOptions(worksheetOptionsNoFileExt)}\n')
  worksheetSelection = promptMenuSelection(worksheetOptions)

  return topicSelection, worksheetSelection

def promptTopicSelection() -> str:
  topicOptions = files.getTopicOptions()

  print(f'\nTopics:\n{formatting.formatMenuOptions(topicOptions)}\n')
  topicSelection = promptMenuSelection(topicOptions)

  return topicSelection

def runGame(topic: str, worksheet: str) -> None:
  printStartHeader()
  problems = loadProblems(topic, worksheet)
  promptProblemSetSolution(problems)

  #TODO

def printProgramHeader():
  print(f'\n{PROGRAM_HEADER}')

def printStartHeader():
  print(f'\n{GAME_START_HEADER}')

def loadProblems(topic: str, worksheet: str) -> List[files.Problem]:
  problems = files.getProblemsFromWorksheet(topic, worksheet)
  randomizedProblemSet = random.sample(problems, k=len(problems))

  return randomizedProblemSet

def promptProblemSetSolution(problems: List[files.Problem]) -> int:
  for problemNumber, problem in enumerate(problems):
    addBlankLineIfFirstProblem(problemNumber)
    selection = promptProblemSolution(problem)
    tellIfCorrect(selection, problem.solution)
    sleep(1)

def addBlankLineIfFirstProblem(problemNumber: int) -> None:
  print()

def promptProblemSolution(problem):
  options = problem.options

  displayProblem(problem)
  selection = promptMenuSelection(options)

  return selection

def displayProblem(problem: files.Problem) -> None:
  options, question = problem.options, problem.question

  formattedOptions = formatting.formatMenuOptions(options)
  print(f"\nQuestion:\n{question}")
  print(f"\n{formattedOptions}\n")

def promptMenuSelection(options: List[str], message: str = 'Selection: ') -> str:
  try:
    intSelection = int(input(message))
    assert (intSelection >= 1), NOT_A_VALID_INTEGER_ERR_MSG
    option = options[intSelection - 1]

  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return promptMenuSelection(options, message)
  except IndexError:
    print(NOT_A_VALID_INTEGER_ERR_MSG)
    return promptMenuSelection(options, message)
  except AssertionError as ae:
    print(ae.args[0])
    return promptMenuSelection(options, message)

  return option

def tellIfCorrect(option: str, solution: str):
  if option == solution:
    print(CORRECT_ANSWER_MSG)
  else:
    print(INCORRECT_ANSWER_MSG)

