import pathlib
from collections import namedtuple


WORKSHEET_DELIMITER = ' --- '

TOPICS_DIRECTORY = str(pathlib.Path(__file__).parent) + '/../../topics'


def getPathBasename(path):
  path = pathlib.PurePath(path)

  return path.name

def getTopicOptions():
  topicPaths = glob(TOPICS_DIRECTORY, '*')
  topicBasenames = [getPathBasename(path) for path in topicPaths]

  return topicBasenames

def getWorksheetOptions(topic):
  worksheetPaths = glob(f'{TOPICS_DIRECTORY}/{topic}/', '*')
  worksheetBasenames = [getPathBasename(path) for path in worksheetPaths]

  return worksheetBasenames

def glob(path, pattern):
  files = pathlib.Path(path).glob(pattern)

  return [path.name for path in files]

def getProblemsFromWorksheet(topic, worksheet):
  worksheet = parseWorksheet(topic, worksheet)
  problems = list()

  for line in worksheet:
    questionAndSolution = line[:2]
    options = line[2:]

    problems.append(Problem(*questionAndSolution, options))

  return problems

Problem = namedtuple("Problem", ("question", "solution", "options"))

def parseWorksheet(topic, worksheet):
  with open(f"{TOPICS_DIRECTORY}/{topic}/{worksheet}") as worksheet:
    lines = worksheet.readlines()
    cleanedLines = [line.strip('\n').split(WORKSHEET_DELIMITER) for line in lines]

    return cleanedLines

def verifyTopicsPathExists():
  topicsPath = pathlib.Path(TOPICS_DIRECTORY)

  return topicsPath.is_dir()

