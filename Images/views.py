from django.shortcuts import render

# Create your views here.
def image_gallery(request):
    galleries = (
        {id: 1, 'img_title': 'Django', 'img_desc': 'Some quick example text to build on the card title and make', 'img_url': 'img/gallery.jpg'},
        {id: 2, 'img_title': 'Python', 'img_desc': 'Some quick example text to build on the card title and make', 'img_url': 'img/lilly.jpg'},
        {id: 3, 'img_title': 'Php', 'img_desc': 'Some quick example text to build on the card title and make', 'img_url': 'img/bug.jpg'},
        {id: 4, 'img_title': 'JavaScript', 'img_desc': 'Some quick example text to build on the card title and make', 'img_url': 'img/butterfly.jpg'},
        {id: 5, 'img_title': 'HTML', 'img_desc': 'Some quick example text to build on the card title and make', 'img_url': 'img/chair.jpeg'}
    )
    return render(request, 'list.html', {'galleries': galleries})
    
def new(request):
    return render(request, 'new.html')


def comments(request, id):
    
    galleriesid = {
        id: 1,
        'comments': [
            {id: 1, 'name': 'he', 'comment': "test"},
            {id: 2, 'name': 'he', 'comment': "test"}
        ]
    }
    return render(request, "comments.html",{'galleriesid': galleriesid})
