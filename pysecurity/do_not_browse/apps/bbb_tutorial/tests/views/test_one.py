import http

import bs4
from django import urls


def test_tutorial_view_returns_bad_request_for_missing_post_data(client) -> None:
    """The POST-request must include a key called `value`."""
    # GIVEN the url to the tutorial view
    tutorial_url = urls.reverse("tutorial:one")

    # WHEN a POST request is made with the key `value`
    response = client.post(tutorial_url)

    # THEN the view response with a bad request
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


def test_unmodified_value_results_in_failure_message(client) -> None:
    """An unmodified username is not the right answer!"""
    # GIVEN the url to the tutorial view
    tutorial_url = urls.reverse("tutorial:one")

    # WHEN a POST request with an unmodified value is made
    response = client.post(tutorial_url, data={"username": "sebastiaan"})

    # THEN the response is OK
    assert response.status_code == http.HTTPStatus.OK
    # AND there is a result message present on the page
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    result_message = soup.find(id="result-message")
    assert isinstance(result_message, bs4.Tag)
    # BUT the result message indicates a failure
    failure_msg = "Something went wrong, the value of username is still 'sebastiaan'."
    assert failure_msg == result_message.get_text(strip=True)


def test_modified_value_results_in_failure_message(client) -> None:
    """A modified username does result in positive feedback."""
    # GIVEN the url to the tutorial view
    tutorial_url = urls.reverse("tutorial:one")

    # WHEN a POST request with an unmodified value is made
    response = client.post(tutorial_url, data={"username": "jeremy"})

    # THEN the response is OK
    assert response.status_code == http.HTTPStatus.OK
    # AND there is a result message present on the page
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    result_message = soup.find(id="result-message")
    assert isinstance(result_message, bs4.Tag)
    # BUT the result message indicates a failure
    failure_msg = "That's right! You posted 'jeremy'."
    assert failure_msg == result_message.get_text(strip=True)
