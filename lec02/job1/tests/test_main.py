"""
Tests for main.py
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
from job1 import main

class MainFunctionTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    @mock.patch('job1.main.save_sales_to_local_disk')
    def test_return_400_request_body_is_empty(
            self,
            get_sales_mock: mock.MagicMock
        ):
        # Raise 400 HTTP code when no request body
        resp = self.client.post(
            '/',
            json={ },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job1.main.save_sales_to_local_disk')
    def test_return_400_date_param_missed(
            self,
            get_sales_mock: mock.MagicMock
        ):
        # Raise 400 HTTP code when no 'date' param       
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/foo/bar/',
                # no 'date' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job1.main.save_sales_to_local_disk')
    def test_return_400_raw_dir_param_missed(
            self,
            get_sales_mock: mock.MagicMock
        ):
        # Raise 400 HTTP code when no 'raw_dir' param       
        resp = self.client.post(
            '/',
            json={
                'date': '2022-08-09',
                # no 'raw_dir' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job1.main.save_sales_to_local_disk')
    def test_return_201_when_all_is_ok(
            self,
            get_sales_mock: mock.MagicMock
        ):
        # Raise 201 HTTP code when all is ok
        resp = self.client.post(
            '/',
            json={
                'date': '2022-08-09',
                'raw_dir': '/foo/bar/'
            },
        )

        self.assertEqual(201, resp.status_code)
    
    @mock.patch('job1.main.save_sales_to_local_disk')
    def test_save_sales_to_local_disk(
            self,
            save_sales_to_local_disk_mock: mock.MagicMock
        ):        
        #Test whether api.get_sales is called with proper params
       
        fake_date = '1970-01-01'
        fake_raw_dir = '/foo/bar/'
        self.client.post(
            '/',
            json={
                'date': fake_date,
                'raw_dir': fake_raw_dir,
            },
        )

        save_sales_to_local_disk_mock.assert_called_with(
            date=fake_date,
            raw_dir=fake_raw_dir,
        )