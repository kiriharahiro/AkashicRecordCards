import json

updates = {
    16: {
        "spiritual_meaning": "Trust / Surrender to the flow",
        "positive": "Faith, letting go of control, inner peace",
        "reverse": "Anxiety, micromanaging, lack of faith",
        "spiritual_level": "Yielding to divine timing",
        "daily_level": "Releasing stress and worry",
        "description": "True spiritual power often requires relinquishing the need to control every outcome. Trusting the universe allows you to flow with the natural currents of life rather than struggling against them. This card indicates a need to surrender your personal agenda and have faith that the Oversoul is orchestrating events for your highest good."
    },
    17: {
        "spiritual_meaning": "Reflection / The mirror of reality",
        "positive": "Self-awareness, introspection, recognizing projections",
        "reverse": "Denial, blaming others, lacking insight",
        "spiritual_level": "Understanding the external world as an internal reflection",
        "daily_level": "Taking responsibility for one's experiences",
        "description": "The physical world acts as a mirror, reflecting our inner state of consciousness. What we see in others and experience in life often highlights what needs attention within ourselves. This card urges you to look inward and realize that by shifting your internal beliefs and emotions, your external reality will transform accordingly."
    },
    18: {
        "spiritual_meaning": "Courage / Overcoming fear",
        "positive": "Bravery, taking risks, stepping into the unknown",
        "reverse": "Cowardice, being paralyzed by fear, playing it safe",
        "spiritual_level": "Trusting the soul's immortality",
        "daily_level": "Facing challenges head-on",
        "description": "Growth requires moving beyond the comfort zone. Fear is often an illusion created by the physical mind's instinct for survival. This card calls upon your innate courage to face the unknown. By trusting in your eternal nature, you can take bold steps forward and embrace the experiences your soul came here to have."
    },
    19: {
        "spiritual_meaning": "Abundance / Universal flow",
        "positive": "Prosperity, gratitude, recognizing limitless resources",
        "reverse": "Scarcity mindset, greed, feeling deprived",
        "spiritual_level": "Aligning with the frequency of plenty",
        "daily_level": "Experiencing material and emotional wealth",
        "description": "The universe is infinitely abundant, and there is more than enough for everyone. Scarcity is a limitation imposed by the mind. This card signifies a time to open yourself to receiving. By practicing gratitude and aligning with the frequency of abundance, you allow prosperity to flow freely into all areas of your life."
    },
    20: {
        "spiritual_meaning": "Transformation / The alchemy of soul",
        "positive": "Metamorphosis, shedding old skins, profound change",
        "reverse": "Resisting change, feeling stuck, painful transitions",
        "spiritual_level": "Transmuting dense energy into light",
        "daily_level": "Undergoing significant life shifts",
        "description": "Transformation is the alchemical process of turning the lead of dense human experience into the gold of spiritual wisdom. This card marks a period of profound metamorphosis. It requires releasing attachments to past identities and allowing the fire of transformation to burn away what is no longer needed, revealing your true essence."
    },
    21: {
        "spiritual_meaning": "Service / The path of the heart",
        "positive": "Compassion, selflessness, helping others, altruism",
        "reverse": "Martyrdom, self-neglect, acting from ego",
        "spiritual_level": "Recognizing the divine in all",
        "daily_level": "Contributing to the well-being of others",
        "description": "True service arises not from a sense of obligation, but from a deep recognition of our shared divinity. When we serve others from the heart, we align with the highest vibrations of love. This card encourages you to offer your gifts and energy to support the collective, while ensuring you also maintain your own energetic boundaries and well-being."
    },
    22: {
        "spiritual_meaning": "Integration / Bringing it all together",
        "positive": "Synthesis, wholeness, alignment of mind, body, and spirit",
        "reverse": "Fragmentation, disjointed efforts, feeling scattered",
        "spiritual_level": "Merging all aspects of the self",
        "daily_level": "Harmonizing different areas of life",
        "description": "Integration is the process of synthesizing all experiences, lessons, and aspects of the self into a cohesive whole. It is the realization that nothing is separate. This card suggests that you are entering a phase where the pieces of the puzzle are coming together. By harmonizing your thoughts, actions, and spiritual beliefs, you achieve a state of profound wholeness."
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
print("Updated cards 16-22")
