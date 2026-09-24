import json
with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for card in data[:4]:
    print("Card", card['no'])
    print("Desc:", card.get('description', '')[:50])
