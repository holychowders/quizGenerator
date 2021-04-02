from src.quizGenerator import messages


def userSelectFromMenu(options, message='Selection: '):
  try:
    intSelection = int(input(message))
    assert (intSelection >= 1), messages.NOT_A_VALID_INTEGER_ERR_MSG
    option = options[intSelection - 1]

  except ValueError:
    print(messages.NOT_AN_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except IndexError:
    print(messages.NOT_A_VALID_INTEGER_ERR_MSG)
    return userSelectFromMenu(options, message)
  except AssertionError as ae:
    print(ae.args[0])
    return userSelectFromMenu(options, message)

  return option

