from datetime import datetime

from pydantic import BaseModel, UrlStr


class Author(BaseModel):
    accept_private_policy: bool
    account_region: str
    ad_cover_url: UrlStr = None
    apple_account: int
    authority_status: int
    avatar_uri: str
    aweme_count: int
    bind_phone: str
    birthday: str
    comment_filter_status: int
    comment_setting: int
    commerce_user_level: int
    constellation: int
    create_time: int
    custom_verify: str
    cv_level: int
    download_prompt_ts: int
    favoriting_count: int
    fb_expire_time: int
    follow_status: int
    follower_count: int
    follower_status: int
    following_count: int
    gender: int
    google_account: str
    has_email: bool
    has_facebook_token: bool
    has_insights: bool
    has_orders: bool
    has_twitter_token: bool
    has_unread_story: bool
    has_youtube_token: bool
    hide_location: bool
    hide_search: bool
    is_ad_fake: bool
    is_block: bool
    is_phone_binded: bool
    is_star: bool
    is_verified: bool
    language: str
    location: str
    nickname: str
    region: str
    sec_uid: str
    short_id: str
    signature: str
    status: int
    story_count: int
    total_favorited: int
    twitter_id: str
    twitter_name: str
    uid: str
    unique_id: str
    unique_id_modify_time: str
    user_canceled: bool
    user_mode: int
    user_rate: int
    verification_type: int
    with_commerce_entry: bool
    with_shop_entry: bool
    youtube_channel_id: str
    youtube_channel_title: str
