__author__ = 'pokey'

import getopt
import sys
from simulator import Simulator



def usage():
    print("BLABLABLA")


def main(argv):
    fname = ""
    try:
        opts, args = getopt.getopt(argv, "hf:", ["help", "file="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            fname = arg

    sim = Simulator()
    if not fname:
        print("--file (-f) option is required.")
        usage()
        sys.exit(2)
    # pr = cProfile.Profile()
    # pr.enable()

    sim.run(fname)

    # s = StringIO.StringIO()
    # sortby = 'cumulative'
    # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # ps.print_stats()
    # print s.getvalue()

if __name__ == "__main__":
    main(sys.argv[1:])