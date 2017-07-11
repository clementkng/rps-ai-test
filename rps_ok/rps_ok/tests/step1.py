test = {
  'name': 'PlayAgain',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert starter.play_again() == True, 'check standard input'
          Want to play again? Starter
          >>> assert starter.play_again() == False, 'check standard input'
          Want to play again? Starter
          >>> assert starter.play_again() == True, 'check uppercase input'
          Want to play again? Starter
          >>> assert starter.play_again() == False, 'check uppercase input'
          Want to play again? Starter
          >>> assert starter.play_again() == False, 'check the third case'
          Want to play again? Starter
          Invalid input!
          Want to play again? Starter
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      >>> import os as os
      >>> import subprocess as subprocess
      >>> import starter_RPS as starter
      >>> import sys as sys
      >>> real_print = print
      >>> def print(string):
      ...   real_print(string.strip())
      >>> starter.print = print
      >>> count = 0
      >>> def input():
      ...   test_inputs = ["yes", "no", "YES", "nO", "blah", "No"]
      ...   global count
      ...   count += 1
      ...   return test_inputs[count - 1]
      >>> starter.input = input
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
