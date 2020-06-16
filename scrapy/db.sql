CREATE TABLE subjects(
    id int(10) unsigned NOT NULL AUTO_INCREMENT,
    douban_id int(10) unsigned NOT NULL DEFAULT 0,
    movie_name varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    star float NOT NULL DEFAULT 0.0,
    description varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY subjects_douban_id_unique (douban_id)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE comments(
    id int(10) unsigned NOT NULL AUTO_INCREMENT,
    douban_id int(10) unsigned NOT NULL DEFAULT '0',
    douban_comment_id int(10) unsigned NOT NULL DEFAULT '0',
    douban_username varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    content text COLLATE utf8mb4 NOT NULL,
    rating varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    comment_time varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    created_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY id,
    KEY comments_douban_id_index douban_id,
    KEY comments_douban_comment_id_index douban_comment_id
) ENGINE =InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSE=utf8mb4 COLLATE=utf8mb4_unicode_ci;