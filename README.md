# ukpostalcode

## Install:

$ pip install ukpostalcode

## Usage:

```import ukpostalcode as ukpc```

```pc = ukpc.ukpc("OX12JD")```


### Validation

```pc.isValid()```

return bool `True` if is valid else `False`


### Format

```pc.format()```

or

```pc.format()```

or wathever the disposition of characters

return `string` `'OX1 2JD'` if `isValid`


### Getting more details (json)

```pc.details()```

this will get information from http://api.getthedata.com/postcode



