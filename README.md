Amazon Linux Container Images と Lambda
=========

準備
--------

```
$ npm install
$ $(npm bin)/sls -v
1.1.0
$
```

NG パターン
--------

```
$ cd test
$ # OSXやCentOS上で pip install した 
$ # ネイティブライブラリを使うパッケージ
$ # (ex.Pillow)はLambda上では動かない。
$ pip install -r requirements.txt -t vendor/
$ $(npm bin)/sls deploy
$ $(npm bin)/sls invoke -f hello
```

エラーが出る
```
{
    "errorMessage": "Unable to import module 'handler'"

}
```

詳細

**_imaging.so: invalid ELF header** で実行出来ない。


```
$ $(npm bin)/sls logs -f hello
START RequestId: fea3d675-a59c-11e6-9977-9db5192e5233 Version: $LATEST
Unable to import module 'handler': /var/task/vendor/PIL/_imaging.so: invalid ELF header

END RequestId: fea3d675-a59c-11e6-9977-9db5192e5233
REPORT RequestId: fea3d675-a59c-11e6-9977-9db5192e5233	Duration: 0.24 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 32 MB

```

OK パターン
--------

Amazon Linux Container Images をpullしておく
http://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html


```
$ cd test
$ rm -rf vendor/
$ docker build . -t amazon-py
$ docker run -it -v $(pwd)/vendor:/app/vendor:rw -t amazon-py
$ $(npm bin)/sls deploy
$ $(npm bin)/sls invoke -t hello
```

```
null
```

ログにもエラーが出てない
```
$ $(npm bin)/sls logs -f hello

START RequestId: e9003709-a59e-11e6-b541-0f7fe552a859 Version: $LATEST
END RequestId: e9003709-a59e-11e6-b541-0f7fe552a859
REPORT RequestId: e9003709-a59e-11e6-b541-0f7fe552a859	Duration: 169.37 ms	Billed Duration: 200 ms 	Memory Size: 1024 MB	Max Memory Used: 33 MB
```
