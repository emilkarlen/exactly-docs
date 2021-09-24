===============================================================================
Type system
===============================================================================

..
   - types
   - symbol
   - def
     - syntax
     - phases
   - ref
     - SYMBOL-REFERENCE
     - SYMBOL-NAME
   - help? type syntax
   - constant
     - cannot be mutated
     - cannot be initialized (ftm) from dynamic data
   - Built in symbols
   - CLI
     - ``symbol``
     - ``help type``
     - ``help syntax``

Exactly has a type system specialized for test cases:

* Data types

   ======= ====================================================================
   list    A sequence of zero or more string elements                                              
   path    A file path, with special support for directories in the "test case directory structure"
   string  A sequence of characters                                                                
   ======= ====================================================================

* Types involving logic

   ================= ==========================================================
   file-matcher      Matches properties of an existing file - type, name and contents                       
   files-condition   A condition of existence of a set of named files                                       
   files-matcher     Matches a set of files (e.g. the contents of a directory)                              
   files-source      Produces a set of files (for populating a directory)                                   
   integer-matcher   Matches an integer                                                                     
   line-matcher      Matches individual lines of a text                                                     
   program           An external program, with optional arguments, and optional transformation of the output
   text-matcher      Matches a text                                                                         
   text-source       Produces a text, from various sources                                                  
   text-transformer  Transforms a text
   ================= ==========================================================

How to use these types are exemplified later in this tutorial.


Symbols
===============================================================================


Definition
-------------------------------------------------------------------------------

Values are assigned to `symbols`::

  def string my_string = 'hello world'

Here, the symbol ``my_string`` is defined to be
a value of type ``string``.

::
   
   def text-matcher my_matcher = equals 'OK' || equals 'SUCCESS'

Here, the symbol ``my_matcher`` is defined to be
a value of type ``text-matcher``.
   
A symbol is a constant - a symbol may not be redefined.

Values are also constant - they may (unfortunately) not depend
on dymanic data (e.g. the output from a program).

Symbols may be defined in the phases

* `setup`
* `before-assert`
* `assert`
* `cleanup`


Reference
-------------------------------------------------------------------------------

Reference a symbol :samp:`{SYMBOL-NAME}`
using :samp:`@[{SYMBOL-NAME}]@`::

  [assert]

  stdout equals @[my_string]@

Here, ``my_string`` must be a symbol defined as either a `string`
or a `text-source`.

On the other hand::

  [assert]

  stdout equals my_string

Here ``my_string`` is treated as a string constant,
since strings need not be quoted.

As a contrast,
a symbol of a type involving logic can often be references
using just :samp:`{SYMBOL-NAME}`,
since instruction arguments of these types are often unambigious::

  [assert]

  def text-matcher my_expectation = equals 'hello world'

  stdout my_expectation

A symbol must be defined before it is referenced.


Built in symbols
===============================================================================

A number of symbols are built in / predefined.

These are listed in the `Reference Manual`_,
but can also be reported via the built in help:

.. code-block:: console

    $ exactly help builtin

Details about a specific built in symbol (e.g. ``OS_LINE_SEP``)
is reported by

.. code-block:: console

    $ exactly help builtin OS_LINE_SEP


Inspecting symbol definitions
===============================================================================

To list all symbols defined in the test case :file:`test.case`:

.. code-block:: console

    $ exactly symbol test.case

To display the definition of the symbol ``my_symbol`` in the same
test case:

.. code-block:: console

    $ exactly symbol test.case my_symbol


And to list all references to it:

.. code-block:: console

    $ exactly symbol test.case my_symbol --ref


Reference Manual
===============================================================================

The types are explained in the `Reference Manual`_,
and that information is also available via the built in help:

.. code-block:: console

    $ exactly help type

.. code-block:: console

    $ exactly help syntax

This will display an overview of the types, and the details of it's syntax
(respectively).
Append the type name to get the corresponding information about
a specific type.
