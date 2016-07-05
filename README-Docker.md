Commands for docker
============================

# DockerでWebアプリを開発

## dbとwebを起動

```
docker-compose up -d
```

`-d` オプションでバックグラウンド実行。
このオプションを指定しないと、フォアグラウンド実行になるので、Ctrl+C などで停止すると
コンテナが終了する。

## webだけ再起動

Docker越しの開発ではファイルの変更を検知してくれないので、コード変更の適用のために手動で再起動する必要がある。

```
docker-compose restart web
```

## dbとwebを停止 & 起動

```
docker-compose stop
docker-compose start
```

ホストOS起動時はコンテナが停止しているので、startする必要がある
ホストOSを停止するときにはコンテナはstop状態になる。


## dbとwebのコンテナを削除

dbのデータはコンテナ内にあるので、削除するとデータが消えます。
webのコンテナは内部にアップロードされたファイルを持っているので、削除するとデータが消えます。

```
docker-compose down
```



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

# 細かいコマンドライン手順

## pyconjp-website Dockerイメージビルド

```
docker build -t pyconjp/website:2016 .
```

## pyconjp-website コンテナ起動手順

```
docker run -it --rm -e DEBUG= -e DB_HOST=postgres -e DB_USER=postgres -e DB_PASSW
ORD=pass -e DB_NAME=pyconjp2016 -e DB_ENGINE=postgresql_psycopg2 -e DB_PORT=5432 -p 8000:8000 --link postgres1:postgres
pyconjp/website:2016
```

