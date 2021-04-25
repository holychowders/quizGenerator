from src.quizGenerator.tui import helpers
from src.quizGenerator import messages

import time


def main():
  topic, worksheet = runMainMenu()
  runGame(topic, worksheet)

  return 0


def runMainMenu():
  print(messages.TITLE_HEADER)

  topicSelection = helpers.getTopicFromUser()
  worksheetSelection = helpers.getWorksheetFromUser(topicSelection)

  return topicSelection, worksheetSelection


def runGame(topic, worksheet):
  print(f'\n{messages.GAME_START_HEADER}')

  problems = helpers.getProblems(topic, worksheet)

  for problemNumber, problem in enumerate(problems):

    if problemNumber > 0: print()
    helpers.displayQuestionAndOptions(problem.question, problem.options)

    selection = helpers.userSelectFromMenu(problem.options)
    selectionIsCorrect = (selection == problem.solution)

    if selectionIsCorrect: print(messages.CORRECT_ANSWER)
    else: print(messages.INCORRECT_ANSWER)

    time.sleep(1)

  #TODO
