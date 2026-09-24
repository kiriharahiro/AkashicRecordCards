import json
with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for card in data:
    print(f"Card {card.get('no')}: {card.get('title_en')}")
    print(f"  Pos: {card.get('positive')}")
    print(f"  Rev: {card.get('reverse')}")
    print(f"  Desc: {card.get('description')}")
