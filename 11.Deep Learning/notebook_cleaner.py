import json

with open("c:/Users/qasad/Documents/1.Datasayns va su_niy intelekt/11.Deep Learning/1.Tayyorgarlik koʻrish.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open("clean_notebook.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)
