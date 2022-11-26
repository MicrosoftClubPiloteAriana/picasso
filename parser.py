import xml.etree.ElementTree as ET
from svg.path import parse_path


class PathParser:
    def __init__(self, file):
        self.tree = ET.parse(file)
        self.paths = []
        self.svg_path = None

        self.parse()

    def parse(self):
        root = self.tree.getroot()
        raw_path = root[0].get("d")
        self.svg_path = parse_path(raw_path)
