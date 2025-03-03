from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Boutique(BaseModel):
    nom: str
    ventes: int
    revenu: float
    produits: int

boutiques = [
    {"nom": "Boutique A", "ventes": 120, "revenu": 4500.50, "produits": 30},
    {"nom": "Boutique B", "ventes": 200, "revenu": 8200.75, "produits": 50},
]

@app.get("/")
def lire_root():
    return {"message": "Bienvenue sur le Dashboard E-commerce IA"}

@app.get("/boutiques")
def lire_boutiques():
    return boutiques

@app.get("/stats")
def statistiques():
    total_ventes = sum(b["ventes"] for b in boutiques)
    total_revenu = sum(b["revenu"] for b in boutiques)
    total_produits = sum(b["produits"] for b in boutiques)
    return {"total_ventes": total_ventes, "total_revenu": total_revenu, "total_produits": total_produits}
