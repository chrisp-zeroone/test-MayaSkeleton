""" Command line utility that uses core_functionality.DataCore """
# Built-in
import sys
import argparse
import logging

# Internal
import core_functionality



def main():
    """ Parse args, and run command """

    parser = argparse.ArgumentParser(
        description="Utility to read core_functionality", 
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-n', '--name', action='store_true', help='Add node name to output')
    parser.add_argument('-p', '--parent_name', action='store_true', help='Add parent name to output')
    parser.add_argument('-c', '--color', action='store_true', help='Add color to output')
    parser.add_argument('-fl', '--flags', action='store_true', help='Add flags to output')
    parser.add_argument('-r', '--radius', action='store_true', help='Add radius to output')
    parser.add_argument('-l', '--length', action='store_true', help='Add length to output')
    parser.add_argument('-m', '--mirror_index', action='store_true', help='Add mirror index to output')
    parser.add_argument('-ms', '--model_space', action='store_true', help='Add model space to output')
    parser.add_argument('-d', '--double_size', action='store_true', help='Double the size of heirarchy')

    parser.add_argument('-rp', '--read_path', help='Path to look in, default is {}'.format(
        core_functionality.DEFAULT_DATA_PATH))
    parser.add_argument('-fp', '--file_path', help='Path to write to, default is {}'.format(
        core_functionality.DEFAULT_WRITE_PATH))
    parser.add_argument('-o', '--std_out', action='store_false', help='Turn off std out')

    args = vars(parser.parse_args())
    core = core_functionality.DataCore(file_path=args['read_path'])
    if args.pop('double_size'):
        core.double_size()
    core.communicate(**args)



if __name__ == '__main__':
    main()
