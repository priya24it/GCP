import pytest
import requests

payload_message = 'abcd'
@pytest.fixture  
def post_request(request):  
    url = 'http://127.0.0.1:5000/incomes'
    header = {"Content-Type": "application/json"}
    data =  request.param
    response = requests.post(url=url,headers=header,data=data)
    return response.text
  
@pytest.mark.parametrize("post_request",[payload_message], indirect=True)  
def test_empty_payload(post_request):
    response = post_request
    if response == '':
        assert 1==2,"payload message is empty,hence TC has failed."
    print("response value..."+post_request)

@pytest.mark.parametrize("post_request",[payload_message], indirect=True)  
def test_populated_message(post_request):
    response = post_request
    assert response in payload_message , "Payload message and output is same hence TC has passed."
