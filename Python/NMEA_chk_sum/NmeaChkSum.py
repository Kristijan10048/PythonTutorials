#!/usr/bin/env python

import re

""" Calculate  the checksum for NMEA sentence 
    from a GPS device. An NMEA sentence comprises
    a number of comma separated fields followed by
    a checksum (in hex) after a "*". An example
    of NMEA sentence with a correct checksum (of
    0x76) is:
    
      GPGSV,3,3,10,26,37,134,00,29,25,136,00*76"
"""

def checksum(sentence):

   # Remove any newlines
    if re.search("\n$", sentence):
        sentence = sentence[:-1]

    nmeadata,cksum = re.split('\*', sentence)

    calc_cksum = 0
    for s in nmeadata:
        calc_cksum ^= ord(s)

    """ Return the nmeadata, the checksum from
        sentence, and the calculated checksum
    """
    return nmeadata, '0x'+cksum, hex(calc_cksum);

	
line = "GPGSV,3,3,20,26,37,134,00,29,25,136,00*76\n"

# Get NMEA data and checksums
data,cksum,calc_cksum = checksum(line)
 
print("NMEA data: %s"%(data));
print("NMEA chk cum: %s"%(cksum));