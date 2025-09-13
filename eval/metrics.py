
from typing import List, Tuple
import numpy as np
from sklearn.metrics import f1_score

def precision_at_k(relevances: List[int], k: int = 3) -> float:
    topk = relevances[:k]
    return sum(topk) / max(k, 1)

def recall_at_k(relevances: List[int], total_relevant: int, k: int = 3) -> float:
    topk = relevances[:k]
    return sum(topk) / max(total_relevant, 1)

def macro_f1(y_true, y_pred) -> float:
    return f1_score(y_true, y_pred, average="macro")
