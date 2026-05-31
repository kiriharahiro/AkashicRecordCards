import json
import os

# JSONデータを読み込む
json_path = r"C:\Users\kirih\.gemini\antigravity-ide\brain\3c0e395c-ab56-4959-8948-f9a5703b3e15\scratch\cards_data.json"
with open(json_path, 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# HTMLの大規模ベーステンプレート
html_template = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akashic Records Reading Board</title>
    <!-- Google Fonts の読み込み -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Noto+Sans+JP:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #05060b;
            --card-bg: rgba(13, 15, 30, 0.7);
            --border-color: rgba(212, 175, 55, 0.25);
            --gold: #d4af37;
            --gold-glow: rgba(212, 175, 55, 0.4);
            --purple: #8a2be2;
            --purple-glow: rgba(138, 43, 226, 0.4);
            --text-color: #f2f2f7;
            --text-muted: #9fa4bc;
            --inhale-color: #00d2ff;
            --hold-color: #ff9f00;
            --exhale-color: #8a2be2;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Noto Sans JP', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 50% 10%, rgba(20, 24, 60, 0.5) 0%, transparent 50%),
                radial-gradient(circle at 10% 80%, rgba(50, 15, 80, 0.3) 0%, transparent 40%),
                radial-gradient(circle at 90% 90%, rgba(10, 40, 70, 0.3) 0%, transparent 40%);
            background-attachment: fixed;
        }

        /* ヘッダー */
        header {
            text-align: center;
            padding: 15px 10px;
            border-bottom: 1px solid var(--border-color);
            background: rgba(5, 6, 11, 0.85);
            backdrop-filter: blur(15px);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        header h1 {
            font-family: 'Cinzel', serif;
            font-size: 1.5rem;
            color: var(--gold);
            letter-spacing: 3px;
            text-shadow: 0 0 10px var(--gold-glow);
        }

        header p {
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 3px;
            letter-spacing: 1px;
        }

        /* メインコンテンツ */
        main {
            flex: 1;
            padding: 15px;
            padding-bottom: 90px; /* ナビバーの余白 */
            max-width: 1000px;
            width: 100%;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
        }

        /* ナビゲーション */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 65px;
            background: rgba(8, 9, 18, 0.95);
            border-top: 1px solid var(--border-color);
            backdrop-filter: blur(20px);
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 9999;
            box-shadow: 0 -5px 30px rgba(0,0,0,0.6);
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.7rem;
            cursor: pointer;
            transition: all 0.3s ease;
            background: none;
            border: none;
            outline: none;
            width: 25%;
            height: 100%;
            justify-content: center;
            gap: 2px;
        }

        .nav-item.active {
            color: var(--gold);
            text-shadow: 0 0 10px var(--gold-glow);
            background: rgba(212,175,55,0.03);
        }

        .nav-icon {
            font-size: 1.3rem;
            transition: transform 0.3s ease;
        }
        
        .nav-item:hover .nav-icon {
            transform: scale(1.15);
        }

        /* 画面共通 */
        .app-view {
            display: none;
            animation: viewFadeIn 0.6s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
        }

        .app-view.active {
            display: block;
        }

        @keyframes viewFadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* パネル */
        .glass-panel {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 20px;
            backdrop-filter: blur(15px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            margin-bottom: 20px;
            position: relative;
        }

        .section-title {
            font-family: 'Cinzel', serif;
            color: var(--gold);
            font-size: 1.15rem;
            margin-bottom: 15px;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            letter-spacing: 2px;
            text-shadow: 0 0 5px var(--gold-glow);
        }

        /* 【新機能1】呼吸瞑想タイマースタイル */
        .breath-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 25px;
            padding: 20px 0;
        }

        .breath-circle-outer {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            border: 2px dashed rgba(255,255,255,0.15);
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            box-shadow: 0 0 30px rgba(0,0,0,0.4);
        }

        .breath-circle-inner {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(20,24,60,0.8) 0%, rgba(5,6,11,0.9) 100%);
            border: 2px solid var(--gold);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: all 1s ease;
            position: relative;
            z-index: 2;
            box-shadow: 0 0 20px var(--gold-glow);
        }

        .breath-ring-glow {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: transparent;
            border: 3px solid var(--inhale-color);
            transition: transform 1s ease, border-color 0.5s ease, opacity 0.5s ease;
            opacity: 0.3;
            transform: scale(0.6);
            pointer-events: none;
        }

        /* 呼吸フェーズ別のデザイン変化 */
        .breath-circle-inner.inhale {
            border-color: var(--inhale-color);
            box-shadow: 0 0 35px rgba(0, 210, 255, 0.4);
        }
        .breath-circle-inner.hold {
            border-color: var(--hold-color);
            box-shadow: 0 0 35px rgba(255, 159, 0, 0.4);
        }
        .breath-circle-inner.exhale {
            border-color: var(--exhale-color);
            box-shadow: 0 0 35px rgba(138, 67, 226, 0.4);
        }

        .breath-instruction {
            font-size: 1.1rem;
            font-weight: bold;
            color: #fff;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }

        .breath-timer {
            font-family: 'Cinzel', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--gold);
        }

        .breath-control-btn {
            background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%);
            color: #05060b;
            border: none;
            padding: 10px 24px;
            font-size: 0.9rem;
            font-weight: bold;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px var(--gold-glow);
        }

        .breath-control-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px var(--gold);
        }

        .sound-toggle-box {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 5px;
        }

        /* 瞑想画面の2カラムグリッド */
        .meditation-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        @media(min-width: 768px) {
            .meditation-grid {
                grid-template-columns: 1fr 1fr;
                align-items: start;
            }
        }

        /* 【新機能2-3】リーディング画面・スプレッドウィザード */
        .wizard-step {
            display: none;
            animation: fadeIn 0.4s ease forwards;
        }
        .wizard-step.active {
            display: block;
        }

        .wizard-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .card-picker-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(75px, 1fr));
            gap: 10px;
            max-height: 280px;
            overflow-y: auto;
            padding: 10px;
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 10px;
            background: rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }

        .picker-card-item {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 6px;
            padding: 5px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .picker-card-item:hover {
            border-color: var(--gold);
            background: rgba(212,175,55,0.08);
            box-shadow: 0 0 10px var(--gold-glow);
        }
        .picker-card-item.selected {
            border: 2.5px solid var(--gold);
            background: rgba(212,175,55,0.12);
            box-shadow: 0 0 15px var(--gold);
        }
        .picker-card-item img {
            width: 100%;
            height: 80px;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 4px;
        }
        .picker-card-item div {
            font-size: 0.65rem;
            color: #fff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* スプレッド選択カード型 */
        .spread-select-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 15px;
        }
        @media(min-width: 600px) {
            .spread-select-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        .spread-opt-box {
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .spread-opt-box:hover, .spread-opt-box.selected {
            border-color: var(--gold);
            background: rgba(212,175,55,0.06);
            box-shadow: 0 5px 20px var(--gold-glow);
        }
        .spread-opt-box h3 {
            font-size: 0.95rem;
            color: var(--gold);
            margin-bottom: 5px;
        }
        .spread-opt-box p {
            font-size: 0.75rem;
            color: var(--text-muted);
            line-height: 1.4;
        }

        /* シャッフルアニメーション */
        .shuffle-zone {
            width: 120px;
            height: 180px;
            position: relative;
            margin: 30px auto;
        }
        .shuffle-card-shadow {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #18192b 0%, #0c0d16 100%);
            border: 1.5px solid var(--gold);
            border-radius: 8px;
            position: absolute;
            top: 0;
            left: 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            transition: transform 0.4s ease;
        }

        /* シャッフル中の舞い踊る多方向アニメーション定義 */
        @keyframes shuffle-left {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(-45px, -10px) rotate(-12deg); }
        }
        @keyframes shuffle-right {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(45px, 10px) rotate(12deg); }
        }
        @keyframes shuffle-up {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(-10px, -25px) rotate(-6deg); }
        }
        @keyframes shuffle-down {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(10px, 25px) rotate(6deg); }
        }
        @keyframes shuffle-diagonal-1 {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(-25px, 20px) rotate(-8deg); }
        }
        @keyframes shuffle-diagonal-2 {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(25px, -20px) rotate(8deg); }
        }

        /* 【重要】タロットリーディングボード（スプレッドボード） */
        .spread-board {
            width: 100%;
            background: rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.03);
            border-radius: 16px;
            padding: 30px 15px;
            margin-top: 15px;
            position: relative;
            overflow-x: auto;
            min-height: 480px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* カードボード配置用ラッパー */
        .board-layout {
            position: relative;
            width: 100%;
            max-width: 600px;
            height: 460px;
            margin: 0 auto;
        }

        /* カードプレースホルダー（タロット置き場） */
        .card-slot {
            position: absolute;
            width: 80px;
            height: 120px;
            border-radius: 8px;
            perspective: 1000px;
            cursor: pointer;
            transition: all 0.3s ease;
            z-index: 10;
        }

        /* スロットのホバー効果 */
        .card-slot:hover {
            transform: scale(1.05);
            z-index: 20;
        }

        /* 空スロット（カードを置く枠） */
        .card-slot::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            border: 1.5px dashed var(--border-color);
            border-radius: 8px;
            background: rgba(255,255,255,0.01);
            transition: all 0.3s ease;
            z-index: 1;
        }
        .card-slot:hover::before {
            border-color: var(--gold);
            background: rgba(212,175,55,0.03);
        }

        /* スロット位置ラベル */
        .slot-label {
            position: absolute;
            bottom: -22px;
            left: -10px;
            right: -10px;
            text-align: center;
            font-size: 0.65rem;
            color: var(--text-muted);
            background: rgba(5,6,11,0.8);
            padding: 2px 4px;
            border-radius: 4px;
            border: 1px solid rgba(255,255,255,0.05);
            white-space: nowrap;
            z-index: 2;
            pointer-events: none;
        }
        .card-slot.active-selection::before {
            border: 2.5px solid var(--gold) !important;
            box-shadow: 0 0 20px var(--gold);
        }

        /* 3Dカードフリップ */
        .card-3d-wrapper {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
            z-index: 5;
        }
        .card-3d-wrapper.flipped {
            transform: rotateY(180deg);
        }

        .card-front-3d, .card-back-3d-play {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            border: 1.5px solid var(--border-color);
        }

        .card-back-3d-play {
            background: linear-gradient(135deg, #121324 0%, #05060b 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 2;
        }
        .card-back-3d-play::after {
            content: "★";
            color: var(--gold);
            font-size: 1.3rem;
            text-shadow: 0 0 5px var(--gold);
        }

        .card-front-3d {
            transform: rotateY(180deg);
            z-index: 1;
            overflow: hidden;
            background: #000;
        }
        .card-front-3d img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* 正逆位置のビジュアル表現（逆位置画像はデータベースに元から天地逆さまで用意されているため、二重反転を防ぐため回転は行いません） */
        .reversed-img img {
            display: block !important;
        }


        /* 障害（ブロック）の横向きスロット（90度回転） */
        .block-card-slot {
            transform: rotate(90deg);
        }
        .block-card-slot:hover {
            transform: rotate(90deg) scale(1.05);
        }
        .block-card-slot .slot-label {
            transform: rotate(-90deg);
            bottom: 40px;
            left: 85px;
        }

        /* 【重要】3大スプレッドの絶対位置配置 */

        /* 1. 一枚引きレイアウト */
        .layout-one .slot-self { top: 260px; left: calc(50% - 40px); }
        .layout-one .slot-theme { top: 80px; left: calc(50% - 40px); }

        /* 2. 四枚引きレイアウト（十字） */
        .layout-four .slot-self { top: 170px; left: calc(50% - 40px); }
        .layout-four .slot-block { top: 170px; left: calc(50% - 40px); } /* 重ねる(下側横向き) */
        .layout-four .slot-past { top: 170px; left: calc(50% - 150px); }
        .layout-four .slot-present { top: 170px; left: calc(50% + 70px); }
        .layout-four .slot-future { top: 20px; left: calc(50% - 40px); }

        /* 3. 九枚引きレイアウト（十字 + 右側縦スタック） */
        .layout-nine .slot-self { top: 170px; left: calc(50% - 90px); }
        .layout-nine .slot-block { top: 170px; left: calc(50% - 90px); } /* 重ねる */
        .layout-nine .slot-past { top: 170px; left: calc(50% - 200px); }
        .layout-nine .slot-present { top: 170px; left: calc(50% + 20px); }
        .layout-nine .slot-future { top: 20px; left: calc(50% - 90px); }

        /* 右側スタック(5〜9枚目) */
        .layout-nine .slot-level5 { top: 320px; left: calc(50% + 130px); } /* 内的葛藤 */
        .layout-nine .slot-level6 { top: 245px; left: calc(50% + 130px); } /* セルフイメージ */
        .layout-nine .slot-level7 { top: 170px; left: calc(50% + 130px); } /* 外側の葛藤 */
        .layout-nine .slot-level8 { top: 95px; left: calc(50% + 130px); }  /* 希望と恐れ */
        .layout-nine .slot-level9 { top: 20px; left: calc(50% + 130px); }  /* 最終結果 */

        /* リアルタイムリーディング詳細パネル */
        .reading-panel {
            background: rgba(10,12,24,0.85);
            border: 1.5px solid var(--gold);
            box-shadow: 0 0 25px rgba(212,175,55,0.15);
            border-radius: 14px;
            padding: 20px;
            margin-top: 20px;
            display: none;
            animation: fadeIn 0.4s ease forwards;
        }

        .reading-slot-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            margin-bottom: 12px;
        }
        .reading-slot-role {
            font-size: 0.8rem;
            color: var(--gold);
            font-weight: bold;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .reading-slot-desc {
            font-size: 0.75rem;
            color: var(--text-muted);
        }

        .reading-card-grid {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        @media(min-width: 600px) {
            .reading-card-grid {
                flex-direction: row;
                align-items: flex-start;
            }
        }
        .reading-card-img-box {
            width: 100px;
            height: 150px;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            flex-shrink: 0;
            background: #000;
        }
        .reading-card-img-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .reading-card-img-box.reversed-img img {
            /* データベースの画像がすでに逆位置用なので、二重反転を防ぐため回転は削除 */
        }
        .reading-card-info {
            flex: 1;
        }
        .reading-card-title {
            font-size: 1.15rem;
            font-weight: bold;
            color: #fff;
            margin-bottom: 5px;
        }
        .reading-badge-container {
            margin-bottom: 10px;
        }

        /* コモンコントロール */
        .form-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }
        @media(min-width: 600px) {
            .form-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .form-group label {
            font-size: 0.8rem;
            color: var(--gold);
            font-weight: bold;
        }
        .form-group select, .form-group input {
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 8px 12px;
            color: #fff;
            outline: none;
            font-size: 0.9rem;
        }
        .form-group select:focus {
            border-color: var(--gold);
            box-shadow: 0 0 10px var(--gold-glow);
        }

        /* トグル */
        .switch-container {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 3px;
        }
        .switch {
            position: relative;
            display: inline-block;
            width: 44px;
            height: 22px;
        }
        .switch input { opacity: 0; width: 0; height: 0; }
        .slider {
            position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
            background-color: #24143a; transition: .4s; border-radius: 22px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .slider:before {
            position: absolute; content: ""; height: 14px; width: 14px; left: 3px; bottom: 3px;
            background-color: var(--text-muted); transition: .4s; border-radius: 50%;
        }
        input:checked + .slider { background-color: var(--gold); }
        input:checked + .slider:before { transform: translateX(22px); background-color: #05060b; }
        .switch-label { font-size: 0.75rem; color: var(--text-muted); }

        /* カード図鑑・モーダル */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
            gap: 12px;
        }
        .grid-card-item {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        .grid-card-item:hover {
            transform: translateY(-4px);
            border-color: var(--gold);
            box-shadow: 0 5px 15px rgba(212,175,55,0.15);
        }
        .grid-card-img {
            width: 100%;
            height: 110px;
            border-radius: 5px;
            overflow: hidden;
            background: #000;
            margin-bottom: 6px;
        }
        .grid-card-img img { width: 100%; height: 100%; object-fit: cover; }
        .grid-card-no { font-size: 0.7rem; color: var(--gold); font-weight: bold; }
        .grid-card-title { font-size: 0.75rem; font-weight: bold; color: #fff; margin-top: 2px; }

        .search-bar { margin-bottom: 15px; }
        .search-bar input {
            width: 100%; background: rgba(255,255,255,0.03); border: 1px solid var(--border-color);
            border-radius: 20px; padding: 10px 18px; color: #fff; font-size: 0.9rem; outline: none;
        }
        .search-bar input:focus { border-color: var(--gold); box-shadow: 0 0 10px var(--gold-glow); }

        /* モーダル */
        .modal-overlay {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(5,6,11,0.95); z-index: 99999; display: none;
            justify-content: center; align-items: center; padding: 15px;
            backdrop-filter: blur(15px);
        }
        .modal-overlay.active { display: flex; }
        .modal-content {
            background: var(--card-bg); border: 1px solid var(--border-color);
            border-radius: 16px; max-width: 600px; width: 100%; padding: 25px;
            position: relative; box-shadow: 0 0 30px rgba(0,0,0,0.8);
            max-height: 90vh; overflow-y: auto;
        }
        .close-btn {
            position: absolute; top: 12px; right: 12px; background: transparent;
            border: none; color: var(--text-muted); font-size: 1.5rem; cursor: pointer;
        }
        .modal-grid { display: flex; flex-direction: column; gap: 20px; }
        @media(min-width: 600px) { .modal-grid { flex-direction: row; } }
        .modal-left { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
        .modal-card-img { width: 150px; height: 225px; border-radius: 10px; overflow: hidden; border: 1.5px solid var(--gold); }
        .modal-card-img img { width: 100%; height: 100%; object-fit: cover; }
        .modal-right { flex: 1; }
        .modal-header { border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-bottom: 10px; }
        .modal-card-no { color: var(--gold); font-size: 0.85rem; font-weight: bold; }
        .modal-card-title-ja { font-size: 1.3rem; font-weight: bold; color: #fff; }
        .modal-card-title-en { font-size: 0.9rem; color: var(--text-muted); }
        .modal-section { margin-bottom: 15px; }
        .modal-section-title { font-size: 0.85rem; font-weight: bold; color: var(--gold); border-left: 2.5px solid var(--gold); padding-left: 8px; margin-bottom: 5px; }
        .modal-text { font-size: 0.85rem; line-height: 1.5; color: var(--text-color); }

        .copyright-notice { text-align: center; font-size: 0.65rem; color: rgba(255,255,255,0.2); padding: 20px 10px; }
    </style>
</head>
<body>

    <!-- ヘッダー -->
    <header>
        <h1>Akashic Records Reading</h1>
        <p>〜 アカシックレコード 瞑想 ＆ カード・スプレッド 〜</p>
    </header>

    <!-- メインコンテンツ -->
    <main>

        <!-- 【画面1】瞑想準備 (🧘 Meditation) -->
        <div id="view-meditation" class="app-view active">
            <div class="meditation-grid">
                <!-- 呼吸瞑想パネル -->
                <div class="glass-panel" style="margin-bottom: 0;">
                    <h2 class="section-title">Preparation: Rhythmic Breathing</h2>
                    <div class="breath-wrapper">
                        <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); max-width: 480px; line-height: 1.5;">
                            セッションの前に「意図」を設定し、呼吸で肉体と意識の中立状態を作ります。<br>
                            <strong>吸う（7秒） ➔ 止める（5秒） ➔ 吐く（12秒）</strong><br>
                            チクタク音に合わせて1分間60拍の比率呼吸を一緒に行いましょう。
                        </p>
                        
                        <div class="breath-circle-outer">
                            <div class="breath-ring-glow" id="breath-glow"></div>
                            <div class="breath-circle-inner" id="breath-circle">
                                <span class="breath-instruction" id="breath-inst">Ready</span>
                                <span class="breath-timer" id="breath-count">0</span>
                            </div>
                        </div>

                        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                            <button class="breath-control-btn" id="breath-btn" onclick="toggleBreathing()">瞑想を開始する</button>
                            <div class="sound-toggle-box">
                                <input type="checkbox" id="sound-chk" checked>
                                <label for="sound-chk">秒針カウント音を鳴らす</label>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 10分セッション＆インテグレーションタイマーパネル -->
                <div class="glass-panel" style="margin-bottom: 0;">
                    <h2 class="section-title">Session & Integration Timer</h2>
                    <div class="breath-wrapper" style="gap: 15px;">
                        <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); max-width: 480px; line-height: 1.5;">
                            リーディング中の集中時間や、カードを引いた後の10分間の「統合瞑想（インテグレーション）」に使用します。<br>
                            10分経過するとアラームが鳴りますが、タイマーとセッションは終了せず継続します。
                        </p>
                        
                        <div style="font-family: 'Cinzel', serif; font-size: 3rem; font-weight: 700; color: var(--gold); text-shadow: 0 0 15px var(--gold-glow); letter-spacing: 2px;" id="session-timer-display">
                            10:00
                        </div>

                        <div style="display: flex; gap: 15px;">
                            <button class="breath-control-btn" id="session-timer-btn" onclick="toggleSessionTimer()">タイマーを開始</button>
                            <button class="breath-control-btn" style="background: transparent; border: 1px solid var(--border-color); color: #fff;" onclick="resetSessionTimer()">リセット</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="wizard-buttons" style="margin-top: 25px;">
                <button class="breath-control-btn" style="background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%); color:#05060b; width: 100%; max-width: 320px;" onclick="skipToReading()">リーディングルームへ入る ➔</button>
            </div>
        </div>

        <!-- 【画面2】リーディングボード (🔮 Reading) -->
        <div id="view-reading" class="app-view">
            <!-- ウィザード1: セルフカードの設定 -->
            <div id="step-self" class="glass-panel wizard-step active">
                <h2 class="section-title">Step 1: Select Self Card</h2>
                <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">
                    リーディングの「中心軸（中立）」となる、あなた自身（セルフ）のカードを選びます。
                </p>
                <div class="card-picker-grid" id="self-picker-grid">
                    <!-- オプションはJSで動的生成 -->
                </div>
                <div class="wizard-buttons">
                    <button class="breath-control-btn" style="background: transparent; border: 1px solid var(--border-color); color: #fff;" onclick="drawSelfRandom()">ランダムに引く</button>
                    <button class="breath-control-btn" onclick="nextToSpreadSelect()">次へ進む</button>
                </div>
            </div>

            <!-- ウィザード2: スプレッドの選択 -->
            <div id="step-spread" class="glass-panel wizard-step">
                <h2 class="section-title">Step 2: Choose Spread</h2>
                <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">
                    リーディングの意図に合わせて、スプレッドを選択します。
                </p>
                <div class="spread-select-grid">
                    <div class="spread-opt-box selected" id="opt-one" onclick="selectSpreadType('one')">
                        <h3>自分のための1枚引き</h3>
                        <p>今日のテーマを知るためのスプレッド。セルフカードの上に1枚展開します。</p>
                    </div>
                    <div class="spread-opt-box" id="opt-four" onclick="selectSpreadType('four')">
                        <h3>4枚スプレッド (洞察)</h3>
                        <p>現在の問題に深い洞察を得たい時。ブロック、過去の態度、今受ける影響、結果を展開。</p>
                    </div>
                    <div class="spread-opt-box" id="opt-nine" onclick="selectSpreadType('nine')">
                        <h3>9枚スプレッド (多次元)</h3>
                        <p>問題に対し、9つの異なる次元レベル（内的葛藤、セルフイメージ、外側の葛藤など）から影響を紐解きます。</p>
                    </div>
                </div>
                <div class="wizard-buttons">
                    <button class="breath-control-btn" style="background: transparent; border: 1px solid var(--border-color); color: #fff;" onclick="prevToSelfSelect()">戻る</button>
                    <button class="breath-control-btn" onclick="nextToShuffle()">次へ進む</button>
                </div>
            </div>

            <!-- ウィザード3: シャッフル ＆ カット -->
            <div id="step-shuffle" class="glass-panel wizard-step">
                <h2 class="section-title">Step 3: Shuffle & Cut</h2>
                <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted);">
                    意図を設定しながら、カードをシャッフルし、重ね合わせます。
                </p>
                <div class="shuffle-zone" id="shuffle-zone-el">
                    <div class="shuffle-card-shadow"></div>
                    <div class="shuffle-card-shadow"></div>
                    <div class="shuffle-card-shadow"></div>
                </div>
                <div class="wizard-buttons">
                    <button class="breath-control-btn" id="shuffle-act-btn" onclick="runShuffle()">シャッフルを行う</button>
                    <button class="breath-control-btn" id="draw-act-btn" style="display: none;" onclick="runDeal()">カードを配る（展開）</button>
                </div>
            </div>

            <!-- スプレッドボード本体 (カード展開エリア) -->
            <div id="reading-board-container" class="glass-panel" style="display: none;">
                <h2 class="section-title" id="board-title-display">Reading Board</h2>
                
                <div class="spread-board">
                    <div class="board-layout" id="board-layout-el">
                        <!-- ここにスロットが動的生成されます -->
                    </div>
                </div>

                <!-- リアルタイムリーディング詳細パネル -->
                <div class="reading-panel" id="reading-panel-el">
                    <div class="reading-slot-header">
                        <div class="reading-slot-role" id="panel-slot-role">障害・ブロック</div>
                        <div class="reading-slot-desc" id="panel-slot-desc">私をブロックしているものは何か？</div>
                    </div>
                    <div class="reading-card-grid">
                        <div class="reading-card-img-box" id="panel-card-img-box">
                            <img id="panel-card-img" src="" alt="Card">
                        </div>
                        <div class="reading-card-info">
                            <div class="reading-card-title" id="panel-card-title">ゲートウェイ</div>
                            <div class="reading-badge-container">
                                <span class="position-badge badge-positive" id="panel-pos-badge">正位置</span>
                                <span id="panel-levels"></span>
                            </div>
                            <div class="card-meaning-box" id="panel-meaning-box" style="margin-top: 5px; margin-bottom: 10px;">
                                <div class="card-meaning-title" id="panel-meaning-title">メッセージ</div>
                                <div id="panel-card-meaning">意味</div>
                            </div>
                            <div class="modal-section-title" style="margin-top: 10px; font-size: 0.8rem;">詳細解説</div>
                            <div class="modal-text" id="panel-card-desc" style="font-size: 0.8rem; line-height: 1.4; max-height: 120px; overflow-y: auto;">
                                解説文
                            </div>
                        </div>
                    </div>
                </div>

                <div class="wizard-buttons" style="margin-top: 20px;">
                    <button class="breath-control-btn" style="background: transparent; border: 1px solid var(--border-color); color: #fff;" onclick="resetReadingSession()">もう一度リーディングを行う</button>
                </div>
            </div>
        </div>

        <!-- 【画面3】手動入力画面 (📝 Entry) -->
        <div id="view-entry" class="app-view">
            <div class="glass-panel" style="max-width: 600px; margin-left: auto; margin-right: auto;">
                <h2 class="section-title">Manual Slot Setting</h2>
                <p style="text-align: center; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 15px;">
                    スプレッド位置に任意のカードをマニュアル配置してリーディングの確認ができます。
                </p>
                <div class="form-grid" style="grid-template-columns: 1fr; gap: 15px;">
                    <div class="form-group">
                        <label for="manual-spread-select">展開するスプレッド</label>
                        <select id="manual-spread-select" onchange="adjustManualFormFields()">
                            <option value="one">自分のための1枚引き</option>
                            <option value="four">4枚スプレッド (洞察)</option>
                            <option value="nine">9枚スプレッド (多次元)</option>
                        </select>
                    </div>

                    <!-- スロット設定リスト（JSで動的生成） -->
                    <div id="manual-slots-container" style="display: flex; flex-direction: column; gap: 15px;">
                        <!-- ここにスロットごとのドロップダウン＆トグルが追加されます -->
                    </div>

                    <button class="draw-btn apply-btn" style="margin-top: 15px;" onclick="applyManualReading()">この設定でスプレッドボードに展開</button>
                </div>
            </div>
        </div>

        <!-- 【画面4】カード一覧 (📖 Cards) -->
        <div id="view-records" class="app-view">
            <div class="glass-panel">
                <h2 class="section-title">Akashic Records Cards</h2>
                
                <!-- 検索窓 -->
                <div class="search-bar">
                    <input type="text" id="search-input" placeholder="カード番号、タイトル、霊的意義で検索..." oninput="filterCards()">
                </div>

                <!-- グリッド表示 -->
                <div class="cards-grid" id="cards-grid-container">
                    <!-- JSで動的生成 -->
                </div>
            </div>
        </div>

        <!-- 著作権の注意書き（下部） -->
        <div class="copyright-notice">
            注意：アカシックレコードカードの著作権はゲリー・ボーネル氏が保有しています。<br>
            当アプリは個人利用・研究目的で作成されたものであり、営利目的での無断転載・配布は固く禁じられています。
        </div>

    </main>

    <!-- モーダル詳細画面 -->
    <div class="modal-overlay" id="card-modal" onclick="closeModal(event)">
        <div class="modal-content">
            <button class="close-btn" onclick="closeModalDirect()">&times;</button>
            <div class="modal-grid">
                
                <div class="modal-left">
                    <div class="modal-card-img">
                        <img id="modal-img" src="" alt="Card Detail">
                    </div>
                </div>

                <div class="modal-right">
                    <div class="modal-header">
                        <div class="modal-card-no" id="modal-no">No. 1</div>
                        <div class="modal-card-title-ja" id="modal-title-ja">ゲートウェイ</div>
                        <div class="modal-card-title-en" id="modal-title-en">Gateway</div>
                    </div>

                    <div class="modal-section">
                        <div class="modal-section-title">霊的意義</div>
                        <div class="modal-text" id="modal-spiritual-meaning">変化の時。</div>
                    </div>

                    <div class="modal-section" id="modal-levels-container">
                        <!-- レベルバッジ -->
                    </div>

                    <div class="modal-section">
                        <div class="modal-section-title">正位置の意味</div>
                        <div class="modal-text" id="modal-meaning-pos">始まり。</div>
                    </div>

                    <div class="modal-section">
                        <div class="modal-section-title">逆位置の意味</div>
                        <div class="modal-text" id="modal-meaning-rev">古い合意を破る。</div>
                    </div>

                    <div class="modal-section">
                        <div class="modal-section-title">詳細な解説</div>
                        <div class="modal-text" id="modal-description">ここに解説テキストが入ります。</div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- ボトムナビゲーション -->
    <nav class="bottom-nav">
        <button class="nav-item active" onclick="switchView('meditation', this)">
            <span class="nav-icon">🧘</span>
            <span>Meditation</span>
        </button>
        <button class="nav-item" onclick="switchView('reading', this)">
            <span class="nav-icon">🔮</span>
            <span>Reading</span>
        </button>
        <button class="nav-item" onclick="switchView('entry', this)">
            <span class="nav-icon">📝</span>
            <span>Entry</span>
        </button>
        <button class="nav-item" onclick="switchView('records', this)">
            <span class="nav-icon">📖</span>
            <span>Cards</span>
        </button>
    </nav>

    <!-- JavaScript 処理 -->
    <script>
        // アカシックレコードカードのデータベース
        const CARDS_DATA = cards_json_placeholder;


        // プレビュー直リンク自動変換関数
        function getDirectImageUrl(driveUrl, isPositive = true) {
            if (!driveUrl) return "";
            let id = "";
            const matches = driveUrl.match(/\/d\/([a-zA-Z0-9_-]+)/);
            if (matches && matches[1]) {
                id = matches[1];
            } else {
                const urlParts = driveUrl.split('?');
                if (urlParts.length > 1) {
                    const urlParams = new URLSearchParams(urlParts[1]);
                    id = urlParams.get('id');
                }
            }
            if (id) {
                return `https://lh3.googleusercontent.com/d/${id}`;
            }
            return driveUrl;
        }

        // 読点「。」で改行して読みやすくするフォーマット関数
        function formatDescription(text) {
            if (!text) return "";
            return text.replace(/。/g, "。<br>");
        }

        // 指定した要素まで、指定した時間(ms)をかけてゆっくりスクロールする関数
        function slowScrollTo(element, duration = 725, forceFast = false) {
            const targetPosition = element.getBoundingClientRect().top + window.pageYOffset - 80; // ヘッダーの高さ等を考慮
            const startPosition = window.pageYOffset;
            const distance = targetPosition - startPosition;
            let startTime = null;

            function animation(currentTime) {
                if (startTime === null) startTime = currentTime;
                const timeElapsed = currentTime - startTime;
                const run = ease(timeElapsed, startPosition, distance, duration, forceFast);
                window.scrollTo(0, run);
                if (timeElapsed < duration) {
                    requestAnimationFrame(animation);
                } else {
                    window.scrollTo(0, targetPosition);
                }
            }

            // カスタムイージング関数
            function ease(t, b, c, d, forceFast = false) {
                if (forceFast) {
                    // 最初から4倍の高速スクロール
                    const p = Math.min(1, t / d);
                    return b + c * p;
                }
                const t1 = 300; // 前半のカットオフ時間 (0.3秒)
                let y;
                if (t < t1) {
                    // 最初の0.3秒間：前回のゆっくりした速度の2倍で加速
                    y = 0.15 * (t / t1) * (t / t1);
                } else {
                    // 0.3秒後：一気に4倍速で残りの85%をスクロール
                    const p2 = (t - t1) / (d - t1);
                    y = 0.15 + 0.85 * Math.min(1, p2);
                }
                return b + c * y;
            }

            requestAnimationFrame(animation);
        }

        // ==========================================
        // 【新機能1】比率呼吸タイマーの実装
        // ==========================================
        let breathState = {
            isRunning: false,
            phase: 'ready', // ready, inhale, hold, exhale
            count: 0,
            intervalId: null
        };
        let audioCtx = null;

        function playMetronomeTick() {
            if (!document.getElementById('sound-chk').checked) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                // フェーズごとに周波数を微変させる（チク・タク）
                if (breathState.phase === 'hold') {
                    osc.frequency.value = 600;
                } else if (breathState.phase === 'inhale') {
                    osc.frequency.value = 900;
                } else {
                    osc.frequency.value = 450;
                }
                
                gain.gain.setValueAtTime(0.015, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.04);
                
                osc.start();
                osc.stop(audioCtx.currentTime + 0.05);
            } catch (e) {
                console.error(e);
            }
        }

        function toggleBreathing() {
            const btn = document.getElementById('breath-btn');
            const circle = document.getElementById('breath-circle');
            const glow = document.getElementById('breath-glow');
            const inst = document.getElementById('breath-inst');
            const countEl = document.getElementById('breath-count');

            if (breathState.isRunning) {
                // 停止処理
                clearInterval(breathState.intervalId);
                breathState.isRunning = false;
                breathState.phase = 'ready';
                btn.textContent = "瞑想を開始する";
                circle.className = "breath-circle-inner";
                glow.style.transform = "scale(0.6)";
                glow.style.opacity = "0.3";
                inst.textContent = "Ready";
                countEl.textContent = "0";
            } else {
                // 開始処理
                breathState.isRunning = true;
                btn.textContent = "瞑想を一時停止";
                
                // 最初の呼吸サイクル開始 (吸う)
                startBreathPhase('inhale');
                
                breathState.intervalId = setInterval(() => {
                    breathState.count++;
                    playMetronomeTick();
                    
                    let phaseMax = 7;
                    if (breathState.phase === 'inhale') phaseMax = 7;
                    else if (breathState.phase === 'hold') phaseMax = 5;
                    else if (breathState.phase === 'exhale') phaseMax = 12;

                    countEl.textContent = breathState.count;

                    // アニメーションリングの脈動調整
                    if (breathState.phase === 'inhale') {
                        const progress = breathState.count / 7;
                        glow.style.transform = `scale(${0.6 + progress * 0.45})`;
                        glow.style.opacity = `${0.3 + progress * 0.6}`;
                    } else if (breathState.phase === 'exhale') {
                        const progress = breathState.count / 12;
                        glow.style.transform = `scale(${1.05 - progress * 0.45})`;
                        glow.style.opacity = `${0.9 - progress * 0.6}`;
                    }

                    if (breathState.count >= phaseMax) {
                        // 次のフェーズへ移行
                        if (breathState.phase === 'inhale') {
                            startBreathPhase('hold');
                        } else if (breathState.phase === 'hold') {
                            startBreathPhase('exhale');
                        } else if (breathState.phase === 'exhale') {
                            startBreathPhase('inhale');
                        }
                    }
                }, 1000);
            }
        }

        function startBreathPhase(phase) {
            breathState.phase = phase;
            breathState.count = 0;
            
            const circle = document.getElementById('breath-circle');
            const glow = document.getElementById('breath-glow');
            const inst = document.getElementById('breath-inst');
            const countEl = document.getElementById('breath-count');

            circle.className = `breath-circle-inner ${phase}`;
            countEl.textContent = "0";

            if (phase === 'inhale') {
                inst.textContent = "吸う (Inhale)";
                glow.style.borderColor = "var(--inhale-color)";
                glow.style.transform = "scale(0.6)";
                glow.style.opacity = "0.3";
            } else if (phase === 'hold') {
                inst.textContent = "止める (Hold)";
                glow.style.borderColor = "var(--hold-color)";
                glow.style.transform = "scale(1.05)";
                glow.style.opacity = "0.9";
            } else if (phase === 'exhale') {
                inst.textContent = "吐く (Exhale)";
                glow.style.borderColor = "var(--exhale-color)";
                glow.style.transform = "scale(1.05)";
                glow.style.opacity = "0.9";
            }
        }

        function skipToReading() {
            if (breathState.isRunning) {
                toggleBreathing(); // タイマー停止
            }
            switchView('reading', document.querySelectorAll('.nav-item')[1]);
        }

        // ==========================================
        // 【新機能】10分セッション＆インテグレーションタイマーの実装
        // ==========================================
        let sessionTimer = {
            isRunning: false,
            duration: 600, // 10分 (600秒)
            timeLeft: 600,
            intervalId: null,
            alarmIntervalId: null,
            isAlarming: false
        };

        function updateSessionTimerDisplay() {
            const display = document.getElementById('session-timer-display');
            const absTime = Math.abs(sessionTimer.timeLeft);
            const mins = Math.floor(absTime / 60);
            const secs = absTime % 60;
            const sign = sessionTimer.timeLeft < 0 ? "-" : "";
            
            const minsStr = String(mins).padStart(2, '0');
            const secsStr = String(secs).padStart(2, '0');
            
            display.textContent = `${sign}${minsStr}:${secsStr}`;
            
            // アラーム鳴動中は赤とゴールドで点滅表示
            if (sessionTimer.isAlarming) {
                display.style.color = (secs % 2 === 0) ? "#ff4757" : "var(--gold)";
            } else {
                display.style.color = "var(--gold)";
            }
        }

        function toggleSessionTimer() {
            const btn = document.getElementById('session-timer-btn');
            if (sessionTimer.isRunning) {
                // 一時停止
                clearInterval(sessionTimer.intervalId);
                sessionTimer.isRunning = false;
                btn.textContent = "タイマーを再開";
                btn.style.background = "linear-gradient(135deg, var(--gold) 0%, #b8860b 100%)";
                
                if (sessionTimer.isAlarming) {
                    stopAlarmSound();
                }
            } else {
                // 開始
                sessionTimer.isRunning = true;
                btn.textContent = "タイマーを一時停止";
                btn.style.background = "linear-gradient(135deg, #e74c3c 0%, #c0392b 100%)";
                
                initAudioContext();
                
                sessionTimer.intervalId = setInterval(() => {
                    sessionTimer.timeLeft--;
                    updateSessionTimerDisplay();
                    
                    if (sessionTimer.timeLeft === 0) {
                        startAlarmSound();
                    }
                }, 1000);
            }
        }

        function resetSessionTimer() {
            clearInterval(sessionTimer.intervalId);
            stopAlarmSound();
            
            sessionTimer.isRunning = false;
            sessionTimer.timeLeft = 600;
            
            const btn = document.getElementById('session-timer-btn');
            btn.textContent = "タイマーを開始";
            btn.style.background = "linear-gradient(135deg, var(--gold) 0%, #b8860b 100%)";
            
            updateSessionTimerDisplay();
        }

        function initAudioContext() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        function startAlarmSound() {
            if (sessionTimer.isAlarming) return;
            sessionTimer.isAlarming = true;
            
            let alarmCount = 0;
            // 最初の2回（1秒目と2秒目）は「ピピッ、ピピッ」、その後（3秒目以降）は1秒サイクルで「ピッ」と鳴る
            sessionTimer.alarmIntervalId = setInterval(() => {
                alarmCount++;
                if (alarmCount <= 2) {
                    playBeep(880, 0.08);
                    setTimeout(() => {
                        playBeep(880, 0.08);
                    }, 120);
                } else {
                    playBeep(880, 0.08);
                }
            }, 1000);
        }

        function playBeep(freq, duration) {
            try {
                initAudioContext();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.frequency.value = freq;
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch (e) {
                console.error("Alarm beep error:", e);
            }
        }

        function stopAlarmSound() {
            if (!sessionTimer.isAlarming) return;
            sessionTimer.isAlarming = false;
            clearInterval(sessionTimer.alarmIntervalId);
            document.getElementById('session-timer-display').style.color = "var(--gold)";
        }

        // ==========================================
        // 【新機能2-3】リーディングセッションウィザード＆スプレッド
        // ==========================================
        let sessionState = {
            selfCardNo: null,
            spreadType: 'one', // one, four, nine
            cardsInPlay: [],   // スロットごとの { role, card, isPositive } のリスト
            revealedSlots: {}, // めくられたスロットの真偽値
            scrollCount: 0     // スクロール回数のカウント
        };

        // スロット役割定義
        const SLOT_ROLES = {
            one: [
                { id: 'self', label: 'セルフカード (中立)', desc: 'あなたの現在の状態・意識のニュートラルな中心点' },
                { id: 'theme', label: '今日のテーマ', desc: 'あなたが今日意識を向けるべきテーマ、霊的使命' }
            ],
            four: [
                { id: 'self', label: 'セルフカード (中立)', desc: 'あなたの現在の状態・他のカードからの基準点' },
                { id: 'block', label: 'ブロック・障害', desc: '私をブロックしているものは何か？（横向き配置）' },
                { id: 'past', label: '過去の態度', desc: 'この問題は、これまでの私の人生にどんな影響をもたらしたか？' },
                { id: 'present', label: '今すぐ受ける影響', desc: 'この問題に対して、今すぐ私にどんな準備が用意されているか？' },
                { id: 'future', label: '最も起こりうる結果', desc: 'この瞬間の意図から、今後もたらされる蓋然性の高い展開' }
            ],
            nine: [
                { id: 'self', label: 'セルフカード (中立)', desc: 'あなたの現在の状態・意識の中心軸' },
                { id: 'block', label: 'ブロック・障害', desc: '私をブロックしているものは何か？（横向き配置）' },
                { id: 'past', label: '過去の態度', desc: 'この問題は、これまでの私の人生にどんな影響をもたらしたか？' },
                { id: 'present', label: '今すぐ受ける影響', desc: 'この問題に対して、今すぐ私にどんな影響がもたらされているか？' },
                { id: 'future', label: '最も起こりうる結果', desc: 'このまま進んだ際に、最も起こりうる結果' },
                { id: 'level5', label: '深い内的葛藤', desc: '問題の奥底にある、あなた自身の当面の心配・懸念事項' },
                { id: 'level6', label: 'セルフイメージ', desc: 'あなた自身が自分をどのように認識しているか？' },
                { id: 'level7', label: '外側の葛藤', desc: '外部や環境から、どのようなネガティブな影響を受けているか？' },
                { id: 'level8', label: '希望と恐れ', desc: '展開していく状況に対して、あなたが期待し、恐れていることは何か？' },
                { id: 'level9', label: '最終的な結果', desc: 'すべての気づきを経て辿り着く、最終的な結論と解放' }
            ]
        };

        // セルフカード選択肢の描画
        function renderSelfPicker() {
            const grid = document.getElementById('self-picker-grid');
            grid.innerHTML = "";
            CARDS_DATA.forEach(card => {
                const item = document.createElement('div');
                item.className = 'picker-card-item';
                if (sessionState.selfCardNo === card.no) item.classList.add('selected');
                
                item.onclick = () => {
                    document.querySelectorAll('.picker-card-item').forEach(el => el.classList.remove('selected'));
                    item.classList.add('selected');
                    sessionState.selfCardNo = card.no;
                };

                item.innerHTML = `
                    <img src="${getDirectImageUrl(card.url_positive)}" alt="${card.theme_ja}" loading="lazy">
                    <div>${card.no}. ${card.theme_ja}</div>
                `;
                grid.appendChild(item);
            });
        }

        function drawSelfRandom() {
            const count = CARDS_DATA.length;
            const idx = Math.floor(Math.random() * count);
            const card = CARDS_DATA[idx];
            sessionState.selfCardNo = card.no;
            
            renderSelfPicker();
            // スクロールで選択位置へ
            const items = document.querySelectorAll('.picker-card-item');
            if (items[idx]) {
                items[idx].scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }

        // ウィザード移動
        function nextToSpreadSelect() {
            if (!sessionState.selfCardNo) {
                alert("セルフカードを1枚選んでください（またはランダムに引くボタンを押してください）");
                return;
            }
            document.getElementById('step-self').classList.remove('active');
            document.getElementById('step-spread').classList.add('active');
        }

        function prevToSelfSelect() {
            document.getElementById('step-spread').classList.remove('active');
            document.getElementById('step-self').classList.add('active');
        }

        function selectSpreadType(type) {
            sessionState.spreadType = type;
            document.querySelectorAll('.spread-opt-box').forEach(el => el.classList.remove('selected'));
            document.getElementById(`opt-${type}`).classList.add('active');
            document.getElementById(`opt-${type}`).classList.add('selected');
        }

        function nextToShuffle() {
            document.getElementById('step-spread').classList.remove('active');
            document.getElementById('step-shuffle').classList.add('active');
            
            // ボタンリセット
            document.getElementById('shuffle-act-btn').style.display = 'inline-block';
            document.getElementById('shuffle-act-btn').textContent = "シャッフルを行う";
            document.getElementById('draw-act-btn').style.display = 'none';

            // スプレッドの種類に応じた枚数のカードをシャッフル用に動的生成
            const zone = document.getElementById('shuffle-zone-el');
            zone.innerHTML = "";

            let cardCount = 2; // デフォルト 1枚引き (テーマ1 + セルフ1)
            if (sessionState.spreadType === 'four') cardCount = 5; // 4枚 + セルフ1
            else if (sessionState.spreadType === 'nine') cardCount = 10; // 9枚 + セルフ1

            for (let i = 0; i < cardCount; i++) {
                const cardEl = document.createElement('div');
                cardEl.className = 'shuffle-card-shadow';
                // わずかに角度をずらして重ねることで、束になっている雰囲気を出します
                cardEl.style.transform = `translate(0, 0) rotate(${ (i - (cardCount - 1) / 2) * 1.5 }deg)`;
                cardEl.style.zIndex = i + 1;
                zone.appendChild(cardEl);
            }
        }

        function runShuffle() {
            const zone = document.getElementById('shuffle-zone-el');
            zone.classList.add('shuffling');
            
            const btn = document.getElementById('shuffle-act-btn');
            btn.disabled = true;
            btn.textContent = "シャッフル中...";

            // 動的生成された各シャッフルカードに異なる動きと時間差(ディレイ)を与える
            const cards = zone.querySelectorAll('.shuffle-card-shadow');
            const anims = ['shuffle-left', 'shuffle-right', 'shuffle-up', 'shuffle-down', 'shuffle-diagonal-1', 'shuffle-diagonal-2'];
            
            cards.forEach((card, idx) => {
                const animName = anims[idx % anims.length];
                const duration = 0.4 + (idx * 0.03); // 速度をわずかにばらけさせる
                const delay = idx * 0.05; // 段階的なディレイで束がほどけるように動く
                card.style.animation = `${animName} ${duration}s infinite alternate ease-in-out ${delay}s`;
            });

            // チクタク音をシャッフル中高速で鳴らす
            let count = 0;
            const metInterval = setInterval(() => {
                playMetronomeTick();
                count++;
                if (count > 6) clearInterval(metInterval);
            }, 250);

            setTimeout(() => {
                zone.classList.remove('shuffling');
                // シャッフル終了後にアニメーションをクリアして、綺麗に束ねる
                cards.forEach((card, idx) => {
                    card.style.animation = "";
                    card.style.transform = `translate(0, 0) rotate(${ (idx - (cards.length - 1) / 2) * 1.5 }deg)`;
                });

                btn.style.display = 'none';
                btn.disabled = false;
                
                const dealBtn = document.getElementById('draw-act-btn');
                dealBtn.style.display = 'inline-block';
                dealBtn.textContent = "カードを配る (展開する)";
            }, 2000);
        }

        // カードを場に展開する
        function runDeal() {
            document.getElementById('step-shuffle').classList.remove('active');
            document.getElementById('reading-board-container').style.display = 'block';

            // ボードタイトルの変更
            const titleEl = document.getElementById('board-title-display');
            if (sessionState.spreadType === 'one') titleEl.textContent = "自分のための1枚引き (テーマ)";
            else if (sessionState.spreadType === 'four') titleEl.textContent = "四枚スプレッド (問題への深い洞察)";
            else if (sessionState.spreadType === 'nine') titleEl.textContent = "九枚スプレッド (多次元レベル)";

            // 1. スプレッド用のカードを決定（セルフカードを除外してシャッフル）
            const pool = CARDS_DATA.filter(c => c.no !== sessionState.selfCardNo);
            const shuffledPool = [...pool].sort(() => Math.random() - 0.5);

            const slots = SLOT_ROLES[sessionState.spreadType];
            sessionState.cardsInPlay = [];
            sessionState.revealedSlots = {};

            let poolIdx = 0;
            slots.forEach(slot => {
                if (slot.id === 'self') {
                    // セルフカードは正位置固定（中立）
                    sessionState.cardsInPlay.push({
                        role: slot.id,
                        label: slot.label,
                        desc: slot.desc,
                        card: CARDS_DATA.find(c => c.no === sessionState.selfCardNo),
                        isPositive: true
                    });
                    // セルフカードは最初から表向き
                    sessionState.revealedSlots['self'] = true;
                } else {
                    const pickedCard = shuffledPool[poolIdx++];
                    const isPositive = Math.random() >= 0.5;
                    sessionState.cardsInPlay.push({
                        role: slot.id,
                        label: slot.label,
                        desc: slot.desc,
                        card: pickedCard,
                        isPositive: isPositive
                    });
                    sessionState.revealedSlots[slot.id] = false;
                }
            });

            // 2. ボードの描画
            renderReadingBoard();
            
            // 3. 最初は自動的にセルフカードを選択状態にする（自動スクロールはさせない）
            selectSlotForReading('self', false);
        }

        // リーディングボードのHTML構築
        function renderReadingBoard() {
            const board = document.getElementById('board-layout-el');
            board.innerHTML = "";

            // レイアウトクラスの設定
            const boardContainer = document.getElementById('reading-board-container');
            const boardLayout = document.getElementById('board-layout-el');
            boardLayout.className = `board-layout layout-${sessionState.spreadType}`;

            sessionState.cardsInPlay.forEach(item => {
                const slot = document.createElement('div');
                
                // ブロックカードは横向きクラスを付与
                let isBlock = item.role === 'block';
                slot.className = `card-slot slot-${item.role} ${isBlock ? 'block-card-slot' : ''}`;
                slot.onclick = () => {
                    // めくられていなければめくる
                    if (!sessionState.revealedSlots[item.role]) {
                        revealCardSlot(item.role);
                    }
                    selectSlotForReading(item.role);
                };

                const imgUrl = getDirectImageUrl(item.isPositive ? item.card.url_positive : item.card.url_reverse, item.isPositive);
                const isRevealed = sessionState.revealedSlots[item.role];

                slot.innerHTML = `
                    <div class="card-3d-wrapper ${isRevealed ? 'flipped' : ''}" id="wrap-${item.role}">
                        <div class="card-back-3d-play"></div>
                        <div class="card-front-3d ${!item.isPositive ? 'reversed-img' : ''}">
                            <img src="${imgUrl}" alt="${item.card.theme_ja}">
                        </div>
                    </div>
                    <div class="slot-label">${item.label}</div>
                `;

                boardLayout.appendChild(slot);
            });
        }

        // カードをめくるアニメーション
        function revealCardSlot(role) {
            sessionState.revealedSlots[role] = true;
            const wrap = document.getElementById(`wrap-${role}`);
            if (wrap) {
                wrap.classList.add('flipped');
                playMetronomeTick(); // めくる瞬間にカチッと音
            }
        }

        // スロットが選択された時の詳細表示
        function selectSlotForReading(role, shouldScroll = true) {
            // アクティブ表示の切り替え
            document.querySelectorAll('.card-slot').forEach(el => el.classList.remove('active-selection'));
            const slotEl = document.querySelector(`.slot-${role}`);
            if (slotEl) slotEl.classList.add('active-selection');

            const item = sessionState.cardsInPlay.find(c => c.role === role);
            if (!item) return;

            const isRevealed = sessionState.revealedSlots[role];
            const panel = document.getElementById('reading-panel-el');
            
            document.getElementById('panel-slot-role').textContent = item.label;
            document.getElementById('panel-slot-desc').textContent = item.desc;

            if (!isRevealed) {
                // まだめくられていない場合、パネルは伏せられた状態
                document.getElementById('panel-card-title').textContent = "（カードが伏せられています）";
                document.getElementById('panel-card-img-box').innerHTML = `<div style="display:flex; justify-content:center; align-items:center; height:100%; color:var(--gold); font-size:1.5rem;">★</div>`;
                document.getElementById('panel-pos-badge').style.display = 'none';
                document.getElementById('panel-levels').innerHTML = "";
                document.getElementById('panel-card-meaning').textContent = "上のカードをクリックしてオープンしてください。";
                document.getElementById('panel-meaning-title').textContent = "メッセージ";
                document.getElementById('panel-card-desc').innerHTML = "カードを開くことで、ゲリー・ボーネル氏による詳細なご神託と解説が表示されます。";
                panel.style.display = 'block';
                return;
            }

            // オープンされている場合
            const card = item.card;
            document.getElementById('panel-card-title').textContent = `${card.no}. ${card.theme_ja} (${card.theme_en})`;
            
            const imgBox = document.getElementById('panel-card-img-box');
            imgBox.className = `reading-card-img-box ${!item.isPositive ? 'reversed-img' : ''}`;
            imgBox.innerHTML = `<img id="panel-card-img" src="${getDirectImageUrl(item.isPositive ? card.url_positive : card.url_reverse, item.isPositive)}" alt="${card.theme_ja}">`;

            const posBadge = document.getElementById('panel-pos-badge');
            posBadge.style.display = 'inline-block';
            
            if (item.isPositive) {
                posBadge.textContent = "正位置";
                posBadge.className = "position-badge badge-positive";
                document.getElementById('panel-card-meaning').textContent = card.positive;
                document.getElementById('panel-meaning-title').textContent = "正位置のメッセージ";
                document.getElementById('panel-meaning-box').className = "card-meaning-box";
            } else {
                posBadge.textContent = "逆位置";
                posBadge.className = "position-badge badge-reversed";
                document.getElementById('panel-card-meaning').textContent = card.reverse;
                document.getElementById('panel-meaning-title').textContent = "逆位置のメッセージ";
                document.getElementById('panel-meaning-box').className = "card-meaning-box reversed-meaning";
            }

            // レベル
            let lvHtml = "";
            if (card.spiritual_level) lvHtml += `<span class="level-badge">霊的：${card.spiritual_level}</span>`;
            if (card.daily_level) lvHtml += `<span class="level-badge">日常：${card.daily_level}</span>`;
            document.getElementById('panel-levels').innerHTML = lvHtml;

            // 解説（「。」で改行フォーマットして innerHTML に設定）
            document.getElementById('panel-card-desc').innerHTML = formatDescription(card.description) || "解説がありません。";

            panel.style.display = 'block';
            
            if (shouldScroll) {
                sessionState.scrollCount++;
                // 1回目のスクロール（最初のカード選択）は二段階ギアチェンジ（725ms）
                // 2回目以降のカード選択は、最初からx4倍の超高速スクロール（350ms）
                const isFirstScroll = sessionState.scrollCount <= 1;
                const duration = isFirstScroll ? 725 : 350;
                slowScrollTo(panel, duration, !isFirstScroll);
            }
        }

        function resetReadingSession() {
            sessionState.selfCardNo = null;
            sessionState.cardsInPlay = [];
            sessionState.revealedSlots = {};
            sessionState.scrollCount = 0; // スクロール回数をリセット
            
            document.getElementById('reading-board-container').style.display = 'none';
            document.getElementById('step-self').classList.add('active');
            
            renderSelfPicker();
        }

        // ==========================================
        // 【画面3】手動入力画面 (📝 Entry) の制御
        // ==========================================
        function adjustManualFormFields() {
            const spread = document.getElementById('manual-spread-select').value;
            const container = document.getElementById('manual-slots-container');
            container.innerHTML = "";

            const slots = SLOT_ROLES[spread];
            
            slots.forEach(slot => {
                const group = document.createElement('div');
                group.className = 'glass-panel';
                group.style.padding = '12px';
                group.style.background = 'rgba(255,255,255,0.01)';
                group.style.marginBottom = '10px';

                // ドロップダウン生成
                let optionsHtml = "";
                CARDS_DATA.forEach(card => {
                    optionsHtml += `<option value="${card.no}">${card.no}. ${card.theme_ja}</option>`;
                });

                group.innerHTML = `
                    <div style="font-size: 0.8rem; font-weight: bold; color: var(--gold); margin-bottom: 8px;">
                        ${slot.label}
                    </div>
                    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                        <div class="form-group" style="flex: 1; min-width: 180px;">
                            <select class="manual-card-select" data-slot="${slot.id}">
                                ${optionsHtml}
                            </select>
                        </div>
                        ${slot.id !== 'self' ? `
                        <div class="form-group">
                            <div class="switch-container" style="margin-top: 5px;">
                                <span class="switch-label">逆位置</span>
                                <label class="switch">
                                    <input type="checkbox" class="manual-pos-chk" data-slot="${slot.id}" checked>
                                    <span class="slider"></span>
                                </label>
                                <span class="switch-label">正位置</span>
                            </div>
                        </div>
                        ` : ''}
                    </div>
                `;
                container.appendChild(group);
            });

            // デフォルトの初期値をずらす
            const selects = container.querySelectorAll('.manual-card-select');
            selects.forEach((sel, idx) => {
                sel.value = Math.min(idx + 1, CARDS_DATA.length);
            });
        }

        function applyManualReading() {
            const spread = document.getElementById('manual-spread-select').value;
            const container = document.getElementById('manual-slots-container');
            const selects = container.querySelectorAll('.manual-card-select');
            
            sessionState.spreadType = spread;
            sessionState.cardsInPlay = [];
            sessionState.revealedSlots = {};

            selects.forEach(sel => {
                const slotId = sel.dataset.slot;
                const cardNo = parseInt(sel.value);
                const roleDef = SLOT_ROLES[spread].find(s => s.id === slotId);

                // 正位置チェック (セルフは正位置固定)
                let isPositive = true;
                if (slotId !== 'self') {
                    const chk = container.querySelector(`.manual-pos-chk[data-slot="${slotId}"]`);
                    isPositive = chk ? chk.checked : true;
                }

                sessionState.cardsInPlay.push({
                    role: slotId,
                    label: roleDef.label,
                    desc: roleDef.desc,
                    card: CARDS_DATA.find(c => c.no === cardNo),
                    isPositive: isPositive
                });

                // 手動入力のカードは最初からすべて「表向き（オープン）」にする
                sessionState.revealedSlots[slotId] = true;
            });

            // セルフカードの設定値も同期
            const selfCard = sessionState.cardsInPlay.find(c => c.role === 'self');
            if (selfCard) sessionState.selfCardNo = selfCard.card.no;

            // リーディング画面に遷移して描画
            document.querySelectorAll('.app-view').forEach(view => view.classList.remove('active'));
            document.getElementById('view-reading').classList.add('active');
            
            // ナビゲーションのactive変更
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.querySelectorAll('.nav-item')[1].classList.add('active');

            // ウィザードを非表示にしてボードを直接表示
            document.querySelectorAll('.wizard-step').forEach(step => step.classList.remove('active'));
            document.getElementById('reading-board-container').style.display = 'block';

            // ボード描画 ＆ 初期スロット選択
            const titleEl = document.getElementById('board-title-display');
            if (spread === 'one') titleEl.textContent = "手動展開: 1枚引き (テーマ)";
            else if (spread === 'four') titleEl.textContent = "手動展開: 四枚スプレッド";
            else if (spread === 'nine') titleEl.textContent = "手動展開: 九枚スプレッド";

            renderReadingBoard();
            selectSlotForReading('self', false);
        }

        // ==========================================
        // 【画面4】カード図鑑・検索・詳細モーダル
        // ==========================================
        function renderCardsGrid(filteredData = CARDS_DATA) {
            const container = document.getElementById('cards-grid-container');
            container.innerHTML = "";

            if (filteredData.length === 0) {
                container.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 40px 0;">カードが見つかりませんでした</div>`;
                return;
            }

            filteredData.forEach(card => {
                const cardEl = document.createElement('div');
                cardEl.className = 'grid-card-item';
                cardEl.onclick = () => openCardModal(card.no);

                const imgUrl = getDirectImageUrl(card.url_positive);

                cardEl.innerHTML = `
                    <div class="grid-card-img">
                        <img src="${imgUrl}" alt="${card.theme_ja}" loading="lazy">
                    </div>
                    <div class="grid-card-no">No. ${card.no}</div>
                    <div class="grid-card-title">${card.theme_ja}</div>
                `;
                container.appendChild(cardEl);
            });
        }

        function filterCards() {
            const query = document.getElementById('search-input').value.toLowerCase().trim();
            if (!query) {
                renderCardsGrid(CARDS_DATA);
                return;
            }

            const filtered = CARDS_DATA.filter(card => {
                return card.no.toString() === query || 
                       card.theme_ja.toLowerCase().includes(query) || 
                       card.theme_en.toLowerCase().includes(query) ||
                       (card.spiritual_meaning && card.spiritual_meaning.toLowerCase().includes(query));
            });
            renderCardsGrid(filtered);
        }

        function openCardModal(cardNo) {
            const card = CARDS_DATA.find(c => c.no === cardNo);
            if (!card) return;

            document.getElementById('modal-no').textContent = `No. ${card.no}`;
            document.getElementById('modal-title-ja').textContent = card.theme_ja;
            document.getElementById('modal-title-en').textContent = card.theme_en;
            document.getElementById('modal-img').src = getDirectImageUrl(card.url_positive);
            document.getElementById('modal-spiritual-meaning').textContent = card.spiritual_meaning || "なし";
            document.getElementById('modal-meaning-pos').textContent = card.positive || "なし";
            document.getElementById('modal-meaning-rev').textContent = card.reverse || "なし";
            document.getElementById('modal-description').innerHTML = formatDescription(card.description) || "解説テキストがありません。";

            const lvContainer = document.getElementById('modal-levels-container');
            lvContainer.innerHTML = "";
            if (card.spiritual_level) {
                const b = document.createElement('span');
                b.className = 'level-badge';
                b.textContent = `霊的レベル：${card.spiritual_level}`;
                lvContainer.appendChild(b);
            }
            if (card.daily_level) {
                const b = document.createElement('span');
                b.className = 'level-badge';
                b.textContent = `日常レベル：${card.daily_level}`;
                lvContainer.appendChild(b);
            }

            document.getElementById('card-modal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal(event) {
            if (event.target === document.getElementById('card-modal')) {
                closeModalDirect();
            }
        }

        function closeModalDirect() {
            document.getElementById('card-modal').classList.remove('active');
            document.body.style.overflow = '';
        }

        // ナビゲーションビュー切り替えのフック
        function switchView(viewId, element) {
            // ナビゲーションアクティブ
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            element.classList.add('active');

            // 画面表示
            document.querySelectorAll('.app-view').forEach(view => view.classList.remove('active'));
            document.getElementById(`view-${viewId}`).classList.add('active');

            // ビュー固有の初期化
            if (viewId === 'reading') {
                renderSelfPicker();
            } else if (viewId === 'entry') {
                adjustManualFormFields();
            }
        }

        // ==========================================
        // 【起動処理】安全な初期起動ロジック
        // ==========================================
        function initializeApp() {
            try {
                // カード一覧の描画
                renderCardsGrid();
                // セルフカード選択の初期化
                renderSelfPicker();
                console.log("Akashic Records App Initialized successfully.");
            } catch (e) {
                console.error("Initialization error:", e);
            }
        }

        // DOMContentLoadedのタイミングバグを回避（ローカルfile:///実行対応）
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", initializeApp);
        } else {
            initializeApp();
        }
    </script>
</body>
</html>
"""

# JSON文字列をプレースホルダーに埋め込む
cards_json_str = json.dumps(cards_data, ensure_ascii=False, indent=12)
html_content = html_template.replace("cards_json_placeholder", cards_json_str)

# HTMLファイルとして出力 (ルートおよびv.01フォルダの両方に保存)
output_paths = [
    r"g:\共有ドライブ\KiriPlayPark\Tool\Antigravity\kiriplaypark-projects\AkashicRecordCard\index.html",
    r"g:\共有ドライブ\KiriPlayPark\Tool\Antigravity\kiriplaypark-projects\AkashicRecordCard\v.01\index.html"
]

for output_html_path in output_paths:
    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated: {output_html_path}")

print(f"Successfully generated full-featured Akashic Reading SPA index.html with {len(cards_data)} cards.")
