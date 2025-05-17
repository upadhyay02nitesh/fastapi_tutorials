from fastapi.testclient import TestClient
from Rest_API_FastAPI import app  # Replace 'your_filename' with the actual filename (without .py)

client = TestClient(app)
import logging

# Configure Logging
logging.basicConfig(
    filename="app.log",
    filemode="a",  # append mode
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Test Home

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello from FastAPI"
    print("Home test passed")

# Test GET with query parameters

def test_query_parameters():
    response = client.get("/fun", params={"emp_id": "EMP123", "name": "Test", "id": 1})
    assert response.status_code == 200
    assert "Hello from FastAPI 1,Test and EMP123" in response.text
    print("Query parameters test passed")
# Test POST /fun (add tea)

def test_add_tea():
    tea = {"id": 1, "name": "Assam", "salary": 15000.0}
    response = client.post("/fun", json=tea)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["added_record"]["name"] == "Assam"
    print("Add tea test passed")

# Test GET /data (after adding tea)

def test_get_tea():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert isinstance(response.json()["updated_record"], list)
    print("Get tea test passed")

# Test PUT /data/{id}

def test_update_tea():
    updated_tea = {"id": 1, "name": "Darjeeling", "salary": 20000.0}
    response = client.put("/data/1", json=updated_tea)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["updated_record"]["name"] == "Darjeeling"
    print("Update tea test passed")

# Test DELETE /data/{id}

def test_delete_tea():
    response = client.delete("/data/1")
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["deleted_data"]["id"] == 1
    print("Delete tea test passed")

# Test GET /data (after deletion)

def test_get_after_delete():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["data"] is None
    print("Get after delete test passed")
