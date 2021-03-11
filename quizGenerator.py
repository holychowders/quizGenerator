#!/usr/bin/python3

from collections import namedtuple

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
    print("Type an integer to answer.")
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

