#!/usr/bin/python

import sys
import os
import struct
from binascii import hexlify

def process_1x_database(data, databaseName, maxInlineSize=1024):
    index = 8
    algorithm = -1

    encFlag = struct.unpack("<L", data[index:index+4])[0]
    index += 4
    if (encFlag & 2 == 2): algorithm = 0
    elif (enc_flag & 8): algorithm = 1
    else:
        print "Unsupported file encryption!"
        return

    version = hexlify(data[index:index+4])
    index += 4
    
    finalRandomseed = hexlify(data[index:index+16])
    index += 16

    encIV = hexlify(data[index:index+16])
    index += 16
    
    numGroups = struct.unpack("<L", data[index:index+4])[0]
    index += 4
    numEntries = struct.unpack("<L", data[index:index+4])[0]
    index += 4

    contentsHash = hexlify(data[index:index+32])
    index += 32

    transfRandomseed = hexlify(data[index:index+32])
    index += 32

    keyTransfRounds = struct.unpack("<L", data[index:index+4])[0]

    filesize = len(data)
    datasize = filesize - 124

    if((filesize + datasize) < maxInlineSize):
        dataBuffer = hexlify(data[124:])
        end = "*1*%ld*%s" %(datasize, hexlify(dataBuffer))
    else:
        end = "0*%s" %(databaseName)

    return "%s:$keepass$*1*%s*%s*%s*%s*%s*%s*%s" %(databaseName, keyTransfRounds, algorithm, finalRandomseed, transfRandomseed, encIV, contentsHash, end)


def process_2x_database(data, databaseName):

    index = 12
    endReached = False
    masterSeed = ''
    transformSeed = ''
    transformRounds = 0
    initializationVectors = ''
    expectedStartBytes = ''

    while endReached == False:

        btFieldID = struct.unpack("B", data[index])[0]
        index += 1
        uSize = struct.unpack("H", data[index:index+2])[0]
        index += 2
        # print "btFieldID : %s , uSize : %s" %(btFieldID, uSize)
        
        if btFieldID == 0:
            endReached = True

        if btFieldID == 4:
            masterSeed = hexlify(data[index:index+uSize])

        if btFieldID == 5:
            transformSeed = hexlify(data[index:index+uSize])

        if btFieldID == 6:
            transformRounds = struct.unpack("H", data[index:index+2])[0]

        if btFieldID == 7:
            initializationVectors = hexlify(data[index:index+uSize])

        if btFieldID == 9:
            expectedStartBytes = hexlify(data[index:index+uSize])

        index += uSize

    dataStartOffset = index
    firstEncryptedBytes = hexlify(data[index:index+32])

    return "%s:$keepass$*2*%s*%s*%s*%s*%s*%s*%s" %(databaseName, transformRounds, dataStartOffset, masterSeed, transformSeed, initializationVectors, expectedStartBytes, firstEncryptedBytes)


def process_database(filename):

    f = open(filename, 'rb')
    data = f.read()
    f.close()

    base = os.path.basename(filename)
    databaseName = os.path.splitext(base)[0]

    fileSignature = hexlify(data[0:8])

    if(fileSignature == '03d9a29a67fb4bb5'):
        # "2.X"
        print process_2x_database(data, databaseName)

    elif(fileSignature == '03d9a29a66fb4bb5'):
        # "2.X pre release"
        print process_2x_database(data, databaseName)

    elif(fileSignature == '03d9a29a65fb4bb5'):
        # "1.X"
        print process_1x_database(data, databaseName)
    else:
        print "ERROR: KeePass signaure unrecognized"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <kdb[x] file[s]>\n" % sys.argv[0])
        sys.exit(-1)

    for i in range(1, len(sys.argv)):
        process_database(sys.argv[i])
