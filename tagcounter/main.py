import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='details',
                                     usage = 'use "%(prog)s --help" for more information',
                                    formatter_class = argparse.RawTextHelpFormatter)

    # Exclude put both arguments - only one of [ get / view ] allowed
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--get', type=str, help='''Query data from remote site. 
Usage: 
    With tag: --get "ydx"  
    With Url: --get "yandex.ru"  
                        '''
                        )
    group.add_argument('--view', type=str, help='Get data saved in DB. Usage: --view "yandex.ru"')

    if len(sys.argv) == 1:
        print('GUI mode')
    else:
        res = parser.parse_args()
        print("TUI mode")
