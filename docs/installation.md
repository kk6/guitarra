# Guitarra インストール方法

Guitarra をインストールして使用を開始する方法を説明します。

## 必要な環境

- **Python**: 3.12 以上
- **uv**: Python パッケージマネージャー（推奨）

## インストール方法

### 1. uvを使用したインストール（推奨）

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/guitarra.git
cd guitarra

# 依存関係をインストール
uv sync

# 開発モードでインストール
uv pip install -e .
```

### 2. pipを使用したインストール

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/guitarra.git
cd guitarra

# 依存関係をインストール
pip install -e .
```

### 3. パッケージからのインストール

```bash
# PyPI からインストール（将来的に利用可能）
pip install guitarra
```

## インストール確認

インストールが正常に完了したかを確認します：

```bash
# コマンドが利用可能か確認
guitar --help

# バージョン情報を確認
guitar --version
```

正常にインストールされていれば、以下のような出力が表示されます：

```
Usage: guitar [OPTIONS] COMMAND [ARGS]...

Guitar practice CLI tool

Options:
  --help  Show this message and exit.

Commands:
  blues  Generate 12 bar blues chord progression.
  scale  Display guitar scale on fretboard.
```

## 基本的な使用例

インストール後、すぐに使用できます：

```bash
# A メジャーブルース
guitar blues A

# C メジャースケール
guitar scale C major
```

## 開発環境のセットアップ

Guitarra の開発に参加したい場合：

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/guitarra.git
cd guitarra

# 開発依存関係を含めてインストール
uv sync --all-extras

# 開発モードでインストール
uv pip install -e .

# テストの実行
python -m pytest tests/

# コードフォーマットとリント
ruff format .
ruff check .

# 型チェック
ty src/
```

## トラブルシューティング

### よくある問題と解決方法

#### 1. "guitar: command not found"

**原因**: インストールが正しく行われていない、またはPATHが通っていない

**解決方法**:
```bash
# インストール状況を確認
pip show guitarra

# パスを確認
which guitar

# 再インストール
pip install -e .
```

#### 2. "ModuleNotFoundError: No module named 'guitarra'"

**原因**: Python パッケージが正しくインストールされていない

**解決方法**:
```bash
# 現在のPython環境を確認
python --version
pip list | grep guitarra

# 再インストール
pip install -e .
```

#### 3. Python 3.12 が見つからない

**原因**: 必要なPythonバージョンがインストールされていない

**解決方法**:
```bash
# pyenv を使用してPython 3.12をインストール
pyenv install 3.12.0
pyenv global 3.12.0

# またはシステムのパッケージマネージャーを使用
# macOS
brew install python@3.12

# Ubuntu/Debian
sudo apt update
sudo apt install python3.12
```

#### 4. uv が見つからない

**原因**: uv がインストールされていない

**解決方法**:
```bash
# uvをインストール
curl -LsSf https://astral.sh/uv/install.sh | sh

# または pip を使用
pip install uv
```

## アンインストール

Guitarra をアンインストールする場合：

```bash
# pipでインストールした場合
pip uninstall guitarra

# 開発モードでインストールした場合
pip uninstall guitarra
```

## 次のステップ

インストールが完了したら、[使用方法ドキュメント](usage.md)を参照して、Guitarra の機能を詳しく学んでください。