# Reddit

Traffic not using OAuth or login 
credentials will be blocked (no default rate limit also).

Free acces rate limits:
* 100 queries per minute per OAuth
* 10 queries per minute without OAuth

The rate limits are monitored in the response header:

* X-Ratelimit-Used: Approximate number of requests used in this period
* X-Ratelimit-Remaining: Approximate number of requests left to use
* X-Ratelimit-Reset: Approximate number of seconds to end of period

Rate limits per plan:

| User without Auth | User with OAuth (Dev)| Commercial Use|
|-----------------|---------------------|---------------|
| 10 req per min | 100 req per minute | Depends of the agreement, but mainly is higher than Dev's plan. Some sources say the minimum is 1000 req per 0.24$|

In the Reddit docs says: 
**"Traffic not using OAuth or login credentials will be blocked, and the default rate limit will not apply."**

## Approval Process

If we want to use the API with OAuth, then we need the `ClientID` and the `Client Secret` vartiable, for this, we need to submit a ticket to the RedditDev page to get the it that have higher limits

![Reddit API Request](/imgs/SS1.png)

Theres no a secure time interval to get response by Reddit, some users comments that get more than 1 month til get a response from Reddit (Approved or Disapproved), others says that after 2 months; theres no documentation or reddit statement that confirms a minimum time response per API approval access request to the Devs or Enterprises.

You need to submit the request and wait til they responses you if they grant you access or not, just that 2 steps.

The ticket request is quite long and rigorous, they ask for a lot of details and within the data agreement service API it mentions that it cannot be used for scraping (fuzzy core). You can see the details in the image below.

![Reddit API Complete Request](/imgs/SS2.png)

These changes are relatively recent, implemented in 2026, because Reddit wants to curb web scraping and abuse of its Data API.

Several users are even complaining about the new rules when trying to register for the Reddit API (which has a low acceptance rate from Reddit), and some developers are looking for alternatives.

* **Ref #1:** https://www.reddit.com/r/AI_Agents/comments/1qw54wr/reddit_api_solution_2026_creating_a_reddit_search/

* **Ref #2:** https://www.reddit.com/r/redditdev/comments/1qtwhsi/has_anyone_got_a_data_api_key_recently/

* **Ref #3:** https://www.reddit.com/r/redditdev/comments/1qdsikx/why_is_getting_api_keys_so_difficult/

* **Ref #4:** https://www.reddit.com/r/redditdev/comments/1oug31u/introducing_the_responsible_builder_policy_new/

This could be a problem because the user volume for which `Fuzzy` is designed is approximately 100,000, which isn't feasible using the Reddit API with the free options due to its inherent risks (prone to being banned) and considering the rate limits. A significant number of developer accounts would be needed, and Reddit is quite strict about granting API access to each developer.

Reddit is also encouraging the use of its new Devvit platform, which also provides API access, but is limited to creating moderator bots for Reddit forums with prior approval from the company itself. Therefore, it wouldn't be suitable for `Fuzzy`.

![Reddit Devvit](/imgs/SS3.png)

But there's a trick with Reddit: when we go to one of its URLs with `.json` at the end, it will give us a complete payload of the page we want to access.

**Ejemplo:**

* Ref sin `.json` al final del URL:

![Reddit JSON1](/imgs/SS4.png)

* Ref con `.json` al final del URL:

![Reddit JSON2](/imgs/SS5.png)

This might be useful when combined with Google Search; however, it's worth noting that Reddit hasn't commented on this and there's no documentation. Developers on Reddit have mentioned that they suspect this functionality may be removed in the future.

## Use of Reddit API

The use of the API is the same having OAuth or not, just changes the header information with an API KEY, in this case i dont have it for the explained before (Reddit complicating the ticket requirements and is reported to get a lot of dissaprovals tickets).

### Search endpoint: `GET /search.json`
### Case: `https://www.reddit.com/search.json?q=John+Cena&limit=1&sort=relevance`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/search.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "q": "John Cena",
    "limit": 1,
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/search.json?q=John+Cena&limit=1&raw_json=1"
}

```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "search",
  "url": "https://www.reddit.com/search.json",
  "params": {
    "q": "John Cena",
    "limit": 1,
    "sort": "relevance",
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:04.596510",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "97.0",
    "x-ratelimit-reset": "175"
  },
  "response": {
    "kind": "Listing",
    "data": {
      "modhash": "",
      "dist": 1,
      "facets": {},
      "after": "t3_1pm3xv9",
      "geo_filter": "",
      "children": [
        {
          "kind": "t3",
          "data": {
            "approved_at_utc": null,
            "subreddit": "REALSquaredCircle",
            "selftext": "",
            "author_fullname": "t2_14uu1z",
            "saved": false,
            "mod_reason_title": null,
            "gilded": 0,
            "clicked": false,
            "title": "I can't lie, the fans really tarnished John Cena's final moment in the ring",
            "link_flair_richtext": [],
            "subreddit_name_prefixed": "r/REALSquaredCircle",
            "hidden": false,
            "pwls": 6,
            "link_flair_css_class": null,
            "downs": 0,
            "thumbnail_height": 78,
            "top_awarded_type": null,
            "hide_score": false,
            "name": "t3_1pm3xv9",
            "quarantine": false,
            "link_flair_text_color": "dark",
            "upvote_ratio": 0.89,
            "author_flair_background_color": "#32cd63",
            "subreddit_type": "public",
            "ups": 2014,
            "total_awards_received": 0,
            "media_embed": {},
            "thumbnail_width": 140,
            "author_flair_template_id": "dfb4959a-aee0-11f0-aa84-e26984b7cf61",
            "is_original_content": false,
            "user_reports": [],
            "secure_media": {
              "reddit_video": {
                "bitrate_kbps": 5000,
                "fallback_url": "https://v.redd.it/glswtibh837g1/CMAF_1080.mp4?source=fallback",
                "has_audio": true,
                "height": 1080,
                "width": 1920,
                "scrubber_media_url": "https://v.redd.it/glswtibh837g1/CMAF_96.mp4",
                "dash_url": "https://v.redd.it/glswtibh837g1/DASHPlaylist.mpd?a=1773532624%2CZWFkMjU5ZWFmMWIxODVjMmVjMzA3MzIxZTJiYWFkMTdhNTU2NjdjYmI0NThmODUxNmEwYjBjZjgyZDU3ZWIzOQ%3D%3D&v=1&f=sd",
                "duration": 268,
                "hls_url": "https://v.redd.it/glswtibh837g1/HLSPlaylist.m3u8?a=1773532624%2CYzYzMWJhMzJjODkxYTBmZTc1ODY4ZmQ4ZGE4MzhmMzZkM2ZkYjk5MjcyMjc1NWNhNDkyZTc2ODNiOTA3MTJiMw%3D%3D&v=1&f=sd",
                "is_gif": false,
                "transcoding_status": "completed"
              }
            },
            "is_reddit_media_domain": true,
            "is_meta": false,
            "category": null,
            "secure_media_embed": {},
            "link_flair_text": null,
            "can_mod_post": false,
            "score": 2014,
            "approved_by": null,
            "is_created_from_ads_ui": false,
            "author_premium": false,
            "thumbnail": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=140&height=78&format=jpg&auto=webp&s=a94d5b2570129627f675f754d2fa9900eaf6cc86",
            "edited": false,
            "author_flair_css_class": null,
            "author_flair_richtext": [
              {
                "e": "text",
                "t": "Grant, of r/REALSquaredCircle"
              }
            ],
            "gildings": {},
            "post_hint": "hosted:video",
            "content_categories": null,
            "is_self": false,
            "mod_note": null,
            "created": 1765682555.0,
            "link_flair_type": "text",
            "wls": 6,
            "removed_by_category": null,
            "banned_by": null,
            "author_flair_type": "richtext",
            "domain": "v.redd.it",
            "allow_live_comments": false,
            "selftext_html": null,
            "likes": null,
            "suggested_sort": null,
            "banned_at_utc": null,
            "url_overridden_by_dest": "https://v.redd.it/glswtibh837g1",
            "view_count": null,
            "archived": false,
            "no_follow": false,
            "is_crosspostable": false,
            "pinned": false,
            "over_18": false,
            "preview": {
              "images": [
                {
                  "source": {
                    "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?format=pjpg&auto=webp&s=6c74d4901bf34eabbb49cfa0e36f370268fe8b5f",
                    "width": 1920,
                    "height": 1080
                  },
                  "resolutions": [
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=108&crop=smart&format=pjpg&auto=webp&s=8653513593f96193089c07d57243db7495f898da",
                      "width": 108,
                      "height": 60
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=216&crop=smart&format=pjpg&auto=webp&s=bcb8cb6f910113cfab1cd8cb48d52b56e9fa3a93",
                      "width": 216,
                      "height": 121
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=320&crop=smart&format=pjpg&auto=webp&s=226b6a0bf6c4f83845c0a260e39c013ff563a496",
                      "width": 320,
                      "height": 180
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=640&crop=smart&format=pjpg&auto=webp&s=d9aceae544ca91acae11b80ca4aea2f98fbd19f0",
                      "width": 640,
                      "height": 360
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=960&crop=smart&format=pjpg&auto=webp&s=4420597dc350e7128264f822639a9c63a229ea4f",
                      "width": 960,
                      "height": 540
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=1080&crop=smart&format=pjpg&auto=webp&s=30f2dd7a0797a57e438c3fbc57e9d29757e2ebee",
                      "width": 1080,
                      "height": 607
                    }
                  ],
                  "variants": {},
                  "id": "a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE"
                }
              ],
              "enabled": false
            },
            "all_awardings": [],
            "awarders": [],
            "media_only": false,
            "can_gild": false,
            "spoiler": false,
            "locked": false,
            "author_flair_text": "Grant, of r/REALSquaredCircle",
            "treatment_tags": [],
            "visited": false,
            "removed_by": null,
            "num_reports": null,
            "distinguished": null,
            "subreddit_id": "t5_f9dd4f",
            "author_is_blocked": false,
            "mod_reason_by": null,
            "removal_reason": null,
            "link_flair_background_color": "",
            "id": "1pm3xv9",
            "is_robot_indexable": true,
            "report_reasons": null,
            "author": "Grrannt",
            "discussion_type": null,
            "num_comments": 1032,
            "send_replies": true,
            "contest_mode": false,
            "mod_reports": [],
            "author_patreon_flair": false,
            "author_flair_text_color": "dark",
            "permalink": "/r/REALSquaredCircle/comments/1pm3xv9/i_cant_lie_the_fans_really_tarnished_john_cenas/",
            "stickied": false,
            "url": "https://v.redd.it/glswtibh837g1",
            "subreddit_subscribers": 10837,
            "created_utc": 1765682555.0,
            "num_crossposts": 1,
            "media": {
              "reddit_video": {
                "bitrate_kbps": 5000,
                "fallback_url": "https://v.redd.it/glswtibh837g1/CMAF_1080.mp4?source=fallback",
                "has_audio": true,
                "height": 1080,
                "width": 1920,
                "scrubber_media_url": "https://v.redd.it/glswtibh837g1/CMAF_96.mp4",
                "dash_url": "https://v.redd.it/glswtibh837g1/DASHPlaylist.mpd?a=1773532624%2CZWFkMjU5ZWFmMWIxODVjMmVjMzA3MzIxZTJiYWFkMTdhNTU2NjdjYmI0NThmODUxNmEwYjBjZjgyZDU3ZWIzOQ%3D%3D&v=1&f=sd",
                "duration": 268,
                "hls_url": "https://v.redd.it/glswtibh837g1/HLSPlaylist.m3u8?a=1773532624%2CYzYzMWJhMzJjODkxYTBmZTc1ODY4ZmQ4ZGE4MzhmMzZkM2ZkYjk5MjcyMjc1NWNhNDkyZTc2ODNiOTA3MTJiMw%3D%3D&v=1&f=sd",
                "is_gif": false,
                "transcoding_status": "completed"
              }
            },
            "is_video": true
          }
        }
      ],
      "before": null
    }
  }
}
```
</details>

And the `images attributes` from the response from `Reddit API` are:

```js
'thumbnails': [],
'images': [],
'videos': [],
'galleries': [],
'preview_images': []
```

### Search endpoint: `GET /r/{subreddit}/search.json`
**Case:** `https://www.reddit.com/r/SquaredCircle/search.json?q=John+Cena&restrict_sr=on`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/r/SquaredCircle/search.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "q": "John Cena",
    "restrict_sr": "on",
    "limit": 1,
    "sort": "relevance",
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/r/SquaredCircle/search.json?q=John+Cena&restrict_sr=on&limit=1&sort=relevance&raw_json=1"
}
```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "search",
  "url": "https://www.reddit.com/search.json",
  "params": {
    "q": "John Cena",
    "limit": 1,
    "sort": "relevance",
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:04.596510",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "97.0",
    "x-ratelimit-reset": "175"
  },
  "response": {
    "kind": "Listing",
    "data": {
      "modhash": "",
      "dist": 1,
      "facets": {},
      "after": "t3_1pm3xv9",
      "geo_filter": "",
      "children": [
        {
          "kind": "t3",
          "data": {
            "approved_at_utc": null,
            "subreddit": "REALSquaredCircle",
            "selftext": "",
            "author_fullname": "t2_14uu1z",
            "saved": false,
            "mod_reason_title": null,
            "gilded": 0,
            "clicked": false,
            "title": "I can't lie, the fans really tarnished John Cena's final moment in the ring",
            "link_flair_richtext": [],
            "subreddit_name_prefixed": "r/REALSquaredCircle",
            "hidden": false,
            "pwls": 6,
            "link_flair_css_class": null,
            "downs": 0,
            "thumbnail_height": 78,
            "top_awarded_type": null,
            "hide_score": false,
            "name": "t3_1pm3xv9",
            "quarantine": false,
            "link_flair_text_color": "dark",
            "upvote_ratio": 0.89,
            "author_flair_background_color": "#32cd63",
            "subreddit_type": "public",
            "ups": 2014,
            "total_awards_received": 0,
            "media_embed": {},
            "thumbnail_width": 140,
            "author_flair_template_id": "dfb4959a-aee0-11f0-aa84-e26984b7cf61",
            "is_original_content": false,
            "user_reports": [],
            "secure_media": {
              "reddit_video": {
                "bitrate_kbps": 5000,
                "fallback_url": "https://v.redd.it/glswtibh837g1/CMAF_1080.mp4?source=fallback",
                "has_audio": true,
                "height": 1080,
                "width": 1920,
                "scrubber_media_url": "https://v.redd.it/glswtibh837g1/CMAF_96.mp4",
                "dash_url": "https://v.redd.it/glswtibh837g1/DASHPlaylist.mpd?a=1773532624%2CZWFkMjU5ZWFmMWIxODVjMmVjMzA3MzIxZTJiYWFkMTdhNTU2NjdjYmI0NThmODUxNmEwYjBjZjgyZDU3ZWIzOQ%3D%3D&v=1&f=sd",
                "duration": 268,
                "hls_url": "https://v.redd.it/glswtibh837g1/HLSPlaylist.m3u8?a=1773532624%2CYzYzMWJhMzJjODkxYTBmZTc1ODY4ZmQ4ZGE4MzhmMzZkM2ZkYjk5MjcyMjc1NWNhNDkyZTc2ODNiOTA3MTJiMw%3D%3D&v=1&f=sd",
                "is_gif": false,
                "transcoding_status": "completed"
              }
            },
            "is_reddit_media_domain": true,
            "is_meta": false,
            "category": null,
            "secure_media_embed": {},
            "link_flair_text": null,
            "can_mod_post": false,
            "score": 2014,
            "approved_by": null,
            "is_created_from_ads_ui": false,
            "author_premium": false,
            "thumbnail": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=140&height=78&format=jpg&auto=webp&s=a94d5b2570129627f675f754d2fa9900eaf6cc86",
            "edited": false,
            "author_flair_css_class": null,
            "author_flair_richtext": [
              {
                "e": "text",
                "t": "Grant, of r/REALSquaredCircle"
              }
            ],
            "gildings": {},
            "post_hint": "hosted:video",
            "content_categories": null,
            "is_self": false,
            "mod_note": null,
            "created": 1765682555.0,
            "link_flair_type": "text",
            "wls": 6,
            "removed_by_category": null,
            "banned_by": null,
            "author_flair_type": "richtext",
            "domain": "v.redd.it",
            "allow_live_comments": false,
            "selftext_html": null,
            "likes": null,
            "suggested_sort": null,
            "banned_at_utc": null,
            "url_overridden_by_dest": "https://v.redd.it/glswtibh837g1",
            "view_count": null,
            "archived": false,
            "no_follow": false,
            "is_crosspostable": false,
            "pinned": false,
            "over_18": false,
            "preview": {
              "images": [
                {
                  "source": {
                    "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?format=pjpg&auto=webp&s=6c74d4901bf34eabbb49cfa0e36f370268fe8b5f",
                    "width": 1920,
                    "height": 1080
                  },
                  "resolutions": [
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=108&crop=smart&format=pjpg&auto=webp&s=8653513593f96193089c07d57243db7495f898da",
                      "width": 108,
                      "height": 60
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=216&crop=smart&format=pjpg&auto=webp&s=bcb8cb6f910113cfab1cd8cb48d52b56e9fa3a93",
                      "width": 216,
                      "height": 121
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=320&crop=smart&format=pjpg&auto=webp&s=226b6a0bf6c4f83845c0a260e39c013ff563a496",
                      "width": 320,
                      "height": 180
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=640&crop=smart&format=pjpg&auto=webp&s=d9aceae544ca91acae11b80ca4aea2f98fbd19f0",
                      "width": 640,
                      "height": 360
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=960&crop=smart&format=pjpg&auto=webp&s=4420597dc350e7128264f822639a9c63a229ea4f",
                      "width": 960,
                      "height": 540
                    },
                    {
                      "url": "https://external-preview.redd.it/a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE.png?width=1080&crop=smart&format=pjpg&auto=webp&s=30f2dd7a0797a57e438c3fbc57e9d29757e2ebee",
                      "width": 1080,
                      "height": 607
                    }
                  ],
                  "variants": {},
                  "id": "a21qMzk3Y2g4MzdnMdopKZ5nvieOAW-hGcwUekyP1SBXGOmm0uaEDv8adUSE"
                }
              ],
              "enabled": false
            },
            "all_awardings": [],
            "awarders": [],
            "media_only": false,
            "can_gild": false,
            "spoiler": false,
            "locked": false,
            "author_flair_text": "Grant, of r/REALSquaredCircle",
            "treatment_tags": [],
            "visited": false,
            "removed_by": null,
            "num_reports": null,
            "distinguished": null,
            "subreddit_id": "t5_f9dd4f",
            "author_is_blocked": false,
            "mod_reason_by": null,
            "removal_reason": null,
            "link_flair_background_color": "",
            "id": "1pm3xv9",
            "is_robot_indexable": true,
            "report_reasons": null,
            "author": "Grrannt",
            "discussion_type": null,
            "num_comments": 1032,
            "send_replies": true,
            "contest_mode": false,
            "mod_reports": [],
            "author_patreon_flair": false,
            "author_flair_text_color": "dark",
            "permalink": "/r/REALSquaredCircle/comments/1pm3xv9/i_cant_lie_the_fans_really_tarnished_john_cenas/",
            "stickied": false,
            "url": "https://v.redd.it/glswtibh837g1",
            "subreddit_subscribers": 10837,
            "created_utc": 1765682555.0,
            "num_crossposts": 1,
            "media": {
              "reddit_video": {
                "bitrate_kbps": 5000,
                "fallback_url": "https://v.redd.it/glswtibh837g1/CMAF_1080.mp4?source=fallback",
                "has_audio": true,
                "height": 1080,
                "width": 1920,
                "scrubber_media_url": "https://v.redd.it/glswtibh837g1/CMAF_96.mp4",
                "dash_url": "https://v.redd.it/glswtibh837g1/DASHPlaylist.mpd?a=1773532624%2CZWFkMjU5ZWFmMWIxODVjMmVjMzA3MzIxZTJiYWFkMTdhNTU2NjdjYmI0NThmODUxNmEwYjBjZjgyZDU3ZWIzOQ%3D%3D&v=1&f=sd",
                "duration": 268,
                "hls_url": "https://v.redd.it/glswtibh837g1/HLSPlaylist.m3u8?a=1773532624%2CYzYzMWJhMzJjODkxYTBmZTc1ODY4ZmQ4ZGE4MzhmMzZkM2ZkYjk5MjcyMjc1NWNhNDkyZTc2ODNiOTA3MTJiMw%3D%3D&v=1&f=sd",
                "is_gif": false,
                "transcoding_status": "completed"
              }
            },
            "is_video": true
          }
        }
      ],
      "before": null
    }
  }
}
```
</details>

---

### User submissions endpoint: `GET /user/{username}/submitted.json`
**Case:** `https://www.reddit.com/user/spez/submitted.json`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/user/spez/submitted.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "limit": 3,
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/user/spez/submitted.json?limit=3&raw_json=1"
}
```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "user_submitted",
  "url": "https://www.reddit.com/user/spez/submitted.json",
  "params": {
    "limit": 3,
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:11.148171",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "98.0",
    "x-ratelimit-reset": "169"
  },
  "response": {
    "kind": "Listing",
    "data": {
      "after": "t3_1qwxst2",
      "dist": 3,
      "modhash": "",
      "children": [
        {
          "kind": "t3",
          "data": {
            "subreddit": "redditstock",
            "title": "TL;DR: Solid end to a strong year for Reddit. Ask your questions for me, Jen, and Drew in r/RDDT.",
            "author": "spez",
            "score": 186,
            "upvote_ratio": 0.97,
            "created_utc": 1770300000.0,
            "url": "https://i.redd.it/example.png",
            "permalink": "/r/redditstock/comments/1qwxst2/",
            "is_self": false,
            "num_comments": 25
          }
        }
      ]
    }
  }
}
```
</details>

---

### Post comments endpoint: `GET /r/{subreddit}/comments/{post_id}.json`
**Case:** `https://www.reddit.com/r/Python/comments/1r2292p.json`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/r/Python/comments/1r2292p.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "limit": 5,
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/r/Python/comments/1r2292p.json?limit=5&raw_json=1"
}
```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "comments",
  "url": "https://www.reddit.com/r/Python/comments/1r2292p.json",
  "params": {
    "limit": 5,
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:15.150472",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "96.0",
    "x-ratelimit-reset": "164"
  },
  "response": [
    {
      "kind": "Listing",
      "data": {
        "children": [
          {
            "kind": "t3",
            "data": {
              "subreddit": "Python",
              "title": "Python Unplugged on PyTV",
              "selftext": "**Check our this Free Online Python Conference on March 4**...",
              "author": "jetbrains",
              "score": 21,
              "created_utc": 1773388800.0,
              "permalink": "/r/Python/comments/1r2292p/python_unplugged_on_pytv/",
              "num_comments": 5
            }
          }
        ]
      }
    },
    {
      "kind": "Listing",
      "data": {
        "children": [
          {
            "kind": "t1",
            "data": {
              "body": "This looks interesting! Thanks for sharing.",
              "author": "python_dev",
              "score": 5,
              "created_utc": 1773390000.0,
              "parent_id": "t3_1r2292p",
              "id": "comment1"
            }
          }
        ]
      }
    }
  ]
}
```

**Note:** Comments endpoint returns an array with 2 listings:
- **First element:** The post itself (`kind: "t3"`)
- **Second element:** The comment tree (`kind: "t1"` for comments)

</details>

---

### User info endpoint: `GET /user/{username}/about.json`
**Case:** `https://www.reddit.com/user/spez/about.json`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/user/spez/about.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/user/spez/about.json?raw_json=1"
}
```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "user_about",
  "url": "https://www.reddit.com/user/spez/about.json",
  "params": {
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:18.293398",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "95.0",
    "x-ratelimit-reset": "161"
  },
  "response": {
    "kind": "t2",
    "data": {
      "name": "spez",
      "created": 1118030400.0,
      "created_utc": 1118030400.0,
      "link_karma": 121753,
      "comment_karma": 813827,
      "total_karma": 935580,
      "is_employee": true,
      "is_gold": true,
      "is_mod": true,
      "verified": true,
      "icon_img": "https://styles.redditmedia.com/t5_3k30p/styles/profileIcon_uj015iwx9s7g1.png",
      "subreddit": {
        "display_name": "u_spez",
        "title": "spez",
        "subscribers": 0
      }
    }
  }
}
```
</details>

---

### Subreddit info endpoint: `GET /r/{subreddit}/about.json`
**Case:** `https://www.reddit.com/r/python/about.json`

<details>
<summary>
<b>Request sample:</b>
</summary>

```js
{
  "url": "https://www.reddit.com/r/python/about.json",
  "method": "GET",
  "headers": {
    "User-Agent": "python:reddit-public-scraper:v0.1"
  },
  "params": {
    "raw_json": 1
  },
  "full_url": "https://www.reddit.com/r/python/about.json?raw_json=1"
}
```
</details>

<details>
<summary>
<b>Response sample:</b>
</summary>

```js
{
  "endpoint": "subreddit_about",
  "url": "https://www.reddit.com/r/python/about.json",
  "params": {
    "raw_json": 1
  },
  "timestamp": "2026-02-12T18:57:21.431485",
  "status_code": 200,
  "headers": {
    "content-type": "application/json; charset=UTF-8",
    "x-ratelimit-remaining": "94.0",
    "x-ratelimit-reset": "158"
  },
  "response": {
    "kind": "t5",
    "data": {
      "display_name": "Python",
      "title": "Python",
      "display_name_prefixed": "r/Python",
      "subscribers": 1448539,
      "active_user_count": 1234,
      "public_description": "The official Python community for Reddit! Stay up to date with the latest news, packages, and meta information relating to the Python programming language.",
      "created": 1201242956.0,
      "created_utc": 1201242956.0,
      "community_icon": "https://styles.redditmedia.com/t5_2qh0y/styles/communityIcon_mkayghu1502d1.png",
      "banner_background_image": "https://styles.redditmedia.com/t5_2qh0y/styles/bannerBackgroundImage_cd73kiu1502d1.png",
      "header_title": "news about the dynamic, interpreted, interactive, object-oriented, extensible programming language Python",
      "primary_color": "#ffcc00",
      "advertiser_category": "Technology",
      "over_18": false
    }
  }
}
```
</details>

---

## Legal State about SerpAPI - Considerations

Using SerpAPI could be a good approach but theres active demand from Reddit to SerpAPI because it dont allows to SerpAPI to scrap his own website.

* Ref: https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc/

* SerpAPI declarations about the case: https://serpapi.com/blog/our-response-to-reddit-inc-v-serpapi-llc-defending-the-first-amendment/

But not just Reddit, also Google are taking legal action against SerpAPI in late 2025:

* Ref: https://blog.google/innovation-and-ai/technology/safety-security/serpapi-lawsuit/
This could impact seriously to the Fuzzy Project considering that the principal API for the Scrapping functionality uses SerpAPI.
