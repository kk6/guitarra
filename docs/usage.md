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
```