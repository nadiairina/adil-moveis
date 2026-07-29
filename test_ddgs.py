from duckduckgo_search import DDGS

ddgs = DDGS()
results = ddgs.images("Sofá Trevor Lourini", max_results=1)
if results:
    print(results[0]['image'])
else:
    print("No results found.")
