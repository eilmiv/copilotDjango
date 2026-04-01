from django.test import TestCase, Client
from django.urls import reverse
from .models import World


class WorldModelTest(TestCase):
    def test_create_world(self):
        world = World.objects.create(name="Earth")
        self.assertEqual(world.name, "Earth")
        self.assertEqual(world.hello_count, 0)

    def test_send_hello_increments_count(self):
        world = World.objects.create(name="Mars")
        world.send_hello()
        self.assertEqual(world.hello_count, 1)

    def test_send_hello_multiple_times(self):
        world = World.objects.create(name="Venus")
        for _ in range(5):
            world.send_hello()
        world.refresh_from_db()
        self.assertEqual(world.hello_count, 5)

    def test_world_str(self):
        world = World.objects.create(name="Jupiter")
        self.assertEqual(str(world), "Jupiter")

    def test_world_name_unique(self):
        World.objects.create(name="Saturn")
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            World.objects.create(name="Saturn")


class WorldViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.world = World.objects.create(name="Earth", hello_count=3)

    def test_world_list_view(self):
        response = self.client.get(reverse('helloworld:world_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Earth")
        self.assertContains(response, "3")

    def test_world_detail_view(self):
        response = self.client.get(reverse('helloworld:world_detail', args=[self.world.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Earth")
        self.assertContains(response, "3")

    def test_world_create_view_get(self):
        response = self.client.get(reverse('helloworld:world_create'))
        self.assertEqual(response.status_code, 200)

    def test_world_create_view_post(self):
        response = self.client.post(
            reverse('helloworld:world_create'),
            {'name': 'NewWorld'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(World.objects.filter(name='NewWorld').exists())

    def test_send_hello_view(self):
        response = self.client.post(reverse('helloworld:send_hello', args=[self.world.pk]))
        self.assertEqual(response.status_code, 302)
        self.world.refresh_from_db()
        self.assertEqual(self.world.hello_count, 4)
        self.assertIn('greeted=1', response['Location'])

    def test_send_hello_get_not_allowed(self):
        response = self.client.get(reverse('helloworld:send_hello', args=[self.world.pk]))
        self.assertEqual(response.status_code, 405)

    def test_world_detail_not_found(self):
        response = self.client.get(reverse('helloworld:world_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_world_list_contains_create_form(self):
        response = self.client.get(reverse('helloworld:world_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form method="post"')
        self.assertContains(response, 'name="name"')

    def test_world_list_inline_create_valid(self):
        response = self.client.post(
            reverse('helloworld:world_list'),
            {'name': 'InlineWorld'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(World.objects.filter(name='InlineWorld').exists())

    def test_world_list_inline_create_duplicate_shows_error(self):
        response = self.client.post(
            reverse('helloworld:world_list'),
            {'name': 'Earth'},  # already exists in setUp
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'already exists')
        self.assertEqual(World.objects.filter(name='Earth').count(), 1)

    def test_world_list_inline_create_empty_name(self):
        response = self.client.post(
            reverse('helloworld:world_list'),
            {'name': ''},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(World.objects.filter(name='').exists())
