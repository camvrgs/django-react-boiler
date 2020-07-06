# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	project_name = '{{ cookiecutter.project_name }}'
	author = '{{ cookiecutter.author }}'
	server_project_name = '{{ cookiecutter.server_project_name }}'
	server_postgres_db_name = '{{ cookiecutter.server_postgres_db_name }}'
	server_postgres_username = '{{ cookiecutter.server_postgres_username }}'
	client_project_name = '{{ cookiecutter.client_project_name }}'
	client_project_description = '{{ cookiecutter.client_project_description }}'
	client_app_style_slug = '{{ cookiecutter.client_style_slug }}'
	client_app_slug = '{{ cookiecutter.client_project_slug }}'
	date_generated = '{{ cookiecutter.date }}'

	context = {
		'project': project_name,
		'author': author,
		'date_generated': date_generated,
		'server_name': server_project_name,
		'server_db_name': server_postgres_db_name,
		'server_db_user': server_postgres_username,
		'client_name': client_project_name,
		'client_desc': client_project_description,
		'client_app_style_slug': client_app_style_slug,
		'client_app_slug': client_app_slug,
	}

	return render(request, 'index.html', context)
