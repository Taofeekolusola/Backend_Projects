from rest_framework.test import APITestCase
from rest_framework import status
from dispatch.models import Box

class BoxServiceTests(APITestCase):
    def setUp(self):
        """
        Set up initial data for testing.
        """
        self.box1 = Box.objects.create(
            txref="BOX1234567890123456",
            weight_limit=500,
            battery_capacity=50,
            state="IDLE"
        )
        self.box2 = Box.objects.create(
            txref="BOX0987654321123456",
            weight_limit=300,
            battery_capacity=20,
            state="IDLE"
        )
        self.valid_item_payload = {
            "name": "ITEM-123",
            "weight": 100,
            "code": "ITEM_12345"
        }

    def test_create_box(self):
        """
        Test the creation of a new box.
        """
        payload = {
            "txref": "BOX0000000000000001",
            "weight_limit": 450,
            "battery_capacity": 80,
            "state": "IDLE"
        }
        response = self.client.post("/api/boxes/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Box.objects.count(), 3)

    def test_load_box_items(self):
        """
        Test loading items into a box.
        """
        payload = [self.valid_item_payload]
        response = self.client.post(f"/api/boxes/{self.box1.txref}/load/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)

    def test_loading_above_weight_limit(self):
        """
        Ensure loading items above the box weight limit is not allowed.
        """
        payload = [{"name": "HeavyItem", "weight": 600, "code": "HEAVY_12345"}]
        response = self.client.post(f"/api/boxes/{self.box1.txref}/load/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Box cannot carry more than 500gr", response.data['error'])

    def test_check_loaded_items(self):
        """
        Test retrieving loaded items for a box.
        """
        self.client.post(f"/api/boxes/{self.box1.txref}/load/", [self.valid_item_payload], format="json")
        response = self.client.get(f"/api/boxes/{self.box1.txref}/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)

    def test_check_available_boxes(self):
        """
        Test retrieving boxes available for loading.
        """
        response = self.client.get("/api/boxes/available/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only box1 is above 25% battery.

    def test_check_battery_level(self):
        """
        Test retrieving battery level for a given box.
        """
        response = self.client.get(f"/api/boxes/{self.box1.txref}/battery/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['battery_capacity'], 50)
