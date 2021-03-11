#!/usr/bin/python3

import os
import glob
from collections import namedtuple

TITLE_HEADER = '---- Quiz Generator ----\n'
NOT_AN_INTEGER_ERR_MSG = 'Type an integer to answer'


#def main():
#  print(TITLE_HEADER)
#
#  print(getTopicOptions())
#  selection = userSelectFromMenu()
#
#  print(getWorksheetOptions(selection)
#
  #playGame()

def formatMenuOptions(options):
  formattedOptions = ''

  for index, option in enumerate(options, 1):
    formattedOptions += f'\n{index}) {option}'

  return formattedOptions

def userSelectFromMenu():
  try:
    return int(input('Selection: '))
  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return userSelectTopic()

def getTopicOptions():
  topicPaths = glob.glob('./topics/*')
  topicBasenames = [os.path.basename(path) for path in topicPaths]

  return topicBasenames

def getWorksheetOptions(topic):
  worksheetPaths = glob.glob(f'./topics/{topic}/*')
  worksheetBasenames = [os.path.basename(path) for path in worksheetPaths]

  return worksheetBasenames

def formatQuestionString(question):
  return f'\nQuestion: "{question}"\n'

def formatSolutionString(solution):
  return f'\nSolution: "{solution}"\n'

def formatOptionsCollection(options):
  optionsString = ''

  for index, option in enumerate(options, 1):
    optionsString += f'\n{index}) {option}\n'

  return optionsString

def getUsersAnswer():
  answer = input('Your answer: ')

  try:
    return int(answer)
  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return getUsersAnswer()

def checkAnswer(userAnswer, solution):
  return userAnswer == solution

def getProblemsFromWorksheet(topic, worksheet):
  parsedWorksheet = _parseWorksheet(topic, worksheet)
  problems = list()

  for problem in parsedWorksheet:
    questionAndSolution = problem[:2]
    answers = problem[2:]

    problems.append(Problem(*questionAndSolution, answers))

  return problems

Problem = namedtuple("Problem", ("question", "solution", "options"))

def _parseWorksheet(topic, worksheet):
  worksheetProblemsRaw = _getRawWorksheetProblems(topic, worksheet)

  worksheetProblemsRawSplit = []

  for problem in worksheetProblemsRaw:
    worksheetProblemsRawSplit.append(problem.split(" --- "))

  return worksheetProblemsRawSplit

def _getRawWorksheetProblems(topic, worksheet):
  with open(f"./topics/{topic}/{worksheet}") as worksheetFile:
    worksheetProblemsRaw = worksheetFile.readlines()

  return worksheetProblemsRaw

