from locust import HttpUser, task, between

class MyStreeTestUser(HttpUser):
    wait_time = between(1,2)

    @task
    def get_posts(self):
        self.client.get("/")
    