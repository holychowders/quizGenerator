from src.quizGenerator.tui import helpers
from src.quizGenerator import formatting, messages, fileOperations


def main():
  topic, worksheet = runMainMenu()
  runGame(topic, worksheet)

  return 0

def runMainMenu():
  print(messages.TITLE_HEADER)

  topicOptions = fileOperations.getTopicOptions()
  print(f'\nTopics:\n{formatting.formatMenuOptions(topicOptions)}\n')
  topicSelection = helpers.userSelectFromMenu(topicOptions)
  print(f'Topic: {topicSelection}')

  worksheetOptions = fileOperations.getWorksheetOptions(topicSelection) 
  print(f'\nWorksheets:\n{formatting.formatMenuOptions(worksheetOptions)}\n')
  worksheetSelection = helpers.userSelectFromMenu(worksheetOptions)
  print(f'Worksheet: {worksheetSelection}')

  return topicSelection, worksheetSelection

def runGame(topic, worksheet):
  print(f'\n{messages.GAME_START_HEADER}')
  problems = fileOperations.getProblemsFromWorksheet(topic, worksheet)
  #TODO


