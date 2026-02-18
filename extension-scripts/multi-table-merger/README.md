# Multi-Table Merger

Author: Daniel Rudaev (D1DX)

Full sync of all records from multiple tables into a single Results table.

## Usage

Extension script for initial bulk synchronization. Prompts for a personal access token, then mirrors all source records into the Results table, handling creates, updates, and soft-deletes.

## Setup

1. Create an Airtable extension in your base
2. Copy `src/sync-all-records.js`
3. Paste into extension code editor
4. Configure the constants at the top of the script:
   - `REFRESH_FIELDS` - fields that trigger a recreate instead of update
   - `TABLES_TO_NOT_SYNC` - tables to exclude
5. Run the extension and enter your personal access token when prompted

## Related

See also: [Multi-Table Merger (Automation)](../../automation-scripts/multi-table-merger/) for incremental webhook-based sync.
