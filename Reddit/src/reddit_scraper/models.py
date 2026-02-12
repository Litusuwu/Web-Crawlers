"""Data models for Reddit scraper."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RedditPost(BaseModel):
    """Model for a Reddit post/submission."""
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.isoformat()}
    )
    
    id: str
    title: str
    body: Optional[str] = None
    author: str
    timestamp: datetime
    subreddit: str
    url: str
    score: int = 0
    num_comments: int = 0
    media_urls: list[str] = Field(default_factory=list)
    permalink: str
    is_self: bool = False
    link_flair_text: Optional[str] = None


class RedditComment(BaseModel):
    """Model for a Reddit comment."""
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.isoformat()}
    )
    
    id: str
    body: str
    author: str
    timestamp: datetime
    score: int = 0
    parent_id: str
    post_id: str
    permalink: str
    is_submitter: bool = False


class RedditUser(BaseModel):
    """Model for a Reddit user."""
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.isoformat()}
    )
    
    username: str
    created_utc: datetime
    comment_karma: int = 0
    link_karma: int = 0
    is_gold: bool = False
    is_mod: bool = False
    verified: bool = False
    verified: bool = False
