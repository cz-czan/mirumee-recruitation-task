import unittest as ut
from unittest import mock as mck
import json
import requests
import os
import sys

# The line below is a hack so that i can import fetch from the parent directory, then i change the working directory to
# that as well, so that the query files can be accessed with the same path as in the module
sys.path.insert(1, os.path.join(sys.path[0], '..'))
os.chdir("..")
import fetch




class FetchTest(ut.TestCase):
    def test_cores_fetch_json(self):
        """
            Makes sure the API returns a valid JSON response and ensures the response has proper structure.
        """
        try:
            json_response = fetch.fetch_cores_information()
        except json.decoder.JSONDecodeError:
            self.fail("SpaceX API fails to respond to the cores query with a valid JSON response")
        except:
            pass

    def test_cores_json_structure(self):
        try:
            json_response = fetch.fetch_cores_information()
            self.assertTrue(type(json_response["data"]) == dict)
            self.assertTrue(type(json_response["data"]["cores"]) == list)
            for core in json_response["data"]["cores"]:
                self.assertTrue(type(core["id"]) == str)
                self.assertTrue(type(core["reuse_count"]) == int)
        except KeyError:
            self.fail("SpaceX API's JSON response has unexpected structure.")

    def test_cores_count(self):
        cores1 = fetch.fetch_cores_information(3)["data"]["cores"]
        cores2 = fetch.fetch_cores_information(0)["data"]["cores"]
        cores3 = fetch.fetch_cores_information(-1)["data"]["cores"]

        self.assertEqual(len(cores1), 3)
        self.assertGreater(len(cores2), 0)
        self.assertEqual(len(cores2), len(cores3))

    def test_missions_fetch_json(self):
        """
            Makes sure the API returns a valid JSON response and ensures the response has proper structure.
        """
        try:
            json_response = fetch.fetch_missions_information()
        except json.decoder.JSONDecodeError:
            self.fail("SpaceX API fails to respond to the cores query with a valid JSON response")
        except:
            pass

    def test_missions_json_structure_and_content(self):
        """
            Ensures the json response has expected structure and content
        """
        try:
            json_response = fetch.fetch_missions_information()
            for mission in json_response:
                self.assertTrue(type(mission["mission_name"]) == str)
                self.assertTrue(type(mission["rocket"]) == dict)
                self.assertTrue(type(mission["rocket"]["first_stage"]) == dict)
                self.assertTrue(type(mission["rocket"]["first_stage"]["cores"]) == list)
                if mission["rocket"]["first_stage"]["cores"]:
                    for core in mission["rocket"]["first_stage"]["cores"]:
                        self.assertTrue(type(core) == dict)
                        self.assertTrue(type(core["core"]) == dict or core["core"] is None)
                        self.assertTrue(type(core["core"]["id"]) == str)
                self.assertTrue(type(mission["rocket"]["second_stage"]) == dict)
                self.assertTrue(type(mission["rocket"]["second_stage"]["payloads"]) == list)
                for payload in mission["rocket"]["second_stage"]["payloads"]:
                    self.assertTrue(type(payload) == dict)
                    self.assertTrue(type(payload["payload_mass_kg"]) == int or payload["payload_mass_kg"] is None)

        except KeyError:
            self.fail("SpaceX API's JSON response has unexpected structure.")
        except:
            pass

    def test_missions_upcoming_fetch_json(self):
        """
            Makes sure the API returns a valid JSON response and ensures the response has proper structure.
        """
        try:
            json_response = fetch.fetch_missions_information(upcoming=True)
        except json.decoder.JSONDecodeError:
            self.fail("SpaceX API fails to respond to the cores query with a valid JSON response")
        except:
            pass

    def test_missions_upcoming_json_structure_and_content(self):
        """
            Ensures the json response fetched by fetch.fetch_missions_information has expected structure and content
        """
        try:
            json_response = fetch.fetch_missions_information(upcoming=True)
            for mission in json_response:
                self.assertTrue(type(mission["mission_name"]) == str)
                self.assertTrue(type(mission["rocket"]) == dict)
                self.assertTrue(type(mission["rocket"]["first_stage"]) == dict)
                self.assertTrue(type(mission["rocket"]["first_stage"]["cores"]) == list)
                if mission["rocket"]["first_stage"]["cores"]:
                    for core in mission["rocket"]["first_stage"]["cores"]:
                        self.assertTrue(type(core) == dict)
                        self.assertTrue(type(core["core"]) == dict or core["core"] is None)
                        self.assertTrue(type(core["core"]["id"]) == str)
                self.assertTrue(type(mission["rocket"]["second_stage"]) == dict)
                self.assertTrue(type(mission["rocket"]["second_stage"]["payloads"]) == list)
                for payload in mission["rocket"]["second_stage"]["payloads"]:
                    self.assertTrue(type(payload) == dict)
                    self.assertTrue(type(payload["payload_mass_kg"]) == int or payload["payload_mass_kg"] is None)

        except KeyError:
            self.fail("SpaceX API's JSON response has unexpected structure.")
        except:
            pass




if __name__ == '__main__':
    ut.main()