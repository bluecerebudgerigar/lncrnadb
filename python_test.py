#!/usr/bin/env python 

from pkg_resources import WorkingSet , DistributionNotFound, VersionConflict, UnknownExtra
import os

working_set = WorkingSet()
requirements = open('requirements.txt', 'r')

for line in requirements:
    try:
        working_set.require(line)
    except DistributionNotFound:
        print "Module %s Not Installed!" % line
    except VersionConflict:
        print "Module %s Version is not correct!" % line
    except ExtractionError:
        print "Module %s Extraction error is foudn " % line
