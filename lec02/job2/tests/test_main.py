"""
Tests for main.py
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
from job2 import main

class MainFunctionTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    @mock.patch('job2.main.rewrite_files')
    def test_return_400_request_body_is_empty(
            self,
            rewrite_files: mock.MagicMock
        ):
        # Raise 400 HTTP code when no request body
        resp = self.client.post(
            '/',
            json={ },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job2.main.rewrite_files')
    def test_return_400_stg_dir_param_missed(
            self,
            rewrite_files: mock.MagicMock
        ):
        # Raise 400 HTTP code when no 'stg_dir' param       
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/path/to/my_dir/raw/',
                # no 'stg_dir' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job2.main.rewrite_files')
    def test_return_400_raw_dir_param_missed(
            self,
            rewrite_files: mock.MagicMock
        ):
        # Raise 400 HTTP code when no 'raw_dir' param       
        resp = self.client.post(
            '/',
            json={
                'stg_dir': '/path/to/my_dir/stg/',
                # no 'raw_dir' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('job2.main.rewrite_files')
    def test_return_201_when_all_is_ok(
            self,
            rewrite_files: mock.MagicMock
        ):
        # Raise 201 HTTP code when all is ok
        resp = self.client.post(
            '/',
            json={
                'stg_dir': '/path/to/my_dir/stg/',
                'raw_dir': '/path/to/my_dir/raw/'
            },
        )

        self.assertEqual(201, resp.status_code)

    @mock.patch('job2.main.rewrite_files')
    def test_rewrite_files_on_local_disk(
            self,
            rewrite_files_on_local_disk: mock.MagicMock
        ):        
        #Test whether rewriter_api.rewrite_files is called with proper params
       
        fake_raw_dir = '/path/to/my_dir/raw/'
        fake_stg_dir = '/path/to/my_dir/stg/'
        
        self.client.post(
            '/',
            json={
                'raw_dir': fake_raw_dir,
                'stg_dir': fake_stg_dir                
            },
        )

        rewrite_files_on_local_disk.assert_called_with(
            raw_dir=fake_raw_dir,
            stg_dir=fake_stg_dir,
        )