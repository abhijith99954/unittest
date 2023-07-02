import unittest
import urllib.request

class WebsiteLoadingTest(unittest.TestCase):
    def test_website_loading(self):
        url = "https://atg.world"

        try:
            response = urllib.request.urlopen(url)
            status_code = response.getcode()
            
            # Print a log statement indicating the status code
            print(f"Status code: {status_code}")

            # Check if the website loads successfully (status code 200)
            self.assertEqual(status_code, 200, "Website failed to load properly")

        except Exception as e:
            # Print the exception if the website fails to load
            print(f"Exception occurred: {e}")
            self.fail("Website failed to load")

if __name__ == '__main__':
    unittest.main()

