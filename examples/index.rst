===============================================================================
Examples (testing)
===============================================================================

Misc
===============================================================================

Inline (wo langauge)::

  [setup]

  stdin = "contents of stdin"

  [act]

  % cat

  [assert]

  stdout equals "contents of stdin"

literal-include (wo language):

.. literalinclude:: literalinclude.xly


literal-include (text):

.. literalinclude:: literalinclude.xly
   :language: text

code-block:

.. code-block:: html

   <h1>code block example</h1>

Shell
===============================================================================

The `console` language:

.. code-block:: console


   $ exactly test.case
   PASS

highlight spec (C)
===============================================================================

.. highlight:: c

.. literalinclude:: c.c
