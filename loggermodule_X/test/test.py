from loggermodule_X.loggermodule_X import configLogger

log = configLogger(__name__, __file__, console_lv='INFO', file_lv='INFO')

log.info('1st LINE !!!!!')
while True:
    log.info('INFO')
    log.debug('DEBUG')
    log.error('ERROR')
    log.warning('WARNING')
    True
