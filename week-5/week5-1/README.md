## Let's use Command Line to connect MySQL and input for the operation of SQL syntax！

- **Log in MySQL**

  - Open Command Line, input "**mysql -u root -p**" and **password**.
  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/login.jpg)

- **Create DATABASE**

  - Input：

  ```mysql
  	CREATE DATABASE `website`;
  ```

  - Modify the name of website that you want.
  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/createDB.jpg)

- **Confirm the created database**

  - Input：

  ```mysql
  	SHOW DATABASES;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/showDB.jpg)

- **USE DATABASE & CREATE TABLE**

  - Set up the column of the data, data types, and storages.
  - Input：

  ```mysql
  	use `website`;
  	CREATE TABLE `member` (
  	`id` bigint AUTO_INCREMENT,
  	`name` varchar(255) NOT NULL,
  	`username` varchar(255) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`follower_count` Int unsigned NOT NULL DEFAULT 0,
  	`time` datetime NOT NULL DEFAULT NOW(),
  	 PRIMARY KEY(id)
  	);
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/createtable.jpg)

- **Confirm the created table**

  - See the information below to confirm the setting.
  - Input：

  ```mysql
  	DESC `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/descmember.jpg)
  - Input：

  ```mysql
  	SHOW TABLES;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/login.jpg)

- **Insert into the data**

  - Input：

  ```mysql
  	INSERT INTO `member` (name, username, password, follower_count, time)
  	VALUES ("Kim", "test", "test", 30, NOW());
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/insert1data.jpg)

- **Insert into a lot of data all at once.**

  - Input：

  ```mysql
  	INSERT INTO `member` (name, username, password, follower_count, time)
  	VALUES ("Mary", "MM", "mary", 300, "2018-07-09 15:10:44"),
  	("Bob", "BB", "bob", 1000, "2019-04-18 17:13:30"),
  	("Amy", "AA", "amy", 10, "2018-03-22 22:13:26"),
  	("Jim", "JJ", "jim", 600, "2021-09-18 17:13:30");
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/insert4data.jpg)

- **Select from all data of member**

  - Input：

  ```mysql
  	SELECT * FROM `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/selectall.jpg)

- **Select from all data of member, according to the column of time and sort in a reverse chronological order.**

  - Input：

  ```mysql
  	SELECT *
  	FROM `member`
  	ORDER BY `time`
  	DESC;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/time.jpg)

- **As described on the previous requirements, get 2~4 member records after sorting.**

  - Input：

  ```mysql
  	SELECT *
  	FROM `member`
  	ORDER BY `time`
  	DESC
  	LIMIT 1, 3;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/time234.jpg)

- **To get the data which the username of member equal "test".**

  - Input：

  ```mysql
  	SELECT *
  	FROM `member`
  	WHERE `username` ='test';
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/test.jpg)

- **As described on the previous requirements, get the data which the password of member also equal "test".**

  - Input：

  ```mysql
  	SELECT *
  	FROM `member`
  	WHERE `username` ='test' AND `password` ='test';
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/testtest.jpg)

- **To find the data which the username of member equal "test" and update the name to "test2".**

  - Input：

  ```mysql
  	UPDATE `member`
  	SET `name`='test2'
  	WHERE `username`= 'test';
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/test2.jpg)

- **Select from all data of member**

  - Input：

  ```mysql
  	SELECT * FROM `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/allmember.jpg)

- **To calculate how many people in the data of member.**

  - Input：

  ```mysql
  	SELECT COUNT(*) FROM `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/countmember.jpg)

- **To sum all follower_count in member.**

  - Input：

  ```mysql
  	SELECT SUM(`follower_count`) FROM `member`;
  ```

  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/follower_count.jpg)

- **To calculate the average of all follower_count in member.**
  - Input：
  ```mysql
  	SELECT AVG(`follower_count`) FROM `member`;
  ```
  - ![images](https://jiashanchang.github.io/Wehelp_Assignments/week-5/week5-1/images/avg.jpg)
