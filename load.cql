use rubbos;
COPY users (id, firstname , lastname , nickname , password , email , rating , access , creation_date ) FROM '/home/deepti/rubbos/RUBBoS/database/users.csv';
COPY stories (id, title, body, date, writer, category) FROM '/home/deepti/rubbos/RUBBoS/database/stories.csv';
COPY old_stories (id, title, body, date, writer, category) FROM '/home/deepti/rubbos/RUBBoS/database/old_stories.csv';
COPY submissions (id, title, body, date, writer, category) FROM '/home/deepti/rubbos/RUBBoS/database/submissions.csv';
COPY comments (id, writer, story_id, parent, childs, rating, date, subject, comment) FROM '/home/deepti/rubbos/RUBBoS/database/comments.csv';
COPY old_comments (id, writer, story_id, parent, childs, rating, date, subject, comment) FROM '/home/deepti/rubbos/RUBBoS/database/old_comments.csv';
COPY moderator_log (id, moderator_id, comment_id, rating) FROM '/home/deepti/rubbos/RUBBoS/database/moderator_log.csv';
COPY user_logins (nickname, password, id, access) FROM '/home/deepti/rubbos/RUBBoS/database/user_logins.csv';
