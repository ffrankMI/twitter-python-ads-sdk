# Copyright (C) 2015 Twitter, Inc.

"""Container for all enum values used by the Ads API SDK."""


def enum(**enums):
    return type('Enum', (), enums)


TRANSFORM = enum(
    TIME=0,
    BOOL=1,
    INT=2,
    LIST=3,
    OBJECT=4
)

AGE_BUCKET = enum(
    AGE_13_TO_24='AGE_13_TO_24',
    AGE_13_TO_34='AGE_13_TO_34',
    AGE_13_TO_49='AGE_13_TO_49',
    AGE_13_TO_54='AGE_13_TO_54',
    AGE_OVER_13='AGE_OVER_13',
    AGE_18_TO_34='AGE_18_TO_34',
    AGE_18_TO_49='AGE_18_TO_49',
    AGE_18_TO_54='AGE_18_TO_54',
    AGE_OVER_18='AGE_OVER_18',
    AGE_21_TO_34='AGE_21_TO_34',
    AGE_21_TO_49='AGE_21_TO_49',
    AGE_21_TO_54='AGE_21_TO_54',
    AGE_OVER_21='AGE_OVER_21',
    AGE_25_TO_49='AGE_25_TO_49',
    AGE_25_TO_54='AGE_25_TO_54',
    AGE_OVER_25='AGE_OVER_25',
    AGE_35_TO_49='AGE_35_TO_49',
    AGE_35_TO_54='AGE_35_TO_54',
    AGE_OVER_35='AGE_OVER_35',
    AGE_OVER_50='AGE_OVER_50'
)

CREATIVE_TYPE = enum(
    BANNER='BANNER',
    INTERSTITIAL='INTERSTITIAL',
    PREROLL='PREROLL',
    VAST_PREROLL='VAST_PREROLL',
    MEDIUM_RECTANGLE='MEDIUM_RECTANGLE',
    BANNER_TABLET='BANNER_TABLET',
    INTERSTITIAL_LANDSCAPE='INTERSTITIAL_LANDSCAPE',
    INTERSTITIAL_TABLET='INTERSTITIAL_TABLET',
    INTERSTITIAL_LANDSCAPE_TABLET='INTERSTITIAL_LANDSCAPE_TABLET'
)

ENTITY = enum(
    ACCOUNT='ACCOUNT',
    FUNDING_INSTRUMENT='FUNDING_INSTRUMENT',
    CAMPAIGN='CAMPAIGN',
    LINE_ITEM='LINE_ITEM',
    MEDIA_CREATIVE='MEDIA_CREATIVE',
    PROMOTED_TWEET='PROMOTED_TWEET',
    ORGANIC_TWEET='ORGANIC_TWEET',
    TARGETING_CRITERION='TARGETING_CRITERION',
    PROMOTED_ACCOUNT='PROMOTED_ACCOUNT',
    TWEET='TWEET'
)

ENTITY_STATUS = enum(
    ACTIVE="ACTIVE",
    DRAFT="DRAFT",
    PAUSED="PAUSED"
)

EVENTS = enum(
    MUSIC_AND_ENTERTAINMENT='MUSIC_AND_ENTERTAINMENT',
    SPORTS='SPORTS',
    HOLIDAY='HOLIDAY',
    CONFERENCE='CONFERENCE',
    OTHER='OTHER'
)

GOAL = enum(
    APP_CLICKS='APP_CLICKS',
    APP_INSTALLS='APP_INSTALLS',
    ENGAGEMENT='ENGAGEMENT',
    FOLLOWERS='FOLLOWERS',
    LINK_CLICKS='LINK_CLICKS',
    MAX_REACH='MAX_REACH',
    PREROLL='PREROLL',
    PREROLL_STARTS='PREROLL_STARTS',
    REACH_WITH_ENGAGEMENT='REACH_WITH_ENGAGEMENT',
    VIDEO_VIEW='VIDEO_VIEW',
    VIEW_3S_100PCT='VIEW_3S_100PCT',
    VIEW_6S='VIEW_6S',
    VIEW_15S='VIEW_15S',
    WEBSITE_CONVERSIONS='WEBSITE_CONVERSIONS'
)

GRANULARITY = enum(
    HOUR='HOUR',
    DAY='DAY',
    TOTAL='TOTAL'
)

MEDIA_CATEGORY = enum(
    AMPLIFY_VIDEO='AMPLIFY_VIDEO',
    TWEET_GIF='TWEET_GIF',
    TWEET_IMAGE='TWEET_IMAGE',
    TWEET_VIDEO='TWEET_VIDEO'
)

MEDIA_TYPE = enum(
    GIF='GIF',
    IMAGE='IMAGE',
    VIDEO='VIDEO'
)

METRIC_GROUP = enum(
    ENGAGEMENT='ENGAGEMENT',
    WEB_CONVERSION='WEB_CONVERSION',
    MOBILE_CONVERSION='MOBILE_CONVERSION',
    MEDIA='MEDIA',
    VIDEO='VIDEO',
    BILLING='BILLING',
    LIFE_TIME_VALUE_MOBILE_CONVERSION='LIFE_TIME_VALUE_MOBILE_CONVERSION'
)

OBJECTIVE = enum(
    APP_ENGAGEMENTS='APP_ENGAGEMENTS',
    APP_INSTALLS='APP_INSTALLS',
    ENGAGEMENTS='ENGAGEMENTS',
    FOLLOWERS='FOLLOWERS',
    LEAD_GENERATION='LEAD_GENERATION',
    PREROLL_VIEWS='PREROLL_VIEWS',
    REACH='REACH',
    VIDEO_VIEWS='VIDEO_VIEWS',
    WEBSITE_CLICKS='WEBSITE_CLICKS',
    WEBSITE_CONVERSIONS='WEBSITE_CONVERSIONS'
)

PAY_BY = enum(
    APP_CLICK='APP_CLICK',
    APP_INSTALL='APP_INSTALL',
    ENGAGEMENT='ENGAGEMENT',
    FOLLOW='FOLLOW',
    LEAD='LEAD',
    LINK_CLICK='LINK_CLICK',
    VIEW='VIEW'
)

PERMISSION_LEVEL = enum(
    READ_ONLY='READ_ONLY',
    READ_WRITE='READ_WRITE'
)

PLACEMENT = enum(
    ALL_ON_TWITTER='ALL_ON_TWITTER',
    TWITTER_SEARCH='TWITTER_SEARCH',
    TWITTER_TIMELINE='TWITTER_TIMELINE',
    PUBLISHER_NETWORK='PUBLISHER_NETWORK',
    TAP_FULL='TAP_FULL',
    TAP_FULL_LANDSCAPE='TAP_FULL_LANDSCAPE',
    TAP_BANNER='TAP_BANNER',
    TAP_NATIVE='TAP_NATIVE',
    TAP_MRECT="TAP_MRECT"
)

PRODUCT = enum(
    PROMOTED_ACCOUNT='PROMOTED_ACCOUNT',
    PROMOTED_TWEETS='PROMOTED_TWEETS'
)

TA_LIST_TYPES = enum(
    EMAIL='EMAIL',
    DEVICE_ID='DEVICE_ID',
    TWITTER_ID='TWITTER_ID',
    HANDLE='HANDLE',
    PHONE_NUMBER='PHONE_NUMBER'
)

TA_OPERATIONS = enum(
    ADD='ADD',
    REMOVE='REMOVE',
    REPLACE='REPLACE'
)

CONVERSATION_TYPE = enum(
    HASHTAG='HASHTAG',
    HANDLE='TARGETING_CRITERIA',
    EVENT='EVENT'
)

LOOKALIKE_EXPANSION = enum(
    BROAD='BROAD',
    DEFINED='DEFINED',
    EXPANDED='EXPANDED'
)

TWEET_TYPE = enum(
    DRAFT='DRAFT',
    PUBLISHED='PUBLISHED',
    SCHEDULED='SCHEDULED'
)

TIMELINE_TYPE = enum(
    ALL='ALL',
    NULLCAST='NULLCAST',
    ORGANIC='ORGANIC'
)

SEGMENTATION_TYPE = enum(
    AGE='AGE',
    APP_STORE_CATEGORY='APP_STORE_CATEGORY',
    AUDIENCES='AUDIENCES',
    METROS='METROS',
    CONVERSATIONS='CONVERSATIONS',
    CONVERSION_TAGS='CONVERSION_TAGS',
    DEVICES='DEVICES',
    EVENTS='EVENTS',
    GENDER='GENDER',
    INTERESTS='INTERESTS',
    KEYWORDS='KEYWORDS',
    LANGUAGES='LANGUAGES',
    LOCATIONS='LOCATIONS',
    PLATFORMS='PLATFORMS',
    PLATFORM_VERSIONS='PLATFORM_VERSIONS',
    POSTAL_CODES='POSTAL_CODES',
    REGIONS='REGIONS',
    SIMILAR_TO_FOLLOWERS_OF_USER='SIMILAR_TO_FOLLOWERS_OF_USER',
    TV_SHOWS='TV_SHOWS'
)