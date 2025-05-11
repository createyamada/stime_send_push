# ssh接続設定（VPC）コンソールにて実行
```
// ファイアウォールの設定
$ sudo firewall-cmd --permanent --add-port=22/tcp
$ sudo firewall-cmd --reload
$ sudo systemctl restart firewalld


// サービス起動確認
$ sudo systemctl status sshd

// activeでない場合
$ sudo systemctl start sshd
$ sudo systemctl enable sshd

// sshポートの確認
$ grep Port /etc/ssh/sshd_config

// 22でない場合
$ ssh -p <ポート番号> root@[IPアドレス]
```


# CentOSユーザ作成
```
// 前提rootユーザでのログイン
$ useradd [利用ユーザ名]
$ passwd [利用ユーザ名]
// プロンプトに従ってパスワードを設定
```

# ユーザをwheelグループに追加する
```
$ gpasswd -a [利用ユーザ名] wheel
```

# wheelグループに属するユーザがsudoコマンドを利用できるようにする
```
$ visudo

開かれたテキストで下記部分を修正

  ## Allows people in group wheel to run all commands
  # %wheel ALL=(ALL) ALL     // この行の先頭にある # を消す
```


# sudoコマンドを制限する
```
$ vim /etc/pam.d/su

開かれたテキストで下記部分を修正
  #auth required pam_wheel.so use_uid     // この行の先頭にある # を消す
```

# 上記までの内容を確認する
```
// rootから作成したユーザに切り替える
$ su [利用ユーザ名]

// sudoが利用できることを確認する（”hello”と表示されればOK）
$ sudo echo hello

// rootユーザに戻る
$ exit

// conoHaとの接続を終了する
$ exit

// 一般ユーザとしてログインできることを確認する
$ ssh [利用ユーザ名]@[IPアドレス]
```

# セキュリティー強化
```
// ホームディレクトに移動
$ cd ~/

// .ssh ディレクトリを作成
$ mkdir .ssh

// .ssh ディレクトリの権限を 700 に変更
$ chmod 700 .ssh

// .ssh ディレクトリに移動
$ cd .ssh

// 鍵を生成
$ ssh-keygen -t rsa -b 2048

  Enter file in which to save the key: [任意の鍵名を入力]
  Enter passphrase: [そのままEnterを押すか、パスワードを入力]
  Enter same passphrase again: [もう一度同じ入力をする]

$ chmod 600 [鍵名].pub
```

# リモートSSH設定を変更する
```
$ sudo vim /etc/ssh/sshd_config

  // 以下の行を探して、コメントを解除したり値を書き換えてください。

  // RSA認証を許可する
  RSAAuthentication yes

  // 公開鍵での認証を許可する
  PubkeyAuthentication yes

  // 公開鍵のファイル場所を指定する
  AuthorizedKeysFile .ssh/[鍵名].pub

  // パスワードでのログインを禁止する
  PasswordAuthentication no

  // root へ直接ログインを禁止する
  PermitRootLogin no

// SSH設定を反映する
$ sudo systemctl restart sshd.service
```

#　秘密鍵を保存する
```
// 秘密鍵を表示 (表示されたら全てコピーしてください)
$ cat .ssh/[鍵名]

// ConoHa との接続を終了する
$ exit

// ローカルの .ssh ディレクトリへ移動
$ cd ~/.ssh

$ vim [鍵名]

  // vim が起動したら、先程コピーした秘密鍵をペーストします
  -----BEGIN RSA PRIVATE KEY-----
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX...
  -----END RSA PRIVATE KEY-----

// 鍵のパーミッションを600に変更
$ chmod 600 [鍵名]
```

# ローカルのSSHの設定を変更する
```
// ディレクトリ移動
$ cd ~/.ssh

// SSH の設定を追加する
$ vim config

  // 編集して以下の内容を入力する
  Host [任意の接続先名]
    HostName [IPアドレス]
    User [ユーザー名]
    Port 22
    IdentityFile ~/.ssh/[鍵名]

// root でログインできないことを確認する
$ ssh root@[IPアドレス]

// 接続先名だけで接続できることを確認する
$ssh [接続先名]
```



# システムを最新にする
```
// システムを最新にする
$ sudo yum -y update
```

# Dockerのインストール
```
$ sudo yum update -y
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ sudo yum install -y docker-ce docker-ce-cli containerd.io
$ sudo yum install httpd-tools

$ docker compose version
```

# Docker起動と自動起動設定
```
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

# Docker Composeインストール
```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

# ローカルのディレクトリをVPSにアップロードする
```
scp -r ./[アップロードしたいディレクトリ] [利用ユーザ名]@[IPアドレス]:[コピー先パス]
```


# コンソール画面の認証に利用するパスワードの設定
```
$ htpasswd -c htpasswd admin
```


#　コンテナ起動
```
$ sudo docker-compose up --build
```
