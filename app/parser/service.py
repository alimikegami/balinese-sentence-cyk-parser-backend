from app.parser.model import ContextFreeGrammar, CYK

def getParsingResult(sentence):
    sentence = sentence.lower()
    cfg = ContextFreeGrammar()
    parser = CYK(sentence, cfg)
    res = parser.parse()
    if res:
        return res, parser.tree
    return res, None
    