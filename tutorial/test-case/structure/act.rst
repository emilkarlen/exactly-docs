===============================================================================
What to test? The `act` phase, `Action To Check` and `Actor`
===============================================================================

..
   execution of program
   os process
   act phase
   actor, action to check
   act phase specifies program
   actor : command-line, file
   act-home

TODO ADD ATC execution environment??


Action To Check
===============================================================================

Exactly tests the execution of a program - the `Action To Check` (ATC).

It executes this as an OS process,
and captures the output - stdout, stderr, exit code -
so that assertions aboute these can be made in the
`assert` phase.

For example::

    [act]

    my-program arg 'second arg'

Here the Action To Check is the executable file :file:`my-program`
given two arguments.


Actor
===============================================================================

To test a Python source code file - :file:`my-program.py` -
invoking it with the same two arguments::

    [conf]

    actor = file % python
    
    [act]

    my-program.py arg 'second arg'

``actor =``
  Sets the `Actor`.

``file``
  Specifies the "file interpreter" Actor.

``% python``
  Specifies the interpreter to be :command:`python`.
  
  ``%`` means that :command:`python` must be a program in the OS PATH.

Thus, the Action To Check is the file :file:`my-program.py` interpreted
by :command:`python`, given two arguments.

The Actor resolves the Action To Check
by reading the contents of the `act` phase.
Executing the `act` phase means executing the Action To Check
as an OS process.

The default Actor is the "command line" Actor.
It reads and executes a value of type `program`.

TODO see-also: external program, action-to-check.


The "null" Actor
-------------------------------------------------------------------------------

If the `act` phase is absent or empty,
then the "null" actor is used.
The Action To Check will be a process with no output on
neither stdout nor stderr, and an exit code of 0.

This is useful for testing existing properties of the OS environment.

The "null" Actor can also be set via
::
  [conf]

  actor = null

The contents of the `act` phase will be ignored.


Paths
===============================================================================

In both examples above, the program files
- :file:`my-program` and :file:`my-program.py` -
must be located in the directory containg the test case file.

The path to the program may be relative::

  [act]

  ../build/my-program

The path may also be relative a directory set in the `conf` phase.
The following is equivalent::

  [conf]

  act-home = ../build

  [act]

  my-program

TODO see-also: TCDS.


Executing the `act` phase, ignoring assertions
===============================================================================


The ``--act`` option tells Exactly to report the output of the
Action To Check - exit code, stdout and stder.
Assertions are ignored.

If :file:`cat.case` is::

  [setup]

  stdin = 'the contents of stdin'

  [act]

  % cat

  [assert]

  stdout equals 'unexpected!'

Then

.. code-block:: console

    $ exactly --act cat.case
    the contents of stdin
    $ echo $?
    0

The assertion here would fail, but is ignored.

This is usefull for debugging the ATC,
or running a program with custom setup and cleanup.
