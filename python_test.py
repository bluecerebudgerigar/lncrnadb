#!/usr/bin/env python 

from pkg_resources import WorkingSet , DistributionNotFound, VersionConflict, UnknownExtra, ExtractionError
import os

working_set = WorkingSet()
requirements = open('requirements.txt', 'r')

for line in requirements:
    try:
        working_set.require(line)
    except DistributionNotFound:
        print "Module %s Not Installed!" % line
        next
    except VersionConflict:
        print "Module %s Version is not correct!" % line
        next
    except ExtractionError:
        print "Module %s Extraction error is foudn " % line
        next
    print "Module %s is installed" % line.strip()
