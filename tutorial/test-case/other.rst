===============================================================================
Kvar
===============================================================================


Test case status
===============================================================================

- ``[conf]/status``
- exit codes, exit identifiers


`integer-matcher`
===============================================================================

Syntax element that do not correspond to a type
===============================================================================

T ex

- ``RICH-STRING``


Overcomming limitations
===============================================================================

Symbols are non dynamic
-------------------------------------------------------------------------------

Files can be used in some cases::

  file f.txt = -stdout-from pgm-that-generates-dynamic-data

or environment variables::

  env my_var = -stdout-from pgm-that-generates-dynamic-data
