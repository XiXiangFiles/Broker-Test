# [深入淺出MQTT]: v3.1.1與v5 的差異
MQTT v3.1.1 與 v5 完全相容，且提供許多Cluster 所需要的功能，如Shared Subscriptions、 User Properties等實用功能，且不會因為新增加功能造成效能低落的問題。

MQTT 起初是由 IBM 在 1999 年提出的，是針對 IoT 裝置設計的 MQ，是屬於發展許久的 MQ。主要設計的原則是：

1. Simple implementation: 可以簡單的被使用。
2. Quality of Service data delivery: 提供不同程度的Data 傳輸品質。
3. Lightweight and bandwidth efficient: 輕量化且高頻寬的效能。
4. Data agnostic: 使用者不用理會資料怎麼來。
5. Continuous session awareness: 當client中斷連線之後，可以重新連線並且訊息不會消失。

雖然起出被設計用於 IoT \(Internet of Thing\) 裝置，但目前MQ被廣泛運用在Platform因此在2019 年時MQTT正式提出v5版本更被推薦，主要就是為了platform 平台新的需求新增加功能。\(目前市面上有兩個版本，v3.1.1、v.5\) MQTT Architecture

![MQTT Architecture](https://cdn-images-1.medium.com/max/800/1*_adP484gIyNNVAvYRZDmVQ.png)

**MQTT v3.1.1 Features**

在功能面MQTT 是以 v3.1.1作為基礎的功能，而v5則是為雲服務進行擴充但也更改一些特性，如**QoS...**。MQTT與傳統意義有些許不一樣。如下比較表:

|  | **MQTT** | **TraditionalMQ** |
| :--- | :--- | :--- |
| Persistent Message | 當consumer 取的訊息之前，可設定將訊息保存在MQ中，直到被取用 | 當consumer 取的訊息之前，可設定將訊息保存在MQ中，直到被取用 |
| Distribution Ability | 透過Topic的方式可很輕鬆的進行傳遞給多個consumer | 傳統的consumer與queue是一對一的綁定，不太能分享訊息 |
| Queue Name | 使用上完全不用理會name 是否衝突的問題，只要在乎想訂閱的Topic | 須自行管理queue 的name |

**MQTT v3.1.1主要功能**有QoS、Topic、Persistent Session\(重新連線後Topic還存在\)、Retained Messages、Last Will。

## **1. Qos\(Quality of Service\):** 

代表的是發送與接收訊息的品質，可設定0-2這個區間。

* _At most once_ \(0\): Producer 就是單純發送之後不用確認是否broker有收到；Broker 發送至consumer也不會確認是否收到。

![](https://cdn-images-1.medium.com/max/800/1*fR9iCJnuoxGEZI6Zb4SGSQ.png)

* _At least once_ \(1\): Producer 就是單純發送之後會等待 **PUBACK 封包確認有收到**；同理Broker 發送至consumer也需等待**PUBACK**。

![](https://cdn-images-1.medium.com/max/800/1*0Cp2cDaXuXdMUv49JaxGKQ.png)

* _Exactly once_ \(2\): Producer 每發送訊息之後**就會進行3向交握**，確認是否有收到，併保證只收到一次；同理consumer 接收broker 訊息也是如此。

![](https://cdn-images-1.medium.com/max/800/1*rANapuhzHKjB794P7rNweg.png)

## **2. Topic**

MQTT Topic是由utf-8 編碼組成，如Http的URL的概念，透過"/"進行分階層。如下圖，myhome階層下groundfloor、livingroom、temperature等，如同REST 架構中對於URI的規範類似。

![](https://cdn-images-1.medium.com/max/800/1*FOrZN9a90ffw8CxO8NW0Pg.png)

**2.1 Topic 特殊符號:**

* ”＃”: 代表的垂直的概念，指的是該階層以下的全部Topic都訂閱， ex: myhome/groundfloor/\#，表示訂閱myhome/groundfloor/kitchen、myhome/groundfloor/livingroom、myhome/groundfloor/livingroom/..的意思。

![](https://cdn-images-1.medium.com/max/800/1*xssnk2qlEhWiU2FEk_jBuw.png)

* ”＋”: 代表水平的概念，使用該符號的階層所處的階層可以替換成任何字元。ex: 以myhome/groundfloor/+/temperature為例，”＋”可替換成kitchen、livingroom 的概念。 代表同時訂閱: myhome/groundfloor/kitchen/temperature、myhome/groundfloor/livingroom/temperature等Topic。

![](https://cdn-images-1.medium.com/max/800/1*KYgWaWcirCoUKgNMPiYzsw.png)

* ”＄”: 以此關鍵字為首的併不支援訂閱的，該關鍵字是MQTT用於輸出內部狀態的保留字。ex: $SYS/broker/clients/connected，可取得有多少裝置連線。 

## **3. Persistent Session:** 

當clinet 對MQTT 連線斷掉時，Topic 將會自動的discard。但為了解決這個問題，Persistent Serssion的設計就是為了解決這個問題而生。

有效時broker 存取的東西：

* Existence of a session \(even if there are no subscriptions\).
* 所有的subscription 。
* QoS 尚未完成傳輸的message。
* QoS 1、2 尚未傳給Client的message都會留存。
* 所有QoS 2 未完成Ack的message 。

**Persistent Session使用方式**  
就是在連線的時候需要將option的clean session 設定為false。

## **4. Retained Messages:** 

主要是在producer上的功能，發送訊息後會將訊息保持在Topic 上，使的新的加入者也可以獲取最新的息。若在沒有設定的情況下，新加入的consumer不會收到上一個以發送過的訊息。

## **5. Last Will and Testament\(lwt\)**

是在producer上的功能，當Producer斷線的時候，可指定lwt的Topic，與想要傳送的訊息。這功能主要用來debug用的，官方提供這種功能很適合放在上online and offline 的管理上。

## **MQTT v5 features and v 3.1.1 features comparison**

在這個版本中整體使用方式，MQTT v5與v3.1.1之間功能上的的差別在於 QoS 1 以上不再重傳訊息、retained messages、persistent sessions不再支援了。

1. **MQTT QoS** _v5 、v3.1_.1 之間的定義是一樣的，但v5 的版本不在TCP 連線健康的情況下重傳訊息。               原先的v3.1.1 版本若在一段時間內沒收到 ack 將會在retry，這可能造成因為效能問題導致未回傳的裝置loading 更重。
2. retained messages: v5中Message Expiry Interval用來取代此功能，可以將其設定一個時間後併刪除。
3. persistent sessions: 在v3.1.1中若中途有producer將clean session設定為true時，之前所存的message將會被一起被刪除，v5 中Session Expiry Interval 進來取代此功能。

## **MQTT v5 User Properties**

![](https://cdn-images-1.medium.com/max/800/1*Yfw6ZIl78ytsuQlFPZiuQQ.gif)

類似http header 的概念，可以在每一個訊息上加入一個property header ，consumer 端可依賴該欄位進行運用。Broker 根據consumer 所訂閱的設定進行訊息routing。

## **MQTT v5 Shared Subscriptions**

在v5的版本中，原生支援load balance的功能，consumer 可在建立連線的時候設定Broker shared選項綁定多個consumer 成為一個群組。

![](https://cdn-images-1.medium.com/max/800/1*pw7M8FeLqakSYl5TwKRv7A.gif)

## MQTT v3.1.1 v.s MQTT v5能力比較

在Intel i7 9750H、16GB RAM在Docker 環境下測試，其中使用 eclipse-mosquitto:2.0.11 Image 作為MQTT broker。由於MQTT v5的版本在Open Source 社群上並未完整支援，以[Eclipse MQTT ](https://www.eclipse.org/paho/index.php?page=downloads.php)社群為例，目前完整支援MQTT v5的只有Java、Python、C/C++等三種。

![](https://gblobscdn.gitbook.com/assets%2F-MZBn9owI5fBe0HrECdk%2F-MeDeVwL86iNRpNpjqaK%2F-MeDf0RGNslkKBqmeVLB%2Fimage.png?alt=media&token=f274f4f9-1e64-441f-ad3c-47103ceff7e0)

但實際使用Java、Python 發現並未完全支援，只有C語言有完整支援，如下圖所示。因此在實驗的部份採用Mosquitto 所提供的mosquitto\_pub 作為Publisher；使用npm 平台的mqtt v4.2.6版本作為Subscriber進行實做。由於Nodejs該模組在publish 的部份，會因Nodejs中的Event 排程受到影響，因此只使用Subscriber 功能。

![](https://gblobscdn.gitbook.com/assets%2F-MZBn9owI5fBe0HrECdk%2F-MeDfQhhC4ZlfuNSsALE%2F-MeDhCHOUdXOGTx56zwc%2Fimage.png?alt=media&token=11b48491-3029-4d38-ab2c-11e61514dde5)

實驗分為兩種測試，**吞吐量測試\(TPS\)、精準度測試\(QoS\)**。_**吞吐量測試**_分為Publisher與Subscriber 兩種角色，在_Publisher 的配置以1、3、5、7、10 個Publisher_ 進行測試；Subscriber 同 Publisher ，_分成1、3、5、7、10 個_ Subscriber的場景配置，**將發送100萬個封包計算平均每秒的吞吐量**。_**精準度測試的部份**_，_配置分成1、3、5、7、10 個_ Subscriber_與1個 Publisher進行測試，將發送100萬個訊息，平均計算每個Subscriber收到的數量_。

* 吞吐量測試(TPS): TPS = Requests/Per Second 
* 精準度測試(Qos) Precision=  sum(Correct Request)/Requests 

### 測試1- \[1, 3, 5, 7 ,10 \] publisher + 1 subscriber 

當Publisher 增加時，Publisher TPS 明顯的下降，但Subscriber TPS 則線性成整且QoS不變，代表著mosquitto不會因為封包數量變大，造成不一樣的Qos。換句話說Client \(Publisher\) 之間並不會互相影響Subscriber所收集到的資訊。

![](https://gblobscdn.gitbook.com/assets%2F-MZBn9owI5fBe0HrECdk%2F-MeIlSRV8qKAbe_6hiAN%2F-MeInRtWLZQFLLcxS__V%2Fimage.png?alt=media&token=9e70fd99-6aa4-4a10-b5be-a234d19a6ee8)

### **測試2- 1 publisher + \[1, 3, 5, 7 ,10 \]  subscriber**

當Subscriber 增加時，Publisher TPS 並沒有什麼改變，且Subscriber TPS、QoS也不變，代表著mosquitto不會因為封包數量變大，造成不一樣的Qos。換句話說Client \(Subscriber\)之間並不會互相影響。

![](https://gblobscdn.gitbook.com/assets%2F-MZBn9owI5fBe0HrECdk%2F-MeIlSRV8qKAbe_6hiAN%2F-MeIo2CQBOHRAwXEl0IG%2Fimage.png?alt=media&token=04249116-f213-4339-8244-5662c5f5d2fb)

### **測試3- 1 publisher + 1 subscriber，以一次1000、10,000、40,000、70,000、100,000 送出訊息，達1,000,000 條訊息後，紀錄TPS、QoS取平均值。**

在Publisher當一次傳輸的封包變少時，TPS、QoS 會以指數的方式成長。一次的數量超過極限的吞吐量，則會造成Subscriber QoS下降，因為mosquitto 預設機制為當QoS > 0時，broker內部給單一個Client的內存queue封包數量為1000條訊息。因此只要超過一定的吞吐量會造成QoS降低。同時訊息數量大，會造成壅塞的情形，使Publisher、Subscriber 的 TPS 受到影響。

![](https://gblobscdn.gitbook.com/assets%2F-MZBn9owI5fBe0HrECdk%2F-MeIW1yMF003P-xZuz0F%2F-MeIl2b7OTQ2SrWW9Y_e%2Fimage.png?alt=media&token=473db978-083a-47b1-a442-36c898cfe8f1)

Subscriber 與 Publisher 都以QoS 為2的狀態下盡情測試，mosquitto 以預設值進行量測。發現MQTT v3.11、v5 並未有明顯差異，且v5的效能些微比v3來的弱一點。_**且透過上述實驗可得到以下幾點結論:**_

1. 使用MQTT時，未必將QoS調整到越高越好，由於當QoS > 0時 Broker將會限制client緩存Queue，就有可能發生Publisher 送出的資料被Broker捨棄的問題，以致實際QoS降低。
2. MQTT Broker並不這麼適合用來當Micro Service中的Broker，由於無法正確預期資料的傳輸，有可能因此導致重要的錯誤。
3. 在大部分情況建議MQTT的QoS設置為0會更好，由於MQTT本基於TCP，因此保證其一定會送至或傳輸到目的地。然而若 QoS > 0則會因為一些確認機制導致變慢，使得TPS、QoS 不如預期。

## 結論

MQTT v3.1.1、 v5效能並未有大的差異，且v5的版本提供更多的功能。雖然官方文件上所述QoS的實作方面有受到調整，但經過測試後並未有大的差異，但市場上的所提供的工具目前很少，相信未來MQTT v5的版本是比v3.1.1來的更好更實用的。

## 參考資料
[MQTT 文章](https://www.hivemq.com/)
[MQTT　Client 工具](https://www.eclipse.org/paho/)