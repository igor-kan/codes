# DRAM

Dynamic RAM stores bits as charge on capacitors, requiring periodic refresh.

## Organization

- **Banks** → **rows** → **columns**, accessed via RAS/CAS.
- **Row buffer:** open row can be read with low latency (row hit).
- **Page policy:** open-page exploits locality; close-page reduces conflicts.

## Performance

- **tRCD**, **tCAS**, **tRP**, **tRAS** timing parameters.
- **Row-buffer conflicts** cost extra cycles.
- Refresh consumes bandwidth.

## Modern interfaces

- DDR4/DDR5, LPDDR, HBM (high bandwidth via 3D stacking and wide buses).
- Multiple channels and ranks interleave addresses for parallelism.

## Implications for software

- Access memory sequentially within rows when possible.
- Avoid strided patterns that thrash the row buffer.
- NUMA: local memory access is far cheaper than remote.
