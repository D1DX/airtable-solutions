# Parent-Children Sync

Author: Daniel Rudaev (D1DX)

Maintains bidirectional parent-child links in Airtable tables.

## Note: No Longer Needed

Airtable has updated their platform. When creating a linked record field to the same table, Airtable now automatically creates the opposite bidirectional link that syncs automatically. This script is preserved for legacy bases or specific edge cases.

## Scripts

- `sync-all.js` - Sync all parent-child relationships in the table
- `sync-record.js` - Sync a single record's parent-child relationships

## Usage

Automation scripts that manage hierarchical table relationships. Triggered by an Airtable automation.

## Setup

1. Copy the desired script from `src/` folder
2. Create an automation in Airtable
3. Add "Run a script" action
4. Paste the code
5. Configure input variables: `table`, `source`, `dest` (and `record` for sync-record.js)

## Parameters

- `table` - Table ID
- `source` - Source linked record field name
- `dest` - Destination linked record field name
- `record` (sync-record.js only) - Record ID to sync
