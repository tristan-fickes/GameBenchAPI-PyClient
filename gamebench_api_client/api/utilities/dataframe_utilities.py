import pandas
from pandas.io.json import json_normalize


def to_dataframe(response_json):
    """ Create a Pandas DataFrame object from a Session response
        json.

        :param response_json: response json returned from a session
            request.
        :return: Pandas DataFrame generated by an entire session
            response json.
    """

    return pandas.DataFrame(response_json)


def session_detail_to_dataframe(metric, response_json):
    """ Creates a Pandas DataFrame for non-time-series session detail.

        The session summary object contains multiple inner dictionaries.  This method
        should be used to get one of those metrics and put the values into a DataFrame.

        :param metric: The specific dictionary needed from the response json (eg: app, device, metric).
        :param response_json: response json returned from a session
                request.
        :return: Pandas DataFrame generated by a single session request
                json dictionary.
    """

    series = pandas.Series(response_json)

    return pandas.DataFrame(
            series[metric],
            index=[metric]
    )


def json_to_normalized_dataframe(response_json):
    """ Normalizes a semi-structured JSON data into a flat table.

        This is necessary for time-series and other similarly-structured objects.

        :param response_json: Response JSON returned from session request.
        :return normalized_dataframe: Pandas DataFrame containing normalized JSON data.
    """

    normalized_dataframe = json_normalize(
            response_json,
            'samples',
            ['id', 'sessionId']
    )

    return normalized_dataframe
