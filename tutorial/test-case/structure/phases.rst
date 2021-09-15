===============================================================================
Phases
===============================================================================

A test case is a sequence of predefined "phases".
``[NAME]`` marks the start of the `NAME` phase.

The following test case uses the phases `setup`, `act` and `assert`:

.. literalinclude:: examples/cat.case


Executing a test case means executing the contents of each phase, in a
predefined order.


Predefined phases
===============================================================================

The phases are - in order of execution:

`conf`
  Configures the execution of the remaining phases by setting "configuration
  parameters".

`setup`
  Sets up the environment that the "action to check" (the `act` phase) is
  executed in.

`act`
  Contains the "action to check" - a program executed as an OS process.

`before-assert`
  Prepares for the `assert` phase.

`assert`
  Assertions on the outcome of the "action to check" (the `act` phase) that
  determine the outcome of the test case.

`cleanup`
  Cleans up pollution from earlier phases.

All phases are optional.

Syntax
===============================================================================

As mentioned earlier, ``[setup]`` marks the start of `setup` phase, ``[act]``
the start of the `act` phase, and so on.

The order of the phases in the test case file is irrelevant, and a phase may
be declared any number of times:

.. literalinclude:: examples/cat-phase-order.case

This test case does the same as the earlier example, except that it adds two
assertions.


Default phase
===============================================================================

`act` is the default phase, so it need not be declared if it appears at the
top of the file:

.. literalinclude:: examples/cat-implicit-act.case
