from django.shortcuts import render

def test_upload_page(request):
    return render(request, "test_upload.html")
