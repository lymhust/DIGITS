# Copyright (c) 2014-2016, NVIDIA CORPORATION.  All rights reserved.

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='DIGITS development server')
    parser.add_argument('-p', '--port',
            type=int,
            default=5000,
            help='Port to run app on (default 5000)'
            )
    parser.add_argument('-d', '--debug',
            action='store_true',
            help='Run the application in debug mode (reloads when the source changes and gives more detailed error messages)'
            )
    parser.add_argument('--version',
            action='store_true',
            help='Print the version number and exit'
            )

    args = vars(parser.parse_args())

    import digits

    if args['version']:
        print digits.__version__
        sys.exit()

    print '  ___ ___ ___ ___ _____ ___'
    print ' |   \_ _/ __|_ _|_   _/ __|'
    print ' | |) | | (_ || |  | | \__ \\'
    print ' |___/___\___|___| |_| |___/', digits.__version__
    print

    import digits.config
    import digits.log
    import digits.webapp

    try:
        if not digits.webapp.scheduler.start():
            print 'ERROR: Scheduler would not start'
        else:
            digits.webapp.app.debug = args['debug']
            digits.webapp.socketio.run(digits.webapp.app, '0.0.0.0', args['port'])
    except KeyboardInterrupt:
        pass
    finally:
        digits.webapp.scheduler.stop()


if __name__ == '__main__':
    main()
