===============================================================================
What to test? The |act__phase|, |atc__cpt__def| and |actor__cpt_def|
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


|atc__cpt|
===============================================================================

Exactly tests the execution of a program - the |atc__cpt__def| (|atc__cpt_acr|).

It executes this as an OS process,
and captures the output - stdout, stderr, exit code -
so that assertions aboute these can be made in the
|assert__phase|.

For example::

    [act]

    my-program arg 'second arg'

Here the |atc__cpt| is the executable file :file:`my-program`
given two arguments.


|actor__cpt|
===============================================================================

To test a Python source code file - :file:`my-program.py` -
invoking it with the same two arguments::

    [conf]

    actor = file % python
    
    [act]

    my-program.py arg 'second arg'

|actor__kwd| ``=``
  Sets the |actor__cpt_def|.

|file__actr_kwd|
  Specifies the |file__actr_name| |actor__cpt|.

|os_path__pgm_kwd| ``python``
  Specifies the interpreter to be :command:`python`.
  
  |os_path__pgm_kwd| means that :command:`python` must be a program in the OS PATH.

Thus, the |atc__cpt| is the file :file:`my-program.py` interpreted
by :command:`python`, given two arguments.

The |actor__cpt| resolves the |atc__cpt|
by reading the contents of the |act__phase|.
Executing the |act__phase| means executing the |atc__cpt|
as an OS process.

The default |actor__cpt| is the |cmd_line__actr_name| |actor__cpt|.
It reads and executes a value of type |program__typ|.

TODO see-also: external program, action-to-check.

TODO examples


The |null__actr_name| |actor__cpt|
-------------------------------------------------------------------------------

If the |act__phase| is absent or empty,
then the |null__actr_name| |actor__cpt| is used.
The |atc__cpt| will be a process with no output on
neither stdout nor stderr, and an exit code of 0.

This is useful for testing existing properties of the OS environment.

The |null__actr_name| |actor__cpt| can also be set via

::

   [conf]

   actor = null

The contents of the |act__phase| will be ignored.


Paths
===============================================================================

In both examples above, the program files
- :file:`my-program` and :file:`my-program.py` -
must be located in the directory containg the test case file.

The path to the program may be relative::

  [act]

  ../build/my-program

The path may also be relative a directory set in the |conf__phase|.
The following is equivalent::

  [conf]

  act-home = ../build

  [act]

  my-program

TODO see-also: TCDS.


Executing the |act__phase|, ignoring assertions
===============================================================================


The |act__opt| option tells Exactly to report the output of the
|atc__cpt| - exit code, stdout and stder.
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

This is usefull for debugging the |atc__cpt_acr|,
or running a program with custom setup and cleanup.
