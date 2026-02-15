# TikTok Headless Browser Scraping Evaluation

## Executive Summary

This document evaluates the feasibility of scraping TikTok's "Make Your Day" public-facing pages using headless browser automation. TikTok is widely regarded as **one of the most difficult targets** for web scraping in 2025-2026 due to its multi-layered anti-bot architecture, custom JavaScript virtual machine, aggressive fingerprinting, and behavioral analysis. Even with tools like `puppeteer-extra-plugin-stealth`, TikTok **frequently flags and blocks** headless browsers.

**Verdict:** Headless browser scraping of TikTok is technically possible but operationally fragile, expensive to maintain, and high-risk for detection. It requires residential proxies, advanced stealth tooling, behavioral simulation, and ongoing maintenance as TikTok updates its defenses.

---

## Table of Contents

1. [TikTok Anti-Bot Architecture](#1-tiktok-anti-bot-architecture)
2. [Target: "Make Your Day" Page Structure](#2-target-make-your-day-page-structure)
3. [Stealth Plugin Requirements](#3-stealth-plugin-requirements)
4. [Proxy Requirements](#4-proxy-requirements)
5. [AWS Lambda Feasibility](#5-aws-lambda-feasibility)
6. [Alternative Approaches](#6-alternative-approaches)
7. [Test Environment Setup (uv)](#7-test-environment-setup-uv)
8. [Proof-of-Concept Test Plan](#8-proof-of-concept-test-plan)
9. [Risk Assessment](#9-risk-assessment)
10. [Appendix A: Dependency Reference](#appendix-a-dependency-reference)
11. [Appendix B: TikTok Detection Techniques (Deep Dive)](#appendix-b-tiktok-detection-techniques-deep-dive)
12. [Appendix C: Test Script Inventory](#appendix-c-test-script-inventory)

---

## 1. TikTok Anti-Bot Architecture

TikTok employs a **custom JavaScript virtual machine (VM)** to obfuscate its client-side anti-bot logic. This is not standard JavaScript obfuscation — it is a full bytecode VM with its own instruction set.

### 1.1 Custom VM Details

| Feature | Details |
|---------|---------|
| **Opcodes** | 178 custom opcodes covering object manipulation, control flow, and stack operations |
| **Encryption** | Dual-layer: AES-256-CBC encryption + Leb128 compression (storage); Base64 encoding + checksum validation (transport) |
| **Memory model** | Hybrid: constant pools, heap memory, and stack memory |
| **Request signing** | Three-layer request signature verification |
| **Obfuscation techniques** | 20+ including ES6+ variable name encryption, control flow flattening, indexed variable reference replacement |

### 1.2 Detection Layers

TikTok's defense is multi-layered — defeating one layer is insufficient:

```
┌──────────────────────────────────────────────────────────┐
│  Layer 1: Transport Fingerprinting                       │
│  - TLS/JA3 fingerprint matching                          │
│  - HTTP/2 header ordering verification                   │
│  - Connection behavior analysis                          │
├──────────────────────────────────────────────────────────┤
│  Layer 2: Browser Environment Fingerprinting             │
│  - navigator.webdriver property detection                │
│  - Canvas fingerprinting via toDataURL                   │
│  - WebGL renderer/vendor strings                         │
│  - navigator.plugins enumeration                         │
│  - navigator.languages consistency                       │
│  - chrome.runtime object presence                        │
│  - Screen resolution & color depth                       │
│  - Timezone & locale consistency                         │
├──────────────────────────────────────────────────────────┤
│  Layer 3: Behavioral Analysis                            │
│  - Scroll cadence and velocity patterns                  │
│  - Click pacing and mouse movement trajectories          │
│  - Page reading time (dwell time)                        │
│  - Interaction timing variance (bots are too consistent) │
│  - Touch event patterns (mobile)                         │
├──────────────────────────────────────────────────────────┤
│  Layer 4: Request-Level Detection                        │
│  - Encrypted custom headers (X-Bogus, _signature)       │
│  - Device fingerprint tokens in requests                 │
│  - Real-time fraud scoring per request                   │
│  - Rate limiting with adaptive thresholds                │
│  - Session correlation across requests                   │
├──────────────────────────────────────────────────────────┤
│  Layer 5: Account & Session Enforcement                  │
│  - Login wall after N unauthenticated page loads         │
│  - CAPTCHA challenges on suspicious patterns             │
│  - Account-level ban for detected automation             │
│  - Shadow-banning (returning empty/stale data)           │
└──────────────────────────────────────────────────────────┘
```

### 1.3 Key Implication

TikTok's VM forces all clients to execute JavaScript in a real browser environment. Lightweight HTTP clients (`httpx`, `requests`) **cannot** generate valid request signatures without reverse-engineering the 178-opcode VM — which TikTok updates frequently.

---

## 2. Target: "Make Your Day" Page Structure

The TikTok landing/explore page (`tiktok.com/en` or `tiktok.com/explore`) is a React-based SPA with:

### 2.1 Page Characteristics

- **React-based SPA** with client-side rendering
- **Infinite scroll** for video feed (no traditional pagination)
- **Dynamic loading**: Content loaded via XHR/fetch to internal APIs
- **Login wall**: Prompted after ~3-5 unauthenticated page loads
- **Hydration data**: `<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__">` contains initial JSON payload

### 2.2 Available Public Data

| Data Category | Fields |
|---------------|--------|
| **Post metadata** | URL, cover image, description text, creation date, location |
| **Engagement metrics** | Likes, shares, plays, comments, saves |
| **Author info** | Username, display name, verified status, bio, follower count |
| **Music info** | Track name, artist, album, original sound flag |
| **Video technical** | Duration, resolution, format, dimensions |

### 2.3 Data Extraction Strategy

1. **Hydration JSON** (preferred): Parse `__UNIVERSAL_DATA_FOR_REHYDRATION__` script tag — contains full page data without needing to interact with the DOM
2. **Network interception**: Capture XHR responses from TikTok's internal API endpoints during scroll
3. **DOM scraping** (least reliable): CSS selectors for visible elements — breaks when TikTok updates class names

---

## 3. Stealth Plugin Requirements

### 3.1 puppeteer-extra-plugin-stealth (Node.js)

**Current status against TikTok: DETECTED**

The stealth plugin (v2.11.2) is explicitly known to be detected by TikTok in both headless and headful modes. The plugin developers acknowledge this is an "ongoing cat and mouse game" and that "completely preventing Chromium detection is probably impossible."

**Partial workarounds reported by the community:**
- Disable `chrome.runtime` evasion
- Disable `navigator.languages` evasion
- Manually delete `navigator.__proto__.webdriver` property
- Use Firefox via puppeteer-firefox (less detection)

**Evasion modules included in stealth plugin:**

| Evasion | Purpose | TikTok Status |
|---------|---------|---------------|
| `chrome.app` | Fakes chrome.app object | Partially effective |
| `chrome.csi` | Fakes chrome.csi object | Partially effective |
| `chrome.loadTimes` | Fakes chrome.loadTimes | Partially effective |
| `chrome.runtime` | Fakes chrome.runtime | **Must disable — causes detection** |
| `navigator.hardwareConcurrency` | Spoofs CPU cores | Effective |
| `navigator.languages` | Spoofs languages | **Must disable — causes detection** |
| `navigator.permissions` | Overrides Notification permission | Effective |
| `navigator.plugins` | Fakes plugin array | Partially effective |
| `navigator.webdriver` | Removes webdriver flag | Necessary but insufficient |
| `window.outerdimensions` | Fakes outer dimensions | Effective |
| `webgl.vendor` | Spoofs WebGL strings | Effective |
| `user-agent-override` | Consistent UA | Necessary but insufficient |
| `media.codecs` | Fakes codec support | Effective |
| `sourceurl` | Hides sourceURL | Effective |
| `iframe.contentWindow` | Patches iframe access | Effective |

### 3.2 playwright-stealth (Python)

Two maintained Python packages:

| Package | Version | Python | Notes |
|---------|---------|--------|-------|
| `playwright-stealth` | 2.0.0 (June 2025) | >=3.9 | Fork by Mattwmaster58 |
| `playwright-stealth-plugin` | 2.5.0 (Nov 2025) | >=3.10 | More actively maintained |

**Against TikTok:** Both provide the same fundamental evasion techniques as the Node.js stealth plugin. They help but are **not sufficient alone**. TikTok's behavioral and request-level detection layers catch what fingerprint evasion misses.

### 3.3 nodriver (Python) — Recommended Alternative

`nodriver` is the successor to `undetected-chromedriver`, created by the same developer. It uses a **custom CDP (Chrome DevTools Protocol) implementation** instead of Selenium/WebDriver, which gives it a structural advantage:

| Feature | nodriver | Playwright + stealth |
|---------|----------|---------------------|
| WebDriver footprint | None (no WebDriver protocol) | Masked but detectable |
| Architecture | Direct CDP communication | WebDriver → CDP bridge |
| Anti-bot bypass | CloudFlare, Imperva, hCaptcha | Depends on stealth plugin |
| Async support | Native async | Sync & async |
| Browser support | Chromium, Chrome, Edge, Brave | Chromium, Firefox, WebKit |
| Maintenance | Active (also forked as `zendriver`) | Active |

**Against TikTok:** `nodriver` has a better theoretical chance due to its non-WebDriver architecture, but no tool guarantees sustained access to TikTok.

### 3.4 Minimum Stealth Configuration

For any headless browser approach against TikTok, the following are **mandatory**:

```python
# Minimum stealth requirements — conceptual, not runnable as-is
stealth_config = {
    # Fingerprint coherence
    "user_agent": "Match real Chrome version exactly",
    "platform": "Must match UA (Win32 for Windows UA, etc.)",
    "viewport": {"width": 1920, "height": 1080},  # Common resolution
    "timezone": "Must match proxy IP geolocation",
    "locale": "Must match timezone region",
    "webgl_vendor": "Must match GPU for declared platform",
    
    # Behavioral simulation
    "mouse_movement": "Bezier curves, not linear",
    "scroll_pattern": "Variable speed, pauses, occasional scrollback",
    "dwell_time": "2-8 seconds between interactions",
    "typing_speed": "50-150ms between keystrokes, variable",
    
    # Network
    "proxy_type": "Residential (datacenter IPs are instantly blocked)",
    "proxy_rotation": "Per-session, not per-request",
    "request_spacing": "Random 3-10 second delays",
}
```

---

## 4. Proxy Requirements

### 4.1 Why Proxies Are Non-Negotiable

TikTok blocks datacenter IP ranges aggressively. Without residential proxies, any scraping attempt will be blocked within the first few requests regardless of stealth configuration.

### 4.2 Proxy Specifications

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Type** | Residential | Residential rotating |
| **Rotation** | Per-session sticky | Sticky 5-10 min sessions |
| **Pool size** | 50+ IPs | 500+ IPs |
| **Geolocation** | Match target market | US/EU residential pools |
| **Protocol** | HTTPS | HTTPS with SOCKS5 option |
| **Bandwidth** | 5 GB/month (testing) | 50+ GB/month (production) |

### 4.3 Proxy Provider Considerations

| Provider Category | Cost Range | Suitability |
|-------------------|------------|-------------|
| **Free/shared proxies** | $0 | Not viable — instantly detected |
| **Datacenter proxies** | $1-5/GB | Not viable — IP range blocked |
| **Residential rotating** | $5-15/GB | Minimum viable for TikTok |
| **ISP static residential** | $2-4/IP/month | Good for session-based scraping |
| **Mobile proxies** | $20-50/GB | Best evasion but expensive |

### 4.4 Bandwidth Estimation

| Operation | Estimated Data per Request | Notes |
|-----------|---------------------------|-------|
| Page load (no video) | 2-5 MB | HTML, JS bundles, thumbnails |
| Profile page | 1-3 MB | Hydration JSON + assets |
| Infinite scroll batch | 0.5-1.5 MB | XHR responses |
| Video metadata only | 0.1-0.3 MB | API response |

**For 1,000 profile scrapes/day:** ~3-5 GB residential proxy bandwidth/month.

---

## 5. AWS Lambda Feasibility

### 5.1 Lambda Constraints for Headless Browsers

| Constraint | Lambda Limit | Headless Browser Need | Assessment |
|------------|-------------|----------------------|------------|
| **Memory** | 128 MB - 10,240 MB | 1,024 MB minimum | Feasible |
| **Timeout** | Max 15 minutes | 30-120s per page | Feasible |
| **Package size** (ZIP) | 50 MB direct / 250 MB uncompressed | Chromium ~130 MB compressed | **Requires container image** |
| **Container image** | Up to 10 GB | Chromium + deps ~500 MB | Feasible |
| **Ephemeral storage** | 512 MB - 10,240 MB | Chromium unpacked ~400 MB | Feasible |
| **Concurrent executions** | 1,000 default | Depends on scale | Feasible |
| **Cold start** | 5-15s (container) | Adds to total time | Acceptable |
| **Networking** | NAT Gateway required for VPC | Must route through proxy | Additional cost |

### 5.2 Lambda Architecture for TikTok Scraping

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
│  EventBridge │───>│ Lambda       │───>│ Residential      │───> TikTok
│  (scheduler) │    │ (Container)  │    │ Proxy Service    │
└─────────────┘    │              │    └──────────────────┘
                   │ Playwright + │
                   │ Chromium +   │         ┌──────────┐
                   │ Stealth      │────────>│ S3       │
                   └──────────────┘         │ (results)│
                                            └──────────┘
```

### 5.3 Lambda Feasibility Verdict

| Aspect | Feasible? | Notes |
|--------|-----------|-------|
| Running Chromium | Yes | Via container image deployment |
| Stealth plugins | Yes | All Python packages install normally |
| Proxy integration | Yes | Route browser traffic through proxy |
| Cold start time | Marginal | 5-15s container cold start + 3-5s browser launch |
| Cost efficiency | Poor | ~$0.05-0.10 per invocation at 1GB/60s |
| Session persistence | No | Lambda is stateless — no cookie/session reuse across invocations |
| IP consistency | No | Each invocation gets a new Lambda IP (mitigated by proxy) |
| Scale | Limited | TikTok rate limits make parallelism counterproductive |

**Lambda is technically feasible but operationally suboptimal for TikTok scraping** because:
1. TikTok's login walls require session persistence (cookies, localStorage)
2. Cold starts add latency that increases detection risk
3. Cost per scrape is high for browser-based Lambda
4. Stateless nature prevents maintaining "warm" browser sessions

**Better alternative:** Long-running EC2 instances or ECS Fargate tasks with persistent browser sessions and proxy rotation.

---

## 6. Alternative Approaches

### 6.1 Comparison Matrix

| Approach | Difficulty | Detection Risk | Cost | Maintainability | Scale |
|----------|-----------|----------------|------|-----------------|-------|
| Headless browser (Playwright + stealth) | High | High | Medium | Low (breaks often) | Low |
| nodriver (CDP-based) | Medium | Medium-High | Medium | Medium | Low-Medium |
| Hydration JSON parsing | Medium | Medium | Low | Medium | Medium |
| Third-party API (Apify, ScrapFly) | Low | Low (they handle it) | High ($$$) | High | High |
| TikTok Research API | Low (if approved) | None | Free | High | Medium (rate limits) |
| Reverse-engineering internal APIs | Very High | Low (if done right) | Low | Very Low (breaks constantly) | High |

### 6.2 Recommended Strategy (Ordered by Priority)

1. **First choice — TikTok Research API**: If the use case qualifies, this is the only legitimate path. Review time: ~4 weeks. (Already evaluated in `TikTokReport.md` — unlikely to be approved for commercial use.)

2. **Second choice — Third-party scraping services**: Apify's TikTok Explore Scraper (99.1% success rate), ScrapFly, or similar. They handle anti-bot bypassing. Cost: usage-based pricing.

3. **Third choice — Hydration JSON + residential proxies**: Parse `__UNIVERSAL_DATA_FOR_REHYDRATION__` without full browser interaction. Lower detection surface than full DOM scraping.

4. **Fourth choice — nodriver + residential proxies**: Best self-hosted headless browser option due to non-WebDriver architecture.

5. **Last resort — Playwright + stealth + residential proxies**: Most flexible but highest detection rate. Use only for PoC evaluation.

---

## 7. Test Environment Setup (uv)

### 7.1 Project Structure

```
TikTok/
├── pyproject.toml              # uv project configuration
├── .python-version             # Python version pin
├── .env.example                # Proxy and config template
├── ruff.toml                   # Linter configuration
├── README.md                   # Setup instructions
├── src/
│   └── tiktok_scraper/
│       ├── __init__.py
│       ├── config.py           # Environment/proxy configuration
│       ├── stealth_config.py   # Browser stealth settings
│       ├── scrapers/
│       │   ├── __init__.py
│       │   ├── playwright_scraper.py   # Playwright + stealth approach
│       │   ├── nodriver_scraper.py     # nodriver/CDP approach
│       │   └── hydration_scraper.py    # JSON hydration approach
│       └── utils/
│           ├── __init__.py
│           ├── proxy.py        # Proxy rotation management
│           ├── fingerprint.py  # Fingerprint generation
│           └── behavioral.py   # Human-like behavior simulation
├── tests/
│   ├── __init__.py
│   ├── test_detection.py       # Verify stealth evasion
│   ├── test_proxy.py           # Validate proxy connectivity
│   └── test_scraping.py        # End-to-end scraping tests
└── scripts/
    ├── check_detection.py      # Run against bot detection test sites
    ├── evaluate_stealth.py     # Compare stealth approaches
    └── benchmark_lambda.py     # Lambda deployment feasibility
```

### 7.2 Dependencies

See `TikTok/pyproject.toml` for the complete dependency specification. Key packages:

**Core scraping:**
- `playwright` — Browser automation framework
- `playwright-stealth-plugin` — Anti-detection evasion for Playwright
- `nodriver` — CDP-based undetected browser automation
- `httpx` — Async HTTP client for API/hydration requests

**Parsing & data:**
- `selectolax` — Fast HTML parser (Modest engine)
- `pydantic` — Data validation and serialization

**Infrastructure:**
- `python-dotenv` — Environment configuration
- `rich` — Terminal output formatting

**Dev/testing:**
- `pytest` / `pytest-asyncio` — Test framework
- `ruff` — Linter

### 7.3 Setup Commands

```bash
# Navigate to project
cd TikTok/

# Create environment and install dependencies
uv sync

# Install Playwright browsers (Chromium)
uv run playwright install chromium

# Verify installation
uv run python -c "from playwright.sync_api import sync_playwright; print('Playwright OK')"
uv run python -c "import nodriver; print('nodriver OK')"

# Copy and configure environment
cp .env.example .env
# Edit .env with proxy credentials

# Run detection tests against bot-test sites
uv run python scripts/check_detection.py

# Run TikTok scraping evaluation
uv run python scripts/evaluate_stealth.py
```

---

## 8. Proof-of-Concept Test Plan

### 8.1 Phase 1: Stealth Baseline (No TikTok)

Test stealth configurations against known bot-detection test pages:

| Test Site | URL | What It Tests |
|-----------|-----|---------------|
| Bot.sannysoft.com | `bot.sannysoft.com` | WebDriver detection, plugins, languages |
| CreepJS | `abrahamjuliot.github.io/creepjs` | Canvas, WebGL, audio fingerprinting |
| BrowserLeaks | `browserleaks.com` | Comprehensive fingerprint analysis |
| Pixelscan | `pixelscan.net` | Headless detection score |
| Incolumitas | `bot.incolumitas.com` | Advanced bot detection |

**Success criteria:** Pass all tests with "human" classification before attempting TikTok.

### 8.2 Phase 2: TikTok Unauthenticated Access

Test each approach against TikTok's public pages:

| Test | Method | Target | Success Criteria |
|------|--------|--------|-----------------|
| T1 | Playwright + stealth | `tiktok.com/en` | Page loads without CAPTCHA |
| T2 | nodriver | `tiktok.com/en` | Page loads without CAPTCHA |
| T3 | httpx + hydration | `tiktok.com/@username` | Extract `__UNIVERSAL_DATA_FOR_REHYDRATION__` JSON |
| T4 | Playwright + proxy | `tiktok.com/explore` | Load explore feed |
| T5 | Scroll simulation | Feed page | Load 3+ batches via infinite scroll |
| T6 | Data extraction | Any page | Extract post metadata from hydration JSON |

### 8.3 Phase 3: Reliability Testing

| Test | Description | Metric |
|------|-------------|--------|
| R1 | 10 sequential requests, same proxy | Success rate % |
| R2 | 10 sequential requests, rotating proxy | Success rate % |
| R3 | 50 requests over 1 hour | Time-to-block |
| R4 | Login wall trigger point | Number of loads before login prompt |
| R5 | CAPTCHA frequency | % of requests returning CAPTCHA |

### 8.4 Phase 4: Lambda Evaluation (Optional)

Only if Phase 2-3 show >70% success rate:

| Test | Description |
|------|-------------|
| L1 | Deploy Playwright container to Lambda |
| L2 | Measure cold start + scrape latency |
| L3 | Validate proxy routing from Lambda |
| L4 | Cost analysis per successful scrape |

---

## 9. Risk Assessment

### 9.1 Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TikTok updates VM/detection | Very High | High | Ongoing maintenance; budget for breakage |
| Stealth plugins become obsolete | High | High | Multiple approach fallbacks (nodriver, hydration) |
| Residential proxy pool gets flagged | Medium | High | Multiple proxy providers; rotation strategy |
| Login wall blocks unauthenticated access entirely | Medium | Critical | Account pools (risky) or API-only approach |
| CAPTCHA solving becomes required | High | Medium | CAPTCHA service integration (2captcha, etc.) |
| Rate limiting reduces throughput | Very High | Medium | Accept low throughput; longer intervals |

### 9.2 Legal & Compliance Risks

| Risk | Details |
|------|---------|
| **TikTok ToS violation** | TikTok explicitly prohibits automated scraping in its Terms of Service |
| **CFAA (US)** | Automated access to computer systems may implicate the Computer Fraud and Abuse Act |
| **GDPR (EU)** | Scraping personal data of EU users requires lawful basis |
| **Rate of change** | Legal landscape for web scraping is evolving rapidly |

### 9.3 Operational Risks

- **High maintenance burden**: TikTok's defenses update frequently; scrapers break regularly
- **No SLA**: Self-hosted scraping has no uptime guarantees
- **Cost unpredictability**: Proxy bandwidth costs scale with failures (retries)
- **Data quality**: Shadow-banning returns stale/empty data without clear error signals

---

## Appendix A: Dependency Reference

### Python Packages (PyPI)

| Package | Version | Purpose | Required? |
|---------|---------|---------|-----------|
| `playwright` | >=1.52.0 | Browser automation | Yes (Approach 1) |
| `playwright-stealth-plugin` | >=2.5.0 | Anti-detection evasion | Yes (Approach 1) |
| `nodriver` | >=0.41 | CDP-based undetected browser | Yes (Approach 2) |
| `httpx` | >=0.28.0 | Async HTTP client | Yes (Approach 3) |
| `selectolax` | >=0.3.0 | Fast HTML/CSS parser | Yes |
| `pydantic` | >=2.12.0 | Data modeling/validation | Yes |
| `python-dotenv` | >=1.2.0 | Environment config | Yes |
| `rich` | >=14.0.0 | Terminal formatting | Optional |
| `pytest` | >=9.0.0 | Testing | Dev |
| `pytest-asyncio` | >=0.26.0 | Async test support | Dev |
| `ruff` | >=0.15.0 | Linting | Dev |

### System Dependencies

| Dependency | Purpose | Install |
|------------|---------|---------|
| Chromium browser | Playwright/nodriver browser engine | `playwright install chromium` |
| Chrome (system) | nodriver default browser | System install or `nodriver` auto-fetch |
| Xvfb (Linux only) | Virtual display for headed mode | `apt install xvfb` |

### Node.js Packages (if evaluating Puppeteer path)

| Package | Version | Purpose |
|---------|---------|---------|
| `puppeteer` | >=24.0.0 | Browser automation |
| `puppeteer-extra` | >=3.3.0 | Plugin framework |
| `puppeteer-extra-plugin-stealth` | >=2.11.0 | Anti-detection |

---

## Appendix B: TikTok Detection Techniques (Deep Dive)

### B.1 WebDriver Detection

TikTok checks for the `navigator.webdriver` property, which is `true` in automated browsers. Stealth plugins remove this, but TikTok also checks:

```javascript
// TikTok's VM checks (simplified representation)
Object.getOwnPropertyDescriptor(navigator, 'webdriver')
navigator.__proto__.webdriver
Object.getOwnPropertyNames(navigator).includes('webdriver')
```

### B.2 Canvas Fingerprinting

TikTok uses `HTMLCanvasElement.toDataURL()` to generate a canvas fingerprint. Headless browsers produce consistent/different canvas outputs compared to real browsers on the same hardware.

### B.3 Request Signature Generation

TikTok API requests include computed signatures:
- `X-Bogus` — Computed by the client-side VM
- `_signature` — Additional request signature
- `msToken` — Session token generated by VM execution

These signatures **cannot be replicated** without running TikTok's JavaScript VM, which is why headless browsers (that execute JS) are required over simple HTTP clients.

### B.4 Behavioral Signals Tracked

| Signal | Bot Pattern | Human Pattern |
|--------|------------|---------------|
| Mouse movement | Linear, teleporting | Curved, with momentum |
| Scroll speed | Constant | Accelerate/decelerate |
| Click timing | Fixed intervals | Variable with natural variance |
| Page dwell time | 0-1 seconds | 3-30 seconds |
| Viewport focus | Always focused | Tab switches, blur events |
| Touch events | None (desktop emulation) | Touch + gesture events (mobile) |

### B.5 TLS Fingerprinting (JA3/JA4)

TikTok correlates the TLS fingerprint of the connection with the declared User-Agent. A Chrome User-Agent with a Python/Node.js TLS fingerprint is an immediate red flag. This is why:
- `httpx`/`requests` alone fail (Python TLS stack fingerprint)
- Real Chromium via Playwright/nodriver matches Chrome's TLS fingerprint

---

## Appendix C: Test Script Inventory

The following scripts are provided in the `TikTok/scripts/` directory for evaluation:

| Script | Purpose | What It Tests |
|--------|---------|--------------|
| `check_detection.py` | Runs stealth browser against bot-detection test sites | Baseline stealth effectiveness |
| `evaluate_stealth.py` | Compares Playwright+stealth vs nodriver vs httpx against TikTok | Approach comparison |
| `benchmark_lambda.py` | Evaluates Lambda container deployment feasibility | Cold start, memory, cost |

### Running Tests

```bash
# Full test suite
cd TikTok/
uv run pytest tests/ -v

# Individual detection check
uv run python scripts/check_detection.py

# Stealth evaluation (requires proxy configuration in .env)
uv run python scripts/evaluate_stealth.py

# Lambda benchmark (requires AWS credentials)
uv run python scripts/benchmark_lambda.py
```

---

## References

- [Castle.io — What TikTok's virtual machine tells us about modern bot defenses](https://blog.castle.io/what-tiktoks-virtual-machine-tells-us-about-modern-bot-defenses/)
- [TikTok VM Reverse Engineering Analysis](https://www.xugj520.cn/en/archives/tiktok-vm-reverse-engineering-webmssdk.html)
- [ScrapFly — How To Scrape TikTok in 2026](https://scrapfly.io/blog/posts/how-to-scrape-tiktok-python-json)
- [Browserless — Stealth Scraping with Puppeteer or Playwright at Scale](https://www.browserless.io/blog/stealth-scraping-puppeteer-playwright)
- [puppeteer-extra issue — TikTok is detecting stealth plugin](https://lightrun.com/answers/berstend-puppeteer-extra-tiktok-is-detecting-puppeteer-extra-plugin-stealth)
- [BrowserStack — Running Playwright on AWS Lambda](https://www.browserstack.com/guide/playwright-aws-lambda)
- [nodriver — GitHub](https://github.com/ultrafunkamsterdam/nodriver)
- [Apify — TikTok Explore Scraper](https://apify.com/clockworks/tiktok-explore-scraper)
