from django.shortcuts import render


kategori_liste=["macera","romantik","dram","bilim kurgu","aksiyon"]
film_liste=["film 1","film 2","film 3"]


def home(request):
    data={
        "kategori":kategori_liste,
        "film":film_liste
    }

    return render(request,"index.html",data)

def movies(request):

    return render(request,"movies.html")