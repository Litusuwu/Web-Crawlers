### **Executive Strategy & Infrastructure Summary**

#### **1\. Instagram: Solving the Discovery Gap**

BrightData is highly effective for data extraction but lacks native keyword search for Instagram. To identify impersonation accounts at scale, we must implement a **Discovery-First** approach:

- **The Solution:** We will integrate a specialized "Social Discovery" layer (e.g., **RocketAPI** or **SociaVault**) to perform keyword searches for brand name variations.
- **The Workflow:** This layer identifies matching Profile URLs, which we then feed into **BrightData’s Instagram Profile API** to extract metadata like `follower_count`, `is_verified`, and `recent_posts` for automated fraud detection.
- **Cost Efficiency:** This hybrid model adds approximately **$80–$100/mo** but eliminates the need to manually discover accounts via Google Search.

#### **2\. GoFundMe: Transitioning to Managed Scraping**

Our current Puppeteer-on-Lambda setup is "fragile" and prone to breaking when GoFundMe updates its DOM.

- **We can** migrate the connection URL in our existing scripts to the **BrightData Scraping Browser**.
- **This allows us** to leverage BrightData's self-healing technology and automated proxy rotation, reducing maintenance overhead from weekly fixes to near-zero.
- **The Cost:** This move increases GoFundMe compute costs from **~$20/mo to ~$100/mo**, which we justify through the reduction in engineering hours required for maintenance.

#### **3\. Reddit: Bypassing Rate-Limit Constraints**

The official Reddit API limits us to 100 requests every 10 minutes, which is insufficient for our 100k+ user scale.

- **We must** use BrightData as our primary engine for bulk discovery across subreddits.
- **We can** maintain a hybrid model: the free official API for high-priority real-time monitoring of specific known threads, and BrightData for the high-volume keyword watchdog.
- **The Result:** This ensures 100% coverage without being throttled by Reddit’s OAuth2 ceilings.

#### **4\. Updated Implementation Roadmap**

To minimize risk and maximize ROI, we will follow a three-phase rollout:

- **Phase 1 (Immediate):** Activate **Option B** (Reddit and TikTok) using BrightData’s structured APIs to capture "low-hanging fruit" impersonations.
- **Phase 2 (Short-term):** Deploy the **Instagram Discovery Layer** to bridge the keyword gap and begin automated deep-scans of flagged profiles.
- **Phase 3 (Long-term):** Monitor **SerpAPI** usage. Once we consistently hit the 15,000 search/month cap, we will consolidate Google and YouTube into BrightData to achieve better per-record economics.

---

**Would you like me to generate a finalized "Consolidated Cost Table" that includes these specific discovery tools for your final appendix?**
