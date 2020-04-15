from geekbang.core.ch12.SearchEngineBase import SearchEngineBase


class SimpleEngine(SearchEngineBase):
    def __init__(self) -> None:
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results
