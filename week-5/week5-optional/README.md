## 使⽤終端機 Command Line 介⾯連結到 MySQL 伺服器中進⾏管理，進階版！

- **建立新資料表紀錄留⾔資訊，取名字為 message**

  - 輸入：

  ```mysql
  	use `website`;
  	CREATE TABLE `message` (
  	`id` bigint PRIMARY KEY AUTO_INCREMENT,
  	`member_id` bigint NOT NULL,
  	`content` varchar(255) NOT NULL,
  	`like_count` Int unsigned NOT NULL DEFAULT 0,
  	`time` datetime NOT NULL DEFAULT NOW(),
  	FOREIGN KEY(member_id) REFERENCES member(id)
  	);
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/message.jpg)

- **確認新建立的資料表資訊**

  - 輸入：

  ```mysql
  	DESC `message`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/descmess.jpg)

  - 輸入：

  ```mysql
  	SHOW TABLES;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/showtables.jpg)

- **確認上次建立的 member 資料表**

  - 輸入：

  ```mysql
  	SELECT * FROM `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/allmember.jpg)

- **一次新增多筆資料到 message 資料表**

  - 輸入：

  ```mysql
  	INSERT INTO `message` (member_id, content, like_count, time)
  	VALUES (1, 'A產品有現貨嗎', 30, '2022-10-20 10:10:44'),
  	(4, '下單後什麼時候會出貨', 150, '2018-04-18 18:14:30'),
  	(1, 'B產品效果不錯', 100, '2022-10-22 10:13:30'),
  	(5, '可以指定出貨日期嗎', 40, '2021-10-30 16:16:30'),
  	(2, 'C產品會補貨嗎', 430, '2018-08-28 20:10:26'),
  	(3, 'D產品有什麼功效', 200, '2019-05-18 12:17:30');
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/insertmess.jpg)

- **確認 message 資料表裡新增的資料**

  - 輸入：

  ```mysql
  	SELECT * FROM `message`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/allmess.jpg)

- **取得所有留⾔，結果須包含留⾔者會員的姓名**

  - 輸入：

  ```mysql
  	SELECT member.name, message.content FROM member
  	INNER JOIN message on member.id=message.member_id;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/messcontent.jpg)

- **取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名**

  - 輸入：

  ```mysql
  	SELECT member.name, message.content FROM member
  	INNER JOIN message on member.username='test' and member.id=message.member_id;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/messcontest.jpg)

- **取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數**
  - 輸入：
  ```mysql
  	SELECT AVG(`like_count`) FROM `message`
  	INNER JOIN member on member.username='test' and member.id=message.member_id;
  ```
  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-optional/images/avgliketest.jpg)
