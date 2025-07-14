# Guitarra CLI 使用方法

Guitarra は、ギター練習のためのコマンドラインツールです。ブルースの12小節コード進行の生成やギターのスケール表示機能を提供します。

## 基本的な使用方法

### コマンドの実行

```bash
guitar [コマンド] [オプション]
```

### 利用可能なコマンド

#### 1. blues - 12小節ブルースコード進行生成

12小節ブルースのコード進行を生成します。

```bash
guitar blues [ルート音]
```

**例：**
```bash
# A メジャーブルース
guitar blues A

# C# メジャーブルース  
guitar blues C#

# Bb メジャーブルース
guitar blues Bb
```

**オプション：**
- `--minor` / `-m`: マイナーブルース進行を生成
- `--degrees` / `-d`: ローマ数字の度数表示を追加

**例：**
```bash
# A マイナーブルース
guitar blues A --minor

# ローマ数字度数付きで表示
guitar blues A --degrees

# マイナーブルース + 度数表示
guitar blues A -m -d
```

#### 2. scale - ギタースケール表示

ギターのフレットボード上にスケールを表示します。

```bash
guitar scale [ルート音] [スケール名]
```

**例：**
```bash
# A メジャースケール
guitar scale A major

# C# マイナーペンタトニック
guitar scale C# pentatonic_minor

# G ブルーススケール
guitar scale G blues
```

**オプション：**
- `--start` / `-s`: 開始フレット位置 (デフォルト: 0)
- `--end` / `-e`: 終了フレット位置 (デフォルト: 12)
- `--degrees` / `-d`: 音名の代わりに度数を表示

**例：**
```bash
# 5-12フレットのA メジャースケール
guitar scale A major --start 5 --end 12

# 度数表示でC マイナースケール
guitar scale C minor --degrees

# 7-19フレットのE ペンタトニック
guitar scale E pentatonic_major -s 7 -e 19
```

### 対応しているルート音

**シャープ記号 (#)：**
- C, C#, D, D#, E, F, F#, G, G#, A, A#, B

**フラット記号 (♭)：**
- Db, Eb, Gb, Ab, Bb

### 対応しているスケール

- **major** - メジャースケール
- **minor** - マイナースケール（ナチュラルマイナー）
- **pentatonic_major** - メジャーペンタトニック
- **pentatonic_minor** - マイナーペンタトニック
- **blues** - ブルーススケール
- **dorian** - ドリアンモード
- **phrygian** - フリジアンモード
- **lydian** - リディアンモード
- **mixolydian** - ミクソリディアンモード
- **aeolian** - エオリアンモード
- **locrian** - ロクリアンモード
- **harmonic_minor** - ハーモニックマイナー
- **melodic_minor** - メロディックマイナー

### タブ補完

bash や zsh を使用している場合、以下の要素でタブ補完が利用できます：

- **ルート音**: `A` + Tab で音名候補を表示
- **スケール名**: `guitar scale A m` + Tab でスケール名候補を表示

### 使用例

```bash
# 基本的なA メジャーブルース
guitar blues A

# F# マイナーブルース（度数表示付き）
guitar blues F# --minor --degrees

# C メジャーペンタトニック（全フレット）
guitar scale C pentatonic_major

# E ブルーススケール（5-12フレット、度数表示）
guitar scale E blues --start 5 --end 12 --degrees

# D ドリアンモード（0-7フレット）
guitar scale D dorian -s 0 -e 7
```

#### 3. metronome - メトロノーム機能

練習用のメトロノームを起動します。

```bash
guitar metronome [BPM]
```

**例：**
```bash
# 120 BPMでメトロノーム開始
guitar metronome 120

# 90 BPMで3/4拍子
guitar metronome 90 --beats 3

# 140 BPMで8分音符の細分化
guitar metronome 140 --subdivisions eighth
```

**オプション：**
- `--beats` / `-b`: 小節あたりの拍数 (デフォルト: 4、範囲: 1-16)
- `--duration` / `-d`: 再生時間（秒）（0で無限、デフォルト: 0）
- `--subdivisions` / `-s`: 細分化タイプ（quarter, eighth, sixteenth, triplets）
- `--style` / `-st`: メトロノームスタイル（simple, practice, performance）

**細分化タイプ：**
- `quarter`: 4分音符（基本）
- `eighth`: 8分音符の細分化
- `sixteenth`: 16分音符の細分化
- `triplets`: 3連符の細分化

**スタイル：**
- `simple`: シンプルなメトロノーム（アクセントなし）
- `practice`: 練習用（控えめなアクセント）
- `performance`: 演奏用（強いアクセント）

**例：**
```bash
# 100 BPMで30秒間
guitar metronome 100 --duration 30

# 80 BPMで3/4拍子、8分音符細分化
guitar metronome 80 --beats 3 --subdivisions eighth

# 160 BPMでパフォーマンススタイル
guitar metronome 160 --style performance

# 120 BPMで16分音符、練習用スタイル
guitar metronome 120 -s sixteenth -st practice
```

**停止方法：**
メトロノームを停止するには `Ctrl+C` を押してください。

### エラーハンドリング

無効な入力があった場合、エラーメッセージと共に有効な選択肢が表示されます：

```bash
# 無効な音名
guitar blues X
# → Error: Invalid root note: X
# → Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# → You can also use flat notation: Db, Eb, Gb, Ab, Bb

# 無効なスケール名
guitar scale A invalid_scale
# → Error: Unknown scale: invalid_scale
# → Available scales: major, minor, pentatonic_major, ...
```

## ヘルプ

各コマンドの詳細なヘルプを表示するには：

```bash
# 全体のヘルプ
guitar --help

# 特定のコマンドのヘルプ
guitar blues --help
guitar scale --help
guitar metronome --help
```