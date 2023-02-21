#!/bin/env python3

import argparse
import logging
import multiprocessing
import pyfiglet
import socket
from datetime import datetime
from typing import List, Tuple

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def scan_port(port: int, target: str) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            logging.info(f"\033[33mPort \033[34m{port}\033[33m is \033[32mopen\033[0m")
            return True

def scan_ports(target: str, start_port: int, end_port: int, num_threads: int) -> None:
    with multiprocessing.Pool(num_threads) as pool:
        if end_port == -1:
            end_port = 65535
        ports = range(start_port, end_port + 1)
        results = pool.starmap(scan_port, [(port, target) for port in ports])
        pool.close()
        pool.join()

def resolve_host(host: str) -> str:
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        logging.error("\033[31mHostname could not be resolved\033[0m")
        raise

def main() -> None:
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("host", help="Target host")
    parser.add_argument("-p", "--port", type=int, help="Scan only this port")
    parser.add_argument("-p-", "--end-port", type=int, default=-1, help="Scan until this port")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads to run concurrently")
    args = parser.parse_args()

    target = resolve_host(args.host)

    if args.port:
        start_port = end_port = args.port
    else:
        start_port = 1
        end_port = args.end_port

    print(pyfiglet.figlet_format("Port Scanner"))

    logging.info("-#" * 25)
    logging.info(f"\033[33mTarget: \033[34m{target}\033[0m")
    logging.info(f"\033[33mScanned at: \033[34m{datetime.now()}\033[0m")
    logging.info("#-" * 25)

    scan_ports(target, start_port, end_port, args.threads)


if __name__ == "__main__":
    main()
