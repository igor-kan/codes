# File Systems (OSTEP)

## Abstraction

Files (named byte arrays) and directories (name → inode maps), organized in a
tree, with metadata (size, timestamps, permissions, owner).

## On-disk structures

- **Superblock:** filesystem metadata.
- **Inode:** per-file metadata and block pointers (direct + indirect).
- **Data blocks:** file contents.
- **Bitmaps:** track free inodes and blocks.
- **Directory:** name → inode number entries.

## Workloads

- **FAT** (linked allocation), **FFS** (cylinders + bitmaps),
- **ext4** (extents, journaling), **XFS**, **ZFS/Btrfs** (copy-on-write, checksums).

## Caching and durability

- Page cache buffers reads/writes.
- `fsync` forces durability; write barriers order writes.
- Journaling makes crash recovery fast and consistent.
