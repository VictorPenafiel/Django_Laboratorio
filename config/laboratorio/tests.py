from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio 1",
            ciudad='Ciudad 1',
            pais='Pais 1'
        )

    def test_laboratorio_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio 1")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad 1")
        self.assertEqual(self.laboratorio.pais, "Pais 1")

    def test_existe_url_correcta(self):
        response = self.client.get("/laboratorio/")
        self.assertEqual(response.status_code, 200)

    def test_pagina(self):
        response = self.client.get(reverse("mostrar-lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mostrar-lab.html")
        self.assertContains(response, "Informacion de Laboratorios")