#!/usr/bin/env python3
"""
Reddit Image URLs - Complete Examples
Shows all the ways Reddit returns image and media URLs.
"""

import json

import requests


def extract_all_media_urls(post_data):
    """Extract all possible media URLs from a Reddit post."""
    urls = {
        "thumbnails": [],
        "images": [],
        "videos": [],
        "galleries": [],
        "preview_images": [],
    }

    # 1. Thumbnail (small preview image)
    if post_data.get("thumbnail") and post_data["thumbnail"] not in [
        "self",
        "default",
        "nsfw",
        "spoiler",
    ]:
        urls["thumbnails"].append(post_data["thumbnail"])

    # 2. Direct image URL (for image posts)
    if post_data.get("url"):
        url = post_data["url"]
        if (
            any(url.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"])
            or "i.redd.it" in url
            or "i.imgur.com" in url
        ):
            urls["images"].append(url)

    # 3. Preview images (multiple resolutions)
    if "preview" in post_data and "images" in post_data["preview"]:
        for img in post_data["preview"]["images"]:
            # Source (highest quality)
            if "source" in img:
                urls["preview_images"].append(
                    {
                        "url": img["source"]["url"],
                        "width": img["source"]["width"],
                        "height": img["source"]["height"],
                        "type": "source",
                    }
                )

            # Resolutions (different sizes)
            if "resolutions" in img:
                for res in img["resolutions"]:
                    urls["preview_images"].append(
                        {
                            "url": res["url"],
                            "width": res["width"],
                            "height": res["height"],
                            "type": "resolution",
                        }
                    )

    # 4. Gallery images (multiple images in one post)
    if post_data.get("is_gallery") and "media_metadata" in post_data:
        for item_id, item_data in post_data["media_metadata"].items():
            if "s" in item_data and "u" in item_data["s"]:
                urls["galleries"].append(
                    {
                        "url": item_data["s"]["u"].replace("&amp;", "&"),
                        "type": item_data.get("e", "unknown"),
                        "id": item_id,
                    }
                )

    # 5. Video URLs
    if "media" in post_data and post_data["media"]:
        if "reddit_video" in post_data["media"]:
            video = post_data["media"]["reddit_video"]
            urls["videos"].append(
                {
                    "fallback_url": video.get("fallback_url"),
                    "dash_url": video.get("dash_url"),
                    "hls_url": video.get("hls_url"),
                    "width": video.get("width"),
                    "height": video.get("height"),
                    "duration": video.get("duration"),
                }
            )

    return urls


def example_image_search():
    """Search for posts with images and show all media URLs."""
    print("=" * 70)
    print("REDDIT IMAGE/MEDIA URLs - Complete Example")
    print("=" * 70)
    print()

    # Search for posts likely to have images
    url = "https://www.reddit.com/r/pics/hot.json"
    params = {"limit": 3, "raw_json": 1}
    headers = {"User-Agent": "python:reddit-media-extractor:v0.1"}

    print(f"📤 Requesting: {url}")
    print("Looking for posts with images...\n")

    response = requests.get(url, params=params, headers=headers, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if "data" in data and "children" in data["data"]:
            for i, child in enumerate(data["data"]["children"], 1):
                post = child["data"]

                print(f"\n{'=' * 70}")
                print(f"POST {i}: {post.get('title', 'No title')[:60]}...")
                print(f"{'=' * 70}")
                print(f"Post ID: {post.get('id')}")
                print(f"Subreddit: r/{post.get('subreddit')}")
                print(f"Author: u/{post.get('author')}")
                print(f"Score: {post.get('score')}")
                print(f"URL: {post.get('url')}")
                print()

                # Extract all media URLs
                media_urls = extract_all_media_urls(post)

                # Show thumbnails
                if media_urls["thumbnails"]:
                    print("📸 THUMBNAIL:")
                    for url in media_urls["thumbnails"]:
                        print(f"  {url}")

                # Show direct images
                if media_urls["images"]:
                    print("\n🖼️  DIRECT IMAGE URLs:")
                    for url in media_urls["images"]:
                        print(f"  {url}")

                # Show preview images
                if media_urls["preview_images"]:
                    print(
                        f"\n🔍 PREVIEW IMAGES ({len(media_urls['preview_images'])} versions):"
                    )
                    # Show only source and one resolution as example
                    sources = [
                        p for p in media_urls["preview_images"] if p["type"] == "source"
                    ]
                    if sources:
                        img = sources[0]
                        print(
                            f"  Source ({img['width']}x{img['height']}): {img['url']}"
                        )

                    resolutions = [
                        p
                        for p in media_urls["preview_images"]
                        if p["type"] == "resolution"
                    ]
                    if resolutions:
                        print(f"  + {len(resolutions)} additional resolutions")

                # Show galleries
                if media_urls["galleries"]:
                    print(f"\n🎨 GALLERY ({len(media_urls['galleries'])} images):")
                    for img in media_urls["galleries"]:
                        print(f"  {img['url']}")

                # Show videos
                if media_urls["videos"]:
                    print("\n🎥 VIDEO:")
                    for video in media_urls["videos"]:
                        print(f"  Fallback: {video['fallback_url']}")
                        if video.get("width") and video.get("height"):
                            print(f"  Resolution: {video['width']}x{video['height']}")
                        if video.get("duration"):
                            print(f"  Duration: {video['duration']}s")

                # Show JSON structure for this post's media
                print("\n📋 JSON STRUCTURE (media fields):")
                media_fields = {
                    "thumbnail": post.get("thumbnail"),
                    "url": post.get("url"),
                    "is_video": post.get("is_video"),
                    "is_gallery": post.get("is_gallery"),
                    "post_hint": post.get("post_hint"),
                    "has_preview": "preview" in post,
                    "has_media": post.get("media") is not None,
                }
                print(json.dumps(media_fields, indent=2))


def example_detailed_structure():
    """Show detailed structure of image/media fields."""
    print("\n\n" + "=" * 70)
    print("DETAILED: Image/Media Field Structure")
    print("=" * 70)
    print("""
Reddit posts can contain media in these fields:

1. 📸 THUMBNAIL (string)
   - Small preview image (140x78 typical)
   - Example: "https://a.thumbs.redditmedia.com/xxx.jpg"
   - Special values: 'self', 'default', 'nsfw', 'spoiler'

   JSON:
   {
     "thumbnail": "https://a.thumbs.redditmedia.com/xxx.jpg",
     "thumbnail_width": 140,
     "thumbnail_height": 78
   }

2. 🖼️  URL (string)
   - Direct link to content
   - Can be: image URL, video URL, or external link
   - Image domains: i.redd.it, i.imgur.com, etc.

   JSON:
   {
     "url": "https://i.redd.it/xyz123.jpg",
     "domain": "i.redd.it"
   }

3. 🔍 PREVIEW (object)
   - Multiple resolutions of the image
   - Contains source (highest quality) and resolutions

   JSON:
   {
     "preview": {
       "images": [{
         "source": {
           "url": "https://preview.redd.it/xyz.jpg",
           "width": 1920,
           "height": 1080
         },
         "resolutions": [
           {"url": "...", "width": 108, "height": 60},
           {"url": "...", "width": 216, "height": 121},
           {"url": "...", "width": 320, "height": 180},
           {"url": "...", "width": 640, "height": 360},
           {"url": "...", "width": 960, "height": 540}
         ]
       }]
     }
   }

4. 🎥 MEDIA (object) - for videos
   - Reddit-hosted video information

   JSON:
   {
     "media": {
       "reddit_video": {
         "fallback_url": "https://v.redd.it/xyz/DASH_1080.mp4",
         "dash_url": "https://v.redd.it/xyz/DASHPlaylist.mpd",
         "hls_url": "https://v.redd.it/xyz/HLSPlaylist.m3u8",
         "width": 1920,
         "height": 1080,
         "duration": 268,
         "is_gif": false
       }
     },
     "is_video": true
   }

5. 🎨 GALLERY (object) - for multiple images
   - Multiple images in one post

   JSON:
   {
     "is_gallery": true,
     "media_metadata": {
       "image_id_1": {
         "s": {
           "u": "https://preview.redd.it/img1.jpg",
           "x": 1920,
           "y": 1080
         }
       },
       "image_id_2": {
         "s": {
           "u": "https://preview.redd.it/img2.jpg",
           "x": 1920,
           "y": 1080
         }
       }
     }
   }

6. 📌 POST HINT (string)
   - Indicates content type
   - Values: 'image', 'hosted:video', 'rich:video', 'link', 'self'

   JSON:
   {
     "post_hint": "image"
   }
    """)


def save_image_urls_example():
    """Save all image URLs to a file."""
    print("\n" + "=" * 70)
    print("SAVING IMAGE URLs to file...")
    print("=" * 70)

    url = "https://www.reddit.com/r/pics/hot.json"
    params = {"limit": 5, "raw_json": 1}
    headers = {"User-Agent": "python:reddit-media-extractor:v0.1"}

    response = requests.get(url, params=params, headers=headers, timeout=10)

    if response.status_code == 200:
        data = response.json()
        all_urls = []

        for child in data["data"]["children"]:
            post = child["data"]
            media = extract_all_media_urls(post)

            post_urls = {
                "post_id": post.get("id"),
                "title": post.get("title"),
                "url": post.get("url"),
                "thumbnails": media["thumbnails"],
                "images": media["images"],
                "preview_images": media["preview_images"],
                "galleries": media["galleries"],
                "videos": media["videos"],
            }
            all_urls.append(post_urls)

        # Save to file
        filename = "reddit_image_urls.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(all_urls, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved {len(all_urls)} posts with media URLs to: {filename}")

        # Show summary
        total_images = sum(
            len(p["images"]) + len(p["preview_images"]) for p in all_urls
        )
        total_videos = sum(len(p["videos"]) for p in all_urls)
        print("\nSummary:")
        print(f"  Total posts: {len(all_urls)}")
        print(f"  Total images: {total_images}")
        print(f"  Total videos: {total_videos}")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("REDDIT IMAGE/MEDIA URLs - Complete Guide")
    print("=" * 70)
    print()

    # Example 1: Extract images from posts
    example_image_search()

    # Example 2: Show detailed structure
    example_detailed_structure()

    # Example 3: Save to file
    save_image_urls_example()

    print("\n" + "=" * 70)
    print("✅ COMPLETE!")
    print("=" * 70)
    print("""
Files created:
  - reddit_image_urls.json (all image URLs from posts)

Key takeaways:
  • Thumbnail: Always check post['thumbnail']
  • Direct images: Check post['url'] and post['domain']
  • High quality: Use post['preview']['images'][0]['source']['url']
  • Videos: Check post['media']['reddit_video']
  • Galleries: Check post['is_gallery'] and post['media_metadata']
    """)


if __name__ == "__main__":
    main()
    main()
