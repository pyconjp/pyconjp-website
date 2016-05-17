Commands for docker
============================

# 依存パッケージのwheel化

このプロジェクトは、wheelhouseディレクトリに本番で利用する依存パッケージを
whlファイルフォーマットで同梱しています。これによって、外的要因による
インストールエラーを防ぎ、環境構築を高速化しています。

以下の手順で、依存パッケージをあらかじめwheel化してwheelhouseディレクトリに入れます。
依存パッケージを追加、更新、削除したら以下の手順でwheelhouseを更新してください。

```
docker build -f Dockerfile.wheel -t pyconjp/wheelhouse:2016 .
docker run -it --rm -v `pwd`/wheelhouse:/app/wheelhouse:ro -v `pwd`/wheelhouse_new:/app/wheelhouse_new pyconjp/wheelhouse:2016
rm -R wheelhouse
mv wheelhouse_new wheelhouse
```

