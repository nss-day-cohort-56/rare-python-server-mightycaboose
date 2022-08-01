CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Fun');
INSERT INTO Categories ('label') VALUES ('Mirth');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'created_on', 'active') VALUES ('Carlos', 'Murphey', 'murphey37@gmail.com', 'its me, carlos', 'CarlosMurphey', 'iamcarlos', '2022-07-26 11:21:52.741174', '1');
INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES (1, 1, 'it is a comment');
INSERT INTO DemotionQueue ('action', 'admin_id', 'approver_one_id') VALUES ('do not demote', 1, 2);
INSERT INTO PostReactions ('user_id', 'reaction_id', 'post_id') VALUES (1, 1, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1);
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content', 'approved') VALUES (1, 1, 'the first one', '2022-07-26 11:21:52.741174', 'look at all this content', 1);
INSERT INTO Reactions ('label') VALUES ('Oh My');
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on')  VALUES (1,1, '2022-07-26 11:21:52.741174');
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content', 'approved') VALUES (1, 2, 'the second one', '2022-07-26 12:21:52.741174', 'look at all this other stuff and content', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content', 'approved') VALUES (1, 3, 'the third one', '2022-07-26 08:21:52.741174', 'look at this. it''s a third stuff!', 1);

DELETE FROM Categories WHERE id = 2
DELETE FROM Users WHERE id = 2
DELETE FROM Posts WHERE user_id = 2

INSERT INTO Categories ('label') VALUES ('Fun');
INSERT INTO Categories ('label') VALUES ('Mirth');
INSERT INTO Categories ('id','label') VALUES ('1', 'Merriment');


INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content', 'approved') VALUES (2, 1, 'the first one from a different user', '2022-07-26 11:21:52.741174', 'look at all this content', 1);
INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'created_on', 'active') VALUES ('Carlos', 'Murphey', 'murphey37@gmail.com', 'its me, carlos', 'CarlosMurphey', 'iamcarlos', '2022-07-26 11:21:52.741174', '1');
