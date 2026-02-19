# Which endpoints are available and what parameters they accept?

<center>

![Reddit Endpoints](/imgs/EndpointsTikTok.png)

</center>

Theres are the endpoints that Bright Data accepts from TikTok.

### TikTok Profiles

Use this endpoint to scrape comprehensive account details like biographies, follower counts, and verification status to audit influencer performance or monitor niche competitors.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|------------------|
|Collect by URL|URL|country|13s per input|
|Discover by search URL|URL|country|13s per input|


<details>
<summary><b>Endpoint 'Collect by URL'</b> response data sample:</summary>

```json
[
  {
    "account_id": "******",
    "nickname": "******",
    "biography": "انا حربي وافتخر واللي مو عاجبه ينتحر!\nاحب عنزة وقحطان وعتيبة ومطير وجهينه وشمر",
    "awg_engagement_rate": null,
    "comment_engagement_rate": null,
    "like_engagement_rate": null,
    "bio_link": null,
    "predicted_lang": "ar",
    "is_verified": false,
    "followers": 3,
    "following": 11,
    "likes": 0,
    "videos_count": 0,
    "create_time": "2021-08-01T04:22:40.000Z",
    "id": "6789621213867066373",
    "url": "https://www.tiktok.com/@i.7rb5",
    "profile_pic_url": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/524f3035deaa6eff700b99c1863dc195~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=6cede74e&x-expires=1771628400&x-signature=6tHGkT484UTaXBBEcaJEqFZdEjg%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "like_count": 0,
    "digg_count": 0,
    "is_private": false,
    "profile_pic_url_hd": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/524f3035deaa6eff700b99c1863dc195~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=8136056b&x-expires=1771628400&x-signature=gLQ58TKUwi2t%2FjWZ584EGfyil20%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "secu_id": "MS4wLjABAAAASxrCB5P-yDoF0YrQhAAyYtkC0jE_AASO_xG6vJHLlDZts0LqSxb24Zy6owxrVsLj",
    "short_id": null,
    "ftc": null,
    "relation": null,
    "open_favorite": false,
    "comment_setting": null,
    "duet_setting": null,
    "stitch_setting": null,
    "is_ad_virtual": false,
    "room_id": null,
    "is_under_age_18": null,
    "top_videos": null,
    "signature": "انا حربي وافتخر واللي مو عاجبه ينتحر!\nاحب عنزة وقحطان وعتيبة ومطير وجهينه وشمر",
    "discovery_input": {},
    "is_commerce_user": false,
    "top_posts_data": null,
    "pinned_posts": null
  }
]
```

</details>

<details>

<summary><b>Endpoint 'Discover by search URL'</b> response data sample:</summary>

```json
[
  {
    "account_id": "******",
    "nickname": "******",
    "biography": "انا حربي وافتخر واللي مو عاجبه ينتحر!\nاحب عنزة وقحطان وعتيبة ومطير وجهينه وشمر",
    "awg_engagement_rate": null,
    "comment_engagement_rate": null,
    "like_engagement_rate": null,
    "bio_link": null,
    "predicted_lang": "ar",
    "is_verified": false,
    "followers": 3,
    "following": 11,
    "likes": 0,
    "videos_count": 0,
    "create_time": "2021-08-01T04:22:40.000Z",
    "id": "6789621213867066373",
    "url": "https://www.tiktok.com/@i.7rb5",
    "profile_pic_url": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/524f3035deaa6eff700b99c1863dc195~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=6cede74e&x-expires=1771628400&x-signature=6tHGkT484UTaXBBEcaJEqFZdEjg%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "like_count": 0,
    "digg_count": 0,
    "is_private": false,
    "profile_pic_url_hd": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/524f3035deaa6eff700b99c1863dc195~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=8136056b&x-expires=1771628400&x-signature=gLQ58TKUwi2t%2FjWZ584EGfyil20%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "secu_id": "MS4wLjABAAAASxrCB5P-yDoF0YrQhAAyYtkC0jE_AASO_xG6vJHLlDZts0LqSxb24Zy6owxrVsLj",
    "short_id": null,
    "ftc": null,
    "relation": null,
    "open_favorite": false,
    "comment_setting": null,
    "duet_setting": null,
    "stitch_setting": null,
    "is_ad_virtual": false,
    "room_id": null,
    "is_under_age_18": null,
    "top_videos": null,
    "signature": "انا حربي وافتخر واللي مو عاجبه ينتحر!\nاحب عنزة وقحطان وعتيبة ومطير وجهينه وشمر",
    "discovery_input": {},
    "is_commerce_user": false,
    "top_posts_data": null,
    "pinned_posts": null
  }
]
```

</details>


### TikTok Posts

Use this endpoint to scrape detailed video metadata, engagement metrics, and direct media URLs from specific links, keywords, or profile feeds to analyze viral trends and content reach.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|----------------|
|Collect by URL|URL (Post link)|country| 28s per input |
|Discover by keyword|search_keyword|num_of_posts,posts_to_not_include,country| 24s per input|
|Discover by profile URL|URL (User profile)|num_of_posts,posts_to_not_include,start_date,end_date,what_to_collect,post_type| 24s per input |
|Discover by URL|URL (User profile)|----| 19s per input|


<details>
<summary><b>Endpoint 'Collect by URL'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@buuubiez/video/7316610702234488106",
    "post_id": "7316610702234488106",
    "description": "merry christmas !",
    "create_time": "2023-12-25T19:06:30.000Z",
    "digg_count": 38,
    "share_count": null,
    "collect_count": 0,
    "comment_count": 10,
    "play_count": 453,
    "video_duration": 5,
    "hashtags": null,
    "original_sound": "unrestrainedz: original sound - smokinaftereat",
    "profile_id": "6680217633672348677",
    "profile_username": "add***ଳ͘",
    "profile_url": "https://www.tiktok.com/@buuubiez",
    "profile_avatar": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/53fec27944cca82f0a8dd040079b22a2~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=2fb98eea&x-expires=1771621200&x-signature=vyNwgFVRKEqVc%2B8wSWgdYl9yQvU%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "profile_biography": null,
    "preview_image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/ocbpI42kAihC0HJUKnZXv0rRyYEBBilEuwgBA~tplv-tiktokx-origin.image?dr=9636&x-expires=1771621200&x-signature=lNXthmzrSE%2F9k0ZYQ9YFoSGGvQw%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast8",
    "post_type": "video",
    "discovery_input": null,
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAXGe4jfco1PpCQC5y1GwwuJ54K4f9OxxaKbpRKuHFNW8MK3vJaewF1ZBnv21p8ieO",
    "original_item": false,
    "shortcode": "7316610702234488106",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token",
    "music": {
      "authorname": "unrestrainedz",
      "covermedium": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/f418e568f2db35eb301913a6b5e22f51~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=c04bcc3a&x-expires=1771621200&x-signature=Ct44JXMTg9Hi%2Ba6PviLHC7ImVfc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
      "id": "7289095840446073605",
      "original": true,
      "playurl": "https://v16m.tiktokcdn-us.com/caa174033fb1ddbb14a254b5d051e6c3/69967f1e/video/tos/useast5/tos-useast5-v-27dcd7c799-tx/oQqy4Rk4ABADAEcHoEfOlEkzHNNMCgAhgKAAoE/?a=1233&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ds=5&ft=GSDrKInz7Thni0ZPXq8Zmo&mime_type=audio_mpeg&qs=13&rc=M2YzNjY6ZjY0bjMzNzU8M0BpM2YzNjY6ZjY0bjMzNzU8M0A0MWNpcjRnMWhgLS1kMTZzYSM0MWNpcjRnMWhgLS1kMTZzcw%3D%3D&vvpl=1&l=202602182110062A89C75835D2A54154E8&btag=e00078000",
      "title": "original sound - smokinaftereat"
    },
    "cdn_url": "https://www.tiktok.com/335501ae-85f8-4be5-8b09-38ce1b7f4509",
    "is_verified": false,
    "account_id": "buuubiez",
    "carousel_images": null,
    "tagged_user": null,
    "profile_followers": 12000,
    "tt_chain_token": "xxT7HiFI+FbW+oKYSo+eVA==",
    "region": "******",
    "commerce_info": null,
    "subtitle_url": null,
    "subtitle_format": null,
    "subtitle_info": [],
    "cdn_link": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token"
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@buuubiez/video/7316610702234488106",
    "post_id": "7316610702234488106",
    "description": "merry christmas !",
    "create_time": "2023-12-25T19:06:30.000Z",
    "digg_count": 38,
    "share_count": null,
    "collect_count": 0,
    "comment_count": 10,
    "play_count": 453,
    "video_duration": 5,
    "hashtags": null,
    "original_sound": "unrestrainedz: original sound - smokinaftereat",
    "profile_id": "6680217633672348677",
    "profile_username": "add***ଳ͘",
    "profile_url": "https://www.tiktok.com/@buuubiez",
    "profile_avatar": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/53fec27944cca82f0a8dd040079b22a2~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=2fb98eea&x-expires=1771621200&x-signature=vyNwgFVRKEqVc%2B8wSWgdYl9yQvU%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "profile_biography": null,
    "preview_image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/ocbpI42kAihC0HJUKnZXv0rRyYEBBilEuwgBA~tplv-tiktokx-origin.image?dr=9636&x-expires=1771621200&x-signature=lNXthmzrSE%2F9k0ZYQ9YFoSGGvQw%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast8",
    "post_type": "video",
    "discovery_input": null,
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAXGe4jfco1PpCQC5y1GwwuJ54K4f9OxxaKbpRKuHFNW8MK3vJaewF1ZBnv21p8ieO",
    "original_item": false,
    "shortcode": "7316610702234488106",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token",
    "music": {
      "authorname": "unrestrainedz",
      "covermedium": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/f418e568f2db35eb301913a6b5e22f51~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=c04bcc3a&x-expires=1771621200&x-signature=Ct44JXMTg9Hi%2Ba6PviLHC7ImVfc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
      "id": "7289095840446073605",
      "original": true,
      "playurl": "https://v16m.tiktokcdn-us.com/caa174033fb1ddbb14a254b5d051e6c3/69967f1e/video/tos/useast5/tos-useast5-v-27dcd7c799-tx/oQqy4Rk4ABADAEcHoEfOlEkzHNNMCgAhgKAAoE/?a=1233&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ds=5&ft=GSDrKInz7Thni0ZPXq8Zmo&mime_type=audio_mpeg&qs=13&rc=M2YzNjY6ZjY0bjMzNzU8M0BpM2YzNjY6ZjY0bjMzNzU8M0A0MWNpcjRnMWhgLS1kMTZzYSM0MWNpcjRnMWhgLS1kMTZzcw%3D%3D&vvpl=1&l=202602182110062A89C75835D2A54154E8&btag=e00078000",
      "title": "original sound - smokinaftereat"
    },
    "cdn_url": "https://www.tiktok.com/335501ae-85f8-4be5-8b09-38ce1b7f4509",
    "is_verified": false,
    "account_id": "buuubiez",
    "carousel_images": null,
    "tagged_user": null,
    "profile_followers": 12000,
    "tt_chain_token": "xxT7HiFI+FbW+oKYSo+eVA==",
    "region": "******",
    "commerce_info": null,
    "subtitle_url": null,
    "subtitle_format": null,
    "subtitle_info": [],
    "cdn_link": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token"
  }
]
```

</details>
<details>
<summary><b>Endpoint 'Discover by profile URL'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@buuubiez/video/7316610702234488106",
    "post_id": "7316610702234488106",
    "description": "merry christmas !",
    "create_time": "2023-12-25T19:06:30.000Z",
    "digg_count": 38,
    "share_count": null,
    "collect_count": 0,
    "comment_count": 10,
    "play_count": 453,
    "video_duration": 5,
    "hashtags": null,
    "original_sound": "unrestrainedz: original sound - smokinaftereat",
    "profile_id": "6680217633672348677",
    "profile_username": "add***ଳ͘",
    "profile_url": "https://www.tiktok.com/@buuubiez",
    "profile_avatar": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/53fec27944cca82f0a8dd040079b22a2~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=2fb98eea&x-expires=1771621200&x-signature=vyNwgFVRKEqVc%2B8wSWgdYl9yQvU%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "profile_biography": null,
    "preview_image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/ocbpI42kAihC0HJUKnZXv0rRyYEBBilEuwgBA~tplv-tiktokx-origin.image?dr=9636&x-expires=1771621200&x-signature=lNXthmzrSE%2F9k0ZYQ9YFoSGGvQw%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast8",
    "post_type": "video",
    "discovery_input": null,
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAXGe4jfco1PpCQC5y1GwwuJ54K4f9OxxaKbpRKuHFNW8MK3vJaewF1ZBnv21p8ieO",
    "original_item": false,
    "shortcode": "7316610702234488106",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token",
    "music": {
      "authorname": "unrestrainedz",
      "covermedium": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/f418e568f2db35eb301913a6b5e22f51~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=c04bcc3a&x-expires=1771621200&x-signature=Ct44JXMTg9Hi%2Ba6PviLHC7ImVfc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
      "id": "7289095840446073605",
      "original": true,
      "playurl": "https://v16m.tiktokcdn-us.com/caa174033fb1ddbb14a254b5d051e6c3/69967f1e/video/tos/useast5/tos-useast5-v-27dcd7c799-tx/oQqy4Rk4ABADAEcHoEfOlEkzHNNMCgAhgKAAoE/?a=1233&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ds=5&ft=GSDrKInz7Thni0ZPXq8Zmo&mime_type=audio_mpeg&qs=13&rc=M2YzNjY6ZjY0bjMzNzU8M0BpM2YzNjY6ZjY0bjMzNzU8M0A0MWNpcjRnMWhgLS1kMTZzYSM0MWNpcjRnMWhgLS1kMTZzcw%3D%3D&vvpl=1&l=202602182110062A89C75835D2A54154E8&btag=e00078000",
      "title": "original sound - smokinaftereat"
    },
    "cdn_url": "https://www.tiktok.com/335501ae-85f8-4be5-8b09-38ce1b7f4509",
    "is_verified": false,
    "account_id": "buuubiez",
    "carousel_images": null,
    "tagged_user": null,
    "profile_followers": 12000,
    "tt_chain_token": "xxT7HiFI+FbW+oKYSo+eVA==",
    "region": "******",
    "commerce_info": null,
    "subtitle_url": null,
    "subtitle_format": null,
    "subtitle_info": [],
    "cdn_link": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token"
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by URL'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@buuubiez/video/7316610702234488106",
    "post_id": "7316610702234488106",
    "description": "merry christmas !",
    "create_time": "2023-12-25T19:06:30.000Z",
    "digg_count": 38,
    "share_count": null,
    "collect_count": 0,
    "comment_count": 10,
    "play_count": 453,
    "video_duration": 5,
    "hashtags": null,
    "original_sound": "unrestrainedz: original sound - smokinaftereat",
    "profile_id": "6680217633672348677",
    "profile_username": "add***ଳ͘",
    "profile_url": "https://www.tiktok.com/@buuubiez",
    "profile_avatar": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/53fec27944cca82f0a8dd040079b22a2~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=9640&refresh_token=2fb98eea&x-expires=1771621200&x-signature=vyNwgFVRKEqVc%2B8wSWgdYl9yQvU%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
    "profile_biography": null,
    "preview_image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/ocbpI42kAihC0HJUKnZXv0rRyYEBBilEuwgBA~tplv-tiktokx-origin.image?dr=9636&x-expires=1771621200&x-signature=lNXthmzrSE%2F9k0ZYQ9YFoSGGvQw%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast8",
    "post_type": "video",
    "discovery_input": null,
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAXGe4jfco1PpCQC5y1GwwuJ54K4f9OxxaKbpRKuHFNW8MK3vJaewF1ZBnv21p8ieO",
    "original_item": false,
    "shortcode": "7316610702234488106",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token",
    "music": {
      "authorname": "unrestrainedz",
      "covermedium": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/f418e568f2db35eb301913a6b5e22f51~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=c04bcc3a&x-expires=1771621200&x-signature=Ct44JXMTg9Hi%2Ba6PviLHC7ImVfc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
      "id": "7289095840446073605",
      "original": true,
      "playurl": "https://v16m.tiktokcdn-us.com/caa174033fb1ddbb14a254b5d051e6c3/69967f1e/video/tos/useast5/tos-useast5-v-27dcd7c799-tx/oQqy4Rk4ABADAEcHoEfOlEkzHNNMCgAhgKAAoE/?a=1233&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ds=5&ft=GSDrKInz7Thni0ZPXq8Zmo&mime_type=audio_mpeg&qs=13&rc=M2YzNjY6ZjY0bjMzNzU8M0BpM2YzNjY6ZjY0bjMzNzU8M0A0MWNpcjRnMWhgLS1kMTZzYSM0MWNpcjRnMWhgLS1kMTZzcw%3D%3D&vvpl=1&l=202602182110062A89C75835D2A54154E8&btag=e00078000",
      "title": "original sound - smokinaftereat"
    },
    "cdn_url": "https://www.tiktok.com/335501ae-85f8-4be5-8b09-38ce1b7f4509",
    "is_verified": false,
    "account_id": "buuubiez",
    "carousel_images": null,
    "tagged_user": null,
    "profile_followers": 12000,
    "tt_chain_token": "xxT7HiFI+FbW+oKYSo+eVA==",
    "region": "******",
    "commerce_info": null,
    "subtitle_url": null,
    "subtitle_format": null,
    "subtitle_info": [],
    "cdn_link": "https://v16-webapp-prime.us.tiktok.com/video/tos/useast5/tos-useast5-pve-0068-tx/oQ4ryBlCJYhwuRjZgBEUJAi0nvgEIa20biQ1B/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4050&bt=2025&cs=0&ds=3&ft=aEeq8qT0mIoPD120guxs3wUjYSAbMeF~O5&mime_type=video_mp4&qs=0&rc=aTdpOTU4aGY3ODM5PDw1PEBpajU1cm45cnB3cDMzZzczNEAyLS9fYmFiNl4xLS81Yi4yYSNhcGJmMmRrMDFgLS1kMS9zcw%3D%3D&btag=e000b0000&expire=1771621811&l=202602182110062A89C75835D2A54154E8&ply_type=2&policy=2&signature=0bc622c55638300f5a8936f343523043&tk=tt_chain_token"
  }
]
```

</details>

### TikTok Shop

Use this endpoint to scrape complete product listings, including pricing, inventory levels, and seller performance metrics for competitive e-commerce research and market analysis.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|--------------------|
|Collect by URL|URL (Product link)|—---| 3m 46s |
|Discover by category|URL (Category)|-----| 3m 46s |
|Discover by keyword|keyword|domain| 3m 46s |
|Discover by shop|URL (Store source)|------| 3m 46s|

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/shop/gb/pdp/1729432556862279311",
    "title": "CORE Pro Handlebar Grips, Soft 170mm - Red",
    "available": true,
    "description": "CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\nIntroducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\nAlso the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\nAbove all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\nCORE Pro Grip Features\n2 x Pro Grips\n2 x Bar Ends (standard size - Will not fit Aluminium Bars)\nLarge Grip length 170mm\nTapered ends for increased comfort\nGeometric engineered design for increased grip performance\nShock absorbing compound\nPro comfort – super soft\nDesigned for Action Sports\nEco-friendly packaging 100% recyclable.\nUniversal size, fits all Stunt Scooters, BMX, Bikes, MTB\nInstallation Instructions:\nFirstly, remove old grips and clean bars thoroughly.\nSecondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\nThen, allow drying for a minimum of 12 hours before use for a secure fit.",
    "currency": "GBP",
    "initial_price": 11.95,
    "final_price": 11.95,
    "discount_percent": 0,
    "initial_price_low": null,
    "initial_price_high": null,
    "final_price_low": 1195,
    "final_price_high": null,
    "sold": 0,
    "colors": null,
    "sizes": null,
    "shipping_fee": 2.99,
    "specifications": [
      {
        "title": "Brand",
        "value": "CORE"
      }
    ],
    "reviews_count": null,
    "reviews": null,
    "store_details": {
      "badge": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/644ab9eb7630441aa578b9f02bbb273f~tplv-o3syd03w52-resize-png:300:300.png?dr=11203&t=555f072d&ps=933b5bde&shp=905da467&shcp=6ce186a1&idc=no1a&from=2422056039",
      "followers": 0,
      "name": "CORE Action Sports",
      "num_of_items": 184,
      "num_sold": 0,
      "rating": null,
      "url": null
    },
    "images": [
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b2a04bb1deb44150adb62c10d9f6513b~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b1696854f79c485ca5945b147b4d83a8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b54a2ffeff594b89a5c2cc26cae6ea13~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/03487dfa9b6d4bec8fb4cc902714f6f8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/9531a3ddef2444bb8462ff7b278cfd39~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/1b11d3f185dd439f91883b729d8d7f36~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/79439eee89964bf8a454998ace830a60~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/04124cd7658c482392598a152daed98d~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/deaf6d2d5df446c782b8724dd6d35548~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393"
    ],
    "domain": "www.tiktok.com",
    "videos": null,
    "category": "Motorcycle Parts",
    "category_url": "https://www.tiktok.com/shop/gb/c/motorcycle-parts/809616",
    "id": "1729432556862279311",
    "seller_id": "749***658***008******",
    "prodct_rating": null,
    "position": null,
    "variations": [
      {
        "currency": "GBP",
        "discount_percent": 0,
        "final_price": 11.95,
        "image": null,
        "initial_price": 11.95,
        "purchase_limit": 200,
        "sku": "1729432560732311183",
        "sku_sales_props": [
          {
            "name": "Specification",
            "value": "Default"
          }
        ],
        "stock": 246
      }
    ],
    "In_stock": true,
    "promotion_items": null,
    "desc_detail": "[{\"type\":\"text\",\"text\":\"CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\"},{\"type\":\"text\",\"text\":\"Introducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\"},{\"type\":\"text\",\"text\":\"Also the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\"},{\"type\":\"text\",\"text\":\"Above all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\"},{\"type\":\"text\",\"text\":\"CORE Pro Grip Features\"},{\"type\":\"ul\",\"content\":[\"2 x Pro Grips\",\"2 x Bar Ends (standard size - Will not fit Aluminium Bars)\",\"Large Grip length 170mm\",\"Tapered ends for increased comfort\",\"Geometric engineered design for increased grip performance\",\"Shock absorbing compound\",\"Pro comfort – super soft\",\"Designed for Action Sports\",\"Eco-friendly packaging 100% recyclable.\",\"Universal size, fits all Stunt Scooters, BMX, Bikes, MTB\"]},{\"type\":\"text\",\"text\":\"Installation Instructions:\"},{\"type\":\"ul\",\"content\":[\"Firstly, remove old grips and clean bars thoroughly.\",\"Secondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\",\"Then, allow drying for a minimum of 12 hours before use for a secure fit.\"]}]",
    "related_videos": null,
    "video_link": null,
    "Shop_performance_metrics": [
      {
        "metric": "24h response rate",
        "value": null
      },
      {
        "metric": "Ships within 2 days",
        "value": "75"
      },
      {
        "metric": "Positive feedback",
        "value": "84"
      }
    ]
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by category'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/shop/gb/pdp/1729432556862279311",
    "title": "CORE Pro Handlebar Grips, Soft 170mm - Red",
    "available": true,
    "description": "CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\nIntroducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\nAlso the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\nAbove all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\nCORE Pro Grip Features\n2 x Pro Grips\n2 x Bar Ends (standard size - Will not fit Aluminium Bars)\nLarge Grip length 170mm\nTapered ends for increased comfort\nGeometric engineered design for increased grip performance\nShock absorbing compound\nPro comfort – super soft\nDesigned for Action Sports\nEco-friendly packaging 100% recyclable.\nUniversal size, fits all Stunt Scooters, BMX, Bikes, MTB\nInstallation Instructions:\nFirstly, remove old grips and clean bars thoroughly.\nSecondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\nThen, allow drying for a minimum of 12 hours before use for a secure fit.",
    "currency": "GBP",
    "initial_price": 11.95,
    "final_price": 11.95,
    "discount_percent": 0,
    "initial_price_low": null,
    "initial_price_high": null,
    "final_price_low": 1195,
    "final_price_high": null,
    "sold": 0,
    "colors": null,
    "sizes": null,
    "shipping_fee": 2.99,
    "specifications": [
      {
        "title": "Brand",
        "value": "CORE"
      }
    ],
    "reviews_count": null,
    "reviews": null,
    "store_details": {
      "badge": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/644ab9eb7630441aa578b9f02bbb273f~tplv-o3syd03w52-resize-png:300:300.png?dr=11203&t=555f072d&ps=933b5bde&shp=905da467&shcp=6ce186a1&idc=no1a&from=2422056039",
      "followers": 0,
      "name": "CORE Action Sports",
      "num_of_items": 184,
      "num_sold": 0,
      "rating": null,
      "url": null
    },
    "images": [
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b2a04bb1deb44150adb62c10d9f6513b~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b1696854f79c485ca5945b147b4d83a8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b54a2ffeff594b89a5c2cc26cae6ea13~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/03487dfa9b6d4bec8fb4cc902714f6f8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/9531a3ddef2444bb8462ff7b278cfd39~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/1b11d3f185dd439f91883b729d8d7f36~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/79439eee89964bf8a454998ace830a60~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/04124cd7658c482392598a152daed98d~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/deaf6d2d5df446c782b8724dd6d35548~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393"
    ],
    "domain": "www.tiktok.com",
    "videos": null,
    "category": "Motorcycle Parts",
    "category_url": "https://www.tiktok.com/shop/gb/c/motorcycle-parts/809616",
    "id": "1729432556862279311",
    "seller_id": "749***658***008******",
    "prodct_rating": null,
    "position": null,
    "variations": [
      {
        "currency": "GBP",
        "discount_percent": 0,
        "final_price": 11.95,
        "image": null,
        "initial_price": 11.95,
        "purchase_limit": 200,
        "sku": "1729432560732311183",
        "sku_sales_props": [
          {
            "name": "Specification",
            "value": "Default"
          }
        ],
        "stock": 246
      }
    ],
    "In_stock": true,
    "promotion_items": null,
    "desc_detail": "[{\"type\":\"text\",\"text\":\"CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\"},{\"type\":\"text\",\"text\":\"Introducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\"},{\"type\":\"text\",\"text\":\"Also the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\"},{\"type\":\"text\",\"text\":\"Above all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\"},{\"type\":\"text\",\"text\":\"CORE Pro Grip Features\"},{\"type\":\"ul\",\"content\":[\"2 x Pro Grips\",\"2 x Bar Ends (standard size - Will not fit Aluminium Bars)\",\"Large Grip length 170mm\",\"Tapered ends for increased comfort\",\"Geometric engineered design for increased grip performance\",\"Shock absorbing compound\",\"Pro comfort – super soft\",\"Designed for Action Sports\",\"Eco-friendly packaging 100% recyclable.\",\"Universal size, fits all Stunt Scooters, BMX, Bikes, MTB\"]},{\"type\":\"text\",\"text\":\"Installation Instructions:\"},{\"type\":\"ul\",\"content\":[\"Firstly, remove old grips and clean bars thoroughly.\",\"Secondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\",\"Then, allow drying for a minimum of 12 hours before use for a secure fit.\"]}]",
    "related_videos": null,
    "video_link": null,
    "Shop_performance_metrics": [
      {
        "metric": "24h response rate",
        "value": null
      },
      {
        "metric": "Ships within 2 days",
        "value": "75"
      },
      {
        "metric": "Positive feedback",
        "value": "84"
      }
    ]
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/shop/gb/pdp/1729432556862279311",
    "title": "CORE Pro Handlebar Grips, Soft 170mm - Red",
    "available": true,
    "description": "CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\nIntroducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\nAlso the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\nAbove all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\nCORE Pro Grip Features\n2 x Pro Grips\n2 x Bar Ends (standard size - Will not fit Aluminium Bars)\nLarge Grip length 170mm\nTapered ends for increased comfort\nGeometric engineered design for increased grip performance\nShock absorbing compound\nPro comfort – super soft\nDesigned for Action Sports\nEco-friendly packaging 100% recyclable.\nUniversal size, fits all Stunt Scooters, BMX, Bikes, MTB\nInstallation Instructions:\nFirstly, remove old grips and clean bars thoroughly.\nSecondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\nThen, allow drying for a minimum of 12 hours before use for a secure fit.",
    "currency": "GBP",
    "initial_price": 11.95,
    "final_price": 11.95,
    "discount_percent": 0,
    "initial_price_low": null,
    "initial_price_high": null,
    "final_price_low": 1195,
    "final_price_high": null,
    "sold": 0,
    "colors": null,
    "sizes": null,
    "shipping_fee": 2.99,
    "specifications": [
      {
        "title": "Brand",
        "value": "CORE"
      }
    ],
    "reviews_count": null,
    "reviews": null,
    "store_details": {
      "badge": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/644ab9eb7630441aa578b9f02bbb273f~tplv-o3syd03w52-resize-png:300:300.png?dr=11203&t=555f072d&ps=933b5bde&shp=905da467&shcp=6ce186a1&idc=no1a&from=2422056039",
      "followers": 0,
      "name": "CORE Action Sports",
      "num_of_items": 184,
      "num_sold": 0,
      "rating": null,
      "url": null
    },
    "images": [
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b2a04bb1deb44150adb62c10d9f6513b~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b1696854f79c485ca5945b147b4d83a8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b54a2ffeff594b89a5c2cc26cae6ea13~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/03487dfa9b6d4bec8fb4cc902714f6f8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/9531a3ddef2444bb8462ff7b278cfd39~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/1b11d3f185dd439f91883b729d8d7f36~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/79439eee89964bf8a454998ace830a60~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/04124cd7658c482392598a152daed98d~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/deaf6d2d5df446c782b8724dd6d35548~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393"
    ],
    "domain": "www.tiktok.com",
    "videos": null,
    "category": "Motorcycle Parts",
    "category_url": "https://www.tiktok.com/shop/gb/c/motorcycle-parts/809616",
    "id": "1729432556862279311",
    "seller_id": "749***658***008******",
    "prodct_rating": null,
    "position": null,
    "variations": [
      {
        "currency": "GBP",
        "discount_percent": 0,
        "final_price": 11.95,
        "image": null,
        "initial_price": 11.95,
        "purchase_limit": 200,
        "sku": "1729432560732311183",
        "sku_sales_props": [
          {
            "name": "Specification",
            "value": "Default"
          }
        ],
        "stock": 246
      }
    ],
    "In_stock": true,
    "promotion_items": null,
    "desc_detail": "[{\"type\":\"text\",\"text\":\"CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\"},{\"type\":\"text\",\"text\":\"Introducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\"},{\"type\":\"text\",\"text\":\"Also the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\"},{\"type\":\"text\",\"text\":\"Above all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\"},{\"type\":\"text\",\"text\":\"CORE Pro Grip Features\"},{\"type\":\"ul\",\"content\":[\"2 x Pro Grips\",\"2 x Bar Ends (standard size - Will not fit Aluminium Bars)\",\"Large Grip length 170mm\",\"Tapered ends for increased comfort\",\"Geometric engineered design for increased grip performance\",\"Shock absorbing compound\",\"Pro comfort – super soft\",\"Designed for Action Sports\",\"Eco-friendly packaging 100% recyclable.\",\"Universal size, fits all Stunt Scooters, BMX, Bikes, MTB\"]},{\"type\":\"text\",\"text\":\"Installation Instructions:\"},{\"type\":\"ul\",\"content\":[\"Firstly, remove old grips and clean bars thoroughly.\",\"Secondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\",\"Then, allow drying for a minimum of 12 hours before use for a secure fit.\"]}]",
    "related_videos": null,
    "video_link": null,
    "Shop_performance_metrics": [
      {
        "metric": "24h response rate",
        "value": null
      },
      {
        "metric": "Ships within 2 days",
        "value": "75"
      },
      {
        "metric": "Positive feedback",
        "value": "84"
      }
    ]
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by shop'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/shop/gb/pdp/1729432556862279311",
    "title": "CORE Pro Handlebar Grips, Soft 170mm - Red",
    "available": true,
    "description": "CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\nIntroducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\nAlso the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\nAbove all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\nCORE Pro Grip Features\n2 x Pro Grips\n2 x Bar Ends (standard size - Will not fit Aluminium Bars)\nLarge Grip length 170mm\nTapered ends for increased comfort\nGeometric engineered design for increased grip performance\nShock absorbing compound\nPro comfort – super soft\nDesigned for Action Sports\nEco-friendly packaging 100% recyclable.\nUniversal size, fits all Stunt Scooters, BMX, Bikes, MTB\nInstallation Instructions:\nFirstly, remove old grips and clean bars thoroughly.\nSecondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\nThen, allow drying for a minimum of 12 hours before use for a secure fit.",
    "currency": "GBP",
    "initial_price": 11.95,
    "final_price": 11.95,
    "discount_percent": 0,
    "initial_price_low": null,
    "initial_price_high": null,
    "final_price_low": 1195,
    "final_price_high": null,
    "sold": 0,
    "colors": null,
    "sizes": null,
    "shipping_fee": 2.99,
    "specifications": [
      {
        "title": "Brand",
        "value": "CORE"
      }
    ],
    "reviews_count": null,
    "reviews": null,
    "store_details": {
      "badge": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/644ab9eb7630441aa578b9f02bbb273f~tplv-o3syd03w52-resize-png:300:300.png?dr=11203&t=555f072d&ps=933b5bde&shp=905da467&shcp=6ce186a1&idc=no1a&from=2422056039",
      "followers": 0,
      "name": "CORE Action Sports",
      "num_of_items": 184,
      "num_sold": 0,
      "rating": null,
      "url": null
    },
    "images": [
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b2a04bb1deb44150adb62c10d9f6513b~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b1696854f79c485ca5945b147b4d83a8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/b54a2ffeff594b89a5c2cc26cae6ea13~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/03487dfa9b6d4bec8fb4cc902714f6f8~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/9531a3ddef2444bb8462ff7b278cfd39~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/1b11d3f185dd439f91883b729d8d7f36~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/79439eee89964bf8a454998ace830a60~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/04124cd7658c482392598a152daed98d~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393",
      "https://p16-oec-eu-common-no.tiktokcdn-eu.com/tos-no1a-i-t5fjg24jzw-no/deaf6d2d5df446c782b8724dd6d35548~tplv-t5fjg24jzw-resize-jpeg:800:800.jpeg?dr=11205&t=555f072d&ps=933b5bde&shp=6ce186a1&shcp=607f11de&idc=no1a&from=1826719393"
    ],
    "domain": "www.tiktok.com",
    "videos": null,
    "category": "Motorcycle Parts",
    "category_url": "https://www.tiktok.com/shop/gb/c/motorcycle-parts/809616",
    "id": "1729432556862279311",
    "seller_id": "749***658***008******",
    "prodct_rating": null,
    "position": null,
    "variations": [
      {
        "currency": "GBP",
        "discount_percent": 0,
        "final_price": 11.95,
        "image": null,
        "initial_price": 11.95,
        "purchase_limit": 200,
        "sku": "1729432560732311183",
        "sku_sales_props": [
          {
            "name": "Specification",
            "value": "Default"
          }
        ],
        "stock": 246
      }
    ],
    "In_stock": true,
    "promotion_items": null,
    "desc_detail": "[{\"type\":\"text\",\"text\":\"CORE Pro Handlebar Grips, Soft 170mm - Red I Scooter Grips\"},{\"type\":\"text\",\"text\":\"Introducing our very first Grip, the CORE Pro Handlebar Grips! Firstly, We spent over a year developing this grip to make it perfect. Our unique compound ensures the perfect softness when riding that gets even better with time. The grip is 170mm in length with a structural design to maximise grip and reduce shock.\"},{\"type\":\"text\",\"text\":\"Also the tapered ends keep your hands in check, and premium bar ends keep your bars as fresh as the day you got them. Time to update your ride.\"},{\"type\":\"text\",\"text\":\"Above all, we have developed our CORE Pro Handlebar grips to fit perfectly onto all scooters and bikes using a super soft and comfy compound with universal design. 100% custom designed to fulfil the needs of action sports riding. Premium design and materials throughout.\"},{\"type\":\"text\",\"text\":\"CORE Pro Grip Features\"},{\"type\":\"ul\",\"content\":[\"2 x Pro Grips\",\"2 x Bar Ends (standard size - Will not fit Aluminium Bars)\",\"Large Grip length 170mm\",\"Tapered ends for increased comfort\",\"Geometric engineered design for increased grip performance\",\"Shock absorbing compound\",\"Pro comfort – super soft\",\"Designed for Action Sports\",\"Eco-friendly packaging 100% recyclable.\",\"Universal size, fits all Stunt Scooters, BMX, Bikes, MTB\"]},{\"type\":\"text\",\"text\":\"Installation Instructions:\"},{\"type\":\"ul\",\"content\":[\"Firstly, remove old grips and clean bars thoroughly.\",\"Secondly, slide grips onto bars using rubbing alcohol, hairspray or grip glue.\",\"Then, allow drying for a minimum of 12 hours before use for a secure fit.\"]}]",
    "related_videos": null,
    "video_link": null,
    "Shop_performance_metrics": [
      {
        "metric": "24h response rate",
        "value": null
      },
      {
        "metric": "Ships within 2 days",
        "value": "75"
      },
      {
        "metric": "Positive feedback",
        "value": "84"
      }
    ]
  }
]
```

</details>

### TikTok Comments

Use this endpoint to scrape the full conversational layer of a video, capturing user text, timestamps, and reply threads to facilitate sentiment analysis and audience engagement tracking.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|-------------------|
|Collect by URL|URL (Post link)|—| 58s per input |

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/t/ZThC242Sp/",
    "post_url": "https://www.tiktok.com/t/ZThC242Sp/",
    "post_id": "7592772230099045662",
    "post_date_created": "2026-01-07T23:54:29.000Z",
    "date_created": "2026-01-17T02:14:26.000Z",
    "comment_text": "Anything with minimal or subtle branding",
    "num_likes": 0,
    "num_replies": 0,
    "commenter_user_name": "wha***ebb***ake***",
    "commenter_id": "6909613253173969926",
    "commenter_url": "https://www.tiktok.com/@whalepebblecake",
    "comment_id": "7596147923726566174",
    "comment_url": "https://www.tiktok.com/t/ZThC242Sp/?comment_id=7596147923726566174",
    "replies": null
  }
]
```

</details>

### TikTok Profile's Fast API

Use this endpoint to scrape recent content and profile snapshots with low latency, enabling high-speed data retrieval for real-time monitoring and large-scale processing.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|------------------|
|Collect by URL|URL (Profile link)|num_of_posts| 3s per input |

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@tudorwatch/video/7509145772001185046",
    "post_id": "7509145772001185046",
    "description": "Can @domi.hmn keep up with a pro cyclist from the Tudor Pro Cycling Team? And how fast would YOU go? #GiroDItalia #TudorWatch #WatchTok #BornToDare",
    "create_time": "2025-05-27T15:20:49.000Z",
    "digg_count": 6385,
    "share_count": "78",
    "collect_count": 252,
    "comment_count": 43,
    "play_count": 1600000,
    "video_duration": 53,
    "hashtags": [
      "giroditalia",
      "tudorwatch",
      "watchtok",
      "borntodare"
    ],
    "original_sound": "tudorwatch: original sound",
    "profile_id": "6760201745815028741",
    "profile_username": "tud***atc***",
    "profile_url": "https://www.tiktok.com/@tudorwatch",
    "profile_avatar": "https://p77-sign-va.tiktokcdn.com/tos-maliva-avt-0068/030764380b9f7cf244eff575c4fa97b1~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&refresh_token=91b432db&x-expires=1770721200&x-signature=2Im7LVTanVpYo6smbhHajwJHh68%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=my2",
    "profile_biography": "Mechanical. Timeless. Built different.\n#BornToDare",
    "preview_image": "https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/o4Aid2ABi1B5aNAEUDPAwYBATYEIXD721ptFL~tplv-tiktokx-origin.image?dr=14575&x-expires=1770721200&x-signature=WJeJLYn44F4nblKRFyV5u%2F3odwA%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=my2",
    "post_type": "video",
    "offical_item": false,
    "secu_id": "MS4wLjABAAAA6o2xoaBgrehqcEP_WOfgg25quLluZ9tO8VY_cZNV2LChlbwM1FrDwam7X-bD_C0H",
    "original_item": false,
    "shortcode": "7509145772001185046",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.tiktok.com/video/tos/no1a/tos-no1a-ve-0068-no/oUdEGSZIZZaiSBBXT24gFx0iVY2B1PYiQAEDY/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=5662&bt=2831&cs=0&ds=3&ft=-Csk_mg_PD12NlGCdd-Uxu6FLY6e3wv25NcAp&mime_type=video_mp4&qs=0&rc=O2Q6ZTQ4OzY8PDM8N2RlO0BpM3M7Zm45cm13MzMzbzczNUBhMTZjYzIwXl8xYTNiNC5gYSNvXmA2MmQ0ZG5hLS1kMTFzcw%3D%3D&btag=e00088000&expire=1770721530&l=2026020819043760B85335454FAEF7B440&ply_type=2&policy=2&signature=b19b37185ab910c6161eb070ea74ecb7&tk=tt_chain_token",
    "music": {
      "authorname": "tudorwatch",
      "covermedium": "https://p77-sign-va.tiktokcdn.com/tos-maliva-avt-0068/030764380b9f7cf244eff575c4fa97b1~tplv-tiktokx-cropcenter:720:720.jpeg?dr=14579&refresh_token=7e25ca99&x-expires=1770721200&x-signature=d5mcdFLTKjuE41OFAYyiAI39ZB4%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=my2",
      "id": "7509145764581346070",
      "original": true,
      "playurl": "https://v77.tiktokcdn.com/f292bd4bbf5b8c94d9cc8c72ec75a3b0/6989bf7a/video/tos/no1a/tos-no1a-v-2370-no/osEJhkoCd5PdNTu1DFE4INFAUAABugfeE2UAhF/?a=1180&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ds=5&ft=.NpOcInz7ThQu1PPXq8Zmo&mime_type=audio_mpeg&qs=13&rc=Mzt1cng5cm53MzMzbzU8NUBpMzt1cng5cm53MzMzbzU8NUBrZGFiMmRzZG5hLS1kMTFzYSNrZGFiMmRzZG5hLS1kMTFzcw%3D%3D&vvpl=1&l=2026020819043760B85335454FAEF7B440&btag=e00048000&cc=13",
      "title": "original sound"
    },
    "cdn_url": "https://v16-webapp-prime.tiktok.com/video/tos/no1a/tos-no1a-ve-0068-no/oUdEGSZIZZaiSBBXT24gFx0iVY2B1PYiQAEDY/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=5662&bt=2831&cs=0&ds=3&ft=-Csk_mg_PD12NlGCdd-Uxu6FLY6e3wv25NcAp&mime_type=video_mp4&qs=0&rc=O2Q6ZTQ4OzY8PDM8N2RlO0BpM3M7Zm45cm13MzMzbzczNUBhMTZjYzIwXl8xYTNiNC5gYSNvXmA2MmQ0ZG5hLS1kMTFzcw%3D%3D&btag=e00088000&expire=1770721530&l=2026020819043760B85335454FAEF7B440&ply_type=2&policy=2&signature=b19b37185ab910c6161eb070ea74ecb7&tk=tt_chain_token",
    "is_verified": true,
    "account_id": "tudorwatch",
    "carousel_images": null,
    "tagged_user": [
      {
        "user_handle": "domi.hmn",
        "user_id": "6808140096241533958",
        "user_name": "@domi",
        "user_url": "https://www.tiktok.com/@domi.hmn"
      }
    ],
    "profile_followers": 74900,
    "tt_chain_token": "yYtUs2pvk79f+h1RXWlHYg==",
    "region": null
  }
]
```

</details>

### TikTok Posts by URL Fast API

Use this endpoint to scrape the layer of the Tiktok's posts.

|Endpoint|Required Input|Optional Parameters|
|--------|--------------|-------------------|
|Collect by URL|URL (Any)|—| 225m 12s |

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@rr.ss58/video/7369216082613194002",
    "post_id": "7369216082613194002",
    "description": "الرد على @rr.ss58 تكمله اول تعليق  مراد علمدار ضد منظمه #foryou  #tiktok  #t  #وادي_الذئاب ",
    "create_time": "1970-01-20T20:36:19.329Z",
    "digg_count": 9707,
    "share_count": "91",
    "collect_count": 779,
    "comment_count": 71,
    "play_count": 265200,
    "video_duration": 208,
    "hashtags": [
      "foryou",
      "tiktok",
      "t",
      "وادي_الذئاب"
    ],
    "original_sound": "Nshamt Al Badyah: Maezufat Dihiat W Hajini",
    "profile_id": "6988049664842957830",
    "profile_username": "عشا***راد***روح******",
    "profile_url": "https://www.tiktok.com/@rr.ss58",
    "profile_avatar": "https://p77-sign-va.tiktokcdn.com/tos-maliva-avt-0068/3076304eff5871c40c2a12905a3a9f99~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&nonce=26343&refresh_token=5d17f79411c252212c6fc6f3c9b4568c&x-expires=1739714400&x-signature=DOsIDoe0xm9WbvYEGJffc%2BTo5NM%3D&idc=maliva&ps=13740610&shcp=81f88b70&shp=a5d48078&t=4d5b0474",
    "profile_biography": "تابع القناة واضغط لايك واتمتع بـالمقاطع رائعه\nالتي تظهر لك تخص وادي الذئاب 🔥🔥",
    "preview_image": "https://p77-sign-va.tiktokcdn.com/tos-maliva-avt-0068/3076304eff5871c40c2a12905a3a9f99~tplv-tiktokx-cropcenter:100:100.jpeg?dr=14579&nonce=7729&refresh_token=0271ad4a13931aac22c20504c56a1a0c&x-expires=1739714400&x-signature=CL6hq8rIWLp4P5rHn7bGHdp72d0%3D&idc=maliva&ps=13740610&shcp=81f88b70&shp=a5d48078&t=4d5b0474",
    "post_type": "video",
    "discovery_input": null,
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAa7gxZR2qgrZABKzqpuPLfpC1wWZ9V9bdO9NNYFiawk_k3qL4mgk0ceWdeka6xbR_",
    "original_item": false,
    "shortcode": "7369216082613194002",
    "width": 480,
    "ratio": "480p",
    "video_url": "https://v16-webapp-prime.tiktok.com/video/tos/alisg/tos-alisg-pve-0037c001/oAAwNQSbEUEBYBZFxvVZ1IZy7kEUxiixzAHhx/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=1086&bt=543&cs=0&ds=3&ft=4fUEKMvx8Zmo05Wz.b4jV8sxJpWrKsd.&mime_type=video_mp4&qs=0&rc=ZjM3NTRoNjk6MzpkOmY4Z0Bpajo0dms5cm5lczMzODczNEBgMy8uNDAtNjMxLjQuNl4vYSNxampsMmRrXi9gLS1kMTFzcw%3D%3D&btag=e00098000&expire=1739716936&l=20250214143847A923477D3215731D5D12&ply_type=2&policy=2&signature=a80dd3385d00b25c11666cc063fce7cb&tk=tt_chain_token",
    "music": {
      "authorname": "Nshamt Al Badyah",
      "covermedium": "https://p16-amd-va.tiktokcdn.com/img/tos-useast2a-v-2774/d5dbc5305f024ba7ade380a7e4311584~c5_200x200.jpeg",
      "id": "7210516886503557121",
      "original": false,
      "playurl": "https://sf16-ies-music-va.tiktokcdn.com/obj/tos-useast2a-ve-2774/oAv2RByqIoQU9hUyUCftAAwLVGY32wIBsHzJWl",
      "title": "Maezufat Dihiat W Hajini"
    },
    "cdn_url": "https://v16-webapp-prime.tiktok.com/video/tos/alisg/tos-alisg-pve-0037c001/oAAwNQSbEUEBYBZFxvVZ1IZy7kEUxiixzAHhx/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=1086&bt=543&cs=0&ds=3&ft=4fUEKMvx8Zmo05Wz.b4jV8sxJpWrKsd.&mime_type=video_mp4&qs=0&rc=ZjM3NTRoNjk6MzpkOmY4Z0Bpajo0dms5cm5lczMzODczNEBgMy8uNDAtNjMxLjQuNl4vYSNxampsMmRrXi9gLS1kMTFzcw%3D%3D&btag=e00098000&expire=1739716936&l=20250214143847A923477D3215731D5D12&ply_type=2&policy=2&signature=a80dd3385d00b25c11666cc063fce7cb&tk=tt_chain_token",
    "is_verified": false,
    "account_id": "rr.ss58",
    "carousel_images": null,
    "tagged_user": [
      {
        "user_handle": "rr.ss58",
        "user_id": "6988049664842957830",
        "user_name": "@rr",
        "user_url": "https://www.tiktok.com/@rr.ss58"
      }
    ],
    "profile_followers": 434700,
    "tt_chain_token": "Efo0I9fQablCfhdmM+SIOw=="
  }
]
```

</details>

### TikTok Posts by Search URL Fast API

Use this endpoint to scrape the layer of the Tiktok's posts.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|-------------------|----------------------|
|Collect by URL|URL (Any)|num_of_posts, country, start_date, end_date| 2m 42s|

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/@marinamaza18/video/7500566878142614806",
    "post_id": "7500566878142614806",
    "description": "WE MADE ITTTTT 🎓🧡🦅 #masters #españolaporusa #internationalstudent #studyabroad #🇺🇸 #eeuu #graduation #mastermind #fyp #livingabroad #parati #estadosunidos #master #girls #graduacion ",
    "create_time": "2025-05-04T12:30:18.000Z",
    "digg_count": 381,
    "share_count": "14",
    "collect_count": 8,
    "comment_count": 5,
    "play_count": 11500,
    "video_duration": 6,
    "hashtags": [
      "masters",
      "españolaporusa",
      "internationalstudent",
      "studyabroad",
      "🇺🇸",
      "eeuu",
      "graduation",
      "mastermind",
      "fyp",
      "livingabroad",
      "parati",
      "estadosunidos",
      "master",
      "girls",
      "graduacion"
    ],
    "original_sound": "Jung Kook & BTS: Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]",
    "profile_id": "6810398379295196165",
    "profile_username": "Marina M**a",
    "profile_url": "https://www.tiktok.com/@marinamaza18",
    "profile_avatar": "https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-avt-0068c001-no/ae9cb225617cde3e3eb7a6c538853c71~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=afb72ba5&x-expires=1768183200&x-signature=ha03%2F1h42sNXNRJDD10WapeL73c%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=no1a",
    "profile_biography": "Ig: marina_maza\n💌mazaortizmarina@gmail.com",
    "preview_image": "https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/owMufAIGQFui87rLIAAraAIfILBueLCA6jQ7Ax~tplv-tiktokx-origin.image?dr=10395&x-expires=1768183200&x-signature=cs4ri603mrkwNRp2gFvYHVEk2qI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
    "post_type": "video",
    "offical_item": false,
    "secu_id": "MS4wLjABAAAAdqdZi90Kl2HUF0MJN-pYPIvLrOTxKTOeaJ7t-v3Mn2soKWu5JwPzS38SAqChsX2P",
    "original_item": false,
    "shortcode": "7500566878142614806",
    "width": 576,
    "ratio": "540p",
    "video_url": "https://v16-webapp-prime.tiktok.com/video/tos/no1a/tos-no1a-ve-0068-no/osuEIESDgjDBP2uFfHoRFgA3QtuPeFIt1mBgak/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4140&bt=2070&cs=0&ds=3&ft=-Csk_mgdPD12N6I~xd-UxMw2hY3W3wv25dcAp&mime_type=video_mp4&qs=0&rc=aDc7OTM7aGU4aDtkOGUzOUBpamt5PHU5cjxvMzMzbzczNUAwYmBfXi9gXzIxLS02XjYxYSNoYnBvMmRrb19hLS1kMTFzcw%3D%3D&btag=e000b0000&expire=1768184181&l=2026011002161563801BAE3CE86C847688&ply_type=2&policy=2&signature=2a1b3011108bf667f57997999a894c5c&tk=tt_chain_token",
    "music": {
      "authorname": "Jung Kook & BTS",
      "covermedium": "https://p77-sg.tiktokcdn.com/aweme/200x200/tos-alisg-v-2774/ooaek3EAgiFLfI3vAvzp4GeIA4GrDCAENAxSvN.jpeg",
      "id": "7167503660023285762",
      "original": false,
      "playurl": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-ve-2774/oY3F0tBhQeZQPMqENf3bVYv7ng85bD5P6dEgCB",
      "title": "Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]"
    },
    "cdn_url": "https://v16-webapp-prime.tiktok.com/video/tos/no1a/tos-no1a-ve-0068-no/osuEIESDgjDBP2uFfHoRFgA3QtuPeFIt1mBgak/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=4140&bt=2070&cs=0&ds=3&ft=-Csk_mgdPD12N6I~xd-UxMw2hY3W3wv25dcAp&mime_type=video_mp4&qs=0&rc=aDc7OTM7aGU4aDtkOGUzOUBpamt5PHU5cjxvMzMzbzczNUAwYmBfXi9gXzIxLS02XjYxYSNoYnBvMmRrb19hLS1kMTFzcw%3D%3D&btag=e000b0000&expire=1768184181&l=2026011002161563801BAE3CE86C847688&ply_type=2&policy=2&signature=2a1b3011108bf667f57997999a894c5c&tk=tt_chain_token",
    "is_verified": false,
    "account_id": "marinamaza18",
    "profile_followers": 19000
  }
]
```

</details>

### TikTok Shop Category Products

Use this endpoint to scrape the layer of the Tiktok's posts.

|Endpoint|Required Input|Optional Parameters|Average Response Time|
|--------|--------------|------------------|----------------------|
|Collect by URL|URL|—| 10m 9s|

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "url": "https://www.tiktok.com/shop/my/pdp/beg-galas-minimalis-nilon-tahan-air-selesa-untuk-wanita/1729573709673760056",
    "product_id": "1729573709673760056",
    "category_url": "https://www.tiktok.com/shop/my/c/functional-bags/902792",
    "category_name": "Functional Bags",
    "sub_categories": [],
    "title": "Beg galas biasa minimalis | Beg Galas Belakang Perempuan Fesyen | Beg galas nilon Beg Ringkas Kasual Uniseks",
    "initial_price": 69.9,
    "final_price": 30.99,
    "currency": "MYR",
    "product_rating": 4.8,
    "sold": 9458,
    "position": "119",
    "product_image": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/6144318f4ccd4a1382cf1efa49e78892~tplv-aphluv4xwc-crop-webp:1000:1000.webp?dr=15592&t=555f072d&ps=933b5bde&shp=8dbd94bf&shcp=e0b1d153&idc=my2&from=2378011839",
    "categories": [
      {
        "name": "Luggage & Bags",
        "url": "https://www.tiktok.com/shop/my/c/luggage-bags/824584"
      },
      {
        "name": "Functional Bags",
        "url": "https://www.tiktok.com/shop/my/c/functional-bags/902792"
      }
    ]
  }
]
```

</details>

<br>

# Whether keyword-based search is supported?

Yes, is supported for two categories.<br>

Supported by TikTok Posts and TikTok Shop.

<br>

# Free tier limitations encountered

We have only 2$ free tier without card, but with registering a card, Bright Data gives 5$ more.




