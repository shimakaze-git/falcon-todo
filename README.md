# Falconを使用してのtodoアプリの作成チュートリアル

---

PythonにはWSGI対応アプリケーションの一つでもある[Falcon](https://falcon.readthedocs.io/en/stable/)という軽量WEBフレームワークがあります

こちらのリポジトリではFalconを使用しての簡単なWEBアプリケーション(主にAPI部分)の作り方についてのサンプルをまとめてあります。

### 主に使用するモジュール

ここのチュートリアルで主に使用するモジュールです

- [SQLAlchemy](https://www.sqlalchemy.org/)
MySQLなどのRDBを扱うためのPythonでは有名なORMの一つです

- [graceful](https://github.com/swistakm/graceful)
FalconでREST frameworkを扱うためのサードパーティー製モジュールです。Django REST frameworkの思想を強く受けており、Django REST frameworkと同じような機能を備えることができます。
~~学習コストが高いので、そこまで本格的には使う予定はありません~~


## Falconとは

Falconは大規模なマイクロサービスなどを開発する用途に主に向いているWEBフレームワークです。

Djangoほどの高機能ではないものの、Flask以上の機能を標準で備えており、なおかつ他のPythonフレームワークよりも高速であることが特徴です。

Pythonで本格的なWEBアプリケーションを開発する場合は、基本的にDjango一択であることがほとんどです。(Pyramidの場合もありますが、最近はほとんど普及率減ってきました)

しかし、Djangoほどの機能を必要としていない場合や、DjangoをAPI用途として使うためのDjango Rest frameworkがあるもののDRF(Django Rest framework)は学習コストが高く、資料が少なく扱いづらいことがよく言われています。

そこで軽量でシンプルなFlaskで開発を行う選択肢もありますが、Flaskでは標準で備えている機能は少なく、パフォーマンス面ではそこまで速くはありません。

Django Rest frameworkほどの学習コストをかけず、DRFほどの高機能は求めない、なおかつFlaskほどの機能では足りない、といった場合のちょうどよい中間的な特徴を持つフレームワークとして、[Falcon](https://falcon.readthedocs.io/en/stable/)というものがあります。

## 特徴

Falconの設計思想としては以下の4点があります。

- 高速
- 信頼性がある
- 柔軟性
- デバッグのしやすさ

## 主なサードパーティー

公式が載せている主な使うサードパーティーモジュールです。

[Add on Catalog](https://github.com/falconry/falcon/wiki/Add-on-Catalog)
こちらにあるよく使うものを以下に載せます

- [falcon-cors](https://github.com/lwcolton/falcon-cors/) FalconでCORSをできるようにするためのモジュール

- [falcon-auth](https://github.com/loanzen/falcon-auth) Falconで認証系の機能を加えるためのモジュール

- [falcon-multipart](https://github.com/yohanboniface/falcon-multipart) Falconが動作しているAPIに画像などのファイル等をアップロードするために必要なモジュール