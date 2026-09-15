# System Design Case Studies

Worked designs for common interview prompts. Each note states the goal, key
ideas, and a checklist for structuring the interview answer.

## Marketplace and commerce

| Design | Prompt |
|:---|:---|
| `url_shortener.md` | short URLs with redirects and analytics |
| `payment_system.md` | exactly-once payments and a ledger |
| `ticket_booking.md` | seat inventory without double-selling |
| `hotel_booking.md` | availability and reservations |
| `stock_exchange.md` | low-latency matching engine |
| `ad_click_aggregator.md` | high-volume click counting with dedup |

## Social and media

| Design | Prompt |
|:---|:---|
| `news_feed.md` | ranked home timeline |
| `twitter_timeline.md` | timeline at extreme scale |
| `instagram.md` | photo upload, feed, media delivery |
| `chat.md` | 1:1 and group messaging |
| `whatsapp.md` | chat with offline delivery |
| `video_streaming.md` | upload, transcode, adaptive delivery |
| `yelp.md` | local business search and reviews |

## Mobility and delivery

| Design | Prompt |
|:---|:---|
| `ride_sharing.md` | realtime rider/driver matching |
| `uber.md` | ride-hailing backend |
| `food_delivery.md` | order, dispatch, tracking |
| `proximity_service.md` | nearby places search |

## Infrastructure and platform

| Design | Prompt |
|:---|:---|
| `distributed_cache.md` | shared low-latency cache |
| `distributed_lock.md` | mutual exclusion across nodes |
| `distributed_queue.md` | durable message queue |
| `key_value_store.md` | distributed KV with quorums |
| `unique_id.md` | distributed unique IDs |
| `metrics_monitoring.md` | time-series metrics platform |
| `api_gateway_design.md` | edge routing and policy |
| `webhook_delivery.md` | reliable outbound webhooks |
| `leaderboard.md` | realtime rankings |
| `code_judge.md` | sandboxed code execution |

## Search, crawling and notifications

| Design | Prompt |
|:---|:---|
| `search_autocomplete.md` | low-latency prefix suggestions |
| `web_crawler.md` | scalable polite crawling |
| `notification_system.md` | email/SMS/push fan-out |

## Files

| Design | Prompt |
|:---|:---|
| `google_drive.md` | file storage and sync |

See also `../fundamentals/`, `../low_level/` and `../ddia/` for the building
blocks these designs rely on.
