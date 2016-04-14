from locust import HttpLocust, TaskSet, TaskSet, task

class WebsiteTasks(TaskSet):
	def on_stat(self):
		pass

	@task
	def index(self):
		self.client.get('/')


class WebsiteUser(HttpLocust):
	task_set = WebsiteTasks
	min_wait = 5000
	max_wait = 15000