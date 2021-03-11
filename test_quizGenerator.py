import quizGenerator
import io

def testUserSelectFromMenu_isValid(monkeypatch):
  monkeypatch.setattr('sys.stdin', io.StringIO('1'))

  assert quizGenerator.userSelectFromMenu() == 1

def testUserSelectFromMenu_isInvalid_canRecover(monkeypatch):
  monkeypatch.setattr('sys.stdin', io.StringIO('error-inducing non-int string'))
  #assert quizGenerator.userSelectTopic() == quizGenerator.NOT_AN_INTEGER_ERR_MSG
  monkeypatch.setattr('sys.stdin', io.StringIO('2'))

  assert quizGenerator.userSelectFromMenu() == 2

def testFormatMenuOptions():
  assert quizGenerator.formatMenuOptions(('option 1', 'option 2')) == '\n1) option 1\n2) option 2'

def testGetWorksheetOptions_fromSampleTopic():
  worksheetCollection = quizGenerator.getWorksheetOptions('sampleTopic')

  assert 'sampleWorksheet_oneProblem1' in worksheetCollection
  assert 'sampleWorksheet_oneProblem2' in worksheetCollection

def testGetTopicOptions():
  topicsCollection = quizGenerator.getTopicOptions()

  assert 'sampleTopic' in topicsCollection
  assert 'sampleTopic2' in topicsCollection

def testCheckAnswer_isCorrect():
  solution = 'sample option 2'
  answer   = 'sample option 2'

  assert quizGenerator.checkAnswer(answer, solution) == True

def testCheckAnswer_isIncorrect():
  solution = 'sample option 2'
  answer   = 'sample option 1'

  assert quizGenerator.checkAnswer(answer, solution) == False

def testGetUsersAnswer_isValid(monkeypatch):
  # This 'mocks' STDIN; IE, this replaces our keyboard as STDIN for this test.
  monkeypatch.setattr('sys.stdin', io.StringIO('1'))
  assert quizGenerator.getUsersAnswer() == 1

def testGetUsersAnswer_isInvalid(monkeypatch):
  monkeypatch.setattr('sys.stdin', io.StringIO('some invalid value'))
  monkeypatch.setattr('sys.stdin', io.StringIO('2'))
  assert quizGenerator.getUsersAnswer() == 2

def testFormatQuestionString():
  assert quizGenerator.formatQuestionString('sample question 1') == '\nQuestion: "sample question 1"\n'

def testFormatOptionsCollection():
  assert quizGenerator.formatOptionsCollection(('sample option 1', 'sample option 2')) \
    == '\n1) sample option 1\n\n2) sample option 2\n'
  
def testFormatSolutionString():
  assert quizGenerator.formatSolutionString('sample option 3') == '\nSolution: "sample option 3"\n'

def testGetProblemsFromSampleWorksheet_WithOneProblem():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem1')
  problem = problems[0]

  assert problem.question   == 'sample question 1' 
  assert problem.solution   == 'sample option 1'
  assert problem.options[0] == 'sample option 1' 
  assert problem.options[1] == 'sample option 2\n' 

def testGetProblemsFromAnotherWorksheet_WithOneProblem():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem2')
  problem = problems[0]

  assert problem.question   == 'sample question 1' 
  assert problem.solution   == 'sample option 2'
  assert problem.options[0] == 'sample option 1' 
  assert problem.options[1] == 'sample option 2\n' 

def testGetProblemsFromAnotherTopicsWorksheet_withTwoProblems():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  # These (and thus the worksheet) should be different so we know, for example,
  # that we're not getting all of our problems from the same worksheet. True for all worksheets.
  problem1 = problems[0]
  problem2 = problems[1]
  print(problems)

  assert problem1.question   == 'sample question 1' 
  assert problem1.solution   == 'sample option 1'
  assert problem1.options[0] == 'sample option 1\n' 

  assert problem2.question   == 'sample question 2' 
  assert problem2.solution   == 'sample option 1'
  assert problem2.options[0] == 'sample option 1\n' 

def testGetProblemsFromWorksheet_WithTwoProblems():
  problems = quizGenerator.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  problem1 = problems[0]
  problem2 = problems[1]
  print(problems)

  assert problem1.question   == 'sample question 1' 
  assert problem1.solution   == 'sample option 1'
  assert problem1.options[0] == 'sample option 1\n' 

  assert problem2.question   == 'sample question 2' 
  assert problem2.solution   == 'sample option 1'
  assert problem2.options[0] == 'sample option 1\n' 

def testParseWorksheet_withOneProblem():
  parsedWorksheet = quizGenerator._parseWorksheet('sampleTopic', 'sampleWorksheet_oneProblem1')

  # After the sample question comes the solution and then all the options (possible answers).
  assert parsedWorksheet[0] == ['sample question 1', 'sample option 1', 'sample option 1', 'sample option 2\n']

def testParseWorksheet_withTwoProblems():
  parsedWorksheet = quizGenerator._parseWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  assert parsedWorksheet[0] == ['sample question 1', 'sample option 1', 'sample option 1\n']
  assert parsedWorksheet[1] == ['sample question 2', 'sample option 1', 'sample option 1\n']

def testGetRawWorksheetProblems_withOneProblem():
  rawWorksheetProblems = quizGenerator._getRawWorksheetProblems('sampleTopic', 'sampleWorksheet_oneProblem1')

  assert rawWorksheetProblems[0] == 'sample question 1 --- sample option 1 --- sample option 1 --- sample option 2\n'

def testGetRawWorksheetProblems_withTwoProblems():
  rawWorksheetProblems = quizGenerator._getRawWorksheetProblems('sampleTopic2', 'sampleWorksheet_twoProblems1')

  assert rawWorksheetProblems[0] == 'sample question 1 --- sample option 1 --- sample option 1\n'
  assert rawWorksheetProblems[1] == 'sample question 2 --- sample option 1 --- sample option 1\n'

