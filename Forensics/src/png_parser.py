#!/usr/bin/env python

import argparse
import struct
import difflib
import binascii


def str_to_hex(s):
    return ''.join(map(lambda x: '\\x{:02x}'.format(ord(x)), s))


def crc_to_hex(c):
    c = hex(c)[2:]

    return ''.join(map(lambda x: '\\x{}'.format(x), (c[2*i: 2*i + 2] for i in range(len(c) / 2))))
    return ''.join(map(lambda x: '\\x{:02x}'.format(ord(x)), s))


def get_chunk_data(png, pos):
    c_length = struct.unpack('>I', png[pos: pos + 4])[0]
    c_type = png[pos + 4: pos + 8]
    c_data = png[pos + 8: pos + 8 + c_length]
    c_crc = png[pos + 8 + c_length: pos + 8 + c_length + 4]

    c_size = 12 + c_length

    return (c_length, c_type, c_data, c_crc, c_size)


def parse_IHDR(c_data):
    width = struct.unpack('>I', c_data[:4][0])
    height = struct.unpack('>I', c_data[4:8][0])
    bit_depth = struct.unpack('>b', c_data[9:10][0])
    compression_method = struct.unpack('>b', c_data[10:11][0])
    filter_method = struct.unpack('>b', c_data[11:12][0])
    interlace_method = struct.unpack('>b', c_data[12:13][0])

    return (width, height, bit_depth, compression_method, filter_method, interlace_method)


def main():
    png = open(args.png, 'r').read()

    suggestions = []
    suggestions_level = []
    error_level = 0

    # Check file header
    png_header = map(chr, [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a])
    if png[:8] != ''.join(png_header):
        print 'Invalid file header:\n' + \
              '\t' + ' '.join(p.encode('hex') for p in png[:8]) + ', should be:\n' + \
              '\t' + ' '.join(p.encode('hex') for p in png_header)
        error_level = 4
        suggestions.append('printf "{}" | dd of={} bs=1 seek={} count={} conv=notrunc'.format(
            str_to_hex(''.join(png_header)), args.png, 0, 8))
        suggestions_level.append(4)

    print
    print 'Chunks:'

    png_valid_headres = ['PLTE', 'IDAT', 'IEND',
                         'cHRM', 'gAMA', 'iCCP', 'sBIT', 'sRGB', 'bKGD', 'hIST', 'tRNS', 'pHYs', 'sPLT', 'tIME', 'iTXt', 'tEXt', 'zTXt']
    parsed_chunks = []
    c_id = 0
    pos = 8

    print '{:<6}{:<15}{:<15}{:<6}{:<15}{:<15}{}'.format('#', 'Start', 'Length', 'type', 'crc', 'size', 'info')

    # Check chunks
    OK = True
    while OK:
        try:
            c_length, c_type, c_data, c_crc, c_size = get_chunk_data(png, pos)
        except:
            break

        c_errors = []

        if c_id == 0:  # First chunk - IHDR
            if c_type != 'IHDR':
                c_errors.append(
                    'Invalid chunk type ({}), should be "{}"'.format(c_type, 'IHDR'))
                error_level = max(error_level, 3)
                suggestions.append(
                    'printf "IHDR" | dd of={} bs=1 seek={} count={} conv=notrunc'.format(args.png, pos+4, 4))
                suggestions_level.append(3)
            if c_length != 13:
                c_errors.append(
                    'Invalid chunk length ({}), should be {}'.format(c_length, 13))
                error_level = max(error_level, 2)
        else:
            if c_type not in png_valid_headres:
                close_matches = difflib.get_close_matches(
                    c_type, png_valid_headres, cutoff=0.3)
                if close_matches != []:
                    c_errors.append('Invalid chunk type ({}), maybe you meant "{}"'.format(
                        c_type, close_matches[0]))
                    error_level = max(error_level, 3)
                    suggestions.append('printf "{}" | dd of={} bs=1 seek={} count={} conv=notrunc'.format(
                        close_matches[0], args.png, pos+4, 4))
                    suggestions_level.append(3)
                else:
                    c_errors.append('Invalid chunk type ({})'.format(c_type))

            if pos + c_length > len(png) - 12 and c_type != 'IEND':
                c_errors.append('Invalid chunk length ({}), maximum is: {}'.format(
                    c_length, len(png) - 12 - pos - 12))
                error_level = max(error_level, 2)
                suggestions.append('printf "{}" | dd of={} bs=1 seek={} count={} conv=notrunc'.format(
                    str_to_hex(struct.pack('>I', len(png) - 12 - pos - 12)),
                    args.png, pos, 4))
                suggestions_level.append(2)

        calculated_crc = binascii.crc32(c_type + c_data) % (1 << 32)
        if c_crc != '{:08x}'.format(calculated_crc).decode('hex'):
            # print '111\n', c_crc, calculated_crc, '111\n'
            c_errors.append('CRC error ({}), should be: {}'.format(
                str_to_hex(c_crc), crc_to_hex(calculated_crc)))
            error_level = max(error_level, 1)
            suggestions.append('printf "{}" | dd of={} bs=1 seek={} count={} conv=notrunc'.format(
                crc_to_hex(calculated_crc), args.png, pos + 8 + c_length, 4))
            suggestions_level.append(1)
            # print c_crc, type(c_crc)
            # print str(binascii.crc32(c_type + c_data) % (1 << 32)).decode('hex'), type(str(binascii.crc32(c_type + c_data) % (1 << 32)).decode('hex'))
            # print struct.pack('<i', binascii.crc32(c_type + c_data))
            # print crc_to_hex(binascii.crc32(c_type + c_data) % (1 << 32)), type(crc_to_hex(binascii.crc32(c_type + c_data) % (1 << 32)))

        parsed_chunks.append(c_type)

        print '{:<6}{:<15}{:<15}{:<6}{:<15}{:<15}{}'.format(c_id, pos, c_length, c_type, c_crc.encode('hex'), c_size, ' | '.join(c_errors))

        c_id += 1
        pos += min(c_size, len(png) - 12 - pos)

        if c_type == 'IEND':
            OK = False

    print
    print 'Suggestions:'
    # if error_level == 4:
    #     suggestions = filter(lambda x: 'Invalid file header' in x, suggestions)
    # elif error_level == 3:
    #     suggestions = filter(lambda x: 'Invalid chunk type' in x, suggestions)
    # elif error_level == 2:
    #     suggestions = filter(lambda x: 'Invalid chunk length' in x, suggestions)
    # elif error_level == 1:
    #     suggestions = filter(lambda x: 'CRC error' in x, suggestions)

    for i, (s, sl) in enumerate(zip(suggestions, suggestions_level)):
        if sl == error_level:
            print '{}'.format(s)

    if error_level > 1:
        print
        print 'Please run the tool again after applying the corrections'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PNG parser.')
    parser.add_argument('png', type=str, help='corrupted png file')
    parser.add_argument('-v', '--verbose',
                        action='store_true', help='add verbosity')

    args = parser.parse_args()
    print args

    main()
