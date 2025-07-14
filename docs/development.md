# 開発者ガイド

このドキュメントでは、guitarraプロジェクトの開発環境のセットアップと開発ワークフローについて説明します。

## 開発環境セットアップ

### 前提条件

- Python 3.12以上
- [uv](https://docs.astral.sh/uv/) (Pythonパッケージマネージャー)

### インストール

1. リポジトリをクローン
```bash
git clone <repository-url>
cd guitarra
```

2. 依存関係をインストール
```bash
uv sync
```

3. 開発モードでインストール
```bash
uv pip install -e .
```

## 開発ツール

### Linter & Formatter - Ruff

プロジェクトではコードの品質を保つために[Ruff](https://docs.astral.sh/ruff/)を使用しています。

#### 設定

`pyproject.toml`で以下の設定を行っています：

```toml
[tool.ruff]
line-length = 88
lint.select = ["E", "F", "I", "N", "W", "UP"]
lint.ignore = []

[tool.ruff.format]
quote-style = "double"
```

#### 使用方法

```bash
# リンターの実行
uv run ruff check

# フォーマッターの実行
uv run ruff format

# 自動修正可能な問題を修正
uv run ruff check --fix
```

### 型チェッカー - ty

静的型解析には[ty](https://github.com/astral-sh/ty)を使用しています。

#### 特徴

- Rust製の高速な型チェッカー
- mypy互換
- 現在プレビュー版

#### 使用方法

```bash
# 型チェックの実行
uv run ty check
```

### テストフレームワーク - pytest

単体テストには[pytest](https://docs.pytest.org/)を使用しています。

#### 設定

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
```

#### 使用方法

```bash
# テストの実行
uv run pytest

# カバレッジ付きでテストを実行
uv run pytest --cov=src
```

### Pre-commit フック

コードの品質を保つためにpre-commitフックを設定することを推奨します。

#### セットアップ

```bash
# pre-commitをインストール
uv add --group=dev pre-commit

# pre-commitフックをインストール
uv run pre-commit install
```

#### 設定例 (.pre-commit-config.yaml)

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: local
    hooks:
      - id: ty
        name: ty
        entry: ty check
        language: system
        types: [python]
        pass_filenames: false
```

## 開発ワークフロー

### 1. 機能開発

1. 新しいブランチを作成
2. コードを実装
3. テストを作成・実行
4. 型チェックを実行
5. リンター・フォーマッターを実行
6. プルリクエストを作成

### 2. コードの品質チェック

開発中は以下のコマンドを定期的に実行することを推奨します：

```bash
# 全体的な品質チェック
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest
```

### 3. 継続的インテグレーション

GitHub ActionsやCIツールでは以下のステップを実行することを推奨します：

1. 依存関係のインストール
2. リンターチェック
3. 型チェック
4. テスト実行
5. カバレッジレポート

## トラブルシューティング

### ty関連の問題

- tyは現在プレビュー版のため、エラーが発生する可能性があります
- 問題が発生した場合は、mypyなどの代替ツールの使用を検討してください

### 依存関係の問題

```bash
# 依存関係を再インストール
uv sync --refresh

# キャッシュをクリア
uv cache clean
```

## 関連リンク

- [Ruff公式ドキュメント](https://docs.astral.sh/ruff/)
- [ty公式リポジトリ](https://github.com/astral-sh/ty)
- [pytest公式ドキュメント](https://docs.pytest.org/)
- [uv公式ドキュメント](https://docs.astral.sh/uv/)