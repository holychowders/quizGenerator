from src.quizGenerator import fileOperations, formatting, messages

import random

from typing import List


def getTopicFromUser() -> str:
  topicOptions = fileOperations.getTopicOptions()

  print(f'\nTopics:\n{formatting.formatMenuOptions(topicOptions)}\n')
  topicSelection = userSelectFromMenu(topicOptions)

  return topicSelection

# TODO: Remove the kwarg
def userSelectFromMenu(options: List[str], message: str = 'Selection: ') -> str:
  try:
    intSelection = int(input(message))
    assert (intSelection >= 1), messages.NOT_A_VALID_INTEGER_ERR_MSG
    option = options[intSelection - 1]

  except ValueError:
    print(messages.NOT_AN_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except IndexError:
    print(messages.NOT_A_VALID_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except AssertionError as ae:
    print(ae.args[0])
    return userSelectFromMenu(options, message)

  return option


def getWorksheetFromUser(topicSelection: str) -> str:
  worksheetOptions = fileOperations.getWorksheetOptions(topicSelection) 

  print(f'\nWorksheets:\n{formatting.formatMenuOptions(worksheetOptions)}\n')
  worksheetSelection = userSelectFromMenu(worksheetOptions)

  return worksheetSelection


def getProblems(topic: str, worksheet: str) -> List[fileOperations.Problem]:
  problems = fileOperations.getProblemsFromWorksheet(topic, worksheet)

  randomizedProblemSet = randomizeProblemSet(problems)

  return list(randomizedProblemSet)

def randomizeProblemSet(problemSet: List[fileOperations.Problem]) -> List[fileOperations.Problem]:
  randomizedProblems = random.sample(problemSet, k=len(problemSet))
  randomizedProblems = randomizeQuestionsInProblemSet(randomizedProblems)

  return randomizedProblems

def randomizeQuestionsInProblemSet(problems: List[fileOperations.Problem]) -> List[fileOperations.Problem]:
  newProblems = []

  for problem in problems:
    randomizedOptions = random.sample(problem.options, k=len(problem.options))

    # This looks confusing. fileOperations.Problem constructs a Problem type. It doesn't have to do with files.
    # It's used to build Problem types when reading problems from files.
    newProblems.append(fileOperations.Problem(problem.question, problem.solution, randomizedOptions))

  return newProblems


def displayQuestionAndOptions(question: str, options: List[str]) -> None:
  print(f"\nQuestion:\n{question}")
  print(f"\n{formatting.formatMenuOptions(options)}\n")

