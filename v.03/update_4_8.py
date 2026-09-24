import json

updates = {
    4: {
        "spiritual_meaning": "Pairing / Integrated Collaboration",
        "positive": "Guardian spirit of reincarnation / Sense of macro",
        "reverse": "Sense of isolation, separation from all that is great, sense of micro",
        "spiritual_level": "Unity in time and space",
        "daily_level": "Integration of beliefs",
        "description": "Two eternal souls with very similar harmonics combine to observe life forms in the dimension of Earth. At that time, each soul creates and exists as an Oversoul. The Oversoul knows that the 'time and space' in observation are a direct observation of the souls of themselves combined. It knows that all reincarnations are expressions of their own harmonics, and that they all exist simultaneously on linear time. In this state, the Oversoul reincarnates into each life as a way to integrate all observations. By setting one reincarnation as the primary timeline, it observes and directs other reincarnations from a single point of view of reality in this dimension. The crown chakra of the Oversoul is located at the point where the universe with 12 intelligences is connected. This is macro wisdom. In this state, the Oversoul connects with all that is great and accesses the intelligence of the Universal Mind. Awakened human beings who have reached enlightenment become a bridge connecting the hexagonal Akasha and the Universal Mind of 'creation' through the chakra system of the physical body. The letters drawn on this card represent alpha and omega, that is, the beginning and the end."
    },
    5: {
        "spiritual_meaning": "Manifestation of reality",
        "positive": "Dimension of home, starting point, zero point",
        "reverse": "Lack of determination to manifest intention, self-destruction, self-sabotage",
        "spiritual_level": "The moment of the beginning of creation",
        "daily_level": "Existing in the present moment without conflict",
        "description": "The role of the eternal unchanging soul is to observe creation in dimensions in preparation for becoming a creator itself. The soul first selects the dimensional world to reincarnate into, and dwells in a body that can merge with the energy of that star system. That star becomes the home for the eternal soul. The soul contrasts the reality of all other dimensions it has stayed in with the reality of this home. The soul's original harmonics appear in different forms in each star system, and 'all that is great' provides the opportunity to perfectly observe creation. The upper circle is the boundary of this universe, and the Flower of Life surrounded by the circle is the creation of this universe itself. The two pillars on both sides represent consciousness in universal reality. Above the left pillar is the combined symbol of masculinity and femininity, and above the right pillar is a single star. Sitting on top of the inverted triangle-shaped masculine symbol with time and space and consciousness attached is a pregnant female Buddha. This represents that the state at the moment of beginning and the evolving energy are equivalent. Inside the symbol, a man is drawn overlapping a pentagram. It symbolizes the intention of consciousness in the physical world to 'govern time and space'."
    },
    6: {
        "spiritual_meaning": "Joy and sorrow, intimacy, familiarity / nostalgia",
        "positive": "Integration, connection, inclusion, becoming companions, mixing together",
        "reverse": "Inappropriate union, division of agreement, isolation, anti-sociality, coldness",
        "spiritual_level": "Combined eternal soul forming a Twin Flame",
        "daily_level": "Requiring a strategic alliance",
        "description": "To reincarnate into a dimension with time and space, the soul needs to combine with another soul that has very similar harmonics. The dove bringing its face close to the center of the silver earth symbolizes this. Combining prevents the soul from falling into the pitfalls of the real world. The soul can safely return to the spiritual dimension. The man and woman are wearing beautiful costumes, and the youthful trumpeter announces their marriage. The wall is a symbol of the path they walk together in time and space. The Celtic knot ties together the dualistic aspects of 'joy and sorrow' that marriage will bring. This card also represents personal relationships between people. Intimacy plays an important role in human relationships, which are places for mutual energy exchange. Such sharing also applies to people who care for each other having shared past lives, or people who share something like having the same interests at present. Even in society, the expression 'to marry' is used with ideas, ideals, and causes raised by closely connected communities."
    },
    7: {
        "spiritual_meaning": "Awakened cooperative system, conscious partnership",
        "positive": "Cooperation, support, purpose",
        "reverse": "Reckless independence, egocentricity, disapproval, non-acceptance",
        "spiritual_level": "Selfless support",
        "daily_level": "Leader / Guide",
        "description": "When we come to Earth, we first pass through one of the 12 Logos. Then we combine with another soul to begin the primary reincarnation. The characteristics of the Logos we chose to pass through will also affect other reincarnations created by our Oversoul while we exist on Earth. Also, each time we reincarnate, the Oversoul selects beings to guide us in advance. The group of guides usually changes for each reincarnation, and consists of Earth-born soul beings, avatars, angelic beings, and elemental beings. These watchers, guardian beings, and helpers pilot us in various ways as we proceed together through the maze of time and space. They undoubtedly help us who live our lives reacting to our choices. Seven helpers surround a child standing on the maze. One of them represents the Logos passed through when coming to Earth. The four-axis wheel symbolizes purpose, and the three swirls symbolize the mission of the soul. That is to observe this world without prejudice through body, mind, and spirit. The symbol drawn below will open your consciousness to a meditative state where you can consciously interact with your guides."
    },
    8: {
        "spiritual_meaning": "Grounding, focused vision",
        "positive": "Strategy, goal, patience / result",
        "reverse": "Lack of resolution and motivation, lack of direction, short-sighted, rash and indiscreet, limited",
        "spiritual_level": "Patience / Endurance",
        "daily_level": "Strategy",
        "description": "The sensory consciousness of the human physical body has an urge to constantly continue to exist in time and space so that humanity can advance further. From a very young age, we are taught strategies for survival. And we continue to use those behavioral tactics throughout our lives. When the evolving spirit of humans, which is the sensory consciousness of the continuing physical body, discovers that it cannot survive without a soul, a very deep core conflict is born there. This core conflict is symbolized by the soul, represented by the Aztec figure in the center of the card, being connected to a human fetus. The two pyramids drawn with a comet flowing from the Pleiades to our solar system are the past and the future. The five palm trees are the five civilizations that have developed since the soul began to dwell in Earthly forms. This card is also a card of patience. The power to thrive even in adversity - the ability not to lose individual wisdom even when adversity blows in the environment or society. Having your feet firmly on the ground and not losing yourself can be said to be true patience."
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
print("Updated cards 4-8")
