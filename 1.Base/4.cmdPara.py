#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

print('para num :', len(sys.argv))
print('para list:', str(sys.argv))
print()
print()

# test
# python 4.cmdPara.py -h
# python 4.cmdPara.py -i inputfile -o outputfile
def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('4.cmdPara.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('4.cmdPara.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            
    print('input file：', inputfile)
    print('output file：', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])   # 过滤掉命令行中的文件名
