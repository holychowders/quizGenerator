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

