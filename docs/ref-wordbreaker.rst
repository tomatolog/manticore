.. raw:: html

   <div class="navheader">

7.5. \ ``wordbreaker`` command reference
`Prev <ref-indextool.html>`__ 
Chapter 7. Command line tools reference
 `Next <sphinxql-reference.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 7.5. \ ``wordbreaker`` command reference
   :name: wordbreaker-command-reference
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

``wordbreaker`` is one of the helper tools within the Sphinx package,
introduced in version 2.1.1-beta. It is used to split compound words, as
usual in URLs, into its component words. For example, this tool can
split “lordoftherings” into its four component words, or
“http://manofsteel.warnerbros.com” into “man of steel warner bros”. This
helps searching, without requiring prefixes or infixes: searching for
“sphinx” wouldn’t match “sphinxsearch” but if you break the compound
word and index the separate components, you’ll get a match without the
costs of prefix and infix larger index files.

Examples of its usage are:

.. code:: programlisting

    echo manofsteel | bin/wordbreaker -dict dict.txt split

The input stream will be separated in words using the ``-dict``
dictionary file. (The dictionary should match the language of the
compound word.) The ``split`` command breaks words from the standard
input, and outputs the result in the standard output. There are also
``test`` and ``bench`` commands that let you test the splitting quality
and benchmark the splitting functionality.

Wordbreaker Wordbreaker needs a dictionary to recognize individual
substrings within a string. To differentiate between different guesses,
it uses the relative frequency of each word in the dictionary: higher
frequency means higher split probability. You can generate such a file
using the ``indexer`` tool, as in

.. code:: programlisting

    indexer --buildstops dict.txt 100000 --buildfreqs myindex -c /path/to/sphinx.conf

which will write the 100,000 most frequent words, along with their
counts, from myindex into dict.txt. The output file is a text file, so
you can edit it by hand, if need be, to add or remove words.

See
http://sphinxsearch.com/blog/2013/01/29/a-new-tool-in-the-trunk-wordbreaker/
for more on this tool.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+---------------------------------------+
| `Prev <ref-indextool.html>`__             | `Up <command-line-tools.html>`__   |  `Next <sphinxql-reference.html>`__   |
+-------------------------------------------+------------------------------------+---------------------------------------+
| 7.4. \ ``indextool`` command reference    | `Home <index.html>`__              |  Chapter 8. SphinxQL reference        |
+-------------------------------------------+------------------------------------+---------------------------------------+

.. raw:: html

   </div>
