# -*- coding: utf-8 -*-

from db.mysqldb import MysqlDB
import utils.tools as tools
from utils.log import log
from config import config

db = MysqlDB(**config.get('mysqldb'))


def save_account(data):
    log.debug(tools.dumps_json(data))

    sql = tools.make_insert_sql('wechat_account', data, insert_ignore=True)
    db.add(sql)


def save_article_list(datas: list):
    log.debug(tools.dumps_json(datas))

    sql, articles = tools.make_batch_sql('wechat_article_list', datas)
    db.add_batch(sql, articles)

    # 存文章任务
    article_task = [
        {
            "sn": article.get('sn'),
            "article_url": article.get('url'),
            "__biz": article.get('__biz')
        }
        for article in datas
    ]

    sql, article_task = tools.make_batch_sql('wechat_article_task', article_task)
    db.add_batch(sql, article_task)


def save_article(data):
    log.debug(tools.dumps_json(data))

    sql = tools.make_insert_sql('wechat_article', data, insert_ignore=True)
    return db.add(sql)

