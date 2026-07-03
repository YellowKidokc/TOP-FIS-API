from file_intelligence_hub.storage.db import Database
from file_intelligence_hub.storage.folder_repo import FolderRepo


def test_folder_repo_creates_nested_folders_with_generated_codes(tmp_path):
    db = Database(tmp_path / "hub.sqlite3")
    repo = FolderRepo(db.conn)

    parent = repo.create_folder(name="Projects", owner_id="david")
    child = repo.create_folder(name="Lean Proofs", parent_id=parent["id"], owner_id="david", wall="framework", wall_code=50002)
    children = repo.list_folders(parent_id=parent["id"], owner_id="david")

    assert parent["folder_code"] == 60020
    assert child["folder_code"] == 60021
    assert child["parent_id"] == parent["id"]
    assert children[0]["name"] == "Lean Proofs"


def test_folder_http_routes_create_and_list(tmp_path):
    from fastapi.testclient import TestClient

    from file_intelligence_hub.api import routes_folders
    from file_intelligence_hub.api.app import create_app

    routes_folders.DEFAULT_DB_PATH = tmp_path / "hub.sqlite3"
    client = TestClient(create_app())

    create_response = client.post("/folders", json={"name": "API Calls", "wall": "code", "wall_code": 50006})
    list_response = client.get("/folders", params={"wall": "code"})

    assert create_response.status_code == 200
    assert create_response.json()["folder"]["folder_code"] == 60020
    assert list_response.json()["folders"][0]["name"] == "API Calls"
