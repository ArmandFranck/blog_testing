from locust import HttpUser, task, between
import random
from faker import Faker

fake = Faker()

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Attendre entre 1 et 5 secondes entre chaque tâche

    @task(1)
    def load_index_page(self):
        """Effectuer une requête GET sur la page d'accueil"""
        self.client.get("/")

    @task(2)
    def submit_newsletter_form(self):
        """Soumettre un email au formulaire de newsletter"""
        email = fake.email()
        response = self.client.post("/is_newsletter", {"email": email})
        if response.status_code == 200:
            print(f"Successfully subscribed email: {email}")
        else:
            print(f"Failed to subscribe email: {email}")

