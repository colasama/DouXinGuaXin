CREATE TABLE User(
User_id int PRIMARY KEY,
User_password varchar(20) not null, -- Î´Ìí¼ÓÔ¼Êø
User_name varchar(20) not null unique,
User_email varchar(20) not null unique,	-- Î´Ìí¼ÓÔ¼Êø
User_phonenum decimal(11,0) not null unique,
User_authority int check(User_authority >= 0 and User_authority <= 3),
User_motto varchar(20)
)
CREATE TABLE Books(
Book_id int PRIMARY KEY,
Book_name varchar(50) not null,
Book_intro varchar(100) not null,
Book_score decimal(2,1) check(Book_score >= 0 and Book_score <= 10),
Book_ISBN decimal(10,0) not null unique,
Book_writer varchar(10) not null,
Book_publisher varchar(15) not null,
Book_src varchar(50) not null
)
CREATE TABLE Movies(
Movie_id int PRIMARY KEY,
Movie_name varchar(50) not null,
Movie_intro varchar(100) not null,
Movie_score decimal(2,1) check(Movie_score >= 0 and Movie_score <= 10),
Movie_director varchar(10) not null,
Movie_src varchar(50) not null
)
CREATE TABLE Book_Comments(
Book_comment_id int PRIMARY KEY,
Book_commit_title varchar(20) not null,
Book_commit_approve int,
Book_commit_disapprove int,
Book_commit_content varchar(200) check(len(Book_commit_content) > 25),
User_id int,
Book_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Book_id) REFERENCES Books(Book_id)
)
CREATE TABLE Movie_Comments(
Movie_comment_id int PRIMARY KEY,
Movie_commit_title varchar(20) not null,
Movie_commit_approve int,
Movie_commit_disapprove int,
Movie_commit_content varchar(200) check(len(Movie_commit_content) > 25),
User_id int,
Movie_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id)
)
CREATE TABLE Topics(
Topic_id int PRIMARY KEY,
Topic_name varchar(20) not null,
Users_num int not null,
Topic_related varchar(200),
Topic_intro varchar(100) not null
)
CREATE TABLE Topic_Contents(
Topic_content_id int PRIMARY KEY,
Topic_content_content varchar(200) not null,
Topic_content_image varchar(200),	-- Í¼Æ¬Â·¾¶
Topic_id int,
User_id int,
FOREIGN KEY (Topic_id) REFERENCES Topics(Topic_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
)
CREATE TABLE Groups(
Group_id int PRIMARY KEY,
Group_name varchar(20) not null,
Group_related varchar(200),
Group_intro varchar(100) not null,
Users_num int,
User_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id)
)
CREATE TABLE Group_Contents(
Group_content_id int PRIMARY KEY,
Group_content_content varchar(200) not null,
Group_content_title varchar(20) not null,
Group_id int,
User_id int,
FOREIGN KEY (Group_id) REFERENCES Groups(Group_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
)
CREATE TABLE Book_Reports(
Book_report_id int PRIMARY KEY,
Book_report_title varchar(20) not null,
Book_report_reason varchar(100) check(len(Book_report_reason) > 15),
User_id int,
Book_comment_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Book_comment_id) REFERENCES Book_Comments(Book_comment_id)
)
CREATE TABLE Movie_Reports(
Movie_report_id int PRIMARY KEY,
Movie_report_title varchar(20) not null,
Movie_report_reason varchar(100) check(len(Movie_report_reason) > 15),
User_id int,
Movie_comment_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Movie_comment_id) REFERENCES Movie_Comments(Movie_comment_id)
)
CREATE TABLE User_Topic(
Topic_id int,
User_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Topic_id) REFERENCES Topics(Topic_id)
)
CREATE TABLE User_Group(
Group_id int,
User_id int,
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Group_id) REFERENCES Groups(Group_id)
)