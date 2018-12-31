Quickstart Usage:

INSTALL:

$ pip install https://git.jquiterio.eu/jquiterio/ukpostalcode.git
>>>import ukpostalcode


VALIDATION
>>>ukpostalcode.isvalid("OX1 2JD")
>>>True


FORMAT


>>>ukpostalcode.format_postalcode("OX12JD")
>>>'OX1 2JD'


or:


>>>ukpostalcode.format_postalcode("O X 12J D")
>>>'OX1 2JD'




