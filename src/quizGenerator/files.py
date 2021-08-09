import json
import pathlib
from dataclasses import dataclass

from typing import List


TOPICS_DIRECTORY = str(pathlib.Path(__file__).parent) + '/../../quizzes/topics'


@dataclass
class Problem:
  question: str
  options: List[str]
  solution: str

def _getPathBasename(path: str) -> str:
  return pathlib.PurePath(path).name

def getTopicOptions() -> List[str]:
  topicPaths = glob(TOPICS_DIRECTORY, '*')
  topicBasenames = [_getPathBasename(path) for path in topicPaths]

  return topicBasenames

def getWorksheetOptions(topic: str) -> List[str]:
  worksheetPaths = glob(f'{TOPICS_DIRECTORY}/{topic}/', '*')
  worksheetBasenames = [_getPathBasename(path) for path in worksheetPaths]

  return worksheetBasenames

def glob(path: str, pattern: str) -> List[str]:
  files = pathlib.Path(path).glob(pattern)

  return [path.name for path in files]

def getProblemsFromWorksheet(topic: str, worksheet: str) -> List[Problem]:
  with open(f'{TOPICS_DIRECTORY}/{topic}/{worksheet}') as f:
    worksheetDict = json.load(f)

  problems = list()
  for _problemName, problemDict in worksheetDict.items():
    problemObj = Problem(
      question = problemDict['question'],
      options = [ problemDict['options'][option] for option in problemDict['options'] ],
      solution = problemDict['options'][problemDict['solution']]
    )

    problems.append(problemObj)

  return problems

