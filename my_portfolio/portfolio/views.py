from django.shortcuts import render

def home(request):
    return render(request, 'home.html',)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = [
    {
        'title': 'Project Information Management System (PIMS)',
        'description': 'An institutional-grade web platform built for MIIT to manage full academic project lifecycles, automations, and role-based access control workflows.',
        'technologies': ['Laravel API', 'React', 'PostgreSQL', 'Tailwind CSS', 'Git Flow'],
        'features': [
            'Role-Based Access Control (RBAC) splitting Admin, Faculty, and Students.',
            'Academic project lifecycle management from initial submission to grading.',
            'Structured RESTful API patterns with a clean separation of concerns.'
        ],
        'status': 'Deployed'
    },
    {
        'title': 'StudyFlow — Productivity SaaS Platform',
        'description': 'A multi-tenant productivity web application engineered to track study velocities, monitor active learning sessions, and manage academic tasks.',
        'technologies': ['Next.js', 'Prisma ORM', 'Supabase', 'shadcn/ui', 'Tailwind CSS'],
        'features': [
            'Serverless database management utilizing high-speed Prisma v7 queries.',
            'Real-time session tracking engines paired with data analytics graphs.',
            'Modular task tracking pipelines leveraging strong structural typed safety.'
        ],
        'status': 'Active Dev'
    },
    {
        'title': 'Cocktail Explorer',
        'description': 'A clean, responsive open-source web application engineered to browse drink recipes, query ingredient compositions, and search fluid drink guides.',
        'technologies': ['Next.js', 'Tailwind CSS', 'shadcn/ui', 'REST API'],
        'features': [
            'Real-time dynamic ingredient filtering and fluid search engines.',
            'High-speed third-party recipe data ingestion layers.',
            'Modern component designs using Radix UI accessible primitives.'
        ],
        'status': 'Open Source'
    },
    {
        'title': 'Native Note-Taking App',
        'description': 'A native Android mobile application built with modern architecture components to deliver secure, lightning-fast local data persistence.',
        'technologies': ['Kotlin', 'Jetpack Compose', 'Room DB', 'MVVM Architecture'],
        'features': [
            'Reactive local storage and state caching using SQLite and Room DB.',
            'Modern declarative user interfaces driven entirely by Jetpack Compose.',
            'Unidirectional data flows separating clean business logic via ViewModels.'
        ],
        'status': 'Android Mobile'
    }
    ]
    
    return render(request, 'projects.html', {'projects': projects})
  
def contact(request):
    return render(request, 'contact.html')