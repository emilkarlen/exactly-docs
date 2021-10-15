===============================================================================
Arranging and asserting
===============================================================================


..
   phases: setup, before-assert, assert, cleanup
   instructions
    - meaning
    - groups
    - syntax
    - instruction descriptions
    - help
   comments


Phases
===============================================================================

The |setup__phase| sets up the environment that the |atc__cpt|
will be executed in (the |act__phase|).

::

   [setup]

   stdin = 'the contents of stdin'

   env MY_ENV_VAR = 'my value'

The |assert__phase| expresses assertions on the outcome of the |atc__cpt_acr|.
Preparations for this may be done in the |before_assert__phase|,
or within the |assert__phase| itself.

::

  [before-assert]

  file my-file.txt = -stdout-from collect-interesting-data

  [assert]

  exit-code == 0

  contents my-file.txt : every line : matches 'IMPORTANT'

At the end, the |cleanup__phase| can do cleanup not handled automatically.

::

  [cleanup]

  run my-database-cleanup-program


|instr__cpt_s|
===============================================================================

All these phases consist of a sequence of |instr__cpt_def_s|.

|instr__cpt_s| in all phases except |assert__ph| are statements
used for their side effects.
In the |assert__phase|, these statements can be used too,
but primarily other |instr__cpt_s| that serve as boolean expressions
checking the result of executing the |atc__cpt_acr|.


Statements
-------------------------------------------------------------------------------

The statement |instr__cpt_s| can be grouped as follows:

* Running external programs

  ==================== ========================================================
  |run_pgm__instr|     Runs a |program__typ|
  |run_os_path__instr| Runs a program installed on the current system
                       (in the OS PATH)
  |run_shell__instr|   Executes a command using
                       the current operating system's shell
  ==================== ========================================================

* Setting up the execution environment for external programs

  ================= ===========================================================
  |env__instr|      Manipulates environment variables
  |cd__instr|       Sets the |cd__cpt|
  |timeout__instr|  Sets the timeout of individual OS processes
  ================= ===========================================================

* Creating files and directories

  ================ ============================================================
  |file_r__instr|  Creates or modifies a regular file
  |file_d__instr|  Creates or modifies a directory
  |copy__instr|    Copies files and directories
  ================ ============================================================

* Defining symbols

  ============= ===============================================================
  |def__instr|  Defines a symbol
  ============= ===============================================================

The |setup__phase| accepts one additional |instr__cpt|:

============== ================================================================
|stdin__instr| Sets the contents of stdin for the |atc__cpt|
============== ================================================================


Assertions
-------------------------------------------------------------------------------

|instr__cpt_s| for assertions in the |assert__phase|:

==================== ==========================================================
|contents_r__instr|  Tests the contents of a regular file
|contents_d__instr|  Tests the contents of a directory
|exists__instr|      Tests the existence, and optionally properties, of a file
|exit_code__instr|   Tests the exit code from the |atc__cpt|,
                     or from a |program__typ|
|stderr__instr|      Tests the contents of stderr from the |atc__cpt|,
                     or from a |program__typ|
|stdout__instr|      Tests the contents of stdout from the |atc__cpt|,
                     or from a |program__typ|
==================== ==========================================================

In the |assert__phase|,
the |instr__cpt_s| for running programs may be used as assertions too.
An exit code of 0 means the assertion passes, otherwise it fails.


|instr__cpt| syntax
-------------------------------------------------------------------------------

The syntax is line oriented - new lines have syntactic meaning.

An |instr__cpt| starts on a new line,
beginning with the name of the |instr__cpt|,
followed by its arguments.

Each |instr__cpt| has its own syntax for arguments.
Most common syntax is that of options and arguments
resembling the Unix shell - options are preceded by a single dash (``-``).
One difference though, is that the order of options is usually significant.

Some |instr__cpt_s| may span multiple lines,
while some must use only a single line.
The syntax is not always consistent, unfortunately.

Mandatory arguments may usually appear on a new line,
while optional arguments may not
(unless followed by mandatory arguments).

TODO ADD exempel

TODO ADD many args are types in the type sys. Ref to types intro??


Help
...............................................................................

Phases and |instr__cpt_s| are documented in the `Reference Manual`_.

Builtin help is also available:

* List of |instr__cpt_s| per phase

  .. code-block:: console

      $ exactly help instructions

* Description of a phase, listing all its |instr__cpt_s|, e.g.:

  .. code-block:: console

      $ exactly help setup

* Description of an |instr__cpt| in a phase, e.g.:

  .. code-block:: console

      $ exactly help setup stdin


|instr__cpt| descriptions
-------------------------------------------------------------------------------

An |instr__cpt| may optionally be preceeded by a description::

  [assert]

  `The last line on stdout should indicate SUCCESS`

  stdout
    -transformed-by
      filter -line-nums -1
    equals 'SUCCESS'

The description is surrounded by back tics (\`).
It may span several lines.

Description are displayed in error messages,
when an |instr__cpt| causes some kind of failure.
They are most usefull in the `assert` phase,
for explaining failing assertions.


Comments
===============================================================================

Exactly supports line comments preceded by ``#``::

  [setup]

  # This is a comment

Unfortunately, comments may not be mixed with |instr__cpt| arguments.

TODO ADD example
