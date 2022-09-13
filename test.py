from loggermodulex import configLogger

log = configLogger(__name__, __file__, console_lv='INFO', file_lv='ERROR')

log.info('INFO')
log.debug('DEBUG')
log.error('ERROR')
log.warning('WARNING')
