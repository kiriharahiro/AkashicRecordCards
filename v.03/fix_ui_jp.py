import codecs

with codecs.open('build_html_en.py', 'r', 'utf-8') as f:
    text = f.read()

replacements = {
    'title="ローカルデータ使用中"': 'title="Using Local Data"',
    'title="同期設定"': 'title="Sync Settings"',
    'id="panel-card-title">ゲートウェイ<': 'id="panel-card-title">Gateway<',
    'id="modal-title-ja">ゲートウェイ<': 'id="modal-title-ja">Gateway<',
    'id="modal-spiritual-meaning">変化の時。<': 'id="modal-spiritual-meaning">Time of change.<',
    'id="modal-meaning-pos">始まり。<': 'id="modal-meaning-pos">Beginning.<',
    'id="modal-meaning-rev">古い合意を破る。<': 'id="modal-meaning-rev">Breaking old agreements.<',
    'id="modal-description">ここに解説テキストが入ります。<': 'id="modal-description">Description text goes here.<',
    '"吸う (Inhale)"': '"Inhale"',
    '"止める (Hold)"': '"Hold"',
    '"吐く (Exhale)"': '"Exhale"',
    '"タイマーを再開"': '"Resume Timer"',
    '"タイマーを一時停止"': '"Pause Timer"',
    '（横向き配置）': '(Horizontal)',
    'HTTPエラー: ': 'HTTP Error: ',
    'レスポンスの形式が正しくありません。': 'Invalid response format.',
    'スプレッドシートのテーブルデータが見つかりません。': 'Spreadsheet table data not found.',
    "スプレッドシートに 'No' または '番号' 列が見つかりません。": "Spreadsheet is missing 'No' column.",
    '有効なカードデータが1件も取得できませんでした。': 'No valid card data retrieved.',
    'スプレッドシートSync Error:': 'Spreadsheet Sync Error:',
    'Connection Test中...': 'Connection Testing...'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with codecs.open('build_html_en.py', 'w', 'utf-8') as f:
    f.write(text)

print("Replaced all Japanese UI text")
