.. raw:: html

   <div class="navheader">

12.4.37. expansion\_limit
`Prev <conf-thread-stack.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-watchdog.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.4.37. expansion\_limit
   :name: expansion_limit
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The maximum number of expanded keywords for a single wildcard. Optional,
default is 0 (no limit). Introduced in version 2.0.1-beta.

When doing substring searches against indexes built with
``dict = keywords`` enabled, a single wildcard may potentially result in
thousands and even millions of matched keywords (think of matching ‘a\*’
against the entire Oxford dictionary). This directive lets you limit the
impact of such expansions. Setting ``expansion_limit = N`` restricts
expansions to no more than N of the most frequent matching keywords (per
each wildcard in the query).

.. rubric:: Example:
   :name: example

.. code:: programlisting

    expansion_limit = 16

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+-----------------------------------+----------------------------------+
| `Prev <conf-thread-stack.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-watchdog.html>`__   |
+--------------------------------------+-----------------------------------+----------------------------------+
| 12.4.36. thread\_stack               | `Home <index.html>`__             |  12.4.38. watchdog               |
+--------------------------------------+-----------------------------------+----------------------------------+

.. raw:: html

   </div>
