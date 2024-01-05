from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceTests(APITestCase):
    def setUp(self):
        self.invoice_data = {'date': '2022-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Item', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
    
    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
    
    def test_retrieve_invoice(self):
        response = self.client.get(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], self.invoice_data['customer_name'])
    
    def test_update_invoice(self):
        updated_data = {'date': '2022-02-01', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/api/invoices/{self.invoice.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.date.strftime('%Y-%m-%d'), updated_data['date'])
    
    def test_delete_invoice(self):
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

class InvoiceDetailTests(APITestCase):
    def setUp(self):
        self.invoice_data = {'date': '2022-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Item', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)
    
    def test_create_invoice_detail(self):
        response = self.client.post('/api/invoices-details/', self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2)
    
    def test_retrieve_invoice_detail(self):
        response = self.client.get(f'/api/invoices-details/{self.invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.invoice_detail_data['description'])
    
    def test_update_invoice_detail(self):
        updated_data = {'description': 'Updated Item', 'quantity': 3, 'unit_price': 15.0, 'price': 45.0}
        response = self.client.put(f'/api/invoices-details/{self.invoice_detail.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice_detail.description, updated_data['description'])
    
    def test_delete_invoice_detail(self):
        response = self.client.delete(f'/api/invoices-details/{self.invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 0)
