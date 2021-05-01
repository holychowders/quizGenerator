import pathlib
from collections import namedtuple

from typing import List


WORKSHEET_DELIMITER = ' --- '
TOPICS_DIRECTORY = str(pathlib.Path(__file__).parent) + '/../../topics'


Problem = namedtuple("Problem", ("question", "solution", "options"))

def getPathBasename(path: str) -> str:
  return pathlib.PurePath(path).name

def getTopicOptions() -> List[str]:
  topicPaths = glob(TOPICS_DIRECTORY, '*')
  topicBasenames = [getPathBasename(path) for path in topicPaths]

  return topicBasenames

def getWorksheetOptions(topic: str) -> List[str]:
  worksheetPaths = glob(f'{TOPICS_DIRECTORY}/{topic}/', '*')
  worksheetBasenames = [getPathBasename(path) for path in worksheetPaths]

  return worksheetBasenames

def glob(path: str, pattern: str) -> List[str]:
  files = pathlib.Path(path).glob(pattern)

  return [path.name for path in files]

def getProblemsFromWorksheet(topic: str, worksheet: str) -> List[Problem]:
  worksheetLines = parseWorksheet(topic, worksheet)
  problems = list()

  for line in worksheetLines:
    questionAndSolution = line[:2]
    options = line[2:]

    problems.append(Problem(*questionAndSolution, options))

  return problems

def parseWorksheet(topic: str, worksheet: str) -> List[List[str]]:
  with open(f"{TOPICS_DIRECTORY}/{topic}/{worksheet}") as worksheetFile:
    lines = worksheetFile.readlines()
    cleanedLines = [line.strip('\n').split(WORKSHEET_DELIMITER) for line in lines]

    return cleanedLines

def verifyTopicsPathExists() -> bool:
  topicsPath = pathlib.Path(TOPICS_DIRECTORY)

  return topicsPath.is_dir()

