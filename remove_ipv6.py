#!/usr/bin/python3

from ipaddress import IPv4Address, AddressValueError
#!/usr/bin/python

import sys
import getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    outfile = open(outputfile, "w")
    for line in open(inputfile, "r"):
        if is_ipv4_only(line):
            outfile.write(line)
    outfile.close()


def is_ipv4_only(addr):
    try:
        IPv4Address(addr.split('/')[0])
        return True
    except AddressValueError:
        return False


if __name__ == "__main__":
    main(sys.argv[1:])
