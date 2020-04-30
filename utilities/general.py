import logging, os, json, csv


def main():

    return None


def init_logging(log_file='log_filename.txt'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug('This is a test log message.')

    return logger


def write_to_json(usage_detail_dict, json_file):
    usage_json = json.dumps(usage_detail_dict)
    with open(json_file, "a") as file:
        file.write(usage_json)
        file.write(",")

    return None


def write_to_csv(usage_detail_dict, csv_file, header):
    preexist = os.path.exists(csv_file)
    with open(csv_file, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        if not preexist:
            writer.writeheader()

        writer.writerow(usage_detail_dict)

    return None


if __name__ == '__main__':
    main()