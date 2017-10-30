# coding: utf-8

import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import NoHostProvided

connection = None

def get_connection(context):
    conn = connection
    if conn is None:
        if context.config.get('AWS_ROLE_BASED_CONNECTION', default=False):
            conn = S3Connection()
        else:
            conn = S3Connection(
                aws_access_key_id = context.config.get('AWS_ACCESS_KEY'),
                aws_secret_access_key = context.config.get('AWS_SECRET_KEY'),
                host = context.config.get('AWS_HOST', default=NoHostProvided),
                port = context.config.get('AWS_PORT', default=None),
                is_secure = context.config.get('AWS_IS_SECURE', default=False),
                calling_format = boto.s3.connection.OrdinaryCallingFormat()
            )

    return conn