from typing import List


def formatMenuOptions(options: List[str]) -> str:
  result = ''

  for index, option in enumerate(options, 1):
    onLastIndex = (index == len(options) )

    result += f'{index}) {option}'
    result += '\n' if not onLastIndex else ''

  return result

def formatQuestionString(question: str) -> str:
  return f'Question: "{question}"'

def formatSolutionString(solution: str) -> str:
  return f'Solution: "{solution}"'

