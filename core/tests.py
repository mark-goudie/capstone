from django.test import TestCase
from .models import Subject, Post, User, ContactSubmission
from django.urls import reverse
# Create your tests here.

from django.test import TestCase
from .models import Subject

# Test the creation of a Subject and ensure its string representation is correct.

class SubjectModelTest(TestCase):
    def setUp(self):
        Subject.objects.create(subject="Mathematics", description="Mathematics Subject")

    def test_subject_content(self):
        subject = Subject.objects.get(id=1)
        expected_object_name = f"{subject.subject}"
        self.assertEqual(expected_object_name, "Mathematics")

# Test the creation of a Post and its string representation.
         
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(username='testuser', password='12345')
        testuser.save()
        testpost = Post.objects.create(user=testuser, post="A test post")
        testpost.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_user = f"{post.user}"
        expected_post = f"{post.post}"
        self.assertEqual(expected_user, "testuser")
        self.assertEqual(expected_post, "A test post")

# Test the index view to ensure it returns a 200 status code and uses the correct template.

class IndexViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

# Test the SubjectListView to ensure it lists subjects.

class SubjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_subjects = 5
        for subject_num in range(number_of_subjects):
            Subject.objects.create(subject=f'Subject {subject_num}')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/subjects/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('subject_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/subject_list.html')

    def test_lists_all_subjects(self):
        response = self.client.get(reverse('subject_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['subjects']) == 5)
