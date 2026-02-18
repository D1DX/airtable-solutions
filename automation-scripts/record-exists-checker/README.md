# Record Exists Checker

Author: Daniel Rudaev (D1DX)

Checks if a record exists in a table and outputs the result.

## Usage

Automation script for validating record presence. Returns true or false via output.set.

## Setup

1. Copy `src/record-exists-checker.js`
2. Create an automation in Airtable
3. Add "Run a script" action
4. Paste the code
5. Pass `recordId` and `tableId` via automation input variables

## Parameters

- `recordId` (input.config) - ID of the record to check
- `tableId` (input.config) - ID of the table to search in

## Output

- `result` (output.set) - `true` if record exists, `false` if not
