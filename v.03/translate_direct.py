import json
import urllib.request
import urllib.parse
import re
import time

def translate_text(text):
    if not isinstance(text, str) or not text.strip():
        return text
    # Only translate if it contains Japanese characters
    if not re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', text):
        return text
        
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=en&dt=t&q=" + urllib.parse.quote(text)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            translated = "".join([i[0] for i in result[0] if i[0]])
            return translated
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fields = ['spiritual_meaning', 'positive', 'reverse', 'spiritual_level', 'daily_level', 'description']

for card in data:
    c_no = card.get('no')
    if c_no < 9:
        continue
    print(f"Translating card {c_no}...")
    for field in fields:
        val = card.get(field, "")
        translated = translate_text(val)
        card[field] = translated
        time.sleep(0.1)

with open('cards_data_en.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Finished translation")
