# Messy Example

This is a typical "quick and dirty" research script. It works, but has several problems.

## Issues with This Code

### 1. Poor Variable Names
- `d` - What kind of data?
- `x` - What does this represent?
- `m` - Mean of what?
- `r` - Results? Records? What?
- `s` - Sum? Score? Something else?

### 2. No Documentation
- No module docstring
- No function docstrings
- No comments explaining logic
- No indication of what the script does

### 3. Magic Numbers
- What does `2` represent in the multiplication?
- Why is `5` the threshold?
- Where do these values come from?

### 4. No Functions
- Everything is in one script
- Can't test individual pieces
- Can't reuse any logic
- Hard to debug

### 5. Mixed Concerns
- Data loading
- Data processing
- Visualization
- Statistical calculations
All jumbled together in one file

### 6. Inefficient Code
- Manual loop to calculate sum instead of using pandas/numpy
- Using iloc in a loop (slow for large datasets)

## Why This Matters

**In 6 months:**
- You won't remember what this code does
- You won't remember why you chose these values
- You'll waste time trying to understand your own code

**For collaborators:**
- They can't understand your methodology
- They can't reproduce your results
- They can't build on your work

**For reproducibility:**
- Hard to verify results
- Difficult to adapt for similar analyses
- Not suitable for publication

## The Fix

See the clean example (`02-clean-example/`) for how to improve this code using:
- Descriptive variable names
- Clear function definitions
- Comprehensive documentation
- Modular structure
