from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from galeria.models import Fotografia


class IndexViewTests(TestCase):
    def test_exibe_categoria_da_fotografia(self):
        Fotografia.objects.create(
            nome='Nebulosa de teste',
            legenda='Legenda de teste',
            categoria='NEBULOSA',
            descricao='Descricao de teste',
            foto='nebulosa.png',
            publicada=True,
            data_fotografia=timezone.now(),
        )

        response = self.client.get(reverse('index'))

        self.assertContains(
            response,
            '<span class="card__tag">Nebulosa</span>',
            html=True,
        )

    def test_exibe_imagem_padrao_quando_foto_esta_vazia(self):
        Fotografia.objects.create(
            nome='Foto sem arquivo',
            legenda='Legenda de teste',
            categoria='GALAXIA',
            descricao='Descricao de teste',
            foto='',
            publicada=True,
            data_fotografia=timezone.now(),
        )

        response = self.client.get(reverse('index'))

        self.assertContains(
            response,
            'src="/static/assets/imagens/galeria/not-found.png"',
        )


class ImagemViewTests(TestCase):
    def test_exibe_imagem_padrao_quando_foto_esta_vazia(self):
        fotografia = Fotografia.objects.create(
            nome='Foto sem arquivo',
            legenda='Legenda de teste',
            categoria='GALAXIA',
            descricao='Descricao de teste',
            foto='',
            publicada=True,
            data_fotografia=timezone.now(),
        )

        response = self.client.get(reverse('imagem', args=[fotografia.pk]))

        self.assertContains(
            response,
            'src="/static/assets/imagens/galeria/not-found.png"',
        )
        self.assertEqual(response.content.count(b'not-found.png'), 1)
