from src.quizGenerator.tui import helpers
from src.quizGenerator import messages

import time

from typing import Tuple


def main() -> int:
  topic, worksheet = runMainMenu()
  runGame(topic, worksheet)

  return 0


def runMainMenu() -> Tuple[str, str]:
  print(messages.TITLE_HEADER)

  topicSelection = helpers.getTopicFromUser()
  worksheetSelection = helpers.getWorksheetFromUser(topicSelection)

  return topicSelection, worksheetSelection

def runGame(topic: str, worksheet: str) -> None:
  print(f'\n{messages.GAME_START_HEADER}')

  problems = helpers.getProblems(topic, worksheet)

  for problemNumber, problem in enumerate(problems):

    options, question, solution = problem.options, problem.question, problem.solution

    if problemNumber > 0: print()
    helpers.displayQuestionAndOptions(question, options)

    selection = helpers.userSelectFromMenu(options)
    selectionIsCorrect = (selection == solution)

    if selectionIsCorrect: print(messages.CORRECT_ANSWER)
    else: print(messages.INCORRECT_ANSWER)

    time.sleep(1)

  #TODO
