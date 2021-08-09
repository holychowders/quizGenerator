from src.quizGenerator import fileOperations, formatting, messages

import random

from typing import Any, List


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

  randomizedProblemSet = randomizeCollection(problems)

  return randomizedProblemSet

def randomizeCollection(collection: Any) -> List[Any]:
  collectionRandom = random.sample(collection, k=len(collection))

  return collectionRandom

def displayQuestionAndOptions(question: str, options: List[str]) -> None:
  print(f"\nQuestion:\n{question}")
  print(f"\n{formatting.formatMenuOptions(options)}\n")

