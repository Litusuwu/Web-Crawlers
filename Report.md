# Reddit

Traffic not using OAuth or login 
credentials will be blocked (no default rate limit also).

Free acces rate limits:
2000 messages per day per recipient
3000 messages per day total
100 queries per minute per OAuth

The rate limits are monitored in the response header:

* X-Ratelimit-Used: Approximate number of requests used in this period
* X-Ratelimit-Remaining: Approximate number of requests left to use
* X-Ratelimit-Reset: Approximate number of seconds to end of period

Rate limits per plan:

|User with OAuth (Dev)| Commercial Use|
|---------------------|---------------|


If we want, maybe we can submit a ticket to reddit to get the commercial use that have higher limits in his dev page:

![Reddit API Request](/imgs/SS1.png)



## Legal State about SerpAPI - Considerations
Using SerpAPI could be a good approach but theres active demand from Reddit to SerpAPI because it dont allows to SerpAPI to scrap his own website.

* Ref: https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc/

* SerpAPI declarations about the case: https://serpapi.com/blog/our-response-to-reddit-inc-v-serpapi-llc-defending-the-first-amendment/

But not just Reddit, also Google are taking legal action against SerpAPI in late 2025:

* Ref: https://blog.google/innovation-and-ai/technology/safety-security/serpapi-lawsuit/

This could impact seriously to the Fuzzy Project considering that the principal API for the Scrapping functionality uses SerpAPI.