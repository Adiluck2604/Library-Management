from django.shortcuts import render, redirect
from .forms import EnquiryForm, EnquiryModelForm
from rest_framework.decorators import api_view
from .serializers import EnquiryModelSerializer
from rest_framework.response import Response
from .models import Enquiry


def home(request):
    ctx = {}

    if request.method == "POST":
        # form = EnquiryForm(data=request.POST)
        form = EnquiryModelForm(data=request.POST)
        if form.is_valid():
            # print(form.data)
            form.save()
            return redirect("pages:home")
    else:
        # form = EnquiryForm()
        form = EnquiryModelForm()

    ctx["form"] = form
    return render(request, "pages/home.html", context=ctx)


@api_view(["GET", "POST"])
def enquiries_api(request):
    if request.method == "POST":
        serializer = EnquiryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    else:
        enquiries = Enquiry.objects.all()
        serializer = EnquiryModelSerializer(instance=enquiries, many=True)
        return Response(data=serializer.data)
