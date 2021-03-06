===============================================================================
Representation and execution
===============================================================================

.. contents:: :local:

Test Case files
===============================================================================

A test case is represented by a text file.
A single file represents a single test case.

The following test case confirms that the :command:`cat` program on the
system copies stdin to stdout:

.. literalinclude:: examples/cat.case

If the file :file:`cat.case` contains this text, then Exactly can
execute it:

.. code-block:: console

    $ exactly cat.case
    PASS

The result is reported by an exit code together with an "exit identifier".
The "exit identifier" in this case is `PASS`. It is printed as a single line
on stdout.

If a test case passes, the exit code is 0. Otherwise it is non zero.

TODO Mention phases


File inclusion
===============================================================================


Explicit
-------------------------------------------------------------------------------

|inclusion_kwd| may be used to include parts of a test case from a file.
Here, the file |my_setup_file| is included under |setup__ph_stx|:

.. literalinclude:: examples/cat-including.case

The path |my_setup_file| is relative the location of the test case file.

.. note::
   |inclusion_kwd| may not be used under |act__ph_stx|.

.. |my_setup_file| replace:: :file:`my-setup.xly`



Implicit
-------------------------------------------------------------------------------

If the directory containing the test case file also contains a file
`exactly.suite`, then contents of this file is included in the test case.

`exactly.suite` represents a test suite - a collection of test cases, but may
also contain contents shared by all test cases in the suite, such as:

.. literalinclude:: examples/exactly-suite-w-tc-contents.xly


Preprocessing the test case file
===============================================================================


- CLI |preproc__opt|


Getting help
===============================================================================

- CLI
- Ref Man
  - online
  - generera via CLI
