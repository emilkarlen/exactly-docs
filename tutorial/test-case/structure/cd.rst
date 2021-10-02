===============================================================================
`Current Directory`
===============================================================================

..
   cd concept
   initial value
   cd instruction
    - cd affects following instructions and phases
    - change to dir only in SDS
   cd is default relativity for paths in the SDS
    - file
    - dir
    - exists
    - contents
    - dir-contents
   cd is cd for external processes
   -rel-cd : rel the cd when the path is *used*

.. contents:: :local:

Exactly manages a `current directory`, much like a Unix shell.

The `act` directory of the SDS is the initial current directory.
It can be changed by the ``cd`` instruction.
It takes a single `path` argument::

  [setup]

  dir subdir

  cd  subdir

The relativity option ``-rel-cd`` denotes the current directory,
and is the default relativity of the `path` argument.

This relativity is also used as default by instrctions that creates
files. In this case, the ``dir`` instruction.
Thus the following is equivalent::

  [setup]

  dir -rel-cd subdir

  cd  -rel-cd subdir
  
And as said, the `act` directory of the SDS is the initial
current directory.
So if it has not been changed previously,
the following is also equivalent::
  
  [setup]

  dir -rel-act subdir

  cd  -rel-act subdir

A change of the current directory stays in effect for all following
instructions and phases, until it is changed again by ``cd``.

It is only possible to change to a directory in the SDS.
This is to avoid modifying permanent files and directories.
Thus, the following is *illegal*::

  [setup]

  cd -rel-home my-sub-dir

And also::

  [setup]

  cd @[EXACTLY_HOME]@


Use of the `current directory`
===============================================================================

The current directory is the default relativity for the initial `path`
argument of instructions that

 - create or modify files
 - asserts on files

::

   [setup]

   file empty.txt

   dir  sub-dir = {
     file empty-again.txt
     dir  sub-sub-dir
     }

   [assert]

   exists       empty.txt : type file && contents is-empty

   exists       sub-dir   : type dir  && dir-contents ( num-files == 2 )

   contents     empty.txt : is-empty

   dir-contents sub-dir   : num-files == 2

The current directory of Exactly is also the current
directory for the Action To Check and
external program run via instructions::

  [setup]

  dir sub-dir

  cd sub-dir

  [act]

  % pwd -P

  [assert]

  stdout equals <<EOF
  @[EXACTLY_ACT]@/sub-dir
  EOF

  stdout -from % pwd -P
         equals <<EOF
  @[EXACTLY_ACT]@/sub-dir
  EOF

Here, ``% pwd -P`` runs the command :command:`pwd` found in the OS PATH
(given the argument ``-P``).


`path` symbols and the `current directory`
===============================================================================

..
   uses cd when *referenced*, not when *defined*
   use string instead of path, when using default relativity

The following defines a `path` symbol relative the current directory::

  def path my_path = -rel-cd my-file

The symbol may be referenced, for example::

  [assert]
  
  exists @[my_path]@

Now what path does this denote?
The path is relative the current directory,
but what is the current directory?
There are two options: the current directory when

* ``my_path`` is defined
* ``my_path`` is referenced

The answer is the latter:
Resolving a `path` symbol defined with ``-rel-cd``
uses the current directory at the point where the symbol is *referenced*.
  
Thus, in the following test case ``@[my_path]@`` will be resolved
to two different paths, since the current directory
is changed inbetween the references::

  [setup]

  def path my_path = -rel-cd my-file

  dir sub-dir

  [assert]

  exists @[my_path]@

  cd sub-dir

  exists @[my_path]@
