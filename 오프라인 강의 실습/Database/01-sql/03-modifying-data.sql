-- 필드 추가

ALTER TABLE 
  examples
ADD COLUMN 
  Country VARCHAR(100) NOT NULL;

ALTER TABLE 
  examples
ADD COLUMN 
  Age INTEGER NOT NULL;

ALTER TABLE 
  examples
ADD COLUMN 
  Address VARCHAR(100) NOT NULL;

ALTER TABLE 
  examples
RENAME COLUMN
  Address TO PostCode;

ALTER TABLE
  examples
DROP COLUMN 
  PostCode;

ALTER TABLE
  examples
RENAME TO
  new_examples2;

DROP TABLE new_examples2;

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(100) NOT NULL,
  createdAt DATE NOT NULL
);

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

UPDATE articles
SET title = 'update title'
WHERE id = 1;

UPDATE articles
SET 
  title = 'update title2',
  content = 'update content2'
WHERE id = 2;

DELETE FROM
  articles
WHERE
  id = 1;
SELECT * FROM articles;

DELETE FROM articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(50) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId)
    REFERENCES users(id)
);

INSERT INTO users(name)
VALUES ('하석주'), ('송윤미'), ('유하선');

INSERT INTO articles (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM articles
INNER JOIN users
  ON users.id = articles.userId;

SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE users.id = 1;

SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;


PRAGMA table_info('articles');