# Design: Video Streaming

**Goal:** upload, transcode, and deliver video.

## Key ideas

- Upload to object storage; transcode into multiple bitrates (DASH/HLS)
- Adaptive bitrate playback; CDN for segments
- Manifest and DRM; per-title encoding ladders
- View counting and recommendations asynchronously

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
