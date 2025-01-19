import api_test
# Test pour l'addition
api_test.tester_service('add_numbers', 6, 1, 2, 3)
# Test pour le message de salutation
api_test.tester_service('greet_user', 'Hello, John!', 'John', message="Hello") 
