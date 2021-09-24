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

The `setup` phase sets up the environment that the Action To Check
will be executed in (the `act` phase).

::

   [setup]

   stdin = 'the contents of stdin'

   env MY_ENV_VAR = 'my value'

The `assert` phase expresses assertions on the outcome of the ATC.
Preparations for this may be done in the `before-assert` phase,
or within the `assert` phase itself.

::

  [before-assert]

  file my-file.txt = -stdout-from collect-interesting-data

  [assert]

  exit-code == 0

  contents my-file.txt : every line : matches 'IMPORTANT'

At the end, the `cleanup` phase can do cleanup not handled automatically.

::

  [cleanup]

  run my-database-cleanup-program

  
Instructions
===============================================================================

All these phases consist of a sequence of `instructions`.

Instructions in all phases except `assert` are statements
used for their side effects.
In the `assert` phase, these statements can be used too,
but also instructions that serve as boolean expressions
checking the result of executing the Action To Check.


Statements
-------------------------------------------------------------------------------

The statement instructions can be grouped as follows:

* Running external programs

  ============= ===============================================================
  ``run``       Runs a "program"
  ``%``         Runs a program installed on the current system (in the OS PATH)
  ``$``         Executes a command using the current operating system's shell   
  ============= ===============================================================

* Setting up the execution environment for external programs

  ============= ===============================================================
  ``env``       Manipulates environment variables
  ``cd``        Sets the "current directory"
  ``timeout``   Sets the timeout of individual OS processes
  ============= ===============================================================

* Creating files and directories

  ========= ===================================================================
  ``file``  Creates or modifies a regular file
  ``dir``   Creates or modifies a directory
  ``copy``  Copies files and directories
  ========= ===================================================================

* Defining symbols

  ========= ===================================================================
  ``def``   Defines a symbol
  ========= ===================================================================

The `setup` phase accepts one additional instruction:

========= =====================================================================
``stdin`` Sets the contents of stdin for the "action to check"
========= =====================================================================


Assertions
-------------------------------------------------------------------------------

Instructions for assertions in the `assert` phase

================ ==============================================================
``contents``     Tests the contents of a regular file                                        
``dir-contents`` Tests the contents of a directory                                           
``exists``       Tests the existence, and optionally properties, of a file                   
``exit-code``    Tests the exit code from the "action to check", or from a "program"         
``stderr``       Tests the contents of stderr from the "action to check", or from a "program"
``stdout``       Tests the contents of stdout from the "action to check", or from a "program"
================ ==============================================================

In the `assert` phase,
the instructions for running programs may be used as assertions too.


Instruction syntax
-------------------------------------------------------------------------------

The syntax is line oriented - new lines have syntactic meaning.

An instruction starts on a new line, beginning with the name of the instruction,
followed by its arguments.

Each instruction has its own syntax for arguments.
Most common syntax is that of options and arguments
resembling the Unix shell - options are preceded by a single dash (``-``).
One difference though, is that the order of options is usually significant.

Some instructions may span multiple lines,
while some must use only a single line.
The syntax is not always consistent, unfortunately.

Mandatory arguments may usually appear on a new line, while optional arguments may not
(unless followed by mandatory arguments).

TODO ADD exempel

TODO ADD many args are types in the type sys. Ref to types intro??


Help
...............................................................................

Phases and instructions are documented in the `Reference Manual`_.

Builtin help is also available:

* List of instructions per phase

  .. code-block:: console

      $ exactly help instructions

* Description of a phase, listing all its instructions, e.g.:

  .. code-block:: console

      $ exactly help setup

* Description of an instruction in a phase, e.g.:

  .. code-block:: console

      $ exactly help setup stdin


Instruction descriptions
-------------------------------------------------------------------------------

An Instruction may optionally be preceeded by a description::

  [assert]

  `The last line on stdout should indicate SUCCESS`

  stdout
    -transformed-by
      filter -line-nums -1
    equals 'SUCCESS'

The description is surrounded by back tics (\`).
It may span several lines.

Description are displayed in error messages,
when an Instruction causes some kind of failure.
They are most usefull in the `assert` phase,
for explaining failing assertions.


Comments
===============================================================================

Exactly supports line comments preceded by ``#``::

  [setup]

  # This is a comment

Unfortunately, comments may not be mixed with Instruction arguments.
