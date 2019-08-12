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
    group.add_argument('--view', type=str, help='Get data saved from DB. Usage: --view "yandex.ru"')

    if len(sys.argv) == 1:
        from ui.gui import Display
        ui = Display()
    else:
        res = parser.parse_args()
        from ui.tui import Display
        ui = Display()

        if res.get is not None:
            ui.get(res.get)
        if res.view is not None:
            ui.view(res.view)
        ui.show()


