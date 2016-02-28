#!/usr/bin/python

import internetarchive
import time

error_log = open('bpl-marcs-errors.log', 'a')

search = internetarchive.search_items('collection:bplscas')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml') change marc.xml to change the file you want like .pdf
    try:
        marc.download()
    except Exception as e:
        error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
        print "There was an error; writing to log."
    else:
        print "Downloading " + itemid + " ..."
        time.sleep(1)
