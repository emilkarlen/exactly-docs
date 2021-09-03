===============================================================================
The structure of a Test Case
===============================================================================

.. plain text file
   execution
  
A test case is a plain text file.

The following test case confirms that the `cat` program on the
system copies stdin to stdout:

.. literalinclude:: examples/cat.case


A test case is executed by giving the path of the test case file to Exactly.
For example, if the file `cat.case` contains the text above:

.. code-block:: console

    $ exactly cat.case
    PASS

.. Phases
.. ===============================================================================

.. phases
   order of phases in file insignificant
   a phase may be declared multiple times - contents is accumulated
   instructions
   comments
   instruction descriptions
