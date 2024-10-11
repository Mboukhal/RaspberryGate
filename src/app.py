from local import get_access
from time import sleep


def main():
  while True:
    get_access.init_db()
    access = get_access.get_access('RQ8YRYBF')
    print(access)
    sleep(1)
  get_access.close_db()


if __name__ == '__main__':
  main()