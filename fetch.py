import requests
import json

url = "http://api.spacex.land/graphql"

headers = {
    'Content-Type': 'application/json'
}


def fetch_missions_information():
    """
            Fetches the following information about all the missions/launches from the API:
                - the mission names
                - the ids of cores within the first stage of the rocket launched in the mission
                - the payload mass carried to space, in kgs.
        """
    payload = '{"query":"{\\r\\n  launchesPast {\\r\\n    mission_name\\r\\n    rocket {\\r\\n      rocket_name\\r\\n      first_stage {\\r\\n        cores {\\r\\n          core {\\r\\n            id\\r\\n          }\\r\\n        }\\r\\n      }\\r\\n      second_stage {\\r\\n        payloads {\\r\\n          payload_mass_kg\\r\\n        }\\r\\n      }\\r\\n    }\\r\\n  }\\r\\n}\\r\\n","variables":{}}'
    return requests.request("POST", url, headers=headers, data=payload).json()


def fetch_cores_information():
    """
        Fetches the following information about all the cores from the API:
            - the core's id
            - the names of missions where the core was used
            - the reuse count
    """
    payload = '{"query":"{\\r\\n  cores {\\r\\n    id\\r\\n    missions {\\r\\n      name\\r\\n    }\\r\\n    reuse_count\\r\\n  }\\r\\n}\\r\\n","variables":{}}'
    return requests.request("POST", url, headers=headers, data=payload).json()
