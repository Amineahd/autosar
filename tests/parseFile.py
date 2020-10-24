import os, sys
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, mod_path)
import autosar
import xml.etree.cElementTree as ElementTree

xmlRoot = ElementTree.parse("EcuExtract.arxml")

(major, minor, patch, release, schema) = autosar.base.parseAutosarVersionAndSchema(xmlRoot)
