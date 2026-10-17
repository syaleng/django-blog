from datetime import date

from django.shortcuts import render


POSTS = [
    {
        "slug": "hike-in-the-mountains",
        "image": "blog/images/mountains.png",
        "author": "SYAL",
        "date": date(2026, 10, 15),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking in the mountains!",
        "content": [
            "The trail climbed steadily above the valley until the entire mountain range opened up in front of me. The clear sky and snow-covered peaks made every step worthwhile.",
            "Hiking teaches patience. You cannot rush a steep path, but every pause gives you another chance to enjoy the view and appreciate how far you have come.",
            "I returned tired, happy, and already planning the next trip. The mountains always leave me with a new story to share.",
        ],
    },
    {
        "slug": "programming-is-great",
        "image": "blog/images/programming.png",
        "author": "SYAL",
        "date": date(2026, 10, 12),
        "title": "Programming Is Great!",
        "excerpt": "Solving one stubborn error can teach you more than hours of reading.",
        "content": [
            "Programming is a mix of creativity, logic, and persistence. A small idea can grow into a useful website when it is divided into clear, manageable steps.",
            "Errors are part of the process. Each bug is a clue that helps us understand the code more deeply and improve the way we solve problems.",
            "The best moment is seeing everything work after careful testing. That feeling makes the difficult parts worth it.",
        ],
    },
    {
        "slug": "nature-at-its-best",
        "image": "blog/images/nature.png",
        "author": "SYAL",
        "date": date(2026, 10, 8),
        "title": "Nature at Its Best",
        "excerpt": "A quiet walk through the forest can reset your whole day.",
        "content": [
            "The forest was bright with morning light, and the narrow trail disappeared between tall trees and green ferns.",
            "Away from traffic and screens, even the smallest sounds became noticeable: moving leaves, distant birds, and footsteps on the path.",
            "Nature offers a simple reminder to slow down, breathe, and pay attention to the world around us.",
        ],
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    latest_posts = sorted(POSTS, key=get_date, reverse=True)[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    sorted_posts = sorted(POSTS, key=get_date, reverse=True)
    return render(request, "blog/all-posts.html", {"posts": sorted_posts})


def post_detail(request, slug):
    post = next((post for post in POSTS if post["slug"] == slug), None)
    if post is None:
        return render(request, "404.html", status=404)
    return render(request, "blog/post-detail.html", {"post": post})


def error_404(request, exception):
    return render(request, "404.html", status=404)
