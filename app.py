# Import classique
import uvicorn
from fastapi import FastAPI
from dao.attack_dao import AttackDao

# On instancie le webservice
app = FastAPI()

# Défintion du endpoint get /todo
@app.get("/attack")
async def get_all_attack():
    # Vous devez récupérer les attaques en base en utilisant votre DAO
    return AttackDao().find_all_attacks()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)