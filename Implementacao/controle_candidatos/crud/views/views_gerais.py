from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def pag_princ(request):
	return render(request,'crud/principal.html')
