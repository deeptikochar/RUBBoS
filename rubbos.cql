CREATE KEYSPACE IF NOT EXISTS rubbos WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2};
USE rubbos;

CREATE TABLE categories (
	id BIGINT,
	name VARCHAR,
	PRIMARY KEY(id)
);

CREATE TABLE users (
	id BIGINT,
	firstname VARCHAR,
	lastname VARCHAR,
	nickname VARCHAR,
	password VARCHAR,
	email VARCHAR,
	rating INT,
	access INT,
	creation_date timestamp,
	PRIMARY KEY(id)
);

CREATE TABLE user_logins (
	nickname VARCHAR,
	password VARCHAR,
	id BIGINT,
	access INT,
	PRIMARY KEY(nickname, password)
);

CREATE TABLE stories (
	id BIGINT,
	title VARCHAR,
	body TEXT,
	date TIMESTAMP,
	writer BIGINT,
	category BIGINT,
	PRIMARY KEY(id, date)
)
WITH CLUSTERING ORDER BY (date DESC);

CREATE INDEX stories_category
	on stories(category);

CREATE TABLE old_stories (
        id BIGINT,
        title VARCHAR,
        body TEXT,
        date TIMESTAMP,
        writer BIGINT,
        category BIGINT,
        PRIMARY KEY(id, date)
)
WITH CLUSTERING ORDER BY (date DESC);

CREATE INDEX old_stories_category
        on old_stories(category);

CREATE TABLE submissions (
	id BIGINT,
	title VARCHAR,
        body TEXT,
        date TIMESTAMP,
        writer BIGINT,
        category BIGINT,
        PRIMARY KEY(id, date)
) 
WITH CLUSTERING ORDER BY (date DESC);

CREATE TABLE comments (
	id BIGINT,
	writer BIGINT,
	story_id BIGINT,
	parent BIGINT,
	childs BIGINT,
	rating INT,
	date TIMESTAMP,
	subject VARCHAR,
	comment TEXT,
	PRIMARY KEY(id, date)
)
WITH CLUSTERING ORDER BY (date DESC);

CREATE INDEX comments_rating
	ON comments(rating);

CREATE INDEX comments_parent
	ON comments(parent);

CREATE TABLE old_comments (
        id BIGINT,
        writer BIGINT,
        story_id BIGINT,
        parent BIGINT,
        childs BIGINT,
        rating INT,
        date TIMESTAMP,
        subject VARCHAR,
        comment TEXT,
        PRIMARY KEY(id, date)
) 
WITH CLUSTERING ORDER BY (date DESC);

CREATE INDEX old_comments_rating
	ON old_comments(rating);

CREATE INDEX old_comments_parent
        ON old_comments(parent);

CREATE TABLE moderator_log (
	id BIGINT,
	moderator_id BIGINT,
	comment_id BIGINT,
	rating INT,
	date TIMESTAMP,
	PRIMARY KEY(id)
);	

CREATE TABLE user_stories (
	nickname VARCHAR, 
	date TIMESTAMP, 
	story_id BIGINT, 
	title TEXT, 
	PRIMARY KEY(nickname, date, story_id)
) WITH CLUSTERING ORDER BY (date DESC);

CREATE TABLE comment_count (
	story_id BIGINT,
	rating INT,
	count INT,
	PRIMARY KEY(story_id, rating)
) WITH CLUSTERING ORDER BY (rating ASC);

