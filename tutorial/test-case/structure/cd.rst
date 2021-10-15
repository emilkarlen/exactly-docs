===============================================================================
|cd__cpt_def|
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

Exactly manages a |cd__cpt_def|, much like a Unix shell.

The |sds_act__ent| directory of the |sds__cpt_acr| is the initial |cd__cpt|.
It can be changed by the |cd__instr| |instr__cpt|.
It takes a single |path__typ| argument::

  [setup]

  dir subdir

  cd  subdir

The |relativity__cpt| option |rel_cd__opt| denotes the |cd__cpt|,
and is the |dflt_relativity__cpt| of the |path__typ| argument.

This |relativity__cpt| is also used as default by |instr__cpt_s| that creates
files. In this case, the |file_d__instr| |instr__cpt|.
Thus the following is equivalent to the example abolve::

  [setup]

  dir -rel-cd subdir

  cd  -rel-cd subdir
  
And as said, the |sds_act__ent| directory of the |sds__cpt_acr| is the initial
|cd__cpt|.
So if it has not been changed previously,
the following is also equivalent to the example abolve::
  
  [setup]

  dir -rel-act subdir

  cd  -rel-act subdir

A change of the |cd__cpt| stays in effect for all following
|instr__cpt| and phases, until it is changed again by |cd__instr|.

It is only possible to change to a directory in the |sds__cpt_acr|.
This is to avoid modifying permanent files and directories.
Thus, the following is *illegal*::

  [setup]

  cd -rel-home my-sub-dir

And also::

  [setup]

  cd @[EXACTLY_HOME]@


Use of the |cd__cpt|
===============================================================================

The |cd__cpt| is the |dflt_relativity__cpt| for the initial |path__typ|
argument of |instr__cpt_s| that

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

The |cd__cpt| of Exactly is also the current
directory for the |atc__cpt| and
external program run via |instr__cpt_s|::

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


|path__typ| symbols and the |cd__cpt|
===============================================================================

..
   uses cd when *referenced*, not when *defined*
   use string instead of path, when using default relativity

The following defines a |path__typ| symbol relative the |cd__cpt|::

  def path my_path = -rel-cd my-file

The symbol may be referenced, for example::

  [assert]
  
  exists @[my_path]@

Now what path does this denote?
The path is relative the |cd__cpt|,
but what is the current directory?
There are two options: the current directory when

* ``my_path`` is defined
* ``my_path`` is referenced

The answer is the latter:
Resolving a |path__type| symbol defined with |rel_cd__opt|
uses the |cd__cpt| at the point where the symbol is *referenced*.
  
Thus, in the following test case ``@[my_path]@`` will be resolved
to two different paths, since the |cd__cpt|
is changed inbetween the references::

  [setup]

  def path my_path = -rel-cd my-file

  dir sub-dir

  [assert]

  exists @[my_path]@

  cd sub-dir

  exists @[my_path]@
