===============================================================================
Permanent and temporary files, and the `path` type
===============================================================================

.. contents:: :local:

Test cases often are faciliated by using permanent
and temporary files.

For example::

  [assert]

  stdout equals -contents-of expected-output.txt

Here the file :file:`expected-output.txt` contains the expected text output
on stdout from the Action To Check.
The expected output is the same for every execution of this test case,
so the file :file:`expected-output.txt` is a permanent file
used by every execution of the test case.

Temporary files, used only by a single execution of a test case,
may also be needed.  Such as in this part of a test of a
:program:`git` commit hook::

  [setup]

  % git init

  copy prepare-commit-msg .git/hooks

.. TODO Change example - git not a good one. Use one with a plain file/dir.

Here, a :program:`git` repository is created,
and the commit hook to test is installed in it.
The repository should not pollute the directories for source code
(including the directories for test case sources).


`Test Case Directory Structure` (TCDS)
===============================================================================

To handle permanent and temporary files, Exactly uses the
`Test Case Directory Structure`, which is divided into two parts -
one for permanent and one for temporary files:


`Home Directory Structure`

  A set of directories for permanent files
  used by every execution of a test case.

`Sandbox Directory Structure`

  A set of temporary directories used by a single execution of a test case.
  One of them is the initial "current directory".


The `path` type
-------------------------------------------------------------------------------

..
   path type
   relativity
   default relativity
   where path values can be used

The ``path`` type is desiged to faciliate referring to these directories.
It uses the concept of `relativity` to tell which directory
a path is relative to.
For example::

  [assert]
  
  stdout equals -contents-of -rel-home expected-output.txt

Here,
``-rel-home expected-output.txt`` is a value of the `path` type.
The option ``-rel-home`` specifies which directory the
path :file:`expected-output.txt` is relative to.
It specifies one of the directories in the TCDS.
(Other options specify other relativities, more about this later).

Paths use a `default relativity`, to minimize the need to specify the
relativity explicitly.
The example below is equivalent to the one above::

  [assert]
  
  stdout equals -contents-of expected-output.txt


Here, ``expected-output.txt`` is a `string` value.
A `string` value is a valid `path`, that uses the default relativity of
the context in which the `path` argument appears.
In this case, the default relativity is ``-rel-home``.

.. note::
   `path` values in different context have different default relativities.
   See the `Reference Manual`_ for details.


`Home Directory Structure` (HDS)
-------------------------------------------------------------------------------

..
   - persistent files existing before execution starts
   - directories
   - relativities, built in symbols
   - default values
   - changed in [conf]
   - validation - files must exist
   - Exactly prevents modification (as far as possible) TODO

Consists of two directories, for storing permanent files
that should probably not be modified:

==========   ==================================================================
`home`       Default location of persistent helper files.
`act-home`   Default location of files referenced from "act" phase.
==========   ==================================================================

Exactly prevents modification of the contents of these directories,
by preventing them from being used by modification operations.

.. note::
   Exactly cannot prevent an external program from modifying their contents.


Both of these directories default to
the directory containing the test case file.
They can be changed in the `conf` phase::

  [conf]

  home = data

  act-home = ../build

The paths (:file:`data` and :file:`../build`) are relative to the directory
containing the test case source code.
This can be the test case file, or a file included from it.

Once set in the `conf` pahse, these directories cannot be changed in later
phases.

Given the above definitions, and the following `act` and `assert` phases::

  [act]

  my-program

  [assert]

  stdout equals -contents-of expected-output.txt

Then

  :file:`my-program` resolves to :file:`../build/my-program`


and
  :file:`expected-output.txt` resolves to :file:`data/expected-output.txt`.

And as said, these paths will in turn be relative to the location of
the file with the above definition of the `conf` phase.

The corresponding relativity option, and built in symbol for the HDS
directories:

==========   ================= ================================================
HDS dir      Relativity option Builtin path symbol
==========   ================= ================================================
`home`       ``-rel-home``     ``EXACTLY_HOME``
`act-home`   ``-rel-act-home`` ``EXACTLY_ACT_HOME``
==========   ================= ================================================

The following path specifications are both equivalent to the ones above::

  [act]

  -rel-act-home my-program

  [assert]

  stdout equals -contents-of -rel-home expected-output.txt

::

  [act]

  @[EXACTLY_ACT_HOME]@/my-program

  [assert]

  stdout equals -contents-of @[EXACTLY_HOME]@/expected-output.txt


Validating the existence of files
...............................................................................

..
   - every file ref in HDS must exist
   - validation (as a whole) occurs before execution (as a whole)
   - validation error halts exe w exit-code,identifier

Files located in the HDS are assumed to be permanent files existing
before the execution of the test case.
Exactly validates that this is acutally the case.

The validation is performed before the actual execution - before
any external program has been executed, or file has been created, e.g.
In other words: *every* file reference is validated before *any*
instruction is executed.

If a missing file is found the validation fails,
and Exactly does not execute the test case.
Instead it halts with a non-zero exit code and an error message
explaining where the file is assumed to be located.

  
`Sandbox Directory Structure` (SDS)
-------------------------------------------------------------------------------

These are temporary directories used for a single execution of a test case.
Everything they contain is removed at the end of the execution.

They cannot be changed the same way the directories in the HDS can.

==========   ==================================================================
`act`        The current directory when the `setup` phase begins.
`result`     Stores OS process outcome of the Action To Check
             (the execution of the `act` phase),
             so that the `assert` phase may check it.
`tmp`        Reserved for custom helper files,
             used by the test case implementation.
	     Exactly itself do not create files here.
==========   ==================================================================

Besides these, the SDS is used for temporary files needed
internally by Exactly.

The relativity options and built in symbols are:

==========   ================= ================================================
SDS dir      Relativity option Builtin path symbol
==========   ================= ================================================
`act`        ``-rel-act``      ``EXACTLY_ACT``
`tmp`        ``-rel-tmp``      ``EXACTLY_TMP``
`result`     ``-rel-result``   ``EXACTLY_RESULT``
==========   ================= ================================================

The `act` and `tmp` directories are both empty when the test case starts.

The purpose of `act` is to be the current directory of the Action To Check.
The `setup` phase can populate it, and also change the current directory
using ``cd``.

.. TODO Example of ``cd``

When the `act` phase is executed, the `result` directory
is populated with files to capture the output from the Action To Check:

* :file:`exit-code`
* :file:`stdout`
* :file:`stderr`

The corresponding instructions in the `assert` phase use these files::

  [assert]

  exit-code == 0
  
  stdout equals 'hello'

  stderr is-empty

The files can also be used directly.
The following is equivalent::

  [assert]

  contents -rel-result exit-code : equals '0'

  contents -rel-result stdout    : equals 'hello'

  contents -rel-result stderr    : is-empty

`tmp` is for temporary helper files, just like a usual :file:`tmp`
directory.
The test case implementer is free to use this for any purpose.


Keeping the SDS
...............................................................................

Invoking Exactly with the ``--keep`` option
prevents the SDS from being deleted.
The SDS root directory will be printed on stdout:

.. code-block:: console

  $ exactly --keep my-test.case
  /tmp/exactly-1strbro1


More `path` relativities
===============================================================================


Location of current source file
-------------------------------------------------------------------------------

..
   -rel-here
     - rel current source file
     - only available in ``def``

When defining a symbol, one extra path relativity is available:
the location of the current source file.
The ``-rel-here`` option denotes this directory::

  def path my_path = -rel-here my-file
  
If the file containg this statement is

  :file:`/path/to/file.xly`

then ``@[my_path]@`` resolves to

  :file:`/path/to/my-file`.


Arbitrary `path` symbol
-------------------------------------------------------------------------------

..
   -rel SYMBOL-NAME

An arbitrary `path` symbol may be used as the relativity root
using the ``-rel`` option::

  def path my_path = -rel my_relativity_root_symbol some-file

Here, ``my_relativity_root_symbol`` must have been defined as a `path`.

Given::

   def path my_relativity_root_symbol = -rel-home sub/dir

then:

  ``@[my_path]@``

resolves to:

  ``-rel-home sub/dir/some-file``

An equivalent definition of ``my_path`` is::

    def path my_path = @[my_relativity_root_symbol]@/some-file

The built in paths can of course also be used with ``-rel``.
The following paths are equivalent:

* ``-rel EXACTLY_ACT my-file``
* ``-rel-act         my-file``
* ``@[EXACTLY_ACT]@/my-file``

Which form to use is a matter of taste.
