# India package
#### Version 0.0.1

This repository makes it easy to access metadata of states and union territories of India.
```python
>>> import india
>>> india.states.AR
Out: <State: Arunachal Pradesh>

```

You can also lookup whether your input is state or not.
```python
>>> import india
>>> india.states.lookup('arunachal pradesh')
Out: <State: Arunachal Pradesh>
```

