# TCP Ping

[![PyPI version](https://badge.fury.io/py/tcpping.svg)](https://badge.fury.io/py/tcpping)

## Installation:
```pip install tcpping```

## Usage:
```python
from tcpping import tcpping

if tcpping(host = '10.10.10.10', port = 22, timeout = 5):
	print('yay!')
else:
	print('boo!')

```

## Credit:
@yantisj for the intitial code