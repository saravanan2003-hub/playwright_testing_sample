from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    request_context = p.request.new_context()
    
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/2")

    assert response.ok, "GET Request Failed"
    
    if response.status == 200 :
        print(response.json())
    else:
        print("Failed to fetch data")
        
        
with sync_playwright() as p:
    request_context = p.request.new_context()
    
    response = request_context.post("https://jsonplaceholder.typicode.com/posts",
        data = {
            "title": "Playwright Test",
            "body": "Learning API testing",
            "userId": 99
        }                          
    )
    
    assert response.status == 201 , "POST methed failed"
    
    if response.status == 201:
        data = response.json()
        print(data)
    else:
        print("Post Method Failed")
        
        

user = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})


with sync_playwright() as p:
    request_context = p.request.new_context()

    response = request_context.post(
        "https://reqres.in/api/login",
        data = user,
        headers={
            "Content-Type": "application/json"
        }
    )

    print("Status code:", response.status)
    print("Response body:", response.json())
    
    assert response.status == 200, "Login failed"
    assert "token" in response.json()

    request_context.dispose()
