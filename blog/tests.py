from django.test import TestCase
from django.urls import reverse


class BlogPageTests(TestCase):
    def test_main_pages_render(self):
        for url in (reverse("starting-page"), reverse("posts-page")):
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "What I Do")
            self.assertContains(response, "SYAL Blog")

    def test_each_post_detail_renders(self):
        slugs = (
            "hike-in-the-mountains",
            "programming-is-great",
            "nature-at-its-best",
        )
        for slug in slugs:
            response = self.client.get(reverse("post-detail-page", args=[slug]))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "By SYAL")

    def test_unknown_post_uses_custom_404(self):
        response = self.client.get(
            reverse("post-detail-page", args=["missing-post"])
        )
        self.assertEqual(response.status_code, 404)
        self.assertContains(
            response,
            "We didn't find that page!",
            status_code=404,
        )
