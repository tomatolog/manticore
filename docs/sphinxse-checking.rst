.. raw:: html

   <div class="navheader">

10.2.3. Checking SphinxSE installation
`Prev <sphinxse-mysql51.html>`__ 
10.2. Installing SphinxSE
 `Next <sphinxse-using.html>`__

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

.. rubric:: 10.2.3. Checking SphinxSE installation
   :name: checking-sphinxse-installation
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

To check whether SphinxSE has been successfully compiled into MySQL,
launch newly built servers, run mysql client and issue ``SHOW ENGINES``
query. You should see a list of all available engines. Sphinx should be
present and “Support” column should contain “YES”:

.. code:: programlisting

    mysql> show engines;
    +------------+----------+-------------------------------------------------------------+
    | Engine     | Support  | Comment                                                     |
    +------------+----------+-------------------------------------------------------------+
    | MyISAM     | DEFAULT  | Default engine as of MySQL 3.23 with great performance      |
      ...
    | SPHINX     | YES      | Sphinx storage engine                                       |
      ...
    +------------+----------+-------------------------------------------------------------+
    13 rows in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------+-------------------------------------+-----------------------------------+
| `Prev <sphinxse-mysql51.html>`__               | `Up <sphinxse-installing.html>`__   |  `Next <sphinxse-using.html>`__   |
+------------------------------------------------+-------------------------------------+-----------------------------------+
| 10.2.2. Compiling MySQL 5.1.x with SphinxSE    | `Home <index.html>`__               |  10.3. Using SphinxSE             |
+------------------------------------------------+-------------------------------------+-----------------------------------+

.. raw:: html

   </div>
