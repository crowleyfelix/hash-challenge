import logging

FORMATTERS = {
    "simple": {
        "format": ("[%(asctime)s] [rid: %(request_id)s] [cid: %(application_source)s] "
                   "[pid: %(process)d] [%(name)s] %(levelname)s: %(message)s"),
        "datefmt": "%Y-%m-%d %H:%M:%S %z",
        "class": "logging.Formatter",
        "validate": False
    },
    "access": {
        "format": ('%a %t [%s] "%r" %b "%{Referer}i" "%{X-Forwarded-Proto}i" '
                   '"%{X-Forwarded-For}i" "%{X-Forwarded-Port}i" "%{User-Agent}i"'),
        "validate": False
    }
}


def set_up(config):
    logging.basicConfig(config)
