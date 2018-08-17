from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ramona Mello', cpf='14761210796',
                    email='ramonabritods@gmail.com', phone='21-98536-5664')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ramonabritods@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ramona Mello',
            '14761210796',
            'ramonabritods@gmail.com',
            '21-98536-5664'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
