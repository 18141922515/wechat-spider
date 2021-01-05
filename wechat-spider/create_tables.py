# -*- coding: utf-8 -*-

from db.mysqldb import MysqlDB
from config import config


def _create_table(mysqldb, sql):
    mysqldb.execute(sql)


def create_table():
    wechat_article_list_table = '''
    CREATE TABLE IF NOT EXISTS `wechat_article_list` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `digest` varchar(2000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `publish_time` datetime DEFAULT NULL,
      `spider_time` datetime DEFAULT NULL,
      `author` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `url` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `__biz` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `sn` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `source_url` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `cover` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `subtype` int(11) DEFAULT NULL,
      `is_multi` int(11) DEFAULT NULL,
      `copyright_stat` int(11) DEFAULT NULL,
      `duration` int(11) DEFAULT NULL,
      `del_flag` int(11) DEFAULT NULL,
      `type` int(11) DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `sn` (`sn`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC
    '''

    wechat_article_task_table = '''
    CREATE TABLE IF NOT EXISTS `wechat_article_task` (
      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
      `sn` varchar(50) DEFAULT NULL,
      `article_url` varchar(255) DEFAULT NULL,
      `state` int(11) DEFAULT '0' COMMENT '文章抓取状态，0 待抓取 2 抓取中 1 抓取完毕 -1 抓取失败',
      `__biz` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `sn` (`sn`) USING BTREE,
      KEY `state` (`state`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    '''


    wechat_article_table = '''
    CREATE TABLE IF NOT EXISTS `wechat_article` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `data_address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `data_source_type` varchar(64) DEFAULT NULL,
      `data_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `collection_mode` varchar(64) DEFAULT NULL,
      `spider_name` varchar(64) DEFAULT NULL,
      `collection_time` datetime DEFAULT NULL,
      `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `publish_time` datetime DEFAULT NULL,
      `text` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `author` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `__biz` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `sn` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `sn` (`sn`),
      KEY `__biz` (`__biz`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC
    '''

    wechat_account_task_table = '''
    CREATE TABLE IF NOT EXISTS `wechat_account_task` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `__biz` varchar(50) DEFAULT NULL,
      `last_publish_time` datetime DEFAULT NULL COMMENT '上次抓取到的文章发布时间，做文章增量采集用',
      `last_spider_time` datetime DEFAULT NULL COMMENT '上次抓取时间，用于同一个公众号每隔一段时间扫描一次',
      `is_zombie` int(11) DEFAULT '0' COMMENT '僵尸号 默认3个月未发布内容为僵尸号，不再检测',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    '''

    wechat_account_table = '''
    CREATE TABLE IF NOT EXISTS `wechat_account` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `__biz` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `account` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `head_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `summary` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `qr_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `verify` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `spider_time` datetime DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `__biz` (`__biz`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC
    '''

    if config.get('mysqldb').get('auto_create_tables'):
        mysqldb = MysqlDB(**config.get('mysqldb'))
        _create_table(mysqldb, wechat_article_list_table)
        _create_table(mysqldb, wechat_article_task_table)
        _create_table(mysqldb, wechat_article_table)
        _create_table(mysqldb, wechat_account_task_table)
        _create_table(mysqldb, wechat_account_table)
