# NTU-LA-2018

## How to Use?

1. Clone or download the repo to your device.

2. Implement your has_cycle in has_cycle.py

```python
def has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    return False
```

3.
Run the script
```bash
cd NTU-LA-2018/hw1_test
pip install pipenv
pipenv run python -m pip install -U pip==18.0  # somebug due to pip 18.1
pipenv install
pipenv run pytest
```
or

```bash
cd NTU-LA-2018/hw1_test
pip install pytest
pytest
```
