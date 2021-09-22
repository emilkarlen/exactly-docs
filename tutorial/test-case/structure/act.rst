===============================================================================
What to test? (act, actor, ATC, PROGRAM)
===============================================================================

..
   execution of program
   os process
   act phase
   actor, action to check
   act phase specifies program
   conf phase configures variations
   actor : command-line, none

Exactly tests the execution of a program - the `Action To Check` (ATC).

It executes this as an OS process,
and captures the output - stdout, stderr, exit code -
so that assertions aboute these can be made in the
`assert` phase.

For example::
  

    [act]

    my-program arg 'second arg'


Here the Action To Check is the executable file :file:`my-program`.
It is invoked with two arguments.

To test a Python source code file - :file:`my-program.py` -
invoking it with the same two arguments::


    [conf]

    actor = file % python
    
    [act]

    my-program.py arg 'second arg'


Here, the `actor` is set to the "file interpreter" actor (``file``).
``% python`` sets the interpreter to the :command:`python` program,
which must be a program found in the OS PATH.
The Action To Check is thus the file :file:`my-program.py` interpreted
by the :command:`python`, given two arguments.

The first example uses the default Actor - the "command line" Actor.

The Actor resolves the Action To Check,
by interpreting the contents of the `act` phase.

In both examples above, the program files to execute
(:file:`my-program` and :file:`my-program.py`)
must be located in the directory containg the test case file.

The path to the program may be relative::

  [act]

  ../build/my-program

The path may also be relative a directory set in the `conf` phase::

  [conf]

  act-home = ../build

  [act]

  my-program
