import json
import re
from deep_translator import MyMemoryTranslator

def contains_japanese(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', text))

with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translator = MyMemoryTranslator(source='japanese', target='english')
fields_to_translate = ['spiritual_meaning', 'positive', 'reverse', 'spiritual_level', 'daily_level', 'description']

print('Starting translation with MyMemoryTranslator (fixed)...')
for card in data:
    if not any(contains_japanese(card.get(f, '')) for f in fields_to_translate):
        continue
    
    print(f'Translating Card {card.get("no")}...')
    for field in fields_to_translate:
        val = card.get(field, '')
        if contains_japanese(val):
            try:
                translated = translator.translate(val)
                card[field] = translated
            except Exception as e:
                print(f'Error translating {field} for card {card.get("no")}: {e}')
                    
with open('cards_data_en.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print('Translation complete.')
