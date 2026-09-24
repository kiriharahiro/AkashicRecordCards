import json

updates = {
    23: {
        "spiritual_meaning": "Intuition / Inner knowing",
        "positive": "Trusting your gut, clear perception, spiritual insight",
        "reverse": "Ignoring intuition, overthinking, clouded judgment",
        "spiritual_level": "Direct communication from the soul",
        "daily_level": "Making decisions based on inner feelings",
        "description": "Intuition is the language of the soul, bypassing the logical mind to deliver profound truths. This card encourages you to quiet the chatter of everyday life and listen to the subtle whispers within. By trusting your inner knowing, you align yourself with a higher perspective and navigate life's challenges with greater ease and accuracy."
    },
    24: {
        "spiritual_meaning": "Patience / Divine timing",
        "positive": "Endurance, calmness, trusting the process",
        "reverse": "Impatience, forcing outcomes, frustration",
        "spiritual_level": "Understanding the rhythm of the universe",
        "daily_level": "Waiting for the right moment to act",
        "description": "The universe unfolds according to its own perfect rhythm. This card reminds you that forcing things before their time often leads to resistance and unnecessary struggle. Practice patience and trust that everything is happening exactly when it is supposed to. Allow the seeds you have planted to grow at their own natural pace."
    },
    25: {
        "spiritual_meaning": "Forgiveness / Releasing the past",
        "positive": "Letting go of resentment, compassion, emotional freedom",
        "reverse": "Holding grudges, bitterness, being trapped by past hurts",
        "spiritual_level": "Dissolving karmic ties",
        "daily_level": "Healing relationships and finding peace",
        "description": "Forgiveness is a powerful act of self-healing. Holding onto anger and resentment only binds you to the past and lowers your vibrational frequency. This card asks you to release old wounds, not to condone the actions of others, but to free yourself from their energetic grip. By forgiving, you open your heart to unconditional love."
    },
    26: {
        "spiritual_meaning": "Authenticity / Living your truth",
        "positive": "Being genuine, speaking your truth, self-acceptance",
        "reverse": "Hiding your true self, trying to please others, wearing masks",
        "spiritual_level": "Expressing the soul's unique signature",
        "daily_level": "Honesty in actions and words",
        "description": "Your soul has a unique frequency that can only be expressed when you are truly authentic. This card urges you to drop the masks you wear for society and embrace your true self. When you live in alignment with your inner truth, you radiate a powerful light that inspires others to do the same."
    },
    27: {
        "spiritual_meaning": "Gratitude / Appreciating the now",
        "positive": "Thankfulness, joy, recognizing blessings",
        "reverse": "Taking things for granted, focusing on what is lacking",
        "spiritual_level": "Elevating your energetic vibration",
        "daily_level": "Finding beauty in everyday moments",
        "description": "Gratitude is one of the highest vibrational states you can embody. It acts as a magnet, drawing even more blessings into your life. This card reminds you to pause and appreciate the abundance that already surrounds you. By shifting your focus from what is lacking to what is present, you transform your reality instantly."
    },
    28: {
        "spiritual_meaning": "Resilience / Bouncing back",
        "positive": "Inner strength, overcoming adversity, adaptability",
        "reverse": "Giving up easily, feeling defeated, inflexibility",
        "spiritual_level": "The soul's enduring power",
        "daily_level": "Recovering from setbacks",
        "description": "Adversity is often the forge in which spiritual strength is tempered. This card represents your innate ability to recover from challenges and emerge even stronger. Trust in your resilience. Every setback is an opportunity for profound growth and a deeper understanding of your own indestructible nature."
    },
    29: {
        "spiritual_meaning": "Synchronicity / Meaningful coincidences",
        "positive": "Being in the flow, recognizing signs, universal alignment",
        "reverse": "Ignoring signs, feeling disconnected, random chaos",
        "spiritual_level": "The universe speaking directly to you",
        "daily_level": "Following the breadcrumbs of intuition",
        "description": "Synchronicity is the universe's way of confirming that you are on the right path. This card encourages you to pay attention to the seemingly random coincidences in your life. These are not accidents, but meaningful signs and guideposts from the higher realms. Stay open and receptive to the subtle messages being sent your way."
    },
    30: {
        "spiritual_meaning": "Surrender / Letting go of ego",
        "positive": "Humility, yielding to a higher power, spiritual release",
        "reverse": "Ego-driven actions, stubbornness, resisting the inevitable",
        "spiritual_level": "Aligning with the Divine Will",
        "daily_level": "Accepting things as they are",
        "description": "Surrender is not about giving up, but about relinquishing the ego's need to control. It is an act of profound trust in the intelligence of the universe. This card invites you to stop fighting against the current of your life. By letting go, you create space for miracles and solutions that the logical mind could never conceive."
    },
    31: {
        "spiritual_meaning": "Joy / The vibration of the soul",
        "positive": "Happiness, playfulness, lightness of being",
        "reverse": "Sorrow, taking life too seriously, heaviness",
        "spiritual_level": "Experiencing the natural state of spirit",
        "daily_level": "Finding pleasure in simple things",
        "description": "Joy is the natural state of the soul. It is a high-frequency energy that effortlessly dissolves fear and density. This card is a reminder to inject playfulness and laughter into your life. Don't take everything so seriously. By choosing joy, you elevate your consciousness and become a beacon of light for others."
    },
    32: {
        "spiritual_meaning": "Wisdom / Applied knowledge",
        "positive": "Deep understanding, good judgment, learning from experience",
        "reverse": "Repeating mistakes, foolishness, ignoring lessons",
        "spiritual_level": "Accessing the Akashic Records",
        "daily_level": "Making informed and thoughtful choices",
        "description": "Wisdom is the synthesis of knowledge and experience, illuminated by spiritual insight. This card suggests that you have gathered valuable lessons from your past. Now is the time to apply that deep understanding to your current situation. Trust your inner sage and draw upon the eternal wisdom stored within your soul."
    },
    33: {
        "spiritual_meaning": "Ascension / Rising to a new level",
        "positive": "Spiritual elevation, enlightenment, expanding consciousness",
        "reverse": "Stagnation, fear of growing, being held back",
        "spiritual_level": "Moving into higher dimensional awareness",
        "daily_level": "A significant breakthrough or milestone",
        "description": "Ascension is the ultimate goal of the soul's journey through time and space—a complete shift into a higher state of consciousness. This card indicates a major spiritual milestone. You are elevating your vibration and stepping into a more expanded version of yourself. Embrace this transformation with an open heart and a clear mind."
    }
}

with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for card in data:
    c_no = card.get('no')
    if c_no in updates:
        for k, v in updates[c_no].items():
            card[k] = v

with open('cards_data_en.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Updated cards 23-33")
