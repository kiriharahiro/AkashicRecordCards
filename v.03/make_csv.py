import json
import csv

with open('cards_data_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The columns based on typical usage in build_html_en.py
headers = ['no', 'theme_en', 'theme_ja', 'title_en', 'title_ja', 'spiritual_meaning', 'positive', 'reverse', 'spiritual_level', 'daily_level', 'description', 'url_positive', 'url_reverse']

with open('AkashicRecordCards_ENG.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for card in data:
        row = {h: card.get(h, '') for h in headers}
        writer.writerow(row)
