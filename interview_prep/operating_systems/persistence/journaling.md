# Journaling

Journaling writes metadata changes to a **write-ahead log** before applying
them, so crashes can be recovered consistently and quickly.

## Write-ahead protocol

1. Write the transaction (journal) block to the log.
2. On completion, write a **commit** record (checksum + marker).
3. Apply (**checkpoint**) the changes to their final locations.
4. Mark the transaction free.

## Modes

| Mode | What is journaled | Trade-off |
|:---|:---|:---|
| Writeback | metadata only | fast; data may be stale after crash |
| Ordered | metadata + ordered data | common default; good balance |
| Data (journal) | metadata and data | strongest; slowest |

## Crash recovery

Replay committed transactions from the log; discard incomplete ones. This is
**redo** journaling. **Undo** logging can also roll back partial changes.

## Related

- Copy-on-write filesystems never overwrite live data (ZFS, Btrfs).
- Checksums detect bit rot.
