from src.quizGenerator import formatting


def test_formatMenuOptions() -> None:
  assert formatting.formatMenuOptions(('option 1', 'option 2')) == '1) option 1\n2) option 2'

def test_formatQuestionString() -> None:
  assert formatting.formatQuestionString('sample question 1') == 'Question: "sample question 1"'

def test_formatSolutionString() -> None:
  assert formatting.formatSolutionString('sample option 3') == 'Solution: "sample option 3"'

