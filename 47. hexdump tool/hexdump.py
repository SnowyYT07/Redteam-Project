import argparse
import os
import struct

def hexdump(filename, format='hex', width=16, start_offset=0, end_offset=None):
    if end_offset is None:
        end_offset = os.path.getsize(filename)
    with open(filename, 'rb') as f:
        f.seek(start_offset)
        offset = start_offset
        while offset < end_offset:
            data = f.read(min(width, end_offset - offset))
            if format == 'hex':
                hexdata = ' '.join(f'{byte:02x}' for byte in data)
                ascii = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data)
                print(f'{offset:08x}: {hexdata:<{width*3}} {ascii}')
            elif format == 'struct':
                while len(data) % 4 != 0:
                    data += b'\x00'
                values = struct.unpack(f'>{len(data)//4}I', data)
                hexdata = ' '.join(f'{value:08x}' for value in values)
                print(f'{offset:08x}: {hexdata}')
            offset += len(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hexadecimal dump - RedTeam Project - https://github.com/SnowyYT07/Redteam-Project')
    parser.add_argument('filename', help='file to hexdump')
    parser.add_argument('-f', '--format', choices=['hex', 'struct'], default='hex', help='output format (default: hex)')
    parser.add_argument('-w', '--width', type=int, default=16, help='number of bytes per line (default: 16)')
    parser.add_argument('-s', '--start', type=int, default=0, help='start offset in bytes (default: 0)')
    parser.add_argument('-e', '--end', type=int, help='end offset in bytes (default: end of file)')
    args = parser.parse_args()

    hexdump(args.filename, format=args.format, width=args.width, start_offset=args.start, end_offset=args.end)
