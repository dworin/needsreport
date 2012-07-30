# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from needs.models import Need

def index(request):
	
	latest_needs_list = Need.objects.all().order_by('-pub_date')[:5]
	output = ', '.join([n.needtext for n in latest_needs_list])
	return HttpResponse(output)

def detail(request, need_id):
	return HttpResponse("You're looking at need %s" % need_id)