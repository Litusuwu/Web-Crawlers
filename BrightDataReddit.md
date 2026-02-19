# Which endpoints are available and what parameters they accept?

<center>


![Reddit Endpoints](/imgs/EndpointsReddit.png)

</center>

Theres are the endpoints that Bright Data accepts from Reddit

### Reddit Posts

Use this endpoint to scrape the general layer of a post.

|Endpoint|Required Input|Optional Parameters|
|--------|--------------|-------------------|
|Collect by URL|URL (Post link)|—|
|Discover by author URL|URL (User profile)|"keyword, sort_by, num_of_posts, sort_by_time"|
|Discover by keyword|"keyword, date"|"num_of_posts, sort_by"|
|Discover by subreddit url|URL (Subreddit link)|"sort_by, num_of_posts, sort_by_time, keyword, start_date"|

<details>
<summary><b>Endpoint 'Collect by URL'</b> response data sample:</summary>

```json
[
  {
    "post_id": "t3_1q1xep3",
    "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/any_one_found_birkenstocks_help_with_their_pf/",
    "user_posted": "Den***Try***79",
    "title": "Any one found Birkenstocks help with their PF ?",
    "description": "Found relief when wearing my birkenstocks but pain after wards when barefoot or wearing other footwear worse. Any one else have a similar story ?",
    "num_comments": 36,
    "date_posted": "2026-01-02T12:29:58.702Z",
    "community_name": "PlantarFasciitis",
    "num_upvotes": 19,
    "photos": null,
    "videos": null,
    "tag": "PF Footwear / Insoles 👟",
    "related_posts": [
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/",
        "num_comments": 48,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Birkenstocks",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/",
        "num_comments": 9,
        "num_upvotes": "32",
        "thumbnail": null,
        "title": "Thank you to this group",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/",
        "num_comments": 25,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "Sending a little hope…",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/",
        "num_comments": 17,
        "num_upvotes": "30",
        "thumbnail": null,
        "title": "What helped me:",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/",
        "num_comments": 42,
        "num_upvotes": "63",
        "thumbnail": null,
        "title": "you are going to be ok!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/",
        "num_comments": 6,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "Every little counts...",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/",
        "num_comments": 6,
        "num_upvotes": "27",
        "thumbnail": null,
        "title": "My experience",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/",
        "num_comments": 11,
        "num_upvotes": "70",
        "thumbnail": null,
        "title": "32,000 Members & Growing!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/",
        "num_comments": 88,
        "num_upvotes": "48",
        "thumbnail": null,
        "title": "Two years of this",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/",
        "num_comments": 60,
        "num_upvotes": "80",
        "thumbnail": null,
        "title": "Just need to vent. Feet are killing me and I'm so tired of this.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/",
        "num_comments": 9,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "THANK YOU ALL!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/",
        "num_comments": 24,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "Finally Getting Some Relief",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/",
        "num_comments": 19,
        "num_upvotes": "43",
        "thumbnail": null,
        "title": "The only thing that's helped",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/",
        "num_comments": 9,
        "num_upvotes": "16",
        "thumbnail": null,
        "title": "Hopefully what worked for me will work for you",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/",
        "num_comments": 22,
        "num_upvotes": "9",
        "thumbnail": null,
        "title": "Is this normal?",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/",
        "num_comments": 14,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "What finally worked",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/",
        "num_comments": 19,
        "num_upvotes": "45",
        "thumbnail": null,
        "title": "Finally some improvement",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/",
        "num_comments": 34,
        "num_upvotes": "97",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/",
        "num_comments": 67,
        "num_upvotes": "105",
        "thumbnail": null,
        "title": "Sharing what works for me.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/",
        "num_comments": 10,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "What's worked for me (so far)",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/",
        "num_comments": 10,
        "num_upvotes": "28",
        "thumbnail": null,
        "title": "What Worked for Me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/",
        "num_comments": 27,
        "num_upvotes": "39",
        "thumbnail": null,
        "title": "Finally found something that's helping",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/",
        "num_comments": 38,
        "num_upvotes": "96",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/",
        "num_comments": 33,
        "num_upvotes": "142",
        "thumbnail": null,
        "title": "You know what we’re normalizing??????",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/",
        "num_comments": 81,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Can't keep living like this, desperate for solutions",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/"
      }
    ],
    "comments": [
      {
        "comment": "Yessss instant relief from that fkn snapping feeling I love a fresh pair of birks so much",
        "date_of_comment": "2026-01-04T08:39:41.104Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxlfg54/",
        "user_commenting": "tough_tiddies69",
        "user_url": "https://www.reddit.com/user/tough_tiddies69/"
      },
      {
        "comment": "Yes! One year of recovery but I still cannot go barefoot for extended stretches of time. The good news is that Birks make sandals!",
        "date_of_comment": "2026-01-04T01:26:39.050Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxjo03x/",
        "user_commenting": "mlk2317",
        "user_url": "https://www.reddit.com/user/mlk2317/"
      },
      {
        "comment": "I have the Ecco Kozmo sandals that look a lot like Birkenstocks. They’re really great on my plantar fasciitis.",
        "date_of_comment": "2026-01-03T20:45:30.955Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxi58xp/",
        "user_commenting": "Alternative_Fun5097",
        "user_url": "https://www.reddit.com/user/Alternative_Fun5097/"
      },
      {
        "comment": "I’m wearing Oofos recovery sandals and it’s the only time my feet are 100% pain-free!",
        "date_of_comment": "2026-01-03T19:42:13.399Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhsful/",
        "user_commenting": "balletgirl2020",
        "user_url": "https://www.reddit.com/user/balletgirl2020/"
      },
      {
        "comment": "I’m adamant that the Birks CAUSED my PF. I hate them.",
        "date_of_comment": "2026-01-03T18:41:40.601Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhfa13/",
        "user_commenting": "Boomshiqua",
        "user_url": "https://www.reddit.com/user/Boomshiqua/"
      },
      {
        "comment": "I used to wear birks almost every day, wound up with PF. Still wore them as they were the only shoes that didn't kill me. I needed gym shoes, got some kuru shoes. Now any time I wear my birks it flairs back up. All that to say, every foot is different and until I really started doing the stretches the shoes only allowed me to walk with less pain but never truly heal.",
        "date_of_comment": "2026-01-03T16:57:13.772Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgsfr0/",
        "user_commenting": "PositionOk3089",
        "user_url": "https://www.reddit.com/user/PositionOk3089/"
      },
      {
        "comment": "Two rough calf and foot massages and Birks all summer seemed to cure me. I think everyone is different. Worth a try.",
        "date_of_comment": "2026-01-03T16:49:24.131Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgqqvu/",
        "user_commenting": "jcclune73",
        "user_url": "https://www.reddit.com/user/jcclune73/"
      },
      {
        "comment": "Birkenstocks pretty much cured my PF (work in a surgical field, now wear Birkenstock clogs religiously) - I was limping daily before wearing them. Have to get through the first 2 weeks of break in before getting results",
        "date_of_comment": "2026-01-03T15:22:31.366Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg8nvf/",
        "user_commenting": "precision324",
        "user_url": "https://www.reddit.com/user/precision324/"
      },
      {
        "comment": "I never had PF until I got Birks last year. Feet were fine when wearing but heels started to hurt when I wasn’t wearing them. It got really bad. I gave them up and all resolved within about three months on its own. Birks are great shoes but not everyone is built to wear them.",
        "date_of_comment": "2026-01-03T14:50:40.581Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg2l11/",
        "user_commenting": "UsualClue3638",
        "user_url": "https://www.reddit.com/user/UsualClue3638/"
      },
      {
        "comment": "I got a lot better when I started wearing Birkenstocks all day every day in the house. I have high arches.",
        "date_of_comment": "2026-01-03T13:52:18.223Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxfs9z7/",
        "user_commenting": "No-Interview-1340",
        "user_url": "https://www.reddit.com/user/No-Interview-1340/"
      },
      {
        "comment": "Yes absolutely. I started wearing them exclusively when I got a stress fracture in my non PF foot because they matched the height of the boot I was in best. When I was dealing with the stress fracture I just gave up on my PF exercises because I was frustrated and overwhelmed and I realised once I was in less pain from the fracture that I was also in less pain from the PF. And it wasn't because I was doing less activity, the walking boot actually increased my activity because I could actually move",
        "date_of_comment": "2026-01-03T11:25:55.857Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxf7oke/",
        "user_commenting": "Munishmo",
        "user_url": "https://www.reddit.com/user/Munishmo/"
      },
      {
        "comment": "They’re the only summer shoe that I can wear so they’re my outdoor and indoor three months of the year - my podiatrist recommended them.",
        "date_of_comment": "2026-01-03T06:24:49.926Z",
        "num_replies": 1,
        "num_upvotes": 1,
        "replies": [
          {
            "date_of_reply": "2026-01-03T11:56:31.261Z",
            "num_replies": 0,
            "num_upvotes": 1,
            "reply": "Yeah I wear them a-lot during summer, my physio recommended them they have helped alot",
            "user_replying": "Dense-Try-5879",
            "user_url": "https://www.reddit.com/user/Dense-Try-5879/"
          }
        ],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe8f6g/",
        "user_commenting": "Ok_Jellyfish_4534",
        "user_url": "https://www.reddit.com/user/Ok_Jellyfish_4534/"
      },
      {
        "comment": "Yes , the first time I had PF about 4 years ago my naturopath told me to get birks with a cork sole. I did and it really helped and gradually healed my PF. This time around they unfortunately don’t seem to help like before. Ordered 2 pairs of Kuru for PF and meh not worth the money . However my Nike Motiva walking shoes are helping so much, and at half the price of the others I’ve tried.",
        "date_of_comment": "2026-01-03T06:08:50.846Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe6f9k/",
        "user_commenting": "Ewwwdavid1",
        "user_url": "https://www.reddit.com/user/Ewwwdavid1/"
      },
      {
        "comment": "Yes! Birkenstocks are the only kind of shoe I can wear. I like their sandals for summer and the sneakers the rest of the year.",
        "date_of_comment": "2026-01-03T05:51:28.954Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe46uz/",
        "user_commenting": "ACB_Toby",
        "user_url": "https://www.reddit.com/user/ACB_Toby/"
      },
      {
        "comment": "Yup yup yup!",
        "date_of_comment": "2026-01-03T04:04:50.518Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdour1/",
        "user_commenting": "Left_One_1308",
        "user_url": "https://www.reddit.com/user/Left_One_1308/"
      },
      {
        "comment": "Likely my cause.",
        "date_of_comment": "2026-01-03T04:01:36.596Z",
        "num_replies": 0,
        "num_upvotes": 3,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdocjo/",
        "user_commenting": "DapperWorth7668",
        "user_url": "https://www.reddit.com/user/DapperWorth7668/"
      },
      {
        "comment": "They helped me heal completely but it took at least a year of wearing them consistently. Slippers, clogs, sandals, etc. They were the only shoes I wore. Now I also have a pair of Altras with a high arch insert.",
        "date_of_comment": "2026-01-03T03:17:02.559Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdh5y1/",
        "user_commenting": "fmaon06",
        "user_url": "https://www.reddit.com/user/fmaon06/"
      },
      {
        "comment": "I have no experience with Birkenstocks, but I’m 100% convinced wearing Chacos nearly everyday last summer helped my PF fully heal.",
        "date_of_comment": "2026-01-03T02:03:53.463Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxd4rmy/",
        "user_commenting": "jmmani2",
        "user_url": "https://www.reddit.com/user/jmmani2/"
      },
      {
        "comment": "Massively.",
        "date_of_comment": "2026-01-03T01:04:13.289Z",
        "num_replies": 0,
        "num_upvotes": 0,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcugd9/",
        "user_commenting": "apja",
        "user_url": "https://www.reddit.com/user/apja/"
      },
      {
        "comment": "They aggravated my PF. I fare better with a soft sole.",
        "date_of_comment": "2026-01-03T00:22:48.518Z",
        "num_replies": 0,
        "num_upvotes": 6,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcmyea/",
        "user_commenting": "5pens",
        "user_url": "https://www.reddit.com/user/5pens/"
      }
    ],
    "community_url": "https://www.reddit.com/r/PlantarFasciitis/",
    "community_description": "Plantar fasciitis is a common foot condition characterized by inflammation of the plantar fascia, a thick band of tissue that runs across the bottom of the foot, connecting the heel bone to the toes. The plantar fascia acts as a shock absorber and supports the arch of the foot. When this tissue becomes irritated or inflamed, it can lead to pain and discomfort, especially around the heel.",
    "community_members_num": 40165,
    "community_rank": {
      "community_rank_type": null,
      "community_rank_value": null
    },
    "post_karma": 0,
    "bio_description": null,
    "embedded_links": null,
    "description_markdown": "\n        \n     \n       \n       \n      Found relief when wearing my birkenstocks but pain after wards  when barefoot or wearing other footwear worse. Any one else have a similar story ?\n     \n     \n     \n    \n    ",
    "subreddit_icon_image": "https://styles.redditmedia.com/t5_35l5c/styles/communityIcon_2i3pz63hnoef1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=8add3f8b2a7bcf38c557a155faae0f12508bb690",
    "author_icon": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png",
    "user_id": "t2_w71ujetkx"
  }
]
```

</details>

<details>
<summary><b>Endpoint 'Discover by author URL'</b> response data sample:</summary>

```json

[
  {
    "post_id": "t3_1q1xep3",
    "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/any_one_found_birkenstocks_help_with_their_pf/",
    "user_posted": "Den***Try***79",
    "title": "Any one found Birkenstocks help with their PF ?",
    "description": "Found relief when wearing my birkenstocks but pain after wards when barefoot or wearing other footwear worse. Any one else have a similar story ?",
    "num_comments": 36,
    "date_posted": "2026-01-02T12:29:58.702Z",
    "community_name": "PlantarFasciitis",
    "num_upvotes": 19,
    "photos": null,
    "videos": null,
    "tag": "PF Footwear / Insoles 👟",
    "related_posts": [
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/",
        "num_comments": 48,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Birkenstocks",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/",
        "num_comments": 9,
        "num_upvotes": "32",
        "thumbnail": null,
        "title": "Thank you to this group",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/",
        "num_comments": 25,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "Sending a little hope…",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/",
        "num_comments": 17,
        "num_upvotes": "30",
        "thumbnail": null,
        "title": "What helped me:",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/",
        "num_comments": 42,
        "num_upvotes": "63",
        "thumbnail": null,
        "title": "you are going to be ok!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/",
        "num_comments": 6,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "Every little counts...",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/",
        "num_comments": 6,
        "num_upvotes": "27",
        "thumbnail": null,
        "title": "My experience",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/",
        "num_comments": 11,
        "num_upvotes": "70",
        "thumbnail": null,
        "title": "32,000 Members & Growing!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/",
        "num_comments": 88,
        "num_upvotes": "48",
        "thumbnail": null,
        "title": "Two years of this",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/",
        "num_comments": 60,
        "num_upvotes": "80",
        "thumbnail": null,
        "title": "Just need to vent. Feet are killing me and I'm so tired of this.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/",
        "num_comments": 9,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "THANK YOU ALL!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/",
        "num_comments": 24,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "Finally Getting Some Relief",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/",
        "num_comments": 19,
        "num_upvotes": "43",
        "thumbnail": null,
        "title": "The only thing that's helped",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/",
        "num_comments": 9,
        "num_upvotes": "16",
        "thumbnail": null,
        "title": "Hopefully what worked for me will work for you",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/",
        "num_comments": 22,
        "num_upvotes": "9",
        "thumbnail": null,
        "title": "Is this normal?",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/",
        "num_comments": 14,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "What finally worked",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/",
        "num_comments": 19,
        "num_upvotes": "45",
        "thumbnail": null,
        "title": "Finally some improvement",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/",
        "num_comments": 34,
        "num_upvotes": "97",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/",
        "num_comments": 67,
        "num_upvotes": "105",
        "thumbnail": null,
        "title": "Sharing what works for me.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/",
        "num_comments": 10,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "What's worked for me (so far)",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/",
        "num_comments": 10,
        "num_upvotes": "28",
        "thumbnail": null,
        "title": "What Worked for Me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/",
        "num_comments": 27,
        "num_upvotes": "39",
        "thumbnail": null,
        "title": "Finally found something that's helping",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/",
        "num_comments": 38,
        "num_upvotes": "96",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/",
        "num_comments": 33,
        "num_upvotes": "142",
        "thumbnail": null,
        "title": "You know what we’re normalizing??????",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/",
        "num_comments": 81,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Can't keep living like this, desperate for solutions",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/"
      }
    ],
    "comments": [
      {
        "comment": "Yessss instant relief from that fkn snapping feeling I love a fresh pair of birks so much",
        "date_of_comment": "2026-01-04T08:39:41.104Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxlfg54/",
        "user_commenting": "tough_tiddies69",
        "user_url": "https://www.reddit.com/user/tough_tiddies69/"
      },
      {
        "comment": "Yes! One year of recovery but I still cannot go barefoot for extended stretches of time. The good news is that Birks make sandals!",
        "date_of_comment": "2026-01-04T01:26:39.050Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxjo03x/",
        "user_commenting": "mlk2317",
        "user_url": "https://www.reddit.com/user/mlk2317/"
      },
      {
        "comment": "I have the Ecco Kozmo sandals that look a lot like Birkenstocks. They’re really great on my plantar fasciitis.",
        "date_of_comment": "2026-01-03T20:45:30.955Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxi58xp/",
        "user_commenting": "Alternative_Fun5097",
        "user_url": "https://www.reddit.com/user/Alternative_Fun5097/"
      },
      {
        "comment": "I’m wearing Oofos recovery sandals and it’s the only time my feet are 100% pain-free!",
        "date_of_comment": "2026-01-03T19:42:13.399Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhsful/",
        "user_commenting": "balletgirl2020",
        "user_url": "https://www.reddit.com/user/balletgirl2020/"
      },
      {
        "comment": "I’m adamant that the Birks CAUSED my PF. I hate them.",
        "date_of_comment": "2026-01-03T18:41:40.601Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhfa13/",
        "user_commenting": "Boomshiqua",
        "user_url": "https://www.reddit.com/user/Boomshiqua/"
      },
      {
        "comment": "I used to wear birks almost every day, wound up with PF. Still wore them as they were the only shoes that didn't kill me. I needed gym shoes, got some kuru shoes. Now any time I wear my birks it flairs back up. All that to say, every foot is different and until I really started doing the stretches the shoes only allowed me to walk with less pain but never truly heal.",
        "date_of_comment": "2026-01-03T16:57:13.772Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgsfr0/",
        "user_commenting": "PositionOk3089",
        "user_url": "https://www.reddit.com/user/PositionOk3089/"
      },
      {
        "comment": "Two rough calf and foot massages and Birks all summer seemed to cure me. I think everyone is different. Worth a try.",
        "date_of_comment": "2026-01-03T16:49:24.131Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgqqvu/",
        "user_commenting": "jcclune73",
        "user_url": "https://www.reddit.com/user/jcclune73/"
      },
      {
        "comment": "Birkenstocks pretty much cured my PF (work in a surgical field, now wear Birkenstock clogs religiously) - I was limping daily before wearing them. Have to get through the first 2 weeks of break in before getting results",
        "date_of_comment": "2026-01-03T15:22:31.366Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg8nvf/",
        "user_commenting": "precision324",
        "user_url": "https://www.reddit.com/user/precision324/"
      },
      {
        "comment": "I never had PF until I got Birks last year. Feet were fine when wearing but heels started to hurt when I wasn’t wearing them. It got really bad. I gave them up and all resolved within about three months on its own. Birks are great shoes but not everyone is built to wear them.",
        "date_of_comment": "2026-01-03T14:50:40.581Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg2l11/",
        "user_commenting": "UsualClue3638",
        "user_url": "https://www.reddit.com/user/UsualClue3638/"
      },
      {
        "comment": "I got a lot better when I started wearing Birkenstocks all day every day in the house. I have high arches.",
        "date_of_comment": "2026-01-03T13:52:18.223Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxfs9z7/",
        "user_commenting": "No-Interview-1340",
        "user_url": "https://www.reddit.com/user/No-Interview-1340/"
      },
      {
        "comment": "Yes absolutely. I started wearing them exclusively when I got a stress fracture in my non PF foot because they matched the height of the boot I was in best. When I was dealing with the stress fracture I just gave up on my PF exercises because I was frustrated and overwhelmed and I realised once I was in less pain from the fracture that I was also in less pain from the PF. And it wasn't because I was doing less activity, the walking boot actually increased my activity because I could actually move",
        "date_of_comment": "2026-01-03T11:25:55.857Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxf7oke/",
        "user_commenting": "Munishmo",
        "user_url": "https://www.reddit.com/user/Munishmo/"
      },
      {
        "comment": "They’re the only summer shoe that I can wear so they’re my outdoor and indoor three months of the year - my podiatrist recommended them.",
        "date_of_comment": "2026-01-03T06:24:49.926Z",
        "num_replies": 1,
        "num_upvotes": 1,
        "replies": [
          {
            "date_of_reply": "2026-01-03T11:56:31.261Z",
            "num_replies": 0,
            "num_upvotes": 1,
            "reply": "Yeah I wear them a-lot during summer, my physio recommended them they have helped alot",
            "user_replying": "Dense-Try-5879",
            "user_url": "https://www.reddit.com/user/Dense-Try-5879/"
          }
        ],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe8f6g/",
        "user_commenting": "Ok_Jellyfish_4534",
        "user_url": "https://www.reddit.com/user/Ok_Jellyfish_4534/"
      },
      {
        "comment": "Yes , the first time I had PF about 4 years ago my naturopath told me to get birks with a cork sole. I did and it really helped and gradually healed my PF. This time around they unfortunately don’t seem to help like before. Ordered 2 pairs of Kuru for PF and meh not worth the money . However my Nike Motiva walking shoes are helping so much, and at half the price of the others I’ve tried.",
        "date_of_comment": "2026-01-03T06:08:50.846Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe6f9k/",
        "user_commenting": "Ewwwdavid1",
        "user_url": "https://www.reddit.com/user/Ewwwdavid1/"
      },
      {
        "comment": "Yes! Birkenstocks are the only kind of shoe I can wear. I like their sandals for summer and the sneakers the rest of the year.",
        "date_of_comment": "2026-01-03T05:51:28.954Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe46uz/",
        "user_commenting": "ACB_Toby",
        "user_url": "https://www.reddit.com/user/ACB_Toby/"
      },
      {
        "comment": "Yup yup yup!",
        "date_of_comment": "2026-01-03T04:04:50.518Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdour1/",
        "user_commenting": "Left_One_1308",
        "user_url": "https://www.reddit.com/user/Left_One_1308/"
      },
      {
        "comment": "Likely my cause.",
        "date_of_comment": "2026-01-03T04:01:36.596Z",
        "num_replies": 0,
        "num_upvotes": 3,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdocjo/",
        "user_commenting": "DapperWorth7668",
        "user_url": "https://www.reddit.com/user/DapperWorth7668/"
      },
      {
        "comment": "They helped me heal completely but it took at least a year of wearing them consistently. Slippers, clogs, sandals, etc. They were the only shoes I wore. Now I also have a pair of Altras with a high arch insert.",
        "date_of_comment": "2026-01-03T03:17:02.559Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdh5y1/",
        "user_commenting": "fmaon06",
        "user_url": "https://www.reddit.com/user/fmaon06/"
      },
      {
        "comment": "I have no experience with Birkenstocks, but I’m 100% convinced wearing Chacos nearly everyday last summer helped my PF fully heal.",
        "date_of_comment": "2026-01-03T02:03:53.463Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxd4rmy/",
        "user_commenting": "jmmani2",
        "user_url": "https://www.reddit.com/user/jmmani2/"
      },
      {
        "comment": "Massively.",
        "date_of_comment": "2026-01-03T01:04:13.289Z",
        "num_replies": 0,
        "num_upvotes": 0,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcugd9/",
        "user_commenting": "apja",
        "user_url": "https://www.reddit.com/user/apja/"
      },
      {
        "comment": "They aggravated my PF. I fare better with a soft sole.",
        "date_of_comment": "2026-01-03T00:22:48.518Z",
        "num_replies": 0,
        "num_upvotes": 6,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcmyea/",
        "user_commenting": "5pens",
        "user_url": "https://www.reddit.com/user/5pens/"
      }
    ],
    "community_url": "https://www.reddit.com/r/PlantarFasciitis/",
    "community_description": "Plantar fasciitis is a common foot condition characterized by inflammation of the plantar fascia, a thick band of tissue that runs across the bottom of the foot, connecting the heel bone to the toes. The plantar fascia acts as a shock absorber and supports the arch of the foot. When this tissue becomes irritated or inflamed, it can lead to pain and discomfort, especially around the heel.",
    "community_members_num": 40165,
    "community_rank": {
      "community_rank_type": null,
      "community_rank_value": null
    },
    "post_karma": 0,
    "bio_description": null,
    "embedded_links": null,
    "description_markdown": "\n        \n     \n       \n       \n      Found relief when wearing my birkenstocks but pain after wards  when barefoot or wearing other footwear worse. Any one else have a similar story ?\n     \n     \n     \n    \n    ",
    "subreddit_icon_image": "https://styles.redditmedia.com/t5_35l5c/styles/communityIcon_2i3pz63hnoef1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=8add3f8b2a7bcf38c557a155faae0f12508bb690",
    "author_icon": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png",
    "user_id": "t2_w71ujetkx"
  }
]

```

</details>

<details>
<summary><b>Endpoint 'Discover by keyword'</b> response data sample:</summary>

```json
[
  {
    "post_id": "t3_1q1xep3",
    "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/any_one_found_birkenstocks_help_with_their_pf/",
    "user_posted": "Den***Try***79",
    "title": "Any one found Birkenstocks help with their PF ?",
    "description": "Found relief when wearing my birkenstocks but pain after wards when barefoot or wearing other footwear worse. Any one else have a similar story ?",
    "num_comments": 36,
    "date_posted": "2026-01-02T12:29:58.702Z",
    "community_name": "PlantarFasciitis",
    "num_upvotes": 19,
    "photos": null,
    "videos": null,
    "tag": "PF Footwear / Insoles 👟",
    "related_posts": [
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/",
        "num_comments": 48,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Birkenstocks",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/",
        "num_comments": 9,
        "num_upvotes": "32",
        "thumbnail": null,
        "title": "Thank you to this group",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/",
        "num_comments": 25,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "Sending a little hope…",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/",
        "num_comments": 17,
        "num_upvotes": "30",
        "thumbnail": null,
        "title": "What helped me:",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/",
        "num_comments": 42,
        "num_upvotes": "63",
        "thumbnail": null,
        "title": "you are going to be ok!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/",
        "num_comments": 6,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "Every little counts...",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/",
        "num_comments": 6,
        "num_upvotes": "27",
        "thumbnail": null,
        "title": "My experience",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/",
        "num_comments": 11,
        "num_upvotes": "70",
        "thumbnail": null,
        "title": "32,000 Members & Growing!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/",
        "num_comments": 88,
        "num_upvotes": "48",
        "thumbnail": null,
        "title": "Two years of this",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/",
        "num_comments": 60,
        "num_upvotes": "80",
        "thumbnail": null,
        "title": "Just need to vent. Feet are killing me and I'm so tired of this.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/",
        "num_comments": 9,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "THANK YOU ALL!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/",
        "num_comments": 24,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "Finally Getting Some Relief",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/",
        "num_comments": 19,
        "num_upvotes": "43",
        "thumbnail": null,
        "title": "The only thing that's helped",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/",
        "num_comments": 9,
        "num_upvotes": "16",
        "thumbnail": null,
        "title": "Hopefully what worked for me will work for you",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/",
        "num_comments": 22,
        "num_upvotes": "9",
        "thumbnail": null,
        "title": "Is this normal?",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/",
        "num_comments": 14,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "What finally worked",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/",
        "num_comments": 19,
        "num_upvotes": "45",
        "thumbnail": null,
        "title": "Finally some improvement",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/",
        "num_comments": 34,
        "num_upvotes": "97",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/",
        "num_comments": 67,
        "num_upvotes": "105",
        "thumbnail": null,
        "title": "Sharing what works for me.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/",
        "num_comments": 10,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "What's worked for me (so far)",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/",
        "num_comments": 10,
        "num_upvotes": "28",
        "thumbnail": null,
        "title": "What Worked for Me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/",
        "num_comments": 27,
        "num_upvotes": "39",
        "thumbnail": null,
        "title": "Finally found something that's helping",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/",
        "num_comments": 38,
        "num_upvotes": "96",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/",
        "num_comments": 33,
        "num_upvotes": "142",
        "thumbnail": null,
        "title": "You know what we’re normalizing??????",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/",
        "num_comments": 81,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Can't keep living like this, desperate for solutions",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/"
      }
    ],
    "comments": [
      {
        "comment": "Yessss instant relief from that fkn snapping feeling I love a fresh pair of birks so much",
        "date_of_comment": "2026-01-04T08:39:41.104Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxlfg54/",
        "user_commenting": "tough_tiddies69",
        "user_url": "https://www.reddit.com/user/tough_tiddies69/"
      },
      {
        "comment": "Yes! One year of recovery but I still cannot go barefoot for extended stretches of time. The good news is that Birks make sandals!",
        "date_of_comment": "2026-01-04T01:26:39.050Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxjo03x/",
        "user_commenting": "mlk2317",
        "user_url": "https://www.reddit.com/user/mlk2317/"
      },
      {
        "comment": "I have the Ecco Kozmo sandals that look a lot like Birkenstocks. They’re really great on my plantar fasciitis.",
        "date_of_comment": "2026-01-03T20:45:30.955Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxi58xp/",
        "user_commenting": "Alternative_Fun5097",
        "user_url": "https://www.reddit.com/user/Alternative_Fun5097/"
      },
      {
        "comment": "I’m wearing Oofos recovery sandals and it’s the only time my feet are 100% pain-free!",
        "date_of_comment": "2026-01-03T19:42:13.399Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhsful/",
        "user_commenting": "balletgirl2020",
        "user_url": "https://www.reddit.com/user/balletgirl2020/"
      },
      {
        "comment": "I’m adamant that the Birks CAUSED my PF. I hate them.",
        "date_of_comment": "2026-01-03T18:41:40.601Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhfa13/",
        "user_commenting": "Boomshiqua",
        "user_url": "https://www.reddit.com/user/Boomshiqua/"
      },
      {
        "comment": "I used to wear birks almost every day, wound up with PF. Still wore them as they were the only shoes that didn't kill me. I needed gym shoes, got some kuru shoes. Now any time I wear my birks it flairs back up. All that to say, every foot is different and until I really started doing the stretches the shoes only allowed me to walk with less pain but never truly heal.",
        "date_of_comment": "2026-01-03T16:57:13.772Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgsfr0/",
        "user_commenting": "PositionOk3089",
        "user_url": "https://www.reddit.com/user/PositionOk3089/"
      },
      {
        "comment": "Two rough calf and foot massages and Birks all summer seemed to cure me. I think everyone is different. Worth a try.",
        "date_of_comment": "2026-01-03T16:49:24.131Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgqqvu/",
        "user_commenting": "jcclune73",
        "user_url": "https://www.reddit.com/user/jcclune73/"
      },
      {
        "comment": "Birkenstocks pretty much cured my PF (work in a surgical field, now wear Birkenstock clogs religiously) - I was limping daily before wearing them. Have to get through the first 2 weeks of break in before getting results",
        "date_of_comment": "2026-01-03T15:22:31.366Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg8nvf/",
        "user_commenting": "precision324",
        "user_url": "https://www.reddit.com/user/precision324/"
      },
      {
        "comment": "I never had PF until I got Birks last year. Feet were fine when wearing but heels started to hurt when I wasn’t wearing them. It got really bad. I gave them up and all resolved within about three months on its own. Birks are great shoes but not everyone is built to wear them.",
        "date_of_comment": "2026-01-03T14:50:40.581Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg2l11/",
        "user_commenting": "UsualClue3638",
        "user_url": "https://www.reddit.com/user/UsualClue3638/"
      },
      {
        "comment": "I got a lot better when I started wearing Birkenstocks all day every day in the house. I have high arches.",
        "date_of_comment": "2026-01-03T13:52:18.223Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxfs9z7/",
        "user_commenting": "No-Interview-1340",
        "user_url": "https://www.reddit.com/user/No-Interview-1340/"
      },
      {
        "comment": "Yes absolutely. I started wearing them exclusively when I got a stress fracture in my non PF foot because they matched the height of the boot I was in best. When I was dealing with the stress fracture I just gave up on my PF exercises because I was frustrated and overwhelmed and I realised once I was in less pain from the fracture that I was also in less pain from the PF. And it wasn't because I was doing less activity, the walking boot actually increased my activity because I could actually move",
        "date_of_comment": "2026-01-03T11:25:55.857Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxf7oke/",
        "user_commenting": "Munishmo",
        "user_url": "https://www.reddit.com/user/Munishmo/"
      },
      {
        "comment": "They’re the only summer shoe that I can wear so they’re my outdoor and indoor three months of the year - my podiatrist recommended them.",
        "date_of_comment": "2026-01-03T06:24:49.926Z",
        "num_replies": 1,
        "num_upvotes": 1,
        "replies": [
          {
            "date_of_reply": "2026-01-03T11:56:31.261Z",
            "num_replies": 0,
            "num_upvotes": 1,
            "reply": "Yeah I wear them a-lot during summer, my physio recommended them they have helped alot",
            "user_replying": "Dense-Try-5879",
            "user_url": "https://www.reddit.com/user/Dense-Try-5879/"
          }
        ],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe8f6g/",
        "user_commenting": "Ok_Jellyfish_4534",
        "user_url": "https://www.reddit.com/user/Ok_Jellyfish_4534/"
      },
      {
        "comment": "Yes , the first time I had PF about 4 years ago my naturopath told me to get birks with a cork sole. I did and it really helped and gradually healed my PF. This time around they unfortunately don’t seem to help like before. Ordered 2 pairs of Kuru for PF and meh not worth the money . However my Nike Motiva walking shoes are helping so much, and at half the price of the others I’ve tried.",
        "date_of_comment": "2026-01-03T06:08:50.846Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe6f9k/",
        "user_commenting": "Ewwwdavid1",
        "user_url": "https://www.reddit.com/user/Ewwwdavid1/"
      },
      {
        "comment": "Yes! Birkenstocks are the only kind of shoe I can wear. I like their sandals for summer and the sneakers the rest of the year.",
        "date_of_comment": "2026-01-03T05:51:28.954Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe46uz/",
        "user_commenting": "ACB_Toby",
        "user_url": "https://www.reddit.com/user/ACB_Toby/"
      },
      {
        "comment": "Yup yup yup!",
        "date_of_comment": "2026-01-03T04:04:50.518Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdour1/",
        "user_commenting": "Left_One_1308",
        "user_url": "https://www.reddit.com/user/Left_One_1308/"
      },
      {
        "comment": "Likely my cause.",
        "date_of_comment": "2026-01-03T04:01:36.596Z",
        "num_replies": 0,
        "num_upvotes": 3,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdocjo/",
        "user_commenting": "DapperWorth7668",
        "user_url": "https://www.reddit.com/user/DapperWorth7668/"
      },
      {
        "comment": "They helped me heal completely but it took at least a year of wearing them consistently. Slippers, clogs, sandals, etc. They were the only shoes I wore. Now I also have a pair of Altras with a high arch insert.",
        "date_of_comment": "2026-01-03T03:17:02.559Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdh5y1/",
        "user_commenting": "fmaon06",
        "user_url": "https://www.reddit.com/user/fmaon06/"
      },
      {
        "comment": "I have no experience with Birkenstocks, but I’m 100% convinced wearing Chacos nearly everyday last summer helped my PF fully heal.",
        "date_of_comment": "2026-01-03T02:03:53.463Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxd4rmy/",
        "user_commenting": "jmmani2",
        "user_url": "https://www.reddit.com/user/jmmani2/"
      },
      {
        "comment": "Massively.",
        "date_of_comment": "2026-01-03T01:04:13.289Z",
        "num_replies": 0,
        "num_upvotes": 0,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcugd9/",
        "user_commenting": "apja",
        "user_url": "https://www.reddit.com/user/apja/"
      },
      {
        "comment": "They aggravated my PF. I fare better with a soft sole.",
        "date_of_comment": "2026-01-03T00:22:48.518Z",
        "num_replies": 0,
        "num_upvotes": 6,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcmyea/",
        "user_commenting": "5pens",
        "user_url": "https://www.reddit.com/user/5pens/"
      }
    ],
    "community_url": "https://www.reddit.com/r/PlantarFasciitis/",
    "community_description": "Plantar fasciitis is a common foot condition characterized by inflammation of the plantar fascia, a thick band of tissue that runs across the bottom of the foot, connecting the heel bone to the toes. The plantar fascia acts as a shock absorber and supports the arch of the foot. When this tissue becomes irritated or inflamed, it can lead to pain and discomfort, especially around the heel.",
    "community_members_num": 40165,
    "community_rank": {
      "community_rank_type": null,
      "community_rank_value": null
    },
    "post_karma": 0,
    "bio_description": null,
    "embedded_links": null,
    "description_markdown": "\n        \n     \n       \n       \n      Found relief when wearing my birkenstocks but pain after wards  when barefoot or wearing other footwear worse. Any one else have a similar story ?\n     \n     \n     \n    \n    ",
    "subreddit_icon_image": "https://styles.redditmedia.com/t5_35l5c/styles/communityIcon_2i3pz63hnoef1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=8add3f8b2a7bcf38c557a155faae0f12508bb690",
    "author_icon": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png",
    "user_id": "t2_w71ujetkx"
  }
]

```

</details>

<details>
<summary><b>Endpoint 'Discover by subreddit URL'</b> response data sample:</summary>

```json
[
  {
    "post_id": "t3_1q1xep3",
    "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/any_one_found_birkenstocks_help_with_their_pf/",
    "user_posted": "Den***Try***79",
    "title": "Any one found Birkenstocks help with their PF ?",
    "description": "Found relief when wearing my birkenstocks but pain after wards when barefoot or wearing other footwear worse. Any one else have a similar story ?",
    "num_comments": 36,
    "date_posted": "2026-01-02T12:29:58.702Z",
    "community_name": "PlantarFasciitis",
    "num_upvotes": 19,
    "photos": null,
    "videos": null,
    "tag": "PF Footwear / Insoles 👟",
    "related_posts": [
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/",
        "num_comments": 48,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Birkenstocks",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mimmas/birkenstocks/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/",
        "num_comments": 9,
        "num_upvotes": "32",
        "thumbnail": null,
        "title": "Thank you to this group",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q35xwd/thank_you_to_this_group/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/",
        "num_comments": 25,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "Sending a little hope…",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ntndyx/sending_a_little_hope/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/",
        "num_comments": 17,
        "num_upvotes": "30",
        "thumbnail": null,
        "title": "What helped me:",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1laizx6/what_helped_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/",
        "num_comments": 42,
        "num_upvotes": "63",
        "thumbnail": null,
        "title": "you are going to be ok!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1qi4tcu/you_are_going_to_be_ok/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/",
        "num_comments": 6,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "Every little counts...",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1p2utn4/every_little_counts/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/",
        "num_comments": 6,
        "num_upvotes": "27",
        "thumbnail": null,
        "title": "My experience",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lftzcu/my_experience/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/",
        "num_comments": 11,
        "num_upvotes": "70",
        "thumbnail": null,
        "title": "32,000 Members & Growing!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m85l2x/32000_members_growing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/",
        "num_comments": 88,
        "num_upvotes": "48",
        "thumbnail": null,
        "title": "Two years of this",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1onuq1d/two_years_of_this/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/",
        "num_comments": 60,
        "num_upvotes": "80",
        "thumbnail": null,
        "title": "Just need to vent. Feet are killing me and I'm so tired of this.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q66whc/just_need_to_vent_feet_are_killing_me_and_im_so/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/",
        "num_comments": 9,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "THANK YOU ALL!",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1leh41z/thank_you_all/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/",
        "num_comments": 24,
        "num_upvotes": "34",
        "thumbnail": null,
        "title": "Finally Getting Some Relief",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pj3586/finally_getting_some_relief/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/",
        "num_comments": 19,
        "num_upvotes": "43",
        "thumbnail": null,
        "title": "The only thing that's helped",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ki6axk/the_only_thing_thats_helped/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/",
        "num_comments": 9,
        "num_upvotes": "16",
        "thumbnail": null,
        "title": "Hopefully what worked for me will work for you",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lqso7e/hopefully_what_worked_for_me_will_work_for_you/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/",
        "num_comments": 22,
        "num_upvotes": "9",
        "thumbnail": null,
        "title": "Is this normal?",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kdkjx7/is_this_normal/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/",
        "num_comments": 14,
        "num_upvotes": "25",
        "thumbnail": null,
        "title": "What finally worked",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mv7x7z/what_finally_worked/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/",
        "num_comments": 19,
        "num_upvotes": "45",
        "thumbnail": null,
        "title": "Finally some improvement",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ix394k/finally_some_improvement/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/",
        "num_comments": 34,
        "num_upvotes": "97",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1mryric/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/",
        "num_comments": 67,
        "num_upvotes": "105",
        "thumbnail": null,
        "title": "Sharing what works for me.",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1m1gpb8/sharing_what_works_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/",
        "num_comments": 10,
        "num_upvotes": "50",
        "thumbnail": null,
        "title": "What's worked for me (so far)",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ob7chj/whats_worked_for_me_so_far/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/",
        "num_comments": 10,
        "num_upvotes": "28",
        "thumbnail": null,
        "title": "What Worked for Me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1kwqp5u/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/",
        "num_comments": 27,
        "num_upvotes": "39",
        "thumbnail": null,
        "title": "Finally found something that's helping",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1lamumf/finally_found_something_thats_helping/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/",
        "num_comments": 38,
        "num_upvotes": "96",
        "thumbnail": null,
        "title": "What worked for me",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1ozsjv6/what_worked_for_me/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/",
        "num_comments": 33,
        "num_upvotes": "142",
        "thumbnail": null,
        "title": "You know what we’re normalizing??????",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1pvxa59/you_know_what_were_normalizing/"
      },
      {
        "community": "plantarfasciitis",
        "community_url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/",
        "num_comments": 81,
        "num_upvotes": "54",
        "thumbnail": null,
        "title": "Can't keep living like this, desperate for solutions",
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1py0axm/cant_keep_living_like_this_desperate_for_solutions/"
      }
    ],
    "comments": [
      {
        "comment": "Yessss instant relief from that fkn snapping feeling I love a fresh pair of birks so much",
        "date_of_comment": "2026-01-04T08:39:41.104Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxlfg54/",
        "user_commenting": "tough_tiddies69",
        "user_url": "https://www.reddit.com/user/tough_tiddies69/"
      },
      {
        "comment": "Yes! One year of recovery but I still cannot go barefoot for extended stretches of time. The good news is that Birks make sandals!",
        "date_of_comment": "2026-01-04T01:26:39.050Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxjo03x/",
        "user_commenting": "mlk2317",
        "user_url": "https://www.reddit.com/user/mlk2317/"
      },
      {
        "comment": "I have the Ecco Kozmo sandals that look a lot like Birkenstocks. They’re really great on my plantar fasciitis.",
        "date_of_comment": "2026-01-03T20:45:30.955Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxi58xp/",
        "user_commenting": "Alternative_Fun5097",
        "user_url": "https://www.reddit.com/user/Alternative_Fun5097/"
      },
      {
        "comment": "I’m wearing Oofos recovery sandals and it’s the only time my feet are 100% pain-free!",
        "date_of_comment": "2026-01-03T19:42:13.399Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhsful/",
        "user_commenting": "balletgirl2020",
        "user_url": "https://www.reddit.com/user/balletgirl2020/"
      },
      {
        "comment": "I’m adamant that the Birks CAUSED my PF. I hate them.",
        "date_of_comment": "2026-01-03T18:41:40.601Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxhfa13/",
        "user_commenting": "Boomshiqua",
        "user_url": "https://www.reddit.com/user/Boomshiqua/"
      },
      {
        "comment": "I used to wear birks almost every day, wound up with PF. Still wore them as they were the only shoes that didn't kill me. I needed gym shoes, got some kuru shoes. Now any time I wear my birks it flairs back up. All that to say, every foot is different and until I really started doing the stretches the shoes only allowed me to walk with less pain but never truly heal.",
        "date_of_comment": "2026-01-03T16:57:13.772Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgsfr0/",
        "user_commenting": "PositionOk3089",
        "user_url": "https://www.reddit.com/user/PositionOk3089/"
      },
      {
        "comment": "Two rough calf and foot massages and Birks all summer seemed to cure me. I think everyone is different. Worth a try.",
        "date_of_comment": "2026-01-03T16:49:24.131Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxgqqvu/",
        "user_commenting": "jcclune73",
        "user_url": "https://www.reddit.com/user/jcclune73/"
      },
      {
        "comment": "Birkenstocks pretty much cured my PF (work in a surgical field, now wear Birkenstock clogs religiously) - I was limping daily before wearing them. Have to get through the first 2 weeks of break in before getting results",
        "date_of_comment": "2026-01-03T15:22:31.366Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg8nvf/",
        "user_commenting": "precision324",
        "user_url": "https://www.reddit.com/user/precision324/"
      },
      {
        "comment": "I never had PF until I got Birks last year. Feet were fine when wearing but heels started to hurt when I wasn’t wearing them. It got really bad. I gave them up and all resolved within about three months on its own. Birks are great shoes but not everyone is built to wear them.",
        "date_of_comment": "2026-01-03T14:50:40.581Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxg2l11/",
        "user_commenting": "UsualClue3638",
        "user_url": "https://www.reddit.com/user/UsualClue3638/"
      },
      {
        "comment": "I got a lot better when I started wearing Birkenstocks all day every day in the house. I have high arches.",
        "date_of_comment": "2026-01-03T13:52:18.223Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxfs9z7/",
        "user_commenting": "No-Interview-1340",
        "user_url": "https://www.reddit.com/user/No-Interview-1340/"
      },
      {
        "comment": "Yes absolutely. I started wearing them exclusively when I got a stress fracture in my non PF foot because they matched the height of the boot I was in best. When I was dealing with the stress fracture I just gave up on my PF exercises because I was frustrated and overwhelmed and I realised once I was in less pain from the fracture that I was also in less pain from the PF. And it wasn't because I was doing less activity, the walking boot actually increased my activity because I could actually move",
        "date_of_comment": "2026-01-03T11:25:55.857Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxf7oke/",
        "user_commenting": "Munishmo",
        "user_url": "https://www.reddit.com/user/Munishmo/"
      },
      {
        "comment": "They’re the only summer shoe that I can wear so they’re my outdoor and indoor three months of the year - my podiatrist recommended them.",
        "date_of_comment": "2026-01-03T06:24:49.926Z",
        "num_replies": 1,
        "num_upvotes": 1,
        "replies": [
          {
            "date_of_reply": "2026-01-03T11:56:31.261Z",
            "num_replies": 0,
            "num_upvotes": 1,
            "reply": "Yeah I wear them a-lot during summer, my physio recommended them they have helped alot",
            "user_replying": "Dense-Try-5879",
            "user_url": "https://www.reddit.com/user/Dense-Try-5879/"
          }
        ],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe8f6g/",
        "user_commenting": "Ok_Jellyfish_4534",
        "user_url": "https://www.reddit.com/user/Ok_Jellyfish_4534/"
      },
      {
        "comment": "Yes , the first time I had PF about 4 years ago my naturopath told me to get birks with a cork sole. I did and it really helped and gradually healed my PF. This time around they unfortunately don’t seem to help like before. Ordered 2 pairs of Kuru for PF and meh not worth the money . However my Nike Motiva walking shoes are helping so much, and at half the price of the others I’ve tried.",
        "date_of_comment": "2026-01-03T06:08:50.846Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe6f9k/",
        "user_commenting": "Ewwwdavid1",
        "user_url": "https://www.reddit.com/user/Ewwwdavid1/"
      },
      {
        "comment": "Yes! Birkenstocks are the only kind of shoe I can wear. I like their sandals for summer and the sneakers the rest of the year.",
        "date_of_comment": "2026-01-03T05:51:28.954Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxe46uz/",
        "user_commenting": "ACB_Toby",
        "user_url": "https://www.reddit.com/user/ACB_Toby/"
      },
      {
        "comment": "Yup yup yup!",
        "date_of_comment": "2026-01-03T04:04:50.518Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdour1/",
        "user_commenting": "Left_One_1308",
        "user_url": "https://www.reddit.com/user/Left_One_1308/"
      },
      {
        "comment": "Likely my cause.",
        "date_of_comment": "2026-01-03T04:01:36.596Z",
        "num_replies": 0,
        "num_upvotes": 3,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdocjo/",
        "user_commenting": "DapperWorth7668",
        "user_url": "https://www.reddit.com/user/DapperWorth7668/"
      },
      {
        "comment": "They helped me heal completely but it took at least a year of wearing them consistently. Slippers, clogs, sandals, etc. They were the only shoes I wore. Now I also have a pair of Altras with a high arch insert.",
        "date_of_comment": "2026-01-03T03:17:02.559Z",
        "num_replies": 0,
        "num_upvotes": 1,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxdh5y1/",
        "user_commenting": "fmaon06",
        "user_url": "https://www.reddit.com/user/fmaon06/"
      },
      {
        "comment": "I have no experience with Birkenstocks, but I’m 100% convinced wearing Chacos nearly everyday last summer helped my PF fully heal.",
        "date_of_comment": "2026-01-03T02:03:53.463Z",
        "num_replies": 0,
        "num_upvotes": 2,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxd4rmy/",
        "user_commenting": "jmmani2",
        "user_url": "https://www.reddit.com/user/jmmani2/"
      },
      {
        "comment": "Massively.",
        "date_of_comment": "2026-01-03T01:04:13.289Z",
        "num_replies": 0,
        "num_upvotes": 0,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcugd9/",
        "user_commenting": "apja",
        "user_url": "https://www.reddit.com/user/apja/"
      },
      {
        "comment": "They aggravated my PF. I fare better with a soft sole.",
        "date_of_comment": "2026-01-03T00:22:48.518Z",
        "num_replies": 0,
        "num_upvotes": 6,
        "replies": [],
        "url": "https://www.reddit.com/r/PlantarFasciitis/comments/1q1xep3/comment/nxcmyea/",
        "user_commenting": "5pens",
        "user_url": "https://www.reddit.com/user/5pens/"
      }
    ],
    "community_url": "https://www.reddit.com/r/PlantarFasciitis/",
    "community_description": "Plantar fasciitis is a common foot condition characterized by inflammation of the plantar fascia, a thick band of tissue that runs across the bottom of the foot, connecting the heel bone to the toes. The plantar fascia acts as a shock absorber and supports the arch of the foot. When this tissue becomes irritated or inflamed, it can lead to pain and discomfort, especially around the heel.",
    "community_members_num": 40165,
    "community_rank": {
      "community_rank_type": null,
      "community_rank_value": null
    },
    "post_karma": 0,
    "bio_description": null,
    "embedded_links": null,
    "description_markdown": "\n        \n     \n       \n       \n      Found relief when wearing my birkenstocks but pain after wards  when barefoot or wearing other footwear worse. Any one else have a similar story ?\n     \n     \n     \n    \n    ",
    "subreddit_icon_image": "https://styles.redditmedia.com/t5_35l5c/styles/communityIcon_2i3pz63hnoef1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=8add3f8b2a7bcf38c557a155faae0f12508bb690",
    "author_icon": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png",
    "user_id": "t2_w71ujetkx"
  }
]

```

</details>


### Reddit Comments

Use this endpoint to scrape the discussion layer of a post.

|Endpoint|Required Input|Optional Parameters|
|-----------------------|--------------|-------------------|
|Collect comments by URL| URL (Post link)|days_back,load_all_replies,comment_limit,sort_by|


<details>
<summary>Endpoint response data sample:</summary>

```json
[
  {
    "url": "https://www.reddit.com/r/TrendoraX/comments/1r6u1aw/comment/o5szlm9/",
    "comment_id": "o5szlm9",
    "user_posted": "Eas***uot***934***",
    "comment": "Can another country have them do it?",
    "date_posted": "2026-02-17T03:30:04.435Z",
    "post_url": "https://www.reddit.com/r/TrendoraX/comments/1r6u1aw/hillary_clinton_just_went_on_the_bbc_and_accused/",
    "post_id": "1r6u1aw",
    "community_name": "TrendoraX",
    "community_url": "https://www.reddit.com/r/TrendoraX",
    "community_description": "Your daily dose of what's trending in tech, sports, entertainment, and beyond!",
    "community_members_num": "26763",
    "community_rank": {
      "community_rank_type": null,
      "community_rank_value": null
    },
    "replies": null,
    "num_upvotes": 4,
    "num_replies": 0,
    "days_back": 180,
    "is_moderator": false,
    "is_pinned": false,
    "has_bot_in_username": false,
    "is_locked": false,
    "is_admin_post": false,
    "is_archived_post": false,
    "is_moderator_post": false,
    "is_quarantined_post": false,
    "is_not_safe_for_work_post": false,
    "is_eligible_for_content_blocking_post": false,
    "is_promoted_post": false,
    "post_language": "en",
    "post_state": null,
    "post_type": "image",
    "images": null,
    "parent_comment_id": null,
    "root_comment_id": null,
    "videos": null
  }
]
```

</details>

### Reddit Profiles

Use this endpoint to scrape the discussion layer of a profile.

|Endpoint|Required Input|
|-----------------------|--------------|
|Collect comments by URL| URL (Profile link)|

<details>
<summary>Endpoint response data sample:</summary>

```json
[
  {
    "url": "https://www.reddit.com/user/CLBHos/",
    "profile_id": "t2_9wlru8jt",
    "name": "CLBHos",
    "followers": 0,
    "social_links": [],
    "karma": 44080,
    "contributions": {
      "comments": 392,
      "posts": 102
    },
    "reddit_age": "4 y",
    "contributor_status": null,
    "active_in": [
      {
        "name": "r/CLBHos",
        "url": "https://www.reddit.com/r/CLBHos/"
      },
      {
        "name": "r/WritingPrompts",
        "url": "https://www.reddit.com/r/WritingPrompts/"
      },
      {
        "name": "r/nosleep",
        "url": "https://www.reddit.com/r/nosleep/"
      },
      {
        "name": "r/shortstories",
        "url": "https://www.reddit.com/r/shortstories/"
      }
    ],
    "description": null
  }
]
```

</details>

<br><br>

# Whether keyword-based search is supported?

Yes, is supported principally by searching reddit posts endpoint.<br><br>

# Response time and reliability

Average response time per input: 18s
Price starts at: $0.0015 Per record

<br>

# Free tier limitations encountered

We have only 2$ free tier without card, but with registering a card, Bright Data gives 5$ more.

# Comparisson with Reddit API Official

I think that the Reddit Official API is good because is free, but the mainly problem in the Fuzzy core is that 100 requests per 10 minuts its not viable with a 100,000 users amount. Also if we are not authenticated it will probably ban us from our DNS domain, even if we use AWS to scrap it.

# Plus from Bright Data

It appears that BrightData supports asynchronous data processing; for example, we can preload some queries or run them in the background, store them in various types of cloud, and thus optimize future flows that Fuzzy App may have.

![Async Option](/imgs/AsyncOption.png)

Evidence about the multi-cloud storage integration support.
<br>

![Cloud Support](/imgs/CloudSupport.png)