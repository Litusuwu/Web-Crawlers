# Evaluation of BrightData for Instagram Crawling

## 1. Available Endpoints and Parameters

- Bright Data for Instagram supports both
synchronous (real-time) and **asynchronous** (snapshot) scraping methods across various endpoints.

- In general, collection capacity is not explicitly limited, but **performance may vary** based on input size and external factors per input.

- The only limitation is on the collection for comments, which is limited to the 15 latest comments per post or reel.

- All pricing is based on the number of records returned, with a **min charge of $0.0015 per record**.

### 1.1. Profiles

- Supports both collecting by URL and discovering by username.
- Since URLs are unique and based on usernames, we only care about the "Collect by URL" method.
- Average response time per input: 6s

- Key parameters:

| Parameter | Required | Type | Example |
| --- | --- | --- | --- |
| URL | yes | string | `https://www.instagram.com/mrbeast/` |

### 1.2. Posts

- Supports collecting by URL of a post, and discovering by profile URL.
- Average response time per input: 5s (collect by URL), 7s (discover by URL)

- Key parameters for "Collect by URL":

| Parameter | Required | Type | Example |
| --- | --- | --- | --- |
| URL | yes | string | `https://www.instagram.com/p/CG0UU3wF1Jv/` |

- Key parameters for "Discover by URL":

| Parameter | Required | Type | Example |
| --- | --- | --- | --- |
| URL | yes | string | `https://www.instagram.com/mrbeast/` |
| num_of_posts | no | integer | `10` |
| posts_to_not_include | no | array of strings (post ID's) | `[CG0UU3wF1Jv]` |
| start_date | no | string (MM-DD-YYYY) | `01-01-2025` |
| end_date | no | string (MM-DD-YYYY) | `01-31-2025` |
| post_type | no | string (Post or Reel) | `Post` |

### 1.3. Reels

- Supports collecting by URL of a reel, discovering by profile URL, and discovering all reels by profile URL.

- The difference between the two discovery methods is that the "All Reels" discovery collector retrieves reels from the Reels tab, while the "Discovery by URL" collector retrieves reels from the Posts tab of an Instagram profile.

- Average response time per input: 7s

- Key parameters for "Collect by URL":

| Parameter | Required | Type | Example |
| --- | --- | --- | --- |
| URL | yes | string | `https://www.instagram.com/reel/CG0UU3wF1Jv/` |
| num_of_posts | no | integer | `10` |
| posts_to_not_include | no | array of strings (post ID's) | `[CG0UU3wF1Jv]` |
| start_date | no | string (MM-DD-YYYY) | `01-01-2025` |
| end_date | no | string (MM-DD-YYYY) | `01-31-2025` |

### 1.4. Comments

- Supports collecting by URL of a post or reel to retrieve the 15 latest comments.

- Average response time per input: 9s

- Key parameters:

| Parameter | Required | Type | Example |
| --- | --- | --- | --- |
| URL | yes | string | `https://www.instagram.com/p/CG0UU3wF1Jv/` |


## 2. Returned Data Fields

The scraper returns structured JSON.

### 2.1. Profiles

|**Column name**|**Description**|**Data type**|**Fill rate**|
|---|---|---|---|
|**account**|The username or handle of the Instagram account|Text|100.00%|
|**fbid**|Facebook ID associated with the account|Text|100.00%|
|**id**|Unique identifier for the Instagram account|Text|100.00%|
|**followers**|The number of followers for the account|Number|99.99%|
|**posts_count**|The total count of posts made by the account|Number|99.95%|
|**is_business_account**|Indicates whether the account is a business account|Boolean|99.77%|
|**is_professional_account**|Indicates whether the account is a professional account|Boolean|99.84%|
|**is_verified**|Indicates whether the account is verified|Boolean|99.66%|
|**avg_engagement**|Average engagement on Instagram is the percentage of likes and comments your posts receive relative to your total number of followers, serving as a measure of audience interaction and content effectiveness|Number|35.14%|
|**external_url**|External websites that users may link to from their Instagram profiles, such as personal blogs or online stores|Array|46.01%|
|**biography**|Brief descriptions or statements that users write to introduce themselves or share their interests and passions on Instagram|Text|44.36%|
|**following**|The number of accounts that the account is following|Number|100.00%|
|**posts**|Data regarding the top posts that the user has published|Array|48.49%|
|**profile_image_link**|URL that link directly to the Instagram profile image|Text|96.92%|
|**profile_name**|The name associated with the account's profile|Text|89.43%|
|**highlights_count**|The count of highlights (featured stories) on the account|Number|99.84%|
|**full_name**|The full name associated with the account|Text|88.48%|
|**is_private**|Indicates whether the account is private|Boolean|98.87%|

Note on unsupported:

| **Column name**|**Description**|**Data type**|**Fill rate**|
|---|---|---|---|
|**post_hashtags**|Hashtags used in the user's posts|-|0.00%|
|**highlights**|Data regarding the highlights (featured stories) on the account|-|0.00%|


### 2.2. Posts

|**Column name**|**Description**|**Data type**|**Fill rate**|
|---|---|---|---|
|**url**||Url|100.00%|
|**user_posted**|Username of the post creator|Text|99.99%|
|**description**|Post text description|Text|95.62%|
|**hashtags**|Hashtags used in the post|Array|62.22%|
|**num_comments**|Number of comments|Number|100.00%|
|**date_posted**|Post publication date|Date|100.00%|
|**likes**|Number of likes|Number|89.10%|
|**photos**|URLs of attached photos, URLs can be expired due to instagram policy|Array|99.99%|
|**videos**|URLs of attached videos, URLs can be expired due to instagram policy|Array|18.50%|
|**location**|Geographical location|Array|26.89%|
|**latest_comments**|Recent comments|Array|58.36%|
|**post_id**|Unique post identifier|Text|100.00%|
|**shortcode**|The shortcode of the Instagram post|Text|100.00%|
|**content_type**|The type of content as Posts/Reels|Text|100.00%|
|**pk**|The primary key of the media content|Text|100.00%|
|**content_id**|The content ID of the media|Text|99.99%|
|**engagement_score_view**|video view count|Number|12.75%|
|**thumbnail**|The URL of the post's display image or video thumbnail|Text|99.99%|
|**video_view_count**|The number of views on the video post|Text|17.30%|
|**tagged_users**||Array|27.35%|
|**video_play_count**|The number of times the video has been played|Number|10.99%|
|**followers**|Number of followers the post owner has|Number|99.99%|
|**posts_count**|The total count of posts made by the account|Number|99.99%|
|**profile_image_link**|URL that link directly to the Instagram profile image|Text|99.99%|
|**is_verified**|Indicates whether the account is verified|Boolean|99.99%|
|**is_paid_partnership**|Is the post sponsored|Boolean|100.00%|
|**partnership_details**|Details of the partnership|Object|100.00%|
|**user_posted_id**|The ID of the user who posted the post|Text|100.00%|
|**post_content**||Array|99.99%|
|**audio**||Object|100.00%|
|**profile_url**|URL of the profile who posted|Url|99.99%|

### 2.3. Reels


| **Column name** | **Description** | **Data type** | **Fill rate** |
| --- | --- | --- | --- |
| **url** | URL of the reel | Url | 100.00% |
| **user_posted** | Username of the reel creator | Text | 100.00% |
| **description** | Reel text description | Text | 96.28% |
| **hashtags** | Hashtags used in the post | Array | 66.90% |
| **num_comments** | Number of comments | Number | 100.00% |
| **date_posted** | Reel publication date | Date | 100.00% |
| **likes** | Number of likes | Number | 100.00% |
| **views** | Number of views | Number | 99.99% |
| **video_play_count** | The number of times the Reel has been played | Number | 98.74% |
| **top_comments** | Top comments | Array | 77.42% |
| **post_id** | Unique post identifier | Text | 100.00% |
| **thumbnail** | The URL of the reel's display image or video thumbnail | Url | 100.00% |
| **shortcode** | The shortcode of the Instagram reel | Text | 100.00% |
| **content_id** | The content ID of the media | Text | 100.00% |
| **length** | Length of the reel | Text | 99.97% |
| **video_url** | The video url | Url | 99.99% |
| **audio_url** | link to the audio connected to the post | Url | 95.27% |
| | | Number | 56.46% |
| **user_profile_url** | | Url | 99.95% |
| **is_paid_partnership** | Is the post sponsored | Boolean | 99.94% |
| **is_verified** | Indicates whether the account is verified | Boolean | 99.99% |


### 2.4. Comments

| **Column name** | **Description** | **Data type** | **Fill rate** |
| --- | --- | --- | --- |
| **url** | | Url | 100.00% |
| **comment_user** | The username commenting | Text | 100.00% |
| **comment_user_url** | Url of the commenting user | Url | 100.00% |
| **comment_date** | Date when the comment was made | Text | 100.00% |
| **comment** | The comment of the comment | Text | 98.68% |
| **likes_number** | Number of likes on the comment | Number | 60.33% |
| **replies_number** | Number of replies on the comment | Number | 100.00% |
| **replies** | replies on the comment | Array | 6.13% |
| **hashtag_comment** | The hashtags used in the comment | Array | 1.33% |
| **tagged_users_in_comment** | The usernames tagged in the comment | Array | 5.55% |
| **post_url** | The URL of the post itself | Url | 100.00% |
| **post_user** | The user posting the original post | Text | 99.68% |
| **comment_id** | unique id for each comment | Text | 100.00% |
| **post_id** | The ID of the original post | Text | 99.98% |


## 3. Keyword-Based Search Support

- **No Discovery by Keyword:** The interface primary focuses on discover by URLs of posts or profiles. There is no a direct `keyword` discovery method for general search terms (e.g., "Nike") across social entities.

## 4. Image/Media URL Accessibility

- **Accessibility:** One can access the media via the returned CDN URLs.
- **Limitation (Signed URLs):** These URLs are **temporary** and typically expire within **2–3 days** due to Instagram's security policies.

## 5. Response Time and Reliability

- In general, collection capacity is not explicitly limited, but **performance may vary** based on input size and external factors per input.

- In summary, response times are generally in the range of **5–9 seconds per input**, with some variability based on the specific endpoint and parameters used.


## 6. Free Tier Limitations

- **Record Limit:** The standard free trial includes 100 records total (across any scrapers one runs).
- **Inputs per Request:** Up to 20 inputs (e.g., 20 profile URLs) in a real‑time request.
- **Synchronous Request Limit:** Synchronous request are subject to a 1 minute timeout limit. If the data retrieval process exceeds this limit, the API will return an HTTP 202 response, indicating that the request is still being processed.