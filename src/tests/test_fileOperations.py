from src.quizGenerator import fileOperations


def test_getWorksheetOptions_fromSampleTopic() -> None:
  worksheets = fileOperations.getWorksheetOptions('sampleTopic')
  assert 'sampleWorksheet.json' in worksheets

def test_getTopicOptions() -> None:
  topicsCollection = fileOperations.getTopicOptions()
  assert 'sampleTopic' in topicsCollection

def test_glob() -> None:
  topics = fileOperations.glob(fileOperations.TOPICS_DIRECTORY, '*')
  assert 'sampleTopic' in topics

def test_verifyTopicsPathExists() -> None:
  assert fileOperations.verifyTopicsPathExists() == True

def test_getPathBasename() -> None:
  path = 'this/is/a/file.txt'
  assert fileOperations.getPathBasename(path) == 'file.txt'

def test_getProblemsFromWorksheet_WithTwoProblems() -> None:
  problems = fileOperations.getProblemsFromWorksheet('sampleTopic', 'sampleWorksheet.json')

  p1 = problems[0]
  p2 = problems[1]


  assert p1.question == 'this is question number 1'
  assert p1.solution == 'this is option number 2, correct'

  assert p1.options[0] == 'this is option number 1'
  assert p1.options[1] == 'this is option number 2, correct'


  assert p2.question == 'this is question number 2'
  assert p2.solution == 'this is option number 1, correct'

  assert p2.options[0] == 'this is option number 1, correct'
  assert p2.options[1] == 'this is option number 2'
  assert p2.options[2] == 'this is option number 3'

