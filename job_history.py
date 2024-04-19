<!-- job_history.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job History</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <div class="container">
        <h1>Job History</h1>
        <ul>
            {% for job in job_list %}
                <li>
                    <h2>{{ job.title }}</h2>
                    <p>{{ job.description }}</p>
                    <p>Duration: {{ job.start_date }} to {{ job.end_date }}</p>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>


# views.py
from django.shortcuts import render
from .models import Job

def job_history(request):
    job_list = Job.objects.all()
    return render(request, 'job_history.html', {'job_list': job_list})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('job-history/', views.job_history, name='job_history'),
]


# models.py
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


/* styles.css */
body {
    background-color: #f5f5f5;
    color: #333;
    font-family: Arial, sans-serif;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    color: #4d2600; /* Brown color */
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 20px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 20px;
}

h2 {
    color: #4d2600; /* Brown color */
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
