# Mean-Variance-Standard Deviation Calculator

A Python function that uses NumPy to calculate the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix — computed along both axes (rows and columns) and for the flattened matrix.


## What it does

The `calculate()` function takes a list of 9 numbers, converts it into a 3x3 NumPy array, and returns a dictionary containing:
- Mean
- Variance
- Standard deviation
- Max
- Min
- Sum

Each statistic is calculated three ways: down each column (axis 1), across each row (axis 2), and across the entire flattened matrix.

## Tech used
- Python
- NumPy

## Example

```python
from mean_var_std import calculate

calculate([0,1,2,3,4,5,6,7,8])
```

Returns:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Running the tests

```bash
python main.py
```

## Error handling

If the input list doesn't contain exactly 9 numbers, the function raises a `ValueError`:
```
List must contain nine numbers.
```
