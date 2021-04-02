from src.quizGenerator import quizGenerator

import pytest
import io


def test_glob():
  topics = quizGenerator.glob(quizGenerator.TOPICS_DIRECTORY, '*')

  assert ('sampleTopic' in topics) and ('sampleTopic2' in topics)

def test_verifyTopicsPathExists():
  assert quizGenerator.verifyTopicsPathExists() == True

def test_getPathBasename():
  path = 'this/is/a/file.txt'

  assert quizGenerator.getPathBasename(path) == 'file.txt'

def test_userSelectFromMenu_isValid(monkeypatch):
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('1'))
  assert quizGenerator.userSelectFromMenu(options) == 'option 1'

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_isZero(monkeypatch):
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('0'))
  assert quizGenerator.userSelectFromMenu(options) == quizGenerator.NOT_A_VALID_INT_MSG

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_invalidString(monkeypatch):
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('some random non-int string'))
  assert quizGenerator.userSelectFromMenu(options) == quizGenerator.NOT_AN_INTEGER_ERR_MSG

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_invalidInt(monkeypatch):
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('5'))
  assert quizGenerator.userSelectFromMenu(options) == quizGenerator.NOT_A_VALID_INT_MSG

@pytest.mark.skip(reason="I don't know how to do this")
def test_userSelectFromMenu_valueError_canRecover(monkeypatch):
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('5'))
  assert quizGenerator.userSelectFromMenu(options) == quizGenerator.NOT_A_VALID_INT_MSG

  # ...and then somehow try again with valid input into the recursive call which should be returned by the function

def test_formatMenuOptions():
  assert quizGenerator.formatMenuOptions(('option 1', 'option 2')) == '1) option 1\n2) option 2'

def test_getWorksheetOptions_fromSampleTopic():
  worksheetCollection = quizGenerator.getWorksheetOptions('sampleTopic')

  assert 'sampleWorksheet_oneProblem1' in worksheetCollection
  assert 'sampleWorksheet_oneProblem2' in worksheetCollection

def test_getTopicOptions():
  topicsCollection = quizGenerator.getTopicOptions()

  assert 'sampleTopic' in topicsCollection
  assert 'sampleTopic2' in topicsCollection

def test_checkAnswer_isCorrect():
  solution = 'sample option 2'
  answer   = 'sample option 2'

  assert quizGenerator.checkAnswer(answer, solution) == True

def test_checkAnswer_isIncorrect():
  solution = 'sample option 2'
  answer   = 'sample option 1'

  assert quizGenerator.checkAnswer(answer, solution) == False

def test_formatQuestionString():
  assert quizGenerator.formatQuestionString('sample question 1') == 'Question: "sample question 1"'

def test_formatSolutionString():
  assert quizGenerator.formatSolutionString('sample option 3') == 'Solution: "sample option 3"'

def test_getProblemsFromSampleWorksheet_WithOneProblem():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem1')
  problem = problems[0]

  assert problem.question   == 'sample question 1'
  assert problem.solution   == 'sample option 1'
  assert problem.options[0] == 'sample option 1'
  assert problem.options[1] == 'sample option 2'

def test_getProblemsFromAnotherWorksheet_WithOneProblem():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem2')
  problem = problems[0]

  assert problem.question   == 'sample question 1'
  assert problem.solution   == 'sample option 2'
  assert problem.options[0] == 'sample option 1'
  assert problem.options[1] == 'sample option 2'

def test_getProblemsFromAnotherTopicsWorksheet_withTwoProblems():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  # These (and thus the worksheet) should be different so we know, for example,
  # that we're not getting all of our problems from the same worksheet. True for all worksheets.
  problem1 = problems[0]
  problem2 = problems[1]
  print(problems)

  assert problem1.question   == 'sample question 1' 
  assert problem1.solution   == 'sample option 1'
  assert problem1.options[0] == 'sample option 1' 

  assert problem2.question   == 'sample question 2' 
  assert problem2.solution   == 'sample option 1'
  assert problem2.options[0] == 'sample option 1' 

def test_getProblemsFromWorksheet_WithTwoProblems():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  problem1 = problems[0]
  problem2 = problems[1]
  print(problems)

  assert problem1.question   == 'sample question 1' 
  assert problem1.solution   == 'sample option 1'
  assert problem1.options[0] == 'sample option 1' 

  assert problem2.question   == 'sample question 2' 
  assert problem2.solution   == 'sample option 1'
  assert problem2.options[0] == 'sample option 1' 

def test_parseWorksheet_withOneProblem():
  parsedWorksheet = quizGenerator.parseWorksheet('sampleTopic', 'sampleWorksheet_oneProblem1')

  # After the sample question comes the solution and then all the options (possible answers).
  assert parsedWorksheet[0] == ['sample question 1', 'sample option 1', 'sample option 1', 'sample option 2']

def test_parseWorksheet_withTwoProblems():
  parsedWorksheet = quizGenerator.parseWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  assert parsedWorksheet[0] == ['sample question 1', 'sample option 1', 'sample option 1']
  assert parsedWorksheet[1] == ['sample question 2', 'sample option 1', 'sample option 1']

