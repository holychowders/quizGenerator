from src.quizGenerator.tui import helpers
from src.quizGenerator import messages

import io

import pytest
import warnings
from typing import Any


def test_getTopicFromUser() -> None:
  warnings.warn("TODO")

def test_getWorksheetFromUser() -> None:
  warnings.warn("TODO")

def test_getProblems() -> None:
  warnings.warn("TODO")

def test_randomizeProblemSet() -> None:
  warnings.warn("TODO")

def test_randomizeQuestionsInProblemSet() -> None:
  warnings.warn("TODO")

def displayQuestionAndOptions() -> None:
  warnings.warn("TODO")

def test_userSelectFromMenu_isValid(monkeypatch: Any) -> None:
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('1'))
  assert helpers.userSelectFromMenu(options) == 'option 1'

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_isZero(monkeypatch: Any) -> None:
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('0'))
  assert helpers.userSelectFromMenu(options) == messages.NOT_A_VALID_INT_MSG

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_invalidString(monkeypatch: Any) -> None:
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('some random non-int string'))
  assert helpers.userSelectFromMenu(options) == messages.NOT_AN_INTEGER_ERR_MSG

@pytest.mark.skip(reason="I don't know how to prevent the EOFError and just get the intial output.")
def test_userSelectFromMenu_invalidInt(monkeypatch: Any) -> None:
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('5'))
  assert helpers.userSelectFromMenu(options) == messages.NOT_A_VALID_INT_MSG

@pytest.mark.skip(reason="I don't know how to do this")
def test_userSelectFromMenu_valueError_canRecover(monkeypatch: Any) -> None:
  options = ['option 1', 'option 2']

  monkeypatch.setattr('sys.stdin', io.StringIO('5'))
  assert helpers.userSelectFromMenu(options) == messages.NOT_A_VALID_INT_MSG

  # ...and then somehow try again with valid input into the recursive call which should be returned by the function

