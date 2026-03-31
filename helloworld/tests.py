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

    def test_send_hello_get_redirects(self):
        response = self.client.get(reverse('helloworld:send_hello', args=[self.world.pk]))
        self.assertEqual(response.status_code, 302)

    def test_world_detail_not_found(self):
        response = self.client.get(reverse('helloworld:world_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)
