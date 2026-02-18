# Multi-Table Merger (Incremental)

Author: Daniel Rudaev (D1DX)

Processes webhook payloads and syncs incremental record changes to a Results table.

## Usage

Automation script triggered by a webhook. Reads changed records from the payload and applies creates, updates, and deletes to the Results table.

## Setup

1. Copy `src/sync-changes-only.js`
2. Create an automation in Airtable triggered by a webhook
3. Add "Run a script" action
4. Paste the code
5. Configure the constants at the top of the script:
   - `SETTINGS_TABLE_NAME` - table name for cursor storage
   - `RESULTS_TABLE_NAME` - target table for synced records
   - `IGNORED_TABLE_NAMES` - tables to exclude from sync
   - `RECREATE_TRIGGER_FIELDS` - fields that trigger delete+recreate instead of update
6. Set up an Airtable secret named `PAT` with your personal access token
7. Pass `webhookId` via the automation input config

## Parameters

- `PAT` (secret) - Airtable personal access token
- `webhookId` (input.config) - Webhook ID to poll payloads from

## Related

See also: [Multi-Table Merger (Extension)](../../extension-scripts/multi-table-merger/) for initial full sync.
