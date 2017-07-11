test = {
  'name': 'GetName',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert starter.get_name() != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "Step 0 is incorrect, please fill in a name"
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
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
