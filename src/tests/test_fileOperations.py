from src.quizGenerator import fileOperations


def test_getWorksheetOptions_fromSampleTopic() -> None:
  worksheetCollection = fileOperations.getWorksheetOptions('sampleTopic')

  assert 'sampleWorksheet_oneProblem1' in worksheetCollection
  assert 'sampleWorksheet_oneProblem2' in worksheetCollection

def test_getTopicOptions() -> None:
  topicsCollection = fileOperations.getTopicOptions()

  assert 'sampleTopic' in topicsCollection
  assert 'sampleTopic2' in topicsCollection

def test_glob() -> None:
  topics = fileOperations.glob(fileOperations.TOPICS_DIRECTORY, '*')

  assert ('sampleTopic' in topics) and ('sampleTopic2' in topics)

def test_verifyTopicsPathExists() -> None:
  assert fileOperations.verifyTopicsPathExists() == True

def test_getPathBasename() -> None:
  path = 'this/is/a/file.txt'

  assert fileOperations.getPathBasename(path) == 'file.txt'

def test_getProblemsFromSampleWorksheet_WithOneProblem() -> None:
  problems = fileOperations.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem1')
  problem = problems[0]

  assert problem.question   == 'sample question 1'
  assert problem.solution   == 'sample option 1'
  assert problem.options[0] == 'sample option 1'
  assert problem.options[1] == 'sample option 2'

def test_getProblemsFromAnotherWorksheet_WithOneProblem() -> None:
  problems = fileOperations.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet_oneProblem2')
  problem = problems[0]

  assert problem.question   == 'sample question 1'
  assert problem.solution   == 'sample option 2'
  assert problem.options[0] == 'sample option 1'
  assert problem.options[1] == 'sample option 2'

def test_getProblemsFromAnotherTopicsWorksheet_withTwoProblems() -> None:
  problems = fileOperations.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

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

def test_getProblemsFromWorksheet_WithTwoProblems() -> None:
  problems = fileOperations.getProblemsFromWorksheet('sampleTopic2', 'sampleWorksheet_twoProblems1')

  problem1 = problems[0]
  problem2 = problems[1]
  print(problems)

  assert problem1.question   == 'sample question 1' 
  assert problem1.solution   == 'sample option 1'
  assert problem1.options[0] == 'sample option 1' 

  assert problem2.question   == 'sample question 2' 
  assert problem2.solution   == 'sample option 1'
  assert problem2.options[0] == 'sample option 1' 

