# RDKitチュートリアル

ARIMデータポータル会員向けセミナー・ワークショップで提供するRDKitを使った化学情報処理の教育用Jupyter Notebook教材です。GitHub: [ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit](https://github.com/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit)



## 対象読者・前提知識

- ARIMデータポータル会員の研究者・技術者
- Pythonの基礎文法（変数、`import`、リスト、`for`文）は理解しているが、RDKit・pandasなどのライブラリには初めて触れる方を想定
- 統計学・機械学習の予備知識は前提としない

## ノートブック一覧

| No. | ファイル | 内容 | Colabで開く | 使用ライブラリ | データセット |
| --- | --- | --- | --- | --- | --- |
| 1 | [`RDKit-1.ipynb`](https://github.com/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit/blob/main/RDKit-1.ipynb) | 基礎編：ファイルの読み取り（MOL/SMILES/SDF）・分子構造の描画・ファイルへの保存 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit/blob/main/RDKit-1.ipynb) | RDKit | アスピリンの構造データ（[ChemSpider](https://www.chemspider.com/) CSID: 2157） |
| 2 | [`RDKit-2.ipynb`](https://github.com/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit/blob/main/RDKit-2.ipynb) | 実践編：pandas DataFrameと連携した複数化合物の一括処理・可視化 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit/blob/main/RDKit-2.ipynb) | RDKit, pandas, matplotlib, seaborn, scikit-learn | Delaney水溶解度データセット（1,128化合物、出典は下記） |
| 3 | [`RDKit-3.ipynb`](./RDKit-3.ipynb) | 発展編：UFF/MMFF力場によるコンフォーマー探索・構造最適化。安定構造をmol/xyz/gjf形式で保存し、量子化学計算（Gaussian・Psi4）への橋渡しを行う | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit/blob/main/RDKit-3.ipynb) | RDKit, py3Dmol, pandas, matplotlib | アスピリンの構造データ（同上）＋`data/smiles_10.csv`（MMFFの適用範囲を確認する演示に使用） |

各ノートブックの冒頭に「対象読者・前提知識・動作環境・版とライセンス」ブロック、章末に「まとめ」「本ノートブックで扱っていないこと（今後の課題）」「演習問題」を掲載しています。


### 今後追加予定の内容

`RDKit-2.ipynb`内で予告されている、以下のトピックは今後の回で扱う想定です。

- 分子記述子の計算（`rdkit.Chem.Descriptors`）
- 分子間の類似性評価（Morganフィンガープリント、Tanimoto係数）
- 部分構造検索（SMARTSパターン）、無効なSMILES・パースエラーのハンドリング
- 記述子・フィンガープリントを特徴量とした水溶解度予測モデルの構築（scikit-learn編との接続）

## 動作環境

- Python 3.10以降
- `rdkit` 2023.x以降（`pip install rdkit`。`RDKit-3.ipynb`の動作確認時点の最新版は2026.03.4）
- `pandas`、`matplotlib`、`seaborn`、`scikit-learn`（`RDKit-2.ipynb`のみ）
- `py3Dmol`（3D構造の可視化、`RDKit-3.ipynb`のみ）
- Jupyter Notebook / JupyterLab、または Google Colab

### 実行方法

**ローカル環境の場合**：このフォルダをそのまま開き、各ノートブックを先頭セルから順に実行してください。`data/`・`img/`フォルダはこのプロジェクトフォルダ内に同梱済みのため、追加のダウンロードは不要です。`output/`フォルダ（保存先）は各ノートブックのコード内で自動的に作成されます。

**Google Colabの場合**：上表の「Colabで開く」バッジから直接開けます。バッジ経由で開いた場合は、各ノートブック冒頭の「教材への接続」セルを実行すると、必要なデータ一式を含む [ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit](https://github.com/ARIM-ACADEMY-2026/Advanced_Tutorial_2_RDKit) リポジトリを自動的にクローンします。ローカル実行時はこのセルの実行は不要です。

## フォルダ構成

GitHubリポジトリ全体（3冊構成）の構造は以下の通りです。

```
.
├── RDKit-1.ipynb         # 基礎編
├── RDKit-2.ipynb         # 実践編
├── RDKit-3.ipynb         # 発展編：力場によるコンフォーマー探索・構造最適化
├── data/
│   ├── aspirin.mol / aspirin.sdf        # アスピリンの構造データ（RDKit-1・3用）
│   ├── aspirin_rdkit.mol / .sdf         # RDKit-1内で生成される保存例
│   ├── smiles_10.csv                    # 10分子のSMILES（RDKit-3のMMFF演示用）
│   └── dataset/delaney-processed.csv    # Delaney水溶解度データセット（RDKit-2用）
├── img/                   # マークダウン図版
├── output/                # 実行時に自動生成される保存先フォルダ（mol/xyz/gjf等）
├── util.py                # RDKit-3用：ファイル書き出し・3D可視化のヘルパー関数
└── README.md
```


## データの出典・ライセンス

- **RDKit本体**：BSD-3-Clauseライセンスで公開されているオープンソースソフトウェアです。
- **アスピリンの構造データ**（`data/aspirin.mol`, `data/aspirin.sdf`）：[ChemSpider](https://www.chemspider.com/)（CSID: 2157）由来のデータを教材用に整形したものです。
- **Delaney水溶解度データセット**（`data/dataset/delaney-processed.csv`）：John S. Delaney, "ESOL: Estimating Aqueous Solubility Directly from Molecular Structure", *J. Chem. Inf. Comput. Sci.*, **44**, 1000–1005 (2004). DOI: [10.1021/ci034243x](https://doi.org/10.1021/ci034243x)
- 本リポジトリ全体は MIT License で公開されています（詳細はGitHubリポジトリの`LICENSE`を参照）。
