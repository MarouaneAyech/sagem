# test_api.py
import services

def tester_service(nom_service, resultat_attendu, *inputs, **options):
    """Test générique d'un service donné en fonction de son nom et de son résultat attendu."""
    
    # Récupérer la fonction par son nom
    service = getattr(services, nom_service)
    
    # Appeler le service avec les arguments positionnels et nommés
    try:
        result = service(*inputs, **options)
        # Vérifier que le résultat est le même que le résultat attendu
        assert result == resultat_attendu, f"Test échoué pour {nom_service}. Résultat: {result}, Attendu: {resultat_attendu}"
        print(f"Test réussi pour {nom_service}.")
    except Exception as e:
        print(f"Test échoué pour {nom_service}: {e}")

