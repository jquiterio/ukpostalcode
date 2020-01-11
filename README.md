# ukpostalcode

## Install:

$ pip install ukpostalcode

## Usage:

```import ukpostalcode as ukpc```

```pc = ukpc.ukpc("OX12JD")```


### Validation

```pc.isValid("OX1 2JD")```

return bool `True` if is valid else `False`


### Format

```pc.format("OX12JD")```

or

```pc.format("O X 12J D")```

or wathever the disposition of characters

return `string` `'OX1 2JD'` it will first validate with `isvalid`


### Getting more details (json)

```pc.details('OX1 2JD')```

this will get information from http://api.getthedata.com/postcode



