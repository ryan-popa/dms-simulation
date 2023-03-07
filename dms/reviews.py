import random

reviews = [
    {
        "text": "The driver was excellent and got me to my destination quickly!",
        "rating": 5,
    },
    {"text": "The taxi was dirty and smelled terrible.", "rating": 2},
    {"text": "The driver was friendly and polite.", "rating": 4},
    {"text": "The taxi was comfortable and clean.", "rating": 5},
    {"text": "The driver took a longer route and I was charged extra.", "rating": 2},
    {"text": "The taxi arrived late and made me miss my flight.", "rating": 1},
    {"text": "The driver drove dangerously and made me feel unsafe.", "rating": 1},
    {"text": "The taxi was modern and had all the amenities I needed.", "rating": 4},
    {"text": "The driver was courteous and professional.", "rating": 5},
    {"text": "The taxi was old and uncomfortable.", "rating": 2},
    {
        "text": "The driver was knowledgeable about the city and gave me some great tips.",
        "rating": 5,
    },
    {
        "text": "The taxi was clean but the air conditioning wasn't working.",
        "rating": 3,
    },
    {
        "text": "The driver was late but made up for it by taking a faster route.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was very professional.",
        "rating": 3,
    },
    {"text": "The driver was rude and unprofessional.", "rating": 1},
    {"text": "The taxi was well-maintained and comfortable.", "rating": 4},
    {
        "text": "The driver didn't speak much English and had trouble understanding me.",
        "rating": 2,
    },
    {"text": "The taxi was clean and smelled nice.", "rating": 4},
    {"text": "The driver was friendly but drove too fast for my liking.", "rating": 3},
    {
        "text": "The taxi was late but the driver made every effort to make up for it.",
        "rating": 4,
    },
    {
        "text": "The driver was very knowledgeable about the local area and gave me some great recommendations.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable but the driver was very friendly.",
        "rating": 3,
    },
    {
        "text": "The driver was very accommodating and went out of their way to help me with my luggage.",
        "rating": 5,
    },
    {"text": "The taxi was dirty and the driver was rude.", "rating": 1},
    {"text": "The driver was very professional and made me feel safe.", "rating": 4},
    {
        "text": "The taxi was expensive but the driver was very knowledgeable about the city.",
        "rating": 3,
    },
    {
        "text": "The driver was very friendly but the taxi was uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable but the driver was rude.",
        "rating": 2,
    },
    {
        "text": "The driver was very friendly and made my journey a pleasant experience.",
        "rating": 5,
    },
    {
        "text": "The taxi was modern and had all the amenities I needed but the driver was late.",
        "rating": 3,
    },
    {
        "text": "The driver was very knowledgeable about the local area and gave me some great tips.",
        "rating": 4,
    },
    {"text": "The taxi was clean and the driver was very professional.", "rating": 4},
    {
        "text": "The driver was very helpful and made sure I got to my destination on time.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable and the driver was rude.",
        "rating": 1,
    },
    {
        "text": "The driver was friendly but the taxi was dirty and had a strange odor.",
        "rating": 2,
    },
    {
        "text": "The taxi was well-maintained and comfortable, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was knowledgeable about the city and took a scenic route that was enjoyable.",
        "rating": 4,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was a bit reckless and made me feel unsafe.",
        "rating": 3,
    },
    {
        "text": "The driver was very polite and accommodating, and the taxi was comfortable and had all the amenities I needed.",
        "rating": 4,
    },
    {
        "text": "The taxi was late and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was friendly and professional, and the taxi was clean and well-maintained.",
        "rating": 5,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations.",
        "rating": 3,
    },
    {
        "text": "The driver was very knowledgeable about the city and gave me a lot of interesting information during the ride.",
        "rating": 4,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey more pleasant.",
        "rating": 3,
    },
    {
        "text": "The driver was very friendly and helpful, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a scenic route that was enjoyable.",
        "rating": 4,
    },
    {
        "text": "The taxi was comfortable and clean, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was friendly and made me feel comfortable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and well-maintained, but the driver was rude and unprofessional.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and professional, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late but the driver made up for it by taking a shorter route.",
        "rating": 4,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for places to visit.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was professional and knowledgeable.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and made the journey enjoyable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was rude and unprofessional.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and accommodating, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a scenic route that was enjoyable.",
        "rating": 4,
    },
    {
        "text": "The taxi was clean and comfortable, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was friendly and made me feel comfortable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was polite and accommodating, and the taxi was clean and comfortable.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and professional, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late but the driver made up for it by taking a shorter route.",
        "rating": 4,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for places to visit.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was professional and knowledgeable.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and made the journey enjoyable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was rude and unprofessional.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and accommodating, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a scenic route that was enjoyable.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was friendly and made me feel comfortable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for places to visit.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, and the driver was rude and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was professional and knowledgeable.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and made the journey enjoyable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was rude and unprofessional.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and accommodating, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was rudeand unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was clean and comfortable, and the driver was friendly and accommodating.",
        "rating": 5,
    },
    {
        "text": "The driver was professional and courteous, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, and the driver was polite and accommodating.",
        "rating": 5,
    },
    {
        "text": "The driver was friendly and professional, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic and made up for it with excellent service.",
        "rating": 4,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for places to eat.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, and the driver was unprofessional and rude.",
        "rating": 1,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and made the journey enjoyable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was not very talkative or engaging.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and accommodating, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a scenic route that was enjoyable.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was friendly and made me feel comfortable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, and the driver was professional and courteous.",
        "rating": 5,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for places to visit.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, and the driver was unprofessional and rude.",
        "rating": 1,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was professional and knowledgeable.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and made the journey enjoyable, but the taxi was old and uncomfortable.",
        "rating": 3,
    },
    {
        "text": "The taxi was clean and comfortable, but the driver was not very talkative or engaging.",
        "rating": 2,
    },
    {
        "text": "The driver was friendly and accommodating, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very friendly or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
    {
        "text": "The driver was knowledgeable about the area and took a direct route that saved me time and money.",
        "rating": 4,
    },
    {
        "text": "The taxi was well-maintained and had all the amenities I needed, but the driver was not very talkative or engaging.",
        "rating": 3,
    },
    {
        "text": "The driver was professional and courteous, and the taxi was modern and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was apologetic, but it was still frustrating.",
        "rating": 2,
    },
    {
        "text": "The driver was knowledgeable about the area and gave me some great recommendations for things to do.",
        "rating": 5,
    },
    {
        "text": "The taxi was old and uncomfortable, but the driver was friendly and made the journey enjoyable.",
        "rating": 3,
    },
    {
        "text": "The driver was polite and courteous, and the taxi was clean and well-maintained.",
        "rating": 4,
    },
    {
        "text": "The taxi was expensive but the driver was knowledgeable about the area and gave me some great recommendations for places to go.",
        "rating": 3,
    },
    {
        "text": "The driver was friendly and engaging, and the taxi was clean and comfortable.",
        "rating": 5,
    },
    {
        "text": "The taxi was late and the driver was unapologetic and unprofessional.",
        "rating": 1,
    },
]

reviews_by_rating = {}

for review in reviews:
    rating = review["rating"]
    text = review["text"]
    if rating not in reviews_by_rating:
        reviews_by_rating[rating] = [text]
    else:
        reviews_by_rating[rating].append(text)


def get_random_review(score):
    pos = random.randint(0, len(reviews_by_rating[score]) - 1)
    # print(pos, len(reviews_by_rating[score]))
    return (reviews_by_rating[score][pos], score)
