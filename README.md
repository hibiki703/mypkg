# mypkg
![test](https://github.com/hibiki703/mypkg/actions/workflows/test.yml/badge.svg)

このパッケージは、talkerが0.5秒刻みで0から順にカウントした整数をlistenerが受け取り表示させるものである。

## 使用方法
### 端末を2つでおこなう方法
#### ①
以下のコマンドをターミナル上で実行する。
```
git clone https://github.com/hibiki703/mypkg.git
```
#### ②
 ①を実行後、以下のコマンドをターミナル上で実行する。
```
ros2 run mypkg talker
```
※②の実行後なにも表示されないので、そのままにしておく。

#### ③
 ②を実行後、別端末を用意し、そこで以下のコマンドをターミナル上で実行する。
```
ros2 run mypkg listener
```
そうすると実行結果が表示される。


### 端末1つでおこなう方法
以下のコマンドをターミナル上で実行する。
```
ros2 launch mypkg talk_lasten.launch.py
```
そうすると実行結果が表示される。


## 必要なソフトウェア
* Python 3.8.10
* ROS 2 foxy

## テスト環境
*Ubuntu 20.04

## 著作権/ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布および使用が許可されます。
* ©2023 Hibiki Iida
