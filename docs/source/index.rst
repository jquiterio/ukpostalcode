.. UK Postal Code and Validation documentation master file, created by
   sphinx-quickstart on Tue Apr 12 13:44:56 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to UK Postal Code and Validation's documentation!
=========================================================

.. toctree::
   :maxdepth: 2

Quickstart Usage::

    from ukpc import postalcode

VALIDATION::

    postalcode.isvalid("OX1 2JD")
    
    >>>True

FORMAT::

    postalcode.format_postalcode("OX12JD")
    
    >>>'OX1 2JD'

or::

    postalcode.format_postalcode("O X 12J D")
    
    >>>'OX1 2JD'


Index
========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

