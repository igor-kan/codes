# Consistency Checking (fsck)

Filesystem checkers verify and repair on-disk structures after an unclean
shutdown when journaling alone is insufficient.

## What it checks

- Superblock sanity and magic numbers.
- Inode allocation bitmap vs inode table consistency.
- Block allocation bitmap vs inode block pointers.
- Link counts and directory entries.
- Orphaned inodes and duplicate block references.

## Phases (classic fsck)

1. Superblock and geometry.
2. Inode scan and link counts.
3. Directory structure and connectivity.
4. Reference counts for blocks.
5. Reconnect orphans to `lost+found`.

## Modern context

- Journaling and copy-on-write reduce the need for full fsck.
- Online scrubbing (ZFS/Btrfs) checksums data continuously.
- `fsck` still runs on ext4 after N mounts or on detected errors.
