# BrightData Final Evaluation Report


## Current Stack Baseline

| Source | Current Solution | Status |
|--------|-----------------|--------|
| Google Search | SerpAPI | Working |
| Google Images | SerpAPI | Working |
| YouTube / Shorts | SerpAPI | Working |
| GoFundMe | Puppeteer on Lambda | Working (fragile) |
| Instagram | None | Not implemented |
| TikTok | None | Not implemented |
| Reddit | None | Not implemented |

**Current monthly cost (confirmed):**
- SerpAPI Production Plan (Google + Images + YouTube): **$150/mo** — includes 15,000 searches/month, 3,000 throughput/hour, U.S. Legal Shield
- Lambda compute (GoFundMe Puppeteer): ~$10–$30/mo at typical watchdog query rates
- Instagram, TikTok, Reddit: $0 (no coverage)

**Total current cost: ~$160–$180/mo** (with 3 sources missing entirely)

> Note: The Production plan's 15,000 searches/month cap (~500 searches/day) is the binding constraint for scaling. At 5,000 queries/day per source, SerpAPI would need to be upgraded to a higher tier or a second account.

---

## Cost Analysis

### Assumptions & Unit Clarification

> **Critical distinction:** SerpAPI charges per **search** (1 API call = 1 SERP page ≈ 10 organic results). BrightData charges per **record** (1 individual result item). These are not the same unit and cannot be compared directly without conversion.

| Unit | SerpAPI | BrightData |
|------|---------|------------|
| Billing unit | 1 search = 1 API call | 1 record = 1 result item |
| Results per call | ~10 organic results per SERP page | 1 |
| Conversion | 1 search ≈ 10 records | 1 record = 1 record |

- **5,000 queries/day per source:**
  - If interpreted as **5,000 searches/day** → 150,000 searches/month → SerpAPI Production plan (15k searches) exceeded in 3 days
  - If interpreted as **5,000 records/day** → ~500 searches/day → 15,000 searches/month → Production plan covers it exactly
- BrightData pricing: **$0.0015 per record** (min), volume discounts available
- BrightData subscription plans: $500/mo (510k records), $1,000/mo (1M records)
- **SerpAPI Production Plan: $150/mo — 15,000 searches/month ≈ 150,000 records/month** (confirmed active subscription)
- Reddit Official API: Free (100 req/10 min), but not scalable for Fuzzy's user volume
- EnsembleData: $200–$400/mo Silver, $800/mo Gold (25k units, ~220k records equivalent)

### Cost Table — Monthly Estimates

> **SerpAPI uses searches (not records) as its billing unit.** The table separates both dimensions. At 5,000 searches/day, the Production plan is exceeded. At 5,000 records/day (~500 searches/day), the Production plan covers it exactly.

#### Scenario: 5,000 records/day per source (≈ 500 searches/day on SerpAPI)

| Source | Records/Month | Searches/Month (SerpAPI equiv.) | Current Stack | Scenario A (BD All) | Scenario B (BD New Only) |
|--------|:------------:|:----------------------------:|---------------|---------------------|--------------------------|
| Google Search | ~150,000 | ~15,000 searches | SerpAPI — bundled in $150/mo plan | BD ~$225 | SerpAPI — bundled $150/mo |
| Google Images | ~150,000 | ~15,000 searches | SerpAPI — bundled in $150/mo plan | BD ~$225 | SerpAPI — bundled |
| YouTube / Shorts | ~150,000 | ~15,000 searches | SerpAPI — bundled in $150/mo plan | BD ~$225 | SerpAPI — bundled |
| GoFundMe | ~150,000 | n/a (scraper) | Lambda ~$20 | BD Scraping Browser ~$100–$200* | Lambda ~$20 |
| Instagram | ~150,000 | n/a | — | BD ~$225 | BD ~$225 |
| TikTok | ~150,000 | n/a | — | BD ~$225 | BD ~$225 |
| Reddit | ~150,000 | n/a | — | BD ~$225 | BD ~$225 |
| **TOTAL** | | | **~$170/mo** | **~$1,450–$1,550/mo** | **~$845/mo** |

> At this volume, the SerpAPI Production plan ($150/mo) covers all 3 Google/YouTube/Images sources exactly (15k searches/mo cap = ~150k records/mo). No plan upgrade needed.

#### Scenario: 5,000 searches/day per source on SerpAPI (= 150,000 searches/month — plan exceeded 10×)

| Source | Searches/Month | Records/Month (equiv.) | SerpAPI Scaled | Scenario A (BD All) | Scenario B (BD New Only) |
|--------|:-----------:|:-------------------:|----------------|---------------------|--------------------------|
| Google Search | ~150,000 | ~1,500,000 | ~$500–$750/mo est. | BD ~$225 | ~$500–$750/mo est. |
| Google Images | ~150,000 | ~1,500,000 | bundled | BD ~$225 | bundled |
| YouTube / Shorts | ~150,000 | ~1,500,000 | bundled | BD ~$225 | bundled |
| GoFundMe | n/a | ~150,000 | Lambda ~$20 | BD ~$100–$200* | Lambda ~$20 |
| Instagram | n/a | ~150,000 | — | BD ~$225 | BD ~$225 |
| TikTok | n/a | ~150,000 | — | BD ~$225 | BD ~$225 |
| Reddit | n/a | ~150,000 | — | BD ~$225 | BD ~$225 |
| **TOTAL** | | | **~$520–$770/mo** | **~$1,450–$1,550/mo** | **~$1,195–$1,445/mo** |

> *GoFundMe on BrightData uses the Scraping Browser (compute-billed), not the Dataset API. Estimate is $0.10–$0.15/hour; at high daily volumes this varies significantly.

> BrightData at 150k records/mo per source × 6 sources = 900k records/mo → fits within the $1,000/mo plan (1M records).

**Key insight:** At 5,000 *records*/day the Production plan already covers Google/YouTube/Images — no upgrade needed, and BrightData would be more expensive for those 3 sources ($675/mo vs $150/mo). The upgrade pressure only applies if Fuzzy needs 5,000 *searches*/day (i.e., 5,000 distinct SERP pages fetched daily), which at ~10 results each would mean 50,000 results/day — a very different scale.

### Scenario B vs EnsembleData Comparison (New Sources Only)

| Metric | EnsembleData Silver | EnsembleData Gold | BrightData (~3 sources) |
|--------|--------------------|--------------------|--------------------------|
| Monthly Cost | $400 | $800 | ~$450–$675 |
| Volume Included | 220k records est. | 220k records est. | 450k records |
| Cost per Record | ~$0.0016 | ~$0.0036 | ~$0.001 |
| Keyword Search | Limited | Limited | Yes (TikTok, Reddit) |
| Instagram Support | No Keywords | No Keywords | Yes (structured API) |

**Verdict:** BrightData is cheaper per record than EnsembleData at comparable volume, and provides more structured, platform-specific endpoints.

---


### New Sources: Can BrightData Support Them?

#### Instagram:
**Hybrid approach (resolved):** BrightData's Instagram API alone is insufficient for watchdog use cases because it requires a known profile URL — it cannot discover accounts by keyword. The solution is a **Discovery-First** layer using a specialized social search tool (e.g., **RocketAPI** or **SociaVault**, ~$80–$100/mo) to perform keyword searches for brand name variations, identify matching profile URLs, and feed those into BrightData's Instagram Profile API for structured data extraction.

- **Data quality: Good.** Structured JSON with 100% fill rates on core fields (`url`, `date_posted`, `likes`, `num_comments`, `post_id`, `is_verified`, `followers`).
- Supports Profiles, Posts, Reels, and Comments via dedicated endpoints.
- Response time: 5–9 seconds per input (synchronous); async available.
- **Discovery gap — mitigated:** No keyword-based search natively. Solved via the Social Discovery layer (RocketAPI/SociaVault) which identifies profile URLs for downstream BrightData extraction of `follower_count`, `is_verified`, `recent_posts`, etc.
- **Image/media URLs expire in 2–3 days** due to Instagram signed CDN policy. Media must be downloaded immediately after scrape if persistence is needed.
- Comments capped at 15 most recent per post.

#### TikTok:
Yes

- **Data quality: Good.** Structured JSON with strong fill rates on `url`, `description`, `play_count`, `digg_count`, `comment_count`, `create_time`, `profile_url`, `video_url`.
- Posts support **keyword-based discovery** — directly useful for Fuzzy watchdog event matching.
- Profile Fast API (3s per input) enables low-latency profile monitoring.
- **Key limitation:** Response times are high: 24–28s for standard post endpoints.

#### Reddit

Yes — **hybrid model confirmed.**

- **Data quality: Good.** Full post body, comments with replies, user info, subreddit metadata, related posts — all returned in a single record.
- Supports **keyword-based discovery** across all posts. Subreddit-level discovery is available. Response time ~18s per input.
- **Hybrid model:** BrightData is the **primary engine for bulk discovery** across subreddits (bypassing the 100 req/10 min OAuth2 ceiling). The **free official Reddit API** is retained for high-priority, real-time monitoring of specific known threads where low latency matters. This ensures 100% coverage without being throttled at scale.

---

### Existing Sources: Can BrightData Replace Them?

#### Google Search & Images
 NO, i think we need to keep SerpAPI; at least, if it stays like a viable option after the legal problems that it have

- BrightData can scrape Google results via their Web Scraper / SERP API, but **SerpAPI is purpose-built** for this with structured output, pagination support, and highly reliable parsing.
- SerpAPI's Google engine returns rich SERP data (knowledge graph, related searches, image results) that BrightData's generic scraper would require custom parsing to match.
- Migration effort: Medium-High. Risk: High (SerpAPI is battle-tested for Fuzzy).
- **Cost comparison (apples to apples):** SerpAPI's Production plan ($150/mo) covers **15,000 searches/month ≈ 150,000 records/month** across all 3 Google sources bundled. BrightData for the equivalent 150k records/month per source would cost **$225/mo per source × 3 = $675/mo** — 4.5× more expensive at the same record volume. The SerpAPI Production plan is a much better deal for Google/YouTube/Images unless Fuzzy needs more than 15,000 *searches* (not records) per month.

#### YouTube / Shorts
Keep SerpAPI

- SerpAPI has a dedicated YouTube engine with structured results (title, channel, views, duration, published date) that is already working in production.
- BrightData does not have a dedicated YouTube structured dataset API in the same tier — it would require Scraping Browser, adding complexity and cost.

#### GoFundMe
**Confirmed: migrate to BrightData Scraping Browser.**

- **Current pain point:** Puppeteer on Lambda is fragile — requires manual proxy rotation, CAPTCHA handling, and breaks when GoFundMe updates its DOM. This results in recurring engineering overhead for weekly fixes.
- **Migration path:** Only the WebSocket `connect()` URL in the existing Puppeteer script needs to change — BrightData's Scraping Browser is a drop-in replacement that adds self-healing technology, automated proxy rotation, and CAPTCHA handling.
- BrightData Scraper Studio (Self-Healing technology) further reduces maintenance when GoFundMe UI changes.
- **Migration effort: Low** — only the WebSocket connection URL in the existing Puppeteer script needs to change.
- **Cost delta:** Lambda ~$20/mo → BD Scraping Browser ~$100/mo. The increase (~$80/mo) is justified by the elimination of recurring engineering hours for maintenance.

---

### Should SerpAPI Be Replaced by BrightData?

| Dimension | SerpAPI | BrightData |
|-----------|---------|------------|
| Google SERP structure | Excellent (purpose-built) | Good (generic scraper) |
| YouTube support | Excellent (dedicated engine) | Limited (no structured API) |
| Google Images | Excellent | Generic |
| Cost at 5k records/day (15k searches/mo) | $150/mo — Production plan covers it  | ~$675/mo (3 sources × $225) |
| Cost at 5k searches/day (150k searches/mo) | ~$500–$750/mo (custom/enterprise tier) | ~$675/mo (same — BD charges per record not per search) |
| Migration effort | — | Medium-High |
| Stability / uptime | High (production-proven) | High (enterprise SLA) |
| Support quality | Good (direct API docs) | Good (enterprise support) |
| Risk of switching | Low (current) | Medium (unknown edge cases) |

**Verdict: Keep SerpAPI at current volume ($150/mo Production plan).** At present query rates the plan is cost-effective and battle-tested. However, if Fuzzy's query volume grows beyond the 15,000/mo cap, SerpAPI scaling costs will exceed BrightData's — at that inflection point, migrating Google/YouTube to BrightData becomes financially justified. This should be re-evaluated when usage consistently hits the plan ceiling.

---

### Known Limitations

| Limitation | Affected Source | Impact |
|-----------|----------------|--------|
| No native keyword search | Instagram | **Mitigated:** Social Discovery layer (RocketAPI/SociaVault, ~$80–$100/mo) performs keyword search and feeds profile URLs to BrightData |
| Signed media URLs expire 2–3 days | Instagram | High: must download/store media at scrape time |
| 15-comment cap | Instagram Comments | Low for watchdog (recent comments only) |
| High latency (24–58s) on some endpoints | TikTok | Medium: async mode recommended |
| Free tier: 100 records total | All BrightData | Only for initial testing |
| Reddit official API: 100 req/10 min | Reddit | High at scale — mitigated: BrightData handles bulk; free API retained for real-time priority threads |
| GoFundMe: fragile Puppeteer on Lambda | GoFundMe | **Resolved:** migrating to BrightData Scraping Browser |

---

### Decision: **Option B — Use BrightData for new sources only (keep SerpAPI)**

| Source | Solution | Rationale |
|--------|----------|-----------|
| **Google Search** | SerpAPI (keep) | Cheaper, purpose-built, production-stable |
| **Google Images** | SerpAPI (keep) | Bundled, no benefit to switch |
| **YouTube / Shorts** | SerpAPI (keep) | Dedicated engine, no BD equivalent |
| **GoFundMe** | BrightData Scraping Browser (**confirmed migration**) | Eliminates fragile Lambda/Puppeteer setup; low-effort swap of WebSocket URL; ~$100/mo justified by reduced engineering overhead |
| **Instagram** | BrightData + Social Discovery layer (adopt) | BrightData handles deep extraction; RocketAPI/SociaVault (~$80–$100/mo) bridges the keyword discovery gap |
| **TikTok** | BrightData (adopt) | Keyword search works; use async for performance |
| **Reddit** | BrightData (adopt) | Free API not scalable; BD is cost-effective at scale |

### Estimated Monthly Cost (Option B)

#### At current query volume (within 15k/mo SerpAPI Production plan):

| Layer | Cost |
|-------|------|
| SerpAPI Production Plan (Google + Images + YouTube, all bundled) | **$150/mo** |
| Social Discovery Layer — Instagram keyword search (RocketAPI/SociaVault) | **~$80–$100/mo** |
| BrightData — Instagram (150k records/mo @ $0.0015) | **$225/mo** |
| BrightData — TikTok (150k records/mo @ $0.0015) | **$225/mo** |
| BrightData — Reddit (150k records/mo @ $0.0015) | **$225/mo** |
| BrightData — GoFundMe Scraping Browser (confirmed migration) | **~$100/mo** |
| **Total** | **~$1,005–$1,025/mo** |

#### At scaled volume (5,000 queries/day per source — SerpAPI 15k/mo cap exceeded):

| Layer | Cost |
|-------|------|
| SerpAPI custom/enterprise tier (Google + Images + YouTube at 450k/mo) | **~$500–$750/mo est.** |
| Social Discovery Layer — Instagram keyword search (RocketAPI/SociaVault) | **~$80–$100/mo** |
| BrightData — Instagram (150k records/mo) | **$225/mo** |
| BrightData — TikTok (150k records/mo) | **$225/mo** |
| BrightData — Reddit (150k records/mo) | **$225/mo** |
| BrightData — GoFundMe Scraping Browser (confirmed migration) | **~$100/mo** |
| **Total** | **~$1,355–$1,625/mo** |

#### At scaled volume — Option A comparison (BD replaces SerpAPI too):

| Layer | Cost |
|-------|------|
| BrightData — Google + Images + YouTube (450k records/mo) | **~$675/mo** |
| BrightData — Instagram + TikTok + Reddit (450k records/mo) | **$675/mo** |
| BrightData — GoFundMe (Scraping Browser) | **~$100–$200/mo** |
| **Total** | **~$1,450–$1,550/mo** |

> At scaled volume, the gap between Option B with SerpAPI ($1,195–$1,445/mo) and Option A with BrightData ($1,450–$1,550/mo) shrinks to ~$100–$250/mo — and BrightData would consolidate all billing into one vendor. The SerpAPI→BrightData migration for Google/YouTube becomes financially justified once the Production plan cap is consistently hit.

The current $150/mo Production plan is cost-efficient for Fuzzy's present query load. Adding BrightData for the three new sources costs $675/mo fixed (3 × $225), totalling **$845/mo** — still below EnsembleData Gold ($800/mo) in platform coverage, and with better per-record economics ($0.001 vs $0.0036).

### Implementation Roadmap

#### Phase 1 — Immediate: Low-Hanging Fruit
- **Reddit:** Activate BrightData keyword and subreddit discovery; plug into watchdog event matching.
- **TikTok:** Activate BrightData Posts endpoint for keyword discovery; use async mode for bulk jobs.

#### Phase 2 — Short-term: Instagram Coverage
- **Instagram:** Deploy the Social Discovery layer (RocketAPI/SociaVault) for keyword-based account discovery. Feed identified profile URLs into BrightData's Instagram Profile API for automated deep-scans of flagged accounts (`follower_count`, `is_verified`, `recent_posts`).
- **GoFundMe:** Swap Puppeteer `connect()` URL to BrightData Scraping Browser WebSocket. Eliminates proxy rotation and CAPTCHA handling overhead.

#### Phase 3 — Long-term: SerpAPI Re-evaluation
- Monitor SerpAPI usage against the 15,000 searches/month cap. Once usage consistently hits the ceiling, consolidate Google, Images, and YouTube into BrightData to achieve better per-record economics and single-vendor billing. At that inflection point the cost gap between Option B and Option A shrinks to ~$100–$250/mo.


