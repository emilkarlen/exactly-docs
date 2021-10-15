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

|conf__ph|
  Configures the execution of the remaining phases by setting "configuration
  parameters".

|setup__ph|
  Sets up the environment that the "action to check" (the `act` phase) is
  executed in.

|act__ph|
  Contains the "action to check" - a program executed as an OS process.

|before_assert__ph|
  Prepares for the `assert` phase.

|assert__ph|
  Assertions on the outcome of the "action to check" (the `act` phase) that
  determine the outcome of the test case.

|cleanup__ph|
  Cleans up pollution from earlier phases.

All phases are optional.

Syntax
===============================================================================

As mentioned earlier, |setup__ph_stx| marks the start of |setup__phase|,
|act__ph_stx| the start of the |act__phase|, and so on.

The order of the phases in the test case file is irrelevant, and a phase may
be declared any number of times:

.. literalinclude:: examples/cat-phase-order.case

This test case does the same as the earlier example, except that it adds two
assertions.


Default phase
===============================================================================

|act__ph| is the default phase, so it need not be declared if it appears at the
top of the file:

.. literalinclude:: examples/cat-implicit-act.case
