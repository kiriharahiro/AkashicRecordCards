import json
import re

updates = {
    9: {
        "spiritual_meaning": "Power / Focus of intent",
        "positive": "Centered, aligned, focused, confident",
        "reverse": "Misguided use of power, scattered focus",
        "spiritual_level": "Manifestation through focused intent",
        "daily_level": "Directing life force energy",
        "description": "True power lies in the alignment of one's physical reality with the soul's divine intent. By focusing attention on a singular goal, energy flows without resistance. This card represents the channeling of universal life force to create tangible results in the physical dimension. When focused and grounded, human beings act as conduits for higher consciousness. This alignment empowers the individual to act decisively, bringing abstract ideas into material existence."
    },
    10: {
        "spiritual_meaning": "Transition / Evolution of consciousness",
        "positive": "Adaptability, embracing change, moving forward",
        "reverse": "Fear of the unknown, stagnation, clinging to the past",
        "spiritual_level": "Ascension of the soul",
        "daily_level": "Navigating life changes",
        "description": "Evolution requires the willingness to let go of old forms and embrace the new. The soul is constantly expanding through experiences in time and space. This card signifies a critical juncture where consciousness shifts to a higher frequency. It encourages embracing the unknown, trusting the guidance of the Oversoul, and allowing transformation to unfold naturally."
    },
    11: {
        "spiritual_meaning": "Balance / Cosmic harmony",
        "positive": "Equilibrium, fairness, centeredness, inner peace",
        "reverse": "Imbalance, extreme views, instability",
        "spiritual_level": "Alignment with universal law",
        "daily_level": "Creating stability in daily life",
        "description": "The universe operates on principles of perfect balance and harmony. To reflect this cosmic order, one must find equilibrium within. This card represents the integration of opposites—light and dark, masculine and feminine, action and stillness. Achieving inner harmony allows the soul to navigate the physical world with grace and wisdom."
    },
    12: {
        "spiritual_meaning": "Healing / Restoration of wholeness",
        "positive": "Recovery, self-care, renewal, clearing blockages",
        "reverse": "Ignoring pain, resisting healing, holding onto trauma",
        "spiritual_level": "Cleansing the energetic body",
        "daily_level": "Physical and emotional recovery",
        "description": "Healing is the process of returning to the original, perfect state of the soul. In the physical realm, trauma and dense energies can block the flow of life force. This card indicates a time for deep restoration. By releasing what no longer serves and allowing divine energy to permeate the body and mind, true wholeness can be reclaimed."
    },
    13: {
        "spiritual_meaning": "Illumination / Inner wisdom",
        "positive": "Clarity, insight, spiritual awakening, truth",
        "reverse": "Confusion, illusion, ignoring inner guidance",
        "spiritual_level": "Connecting with the higher mind",
        "daily_level": "Gaining understanding of a situation",
        "description": "When the veil of illusion is lifted, the soul's infinite wisdom shines through. Illumination is the sudden realization of spiritual truth that transcends the limitations of the physical mind. This card heralds a moment of clarity and expanded awareness. Trust the insights that arise from within, as they are direct communications from the Oversoul."
    },
    14: {
        "spiritual_meaning": "Creation / Birthing the new",
        "positive": "Creativity, inspiration, fertility, innovation",
        "reverse": "Creative block, lack of inspiration, barrenness",
        "spiritual_level": "Co-creating with the divine",
        "daily_level": "Starting a new project or phase",
        "description": "The impulse to create is a reflection of the Creator's nature. Every soul has the capacity to bring forth new forms and ideas into the physical world. This card signifies a fertile period where inspiration flows freely. It invites you to express your unique gifts and collaborate with universal energies to manifest your visions."
    },
    15: {
        "spiritual_meaning": "Connection / Web of life",
        "positive": "Interdependence, community, shared purpose, empathy",
        "reverse": "Isolation, feeling disconnected, self-absorption",
        "spiritual_level": "Recognizing the unity of all beings",
        "daily_level": "Building relationships and networks",
        "description": "All life is interconnected through an invisible web of energy. This card reminds us that we are not isolated individuals, but integral parts of a vast cosmic community. By fostering genuine connections and acting with empathy, we strengthen the collective consciousness and contribute to the harmonious evolution of all."
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
print("Updated cards 9-15")
