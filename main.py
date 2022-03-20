#!/usr/bin/python3.8
import sys
import select
from time import sleep
import tkinter as tk

if __name__ == '__main__':
    while True:
        sys.stdout.write(f"{sys.argv[1]}\n")
        sleep(5)
        if select.select([sys.stdin, ], [], [], 0.0)[0]:
            print("Have data!")
            for line in sys.stdin:
                sys.stderr.write(f"reception de {line} dans {sys.argv[1]}")
                break
        else:
            sys.stderr.write(f"No Data dans {sys.argv[1]} \n")

        sys.stdout.write(f"\n")