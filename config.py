import logging

logger = logging.getLogger('log.' + __name__)


## SMTP Configuration ##
smtp_host = ''
smtp_port = 10000
email_to = ['']
email_subject = ''
email_body = ''
email_from = ''

logger.info('SMTP parameters are set')

## SFTP Configuration ##

sftp_host = ''
sftp_port = 22
sftp_user = 'username'
sftp_pass = 'password'

logger.info('SFTP parameters are set')
#print('lets do a warning log message...')
logger.warning(f'testing a warning message from {__name__}')