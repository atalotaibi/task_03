from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
            {
                "restaurant_name" : 'McDonalds',
                "food_type": 'Fast Food'
            },
            {
                "restaurant_name" : 'Tarib',
                "food_type": 'Traditional'
            },
            {
                "restaurant_name" : 'Red Lobstor',
                "food_type": 'Sea Food'
            }
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object" : {
            "restaurant_name" : 'Tarib',
            "food_type": 'Traditional',
            "created_on": 'Yesterday',
            "last_updated_on": 'Today',
            "author": 'Me and Me'
        }

    }
    return render(request, 'detail.html', context)
