import logging

class Logger:
    def dev_logger(self):
        log = logging.getLogger('job-autesearch_dev')
        if not log.handlers:
            log.setLevel(logging.DEBUG)
            file = logging.FileHandler(filename=f'dev.log', mode='a', encoding='utf-8')
            console = logging.StreamHandler()

            file.setLevel(logging.INFO)
            console.setLevel(logging.INFO)

            file.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s: %(message)s: %(filename)s:  %(lineno)d %(funcName)s:', datefmt='%d/%m  %H:%M:%S'))
            console.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s: %(message)s: %(filename)s:  %(lineno)d %(funcName)s:', datefmt='%H:%M:%S'))

            log.addHandler(file)
            log.addHandler(console)
        return log
    
    def user_logger(self):
        log = logging.getLogger('job-autesearch_user')
        if not log.handlers:
            
            log.setLevel(logging.INFO)

            file = logging.FileHandler(filename=f'Job-search-report.log', mode='a', encoding='utf-8')

            file.setLevel(logging.INFO)

            file.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s: %(message)s:', datefmt='%d/%m  %H:%M:%S'))

            log.addHandler(file)

        return log


