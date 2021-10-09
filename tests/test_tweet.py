import argparse
import logging

from ShiningArmor import twitter
from ShiningArmor import sqliteDB as DB

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


def get_cmd_line_args():
    # parse the command line arguments
    ap = argparse.ArgumentParser()

    ap.add_argument("-t", "--tokens_file", required=True)
    ap.add_argument("-d", "--db_file", required=True)
    ap.add_argument("-s", "--sql_file", required=True)
    ap.add_argument("-ht", "--hash_tag", required=True)

    args = vars(ap.parse_args())

    for i in args:
        logging.info(f'Command line argument {i}={args[i]}')

    return args


if __name__ == "__main__":
    # Parse command line arguments
    args = get_cmd_line_args()

    # Get DB connection
    (db, rc) = DB.connect(args['db_file'])

    if rc == 0:
        # Get SQL statements
        (sql_stmt, rc) = DB.sqlstmt(args['sql_file'])

    if rc == 0:
        # 1. Parse the SQL and replace with dynamic value
        # 2. Prepare & Execute SQL
        sql_stmt['select'] = str(sql_stmt['select']).replace('ZZZ', f"{args['hash_tag']}")
        logging.debug(f"SQL: {sql_stmt['select']}")

        (rec, rc) = DB.select(db, sql_stmt)
    if rc == 0:
        (rowid, msg) = (rec[0], rec[1])
        logging.debug(f'rowid - {rowid}, msg - {msg}')

        # Append the hash tag to the tweet message
        msg = f'{msg} \n\n#{args["hash_tag"]}'

    try:
        tokens = twitter.tokens(args['tokens_file'])
        api = twitter.auth(tokens)
        # twitter.tweet(api, msg)
        logging.debug(f'Message: {msg}')
        logging.info('Successfully sent the TWEET')
    except Exception as err:
        logging.error(err)
        rc = 1
    finally:
        if rc == 0:
            # Update DB:
            #   - parse the SQL and replace with dynamic value
            sql_stmt['update'] = str(sql_stmt['update']).replace('ZZZ', f'{rowid}')
            logging.debug(sql_stmt['update'])

            DB.update(db, sql_stmt)

        # Close DB connection
        DB.close(db)
