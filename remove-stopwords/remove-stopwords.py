def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    tokens=np.asarray(tokens,dtype=str)
    stopwords=np.asarray(stopwords,dtype=str)
    return tokens[~np.isin(tokens,stopwords)].tolist()
    