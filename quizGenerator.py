#!/usr/bin/env python

import os
import glob
from collections import namedtuple


TITLE_HEADER = '---- Quiz Generator ----'
GAME_START_HEADER = '---- Start ----'

# Delimeter used for parsing each worksheet line containing a problem, solution, and answers.
WORKSHEET_DELIMITER = ' --- '

NOT_AN_INTEGER_ERR_MSG = 'Type an integer to answer'
NOT_A_VALID_INTEGER_ERR_MSG = 'Not a valid selection'


def main():
  topic, worksheet = runMainMenu()
  runGame(topic, worksheet)

# Not in test suite
def runMainMenu():
  print(TITLE_HEADER)

  topicOptions = getTopicOptions()
  print(f'\nTopics:\n{formatMenuOptions(topicOptions)}\n')
  topicSelection = userSelectFromMenu(topicOptions)
  print(f'Topic: {topicSelection}')

  worksheetOptions = getWorksheetOptions(topicSelection) 
  print(f'\nWorksheets:\n{formatMenuOptions(worksheetOptions)}\n')
  worksheetSelection = userSelectFromMenu(worksheetOptions)
  print(f'Worksheet: {worksheetSelection}')

  return topicSelection, worksheetSelection

def runGame(topic, worksheet):
  print(f'\n{GAME_START_HEADER}')
  problems = getProblemsFromWorksheet(topic, worksheet)
  #TODO


### MAIN PARTITION ABOVE ###

### MISC BELOW ###


Problem = namedtuple("Problem", ("question", "solution", "options"))

def checkAnswer(userAnswer, solution):
  return userAnswer == solution


### FORMATTING BELOW ###


def formatMenuOptions(options):
  result = ''

  for index, option in enumerate(options, 1):
    onLastIndex = (index == len(options) )

    result += f'{index}) {option}'
    result += '\n' if not onLastIndex else ''

  return result

## Duplicate?
def formatOptionsCollection(options):
  optionsString = ''

  for index, option in enumerate(options, 1):
    optionsString += f'\n{index}) {option}\n'

  return optionsString

def formatQuestionString(question):
  return f'Question: "{question}"'

def formatSolutionString(solution):
  return f'Solution: "{solution}"'


### USER INTERACTION BELOW ###


def userSelectFromMenu(options, message='Selection: '):
  try:
    intSelection = int(input(message))
    return options[intSelection - 1]

  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except IndexError:
    print(NOT_A_VALID_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)

def getUsersAnswer():
  answer = input('Your answer: ')

  try:
    return int(answer)

  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return getUsersAnswer()


### WORKSHEET STUFF BELOW ###


def getTopicOptions():
  topicPaths = glob.glob('./topics/*')
  topicBasenames = [os.path.basename(path) for path in topicPaths]

  return topicBasenames

def getWorksheetOptions(topic):
  worksheetPaths = glob.glob(f'./topics/{topic}/*')
  worksheetBasenames = [os.path.basename(path) for path in worksheetPaths]

  return worksheetBasenames

def getProblemsFromWorksheet(topic, worksheet):
  parsedWorksheet = _parseWorksheet(topic, worksheet)
  problems = list()

  for problem in parsedWorksheet:
    questionAndSolution = problem[:2]
    answers = problem[2:]

    problems.append(Problem(*questionAndSolution, answers))

  return problems

def _parseWorksheet(topic, worksheet):
  worksheetProblemsRaw = _getRawWorksheetProblems(topic, worksheet)

  worksheetProblemsRawSplit = []

  for problem in worksheetProblemsRaw:
    worksheetProblemsRawSplit.append(problem.split(WORKSHEET_DELIMITER))

  return worksheetProblemsRawSplit

def _getRawWorksheetProblems(topic, worksheet):
  with open(f"./topics/{topic}/{worksheet}") as worksheetFile:
    worksheetProblemsRaw = worksheetFile.readlines()

  return worksheetProblemsRaw


if __name__ == "__main__":
  main()
