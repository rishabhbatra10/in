# India package

![deployment](https://github.com/rishabhbatra10/in/workflows/deployment/badge.svg)
#### Version 1.1.1
### Installation
Installation Using pip
```bash
pip install pyindia
```

#### Running Tests

```bash
python -m unittest discover -s tests
```
### Usage
This repository makes it easy to access metadata of states and union territories of India.
```python
>>> import india
>>> india.states.AR
OUT: <State: Arunachal Pradesh>
```

You can also lookup whether your input is state or not.
```python
>>> import india
>>> india.states.lookup('arunachal pradesh')
OUT: <State: Arunachal Pradesh>
```

New release enables you to access districts/cities across india with several attributes
```python
>>> import india
>>> india.cities.KA_BLR
OUT: <City: Bangalore>

```

Lookup for cities
```python
>>> import india
>>> india.cities.lookup('Bangalore')
OUT: <City: Bangalore>
```

Check whether the city is capital
```python
>>> import india
>>> india.cities.lookup('Bangalore').iscapital()
OUT: True
```

### Attributes

Attributes of state object

```python
state.name       # name of the state
state.capital    # returns the capital of that state
state.population # returns the population of the state
state.area       # returns the area of state in km^2
state.density    # returns population density per km^2 of state
state.language   # primary official language of the state
```

Attributes of Cities object

```python
city.name       # name of the city
city.state      # returns the state of city
city.population # returns the population of the city
city.area       # returns the area of the district
city.density    # returns population density per km^2 of the city
city.url        # returns official webpage of the city
```

### Release Notes

<li> Added cities of india with there attributes and states they belong to.
<li> Added attributes to state objects including population, area and language.
<li> Added cities string access.
<li> Added states string access.
<li> Added uts string access.
<li> Added Jammu and Kashmir and Ladhakh as Union territories.
