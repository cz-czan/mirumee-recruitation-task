import fetch as f


def get_full_core_information(fetch_count :int, unsuccessful :bool, planned :bool):
    """
        Crosses/links information fetched by fetch.fetch_cores_information() and fetch.fetch_missions_information() so that we achieve the
        following information about all cores:
            - the core's id
            - it's reuse count
            - the total mass of the payloads it carried to space in all missions it took part in ( in the first stage ).
    """
    # As of right now i've got 0 idea how to use the "order:" option in the GraphQL query for this API, so i'm leaving
    # the implementation of the fetch_count parameter for later. Will implement unsuccessful/planned launches inclusion
    # once core functionality is working.

    missions_information = f.fetch_missions_information()
    cores_information = f.fetch_cores_information()
