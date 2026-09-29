def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    
    chunks=[]
    step=chunk_size-overlap
    for start in range(0,len(tokens),step):
        window=tokens[start:start + chunk_size]
        chunks.append(window)
        if start + chunk_size >= len(tokens):
            break
    return chunks