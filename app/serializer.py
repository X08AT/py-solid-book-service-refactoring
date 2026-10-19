import json
import xml.etree.ElementTree as element_tree
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = element_tree.Element("book")
        title = element_tree.SubElement(root, "title")
        title.text = book.title
        content = element_tree.SubElement(root, "content")
        content.text = book.content
        return element_tree.tostring(root, encoding="unicode")
