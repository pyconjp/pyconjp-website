Commands for docker
============================

# 依存パッケージのwheel化

依存パッケージをあらかじめwheel化してwheelhouseディレクトリに入れておく手順です。
依存パッケージを増やした場合にもこの手順で更新します。

```
docker build -f Dockerfile.wheel -t pyconjp/wheelhouse:2016 .
docker run -it --rm -v `pwd`/wheelhouse:/app/wheelhouse:ro -v `pwd`/wheelhouse_new:/app/wheelhouse_new pyconjp/wheelhouse:2016
rm -R wheelhouse
mv wheelhouse_new wheelhouse
```

