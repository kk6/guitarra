# タブ補完機能 - 技術仕様書

## 概要

`guitar` コマンドのタブ補完機能について、技術的な実装詳細と使用方法を説明します。

## 実装方式

### Typer標準補完システム

- **フレームワーク**: Typer 0.12.0の標準補完機能を使用（内部でClickを使用）
- **自動有効化**: パッケージとしてインストールすることで自動的に有効になる
- **対応シェル**: zsh, bash, fish, PowerShell

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

### パッケージインストール（推奨）

```bash
# パッケージとしてインストール
uv pip install -e .

# または
pip install -e .
```

**注意**: パッケージとしてインストールすることで、タブ補完は自動的に有効になります。追加の設定は不要です。

### 開発環境でのテスト

```bash
# 開発環境でのテスト実行
python -m guitarra.cli <TAB>
```

開発環境では、パッケージがインストールされていないため、タブ補完は動作しません。

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
# パッケージが正しくインストールされているか確認
pip list | grep guitarra

# guitarコマンドが実行可能か確認
which guitar

# パッケージを再インストール
pip uninstall guitarra
pip install -e .
```

#### 2. 開発環境での補完テスト

```bash
# typerコマンドを使って補完テスト
typer guitarra/cli.py run --help
```

## 技術的な詳細

### 環境変数

- `COMP_WORDS`: 現在のコマンドライン全体
- `COMP_CWORD`: 現在の単語のインデックス
- `_GUITAR_COMPLETE`: 補完モード（`zsh_complete`）

### 補完出力フォーマット

Typer（Click）の補完出力は以下の形式：

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

- 開発環境（`python -m guitarra.cli`）では補完が動作しない
- パッケージインストール後のみ有効
- 動的補完（現在のコンテキストに基づく補完）は未実装

## 将来の拡張

- 動的補完（キーに基づくスケール候補の絞り込み）
- 補完候補の説明文の多言語対応
- コンテキストを考慮した補完機能の強化