from collections import defaultdict
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rubrica import Rubrica 
from appv1.models.item_rubrica import Item_rubrica

def transform_results(results):
    rubricas_dict = defaultdict(lambda: {
        'id_rubrica': None,
        'titulo': None,
        'id_etapa': None,
        'id_modalidad': None,
        'items': []
    })

    for (id_rubrica, titulo, id_etapa, id_modalidad, id_item_rubrica, item_titulo, componente, valor_max) in results:
        rubrica = rubricas_dict[id_rubrica]
        rubrica['id_rubrica'] = id_rubrica
        rubrica['titulo'] = titulo
        rubrica['id_etapa'] = id_etapa
        rubrica['id_modalidad'] = id_modalidad
        if id_item_rubrica is not None:
            rubrica['items'].append({
                'id_item_rubrica': id_item_rubrica,
                'titulo': item_titulo,
                'componente': componente,
                'valor_max': valor_max
            })

    return list(rubricas_dict.values())


def get_all_rubricas(db: Session):
    try:
        return  db.query(Rubrica).all()
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)

