#!/usr/bin/env python
# Calculate the PG ID from the object hash
# vimal@redhat.com
import sys

def pg_id_calc(*args):
    if any([len(args) == 0, len(args) > 3, len(args) < 3]):
        help()
    else:
        hash_hex = args[0]
        pg_num = int(args[1])
        pool_id = int(args[2])
        hash_dec = int(hash_hex, 16)
        id_dec = hash_dec % pg_num
        id = hex(id_dec)
        pg_id = str(pool_id) + "." + str(id)[2:]
        print("\nThe PG ID is %s\n" % pg_id)

def help():
    print("Usage:")
    print(
        "This script expects the hash (in Hex), pg_num of the pool, and the pool id as arguments, in order")
    print("\nExample:")
    print("./pg_id_calc.py 0x8e2fe5d7 2048 12")
    sys.exit()


if __name__ == '__main__':
    pg_id_calc(*sys.argv[1:])
