===============================================================================
Permanent and temporary files, and the |path__typ| type
===============================================================================

.. contents:: :local:

Test cases often are faciliated by using permanent
and temporary files.

For example::

  [assert]

  stdout equals -contents-of expected-output.txt

Here the file :file:`expected-output.txt` contains the expected text output
on stdout from the |atc__cpt|.
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


|tcds__cpt_def| (|tcds__cpt_acr|)
===============================================================================

To handle permanent and temporary files, Exactly uses the
|tcds__cpt_def|, which is divided into two parts -
one for permanent and one for temporary files:


|hds__cpt_def|

  A set of directories for permanent files
  used by every execution of a test case.

|sds__cpt_def|

  A set of temporary directories used by a single execution of a test case.
  One of them is the initial |cd__cpt|.


The |path__type|
-------------------------------------------------------------------------------

..
   path type
   relativity
   default relativity
   where path values can be used

The |path__type| is desiged to faciliate referring to these directories.
It uses the concept of |relativity__cpt_def| to tell which directory
a path is relative to.
For example::

  [assert]
  
  stdout equals -contents-of -rel-home expected-output.txt

Here,
``-rel-home expected-output.txt`` is a value of the |path__type|.
The option ``-rel-home`` specifies which directory the
path :file:`expected-output.txt` is relative to.
It specifies one of the directories in the |tcds__cpt_acr|.
(Other options specify other |relativity__cpt_s|, more about this later).

Paths use a |dflt_relativity__cpt_def|, to minimize the need to specify the
relativity explicitly.
The example below is equivalent to the one above::

  [assert]
  
  stdout equals -contents-of expected-output.txt


Here, ``expected-output.txt`` is a |string__type| value.
A |string__typ| value is a valid |path__typ|, that uses the |dflt_relativity__cpt| of
the context in which the |path__typ| argument appears.
In this case, the default relativity is ``-rel-home``.

.. note::
   |path__typ| values in different context have different default relativities.
   See the `Reference Manual`_ for details.


|hds__cpt_def| (|hds__cpt_acr|)
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

===================  ==========================================================
|hds_home__ent|      Default location of persistent helper files.
|hds_act_home__ent|  Default location of files referenced from |act__phase|.
===================  ==========================================================

Exactly prevents modification of the contents of these directories,
by preventing them from being used by modification operations.

.. note::
   Exactly cannot prevent an external program from modifying their contents.


Both of these directories default to
the directory containing the test case file.
They can be changed in the |conf__phase|::

  [conf]

  home = data

  act-home = ../build

The paths (:file:`data` and :file:`../build`) are relative to the directory
containing the test case source code.
This can be the test case file, or a file included from it.

Once set in the |conf__phase|, these directories cannot be changed in later
phases.

Given the above definitions, and the following |act__ph| and |assert__ph| phases::

  [act]

  my-program

  [assert]

  stdout equals -contents-of expected-output.txt

Then

  :file:`my-program` resolves to :file:`../build/my-program`

and

  :file:`expected-output.txt` resolves to :file:`data/expected-output.txt`.

And as said, these paths will in turn be relative to the location of
the file with the above definition of the |conf__phase|.

The corresponding relativity option, and built in symbol for the |hds__cpt_acr|
directories:

===================  ===================  =====================================
|hds__cpt_acr| dir   Relativity option    Builtin path symbol
===================  ===================  =====================================
|hds_home__ent|      |hds_home__opt|      |hds_home__bi|
|hds_act_home__ent|  |hds_act_home__opt|  |hds_act_home__bi|
===================  ===================  =====================================

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

Files located in the |hds__cpt_acr| are assumed to be permanent files existing
before the execution of the test case.
Exactly validates that this is acutally the case.

The validation is performed before the actual execution - before
any external program has been executed, or file has been created, e.g.
In other words: *every* file reference is validated before *any*
|instr__cpt| is executed.

If a missing file is found the validation fails,
and Exactly does not execute the test case.
Instead it halts with a non-zero exit code and an error message
explaining where the file is assumed to be located.

  
|sds__cpt_def| (|sds__cpt_acr|)
-------------------------------------------------------------------------------

These are temporary directories used for a single execution of a test case.
Everything they contain is removed at the end of the execution.

They cannot be changed the same way the directories in the |hds__cpt_acr| can.

=================  ==================================================================
|sds_act__ent|     The current directory when the |setup__phase| begins.
|sds_result__ent|  Stores OS process outcome of the |atc__cpt|
                   (the execution of the |act__phase|),
                   so that the |assert__phase| may check it.
|sds_tmp__ent|     Reserved for custom helper files,
                   used by the test case implementation.

                   Exactly itself do not create files here.
=================  ==================================================================

Besides these, the |sds__cpt_acr| is used for temporary files needed
internally by Exactly.

The relativity options and built in symbols are:

=================  ========================  ==================================
SDS dir            |relativity__cpt| option  Builtin |path__typ| symbol
=================  ========================  ==================================
|sds_act__ent|     |sds_act__opt|            |sds_act__bi|
|sds_tmp__ent|     |sds_tmp__opt|            |sds_tmp__bi|
|sds_result__ent|  |sds_result__opt|         |sds_result__bi|
=================  ========================  ==================================

The |sds_act__ent| and |sds_tmp__ent| directories
are both empty when the test case starts.

The purpose of |sds_act__ent| is to be the |cd__cpt| of the |atc__cpt|.
The |setup__phase| can populate it, and also change the |cd__cpt|
using |cd__instr|.

.. TODO Example of ``cd``

When the |act__phase| is executed, the |sds_result__ent| directory
is populated with files to capture the output from the |atc__cpt|:

* :file:`exit-code`
* :file:`stdout`
* :file:`stderr`

The corresponding instructions in the |assert__phase| use these files::

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

|sds_tmp__ent| is for temporary helper files, just like a usual :file:`tmp`
directory.
The test case implementer is free to use this for any purpose.


Keeping the |sds__cpt_acr|
...............................................................................

Invoking Exactly with the |keep__opt| option
prevents the |sds__cpt_acr| from being deleted.
The |sds__cpt_acr| root directory will be printed on stdout:

.. code-block:: console

  $ exactly --keep my-test.case
  /tmp/exactly-1strbro1


More |path__typ| |relativity__cpt_s|
===============================================================================


Location of current source file
-------------------------------------------------------------------------------

..
   -rel-here
     - rel current source file
     - only available in ``def``

When defining a symbol, one extra path |relativity__cpt| is available:
the location of the current source file.
The |rel_here__opt| option denotes this directory::

  def path my_path = -rel-here my-file
  
If the file containg this statement is

  :file:`/path/to/file.xly`

then ``@[my_path]@`` resolves to

  :file:`/path/to/my-file`.


Arbitrary |path__typ| symbol
-------------------------------------------------------------------------------

..
   -rel SYMBOL-NAME

An arbitrary |path__typ| symbol may be used as the |relativity__cpt| root
using the |rel_sym__opt| option::

  def path my_path = -rel my_relativity_root_symbol some-file

Here, ``my_relativity_root_symbol`` must have been defined as a |path__typ|.

.. HARD CODED

Given::

   def path my_relativity_root_symbol = -rel-home sub/dir

then:

  ``@[my_path]@``

resolves to:

  ``-rel-home sub/dir/some-file``

An equivalent definition of ``my_path`` is::

    def path my_path = @[my_relativity_root_symbol]@/some-file

The built in paths can of course also be used with |rel_sym__opt|.
The following paths are equivalent:

.. HARD CODED

* ``-rel-act         my-file``
* ``-rel EXACTLY_ACT my-file``
* ``@[EXACTLY_ACT]@/my-file``

Which form to use is a matter of taste.
