import os
import subprocess

import boto3

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET = os.getenv('AWS_S3_BUCKET')
AWS_S3_KEY = os.getenv('AWS_S3_KEY')
DUMP_FILENAME = '/tmp/backup.pgdump'

s3 = boto3.resource('s3')


class S3PostgresDump(object):
    def handle(self):
        self.download_dump(DUMP_FILENAME)
        s3.meta.client.upload_file(DUMP_FILENAME, AWS_S3_BUCKET, AWS_S3_KEY)

    def download_dump(self, filename):
        command = [
            'pg_dump',
            '-vwf',
            filename,
            '--format=custom',
        ]
        completed = subprocess.run(command)
        completed.check_returncode()
