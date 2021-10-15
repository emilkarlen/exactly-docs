rst_prolog = """
.. _Reference Manual: https://emilkarlen.github.io/exactly/version/0-15-0/reference-manual.html

.. |conf__ph|     replace:: :emphasis:`conf`
.. |conf__phase|  replace:: |conf__ph| phase
.. |conf__ph_stx| replace:: :literal:`[conf]`

.. |setup__ph|     replace:: :emphasis:`setup`
.. |setup__phase|  replace:: |setup__ph| phase
.. |setup__ph_stx| replace:: :literal:`[setup]`

.. |act__ph|     replace:: :emphasis:`act`
.. |act__phase|  replace:: |act__ph| phase
.. |act__ph_stx| replace:: :literal:`[act]`

.. |before_assert__ph|     replace:: :emphasis:`before-assert`
.. |before_assert__phase|  replace:: |before_assert__ph| phase
.. |before_assert__ph_stx| replace:: :literal:`[before-assert]`

.. |assert__ph|     replace:: :emphasis:`assert`
.. |assert__phase|  replace:: |assert__ph| phase
.. |assert__ph_stx| replace:: :literal:`[assert]`

.. |cleanup__ph|     replace:: :emphasis:`cleanup`
.. |cleanup__phase|  replace:: |cleanup__ph| phase
.. |cleanup__ph_stx| replace:: :literal:`[cleanup]`

.. |atc__cpt|       replace:: Action To Check
.. |atc__cpt__def|  replace:: :emphasis:`Action To Check`
.. |atc__cpt_acr|   replace:: ATC
.. |actor__cpt|     replace:: Actor
.. |actor__cpt_def| replace:: :emphasis:`Actor`

.. |actor__kwd| replace:: :literal:`actor`

.. |file__actr_kwd|      replace:: :literal:`file`
.. |file__actr_name|     replace:: "file interpreter"
.. |source__actr_kwd|    replace:: :literal:`source`
.. |source__actr_name|   replace:: "source interpreter"
.. |cmd_line__actr_kwd|  replace:: :literal:`command`
.. |cmd_line__actr_name| replace:: "command line"
.. |null__actr_kwd|      replace:: :literal:`null`
.. |null__actr_name|     replace:: "null"

.. |instr__cpt|       replace:: Instruction
.. |instr__cpt_def_s| replace:: :emphasis:`Instructions`
.. |instr__cpt_s|     replace:: Instructions

.. |cd__cpt|          replace:: Current Directory
.. |cd__cpt_def|      replace:: :emphasis:`Current Directory`

.. |tcds__cpt|        replace:: Test Case Directory Structure
.. |tcds__cpt_def|    replace:: :emphasis:`Test Case Directory Structure`
.. |tcds__cpt_acr|    replace:: TCDS


.. |hds__cpt|           replace:: Home Directory Structure
.. |hds__cpt_def|       replace:: :emphasis:`Home Directory Structure`
.. |hds__cpt_acr|       replace:: HDS

.. |hds_home__ent|      replace:: :emphasis:`home`
.. |hds_home__opt|      replace:: :literal:`-rel-home`
.. |hds_home__bi|       replace:: :literal:`EXACTLY_HOME`
.. |hds_act_home__ent|  replace:: :emphasis:`act-home`
.. |hds_act_home__opt|  replace:: :literal:`-rel-act-home`
.. |hds_act_home__bi|   replace:: :literal:`EXACTLY_ACT_HOME`

.. |sds__cpt|        replace:: Sandbox Directory Structure
.. |sds__cpt_def|    replace:: :emphasis:`Sandbox Directory Structure`
.. |sds__cpt_acr|    replace:: SDS

.. |sds_act__ent|    replace:: :emphasis:`act`
.. |sds_act__opt|    replace:: :literal:`-rel-act`
.. |sds_act__bi|     replace:: :literal:`EXACTLY_ACT`
.. |sds_result__ent| replace:: :emphasis:`result`
.. |sds_result__opt| replace:: :literal:`-rel-result`
.. |sds_result__bi|  replace:: :literal:`EXACTLY_RESULT`
.. |sds_tmp__ent|    replace:: :emphasis:`tmp`
.. |sds_tmp__opt|    replace:: :literal:`-rel-tmp`
.. |sds_tmp__bi|     replace:: :literal:`EXACTLY_TMP`

.. |rel_here__opt|   replace:: :literal:`-rel-here`
.. |rel_sym__opt|    replace:: :literal:`-rel`
.. |rel_cd__opt|     replace:: :literal:`-rel-cd`

.. |relativity__cpt|          replace:: Realtivity
.. |relativity__cpt_s|        replace:: Realtivities
.. |relativity__cpt_def|      replace:: :emphasis:`Realtivity`
..                       |dflt_relativity__cpt|     replace:: Default Realtivity
.. |dflt_relativity__cpt_def| replace:: :emphasis:`Default Realtivity`

.. |os_path__pgm_kwd| replace:: :literal:`%`
.. |shell__pgm_kwd|   replace:: :literal:`$`
.. |pgm__pgm_kwd|     replace:: :literal:`run`

.. |string__typ|      replace:: :emphasis:`string`
.. |string__type|     replace:: |string__typ| type
.. |list__typ|        replace:: :emphasis:`list`
.. |list__type|       replace:: |list__typ| type
.. |path__typ|        replace:: :emphasis:`path`
.. |path__type|       replace:: |path__typ| type
.. |program__typ|     replace:: :emphasis:`program`
.. |program__type|    replace:: |program__typ| type
.. |file_m__typ|      replace:: :emphasis:`file-matcher`
.. |file_m__type|     replace:: |file_m__typ| type
.. |files_cond__typ|  replace:: :emphasis:`files-condition`
.. |files_cond__type| replace:: |files_cond__typ| type
.. |files_m__typ|     replace:: :emphasis:`files-matcher`
.. |files_m__type|    replace:: |files_m__typ| type
.. |files_src__typ|   replace:: :emphasis:`files-source`
.. |files_src__type|  replace:: |files_src__typ| type
.. |int_m__typ|       replace:: :emphasis:`integer-matcher`
.. |int_m__type|      replace:: |int_m__typ| type
.. |line_m__typ|      replace:: :emphasis:`line-matcher`
.. |line_m__type|     replace:: |line_m__typ| type
.. |text_m__typ|      replace:: :emphasis:`text-matcher`
.. |text_m__type|     replace:: |text_m__typ| type
.. |text_src__typ|    replace:: :emphasis:`text-source`
.. |text_src__type|   replace:: |text_src__typ| type
.. |text_trans__typ|  replace:: :emphasis:`text-transformer`
.. |text_trans__type| replace:: |text_trans__typ| type


.. |run_pgm__instr|       replace:: |pgm__pgm_kwd|
.. |run_os_path__instr|   replace:: |os_path__pgm_kwd|
.. |run_shell__instr|     replace:: |shell__pgm_kwd|

.. |env__instr|           replace:: :literal:`env`
.. |cd__instr|            replace:: :literal:`cd`
.. |timeout__instr|       replace:: :literal:`timeout`
.. |file_r__instr|        replace:: :literal:`file`
.. |file_d__instr|        replace:: :literal:`dir`
.. |copy__instr|          replace:: :literal:`copy`
.. |def__instr|           replace:: :literal:`def`
.. |stdin__instr|         replace:: :literal:`stdin`

.. |contents_r__instr|    replace:: :literal:`contents`
.. |contents_d__instr|    replace:: :literal:`dir-contents`
.. |exists__instr|        replace:: :literal:`exists`
.. |exit_code__instr|     replace:: :literal:`exit-code`
.. |stderr__instr|        replace:: :literal:`stderr`
.. |stdout__instr|        replace:: :literal:`stdout`

.. |inclusion_kwd|      replace:: :literal:`including`


.. |preproc__opt| replace:: :literal:`--preprocessor`
.. |act__opt|     replace:: :literal:`--act`
.. |keep__opt|    replace:: :literal:`--keep`
"""
