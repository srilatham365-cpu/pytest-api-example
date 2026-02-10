# Bugs Found During Assessment

## 1. Schema Bug in schemas.py
**Location:** `schemas.py`, line 9
**Issue:** The `name` property in the pet schema was defined as `"type": "integer"` instead of `"type": "string"`.
**Fix:** Changed to `"type": "string"` to match the actual data type of pet names.

## 2. String Formatting Bug in app.py
**Location:** `app.py`, line 101
**Issue:** The error message `'Invalid pet status {status}'` was not using f-string formatting, causing the literal string "{status}" to be displayed instead of the actual status value.
**Fix:** Changed to `f'Invalid pet status {status}'` to properly format the error message.
