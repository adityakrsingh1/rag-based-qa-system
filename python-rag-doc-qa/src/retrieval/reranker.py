from typing import List, Dict

class Reranker:
    def __init__(self, scoring_function):
        self.scoring_function = scoring_function

    def rerank(self, documents: List[Dict], query_embedding) -> List[Dict]:
        scored_documents = []
        for doc in documents:
            score = self.scoring_function(doc['embedding'], query_embedding)
            scored_documents.append({'document': doc, 'score': score})

        # Sort documents by score in descending order
        scored_documents.sort(key=lambda x: x['score'], reverse=True)
        
        # Return the documents sorted by relevance
        return [item['document'] for item in scored_documents]