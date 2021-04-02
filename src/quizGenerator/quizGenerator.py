import pathlib
from collections import namedtuple


TITLE_HEADER = '---- Quiz Generator ----'
GAME_START_HEADER = '---- Start ----'

WORKSHEET_DELIMITER = ' --- '

TOPICS_DIRECTORY = str(pathlib.Path(__file__).parent) + '/../../topics'

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

# Not in test suite
def runGame(topic, worksheet):
  print(f'\n{GAME_START_HEADER}')
  problems = getProblemsFromWorksheet(topic, worksheet)
  #TODO


### MAIN PARTITION ABOVE ###

### PROBLEM-RELATED BELOW ###


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

def formatQuestionString(question):
  return f'Question: "{question}"'

def formatSolutionString(solution):
  return f'Solution: "{solution}"'


### USER INTERACTION BELOW ###


def userSelectFromMenu(options, message='Selection: '):
  try:
    intSelection = int(input(message))
    assert (intSelection >= 1), NOT_A_VALID_INTEGER_ERR_MSG
    option = options[intSelection - 1]

  except ValueError:
    print(NOT_AN_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except IndexError:
    print(NOT_A_VALID_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except AssertionError as ae:
    print(ae.args[0])
    return userSelectFromMenu(options, message)

  return option


### WORKSHEET STUFF BELOW ###


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

def parseWorksheet(topic, worksheet):
  with open(f"{TOPICS_DIRECTORY}/{topic}/{worksheet}") as worksheet:
    lines = worksheet.readlines()
    cleanedLines = [line.strip('\n').split(WORKSHEET_DELIMITER) for line in lines]

    return cleanedLines

def verifyTopicsPathExists():
  topicsPath = pathlib.Path(TOPICS_DIRECTORY)

  return topicsPath.is_dir()


if __name__ == "__main__":
  main()
