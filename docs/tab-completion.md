# タブ補完機能 - 技術仕様書

## 概要

`guitar` コマンドのタブ補完機能について、技術的な実装詳細と使用方法を説明します。

## 実装方式

### Click 8.x系標準補完システム

- **フレームワーク**: Click 8.2.1の標準補完機能を使用
- **依存関係**: `click-completion` パッケージを使用せず、Clickの標準機能のみを使用
- **対応シェル**: zsh, bash, fish

### zsh用補完関数

```bash
#compdef guitar
_guitar() {
  local -a completions
  local -a completions_with_descriptions
  local -a response
  (( ! $+commands[guitar] )) && return 1

  response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _GUITAR_COMPLETE=zsh_complete guitar)}")

  for type key descr in ${response}; do
    if [[ "$type" == "plain" ]]; then
      if [[ "$descr" == "_" ]]; then
        completions+=("$key")
      else
        completions_with_descriptions+=("$key":"$descr")
      fi
    elif [[ "$type" == "dir" ]]; then
      _path_files -/
    elif [[ "$type" == "file" ]]; then
      _path_files -f
    fi
  done

  if [ "$completions_with_descriptions" ]; then
    _describe -V unsorted completions_with_descriptions -U
  fi

  if [ "$completions" ]; then
    compadd -U -V unsorted -a completions
  fi
}

if [[ "$(basename -- ${(%):-%x})" != "_guitar" ]]; then
  compdef _guitar guitar
fi
```

## 補完対象

### 1. メインコマンド補完

```bash
$ guitar <TAB>
blues               Generate 12 bar blues chord progression.
install-completion  Install tab completion for the current shell.
scale               Display guitar scale on fretboard.
```

### 2. スケール名補完

```bash
$ guitar scale C <TAB>
major              minor              pentatonic_major   pentatonic_minor
dorian             phrygian           lydian             mixolydian
aeolian            locrian            blues              harmonic_minor
melodic_minor
```

### 3. オプション補完

```bash
$ guitar blues A --<TAB>
--minor     Generate minor blues progression
--degrees   Show Roman numeral degrees
--help      Show this message and exit.

$ guitar scale C major --<TAB>
--start     Start fret position
--end       End fret position
--degrees   Show scale degrees instead of note names
--help      Show this message and exit.
```

## インストール方法

### 自動インストール（推奨）

```bash
# シェル自動検出
guitar install-completion

# 設定反映
source ~/.zshrc
```

### 手動インストール

```bash
# シェル指定
guitar install-completion --shell zsh

# 設定反映
source ~/.zshrc
```

## 動作確認

### 補完機能のテスト

```bash
# 基本動作確認
guitar <TAB>

# スケール名補完確認
guitar scale C <TAB>

# オプション補完確認
guitar blues A --<TAB>
```

### トラブルシューティング

#### 1. 補完が動作しない場合

```bash
# 補完設定の確認
grep "_guitar" ~/.zshrc

# 補完関数の再読み込み
source ~/.zshrc

# 補完システムの初期化
autoload -U compinit
compinit
```

#### 2. 重複設定の削除

```bash
# 古い設定を削除
sed -i '' '/^#compdef guitar/,/^fi$/d' ~/.zshrc

# 新しい設定を追加
guitar install-completion
source ~/.zshrc
```

## 技術的な詳細

### 環境変数

- `COMP_WORDS`: 現在のコマンドライン全体
- `COMP_CWORD`: 現在の単語のインデックス
- `_GUITAR_COMPLETE`: 補完モード（`zsh_complete`）

### 補完出力フォーマット

Click 8.xの補完出力は以下の形式：

```
plain <候補> <説明>
dir <ディレクトリ名> <説明>
file <ファイル名> <説明>
```

### zsh補完関数の処理フロー

1. **コマンド存在確認**: `(( ! $+commands[guitar] )) && return 1`
2. **補完候補取得**: `env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _GUITAR_COMPLETE=zsh_complete guitar`
3. **出力解析**: `for type key descr in ${response}`
4. **候補分類**: `plain`, `dir`, `file`タイプごとに処理
5. **補完表示**: `_describe`と`compadd`を使用

## 制限事項

- 現在はzsh用の実装のみ提供
- bash, fish用の実装は将来的に追加予定
- 動的補完（現在のコンテキストに基づく補完）は未実装

## 将来の拡張

- bash用補完関数の実装
- fish用補完関数の実装
- 動的補完（キーに基づくスケール候補の絞り込み）
- 補完候補の説明文の多言語対応