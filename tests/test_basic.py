def test_basic(client):
    response = client.get("/")
    assert "Basic CRUD App with Python Flask" in response.text
    assert "Nothing yet..." in response.text
    assert "Delete" not in response.text
    assert "Update" not in response.text


def poster(client, content: str):
    return client.post("/", data=dict(content=content), follow_redirects=True)


def deleter(client, id_: int):
    return client.get("/delete/{0}".format(id_), follow_redirects=True)


def updater(client, id_: int, content: str):
    return client.post("/update/{0}".format(id_),
                       data=dict(content=content), follow_redirects=True)


def test_create_task(client):
    response = poster(client, "Yolo")
    assert response.status_code == 200
    response = client.get("/")
    assert "Yolo" in response.text
    response = deleter(client, 1)
    assert response.status_code == 200
    response = deleter(client, 1)
    assert response.status_code == 404
    response = client.get("/")
    assert "Yolo" not in response.text


def test_update(client):
    response = poster(client, "Yolo")
    assert response.status_code == 200
    response = updater(client, 1, "Yolo_modified")
    assert response.status_code == 200
    response = client.get("/")
    assert "Yolo_modified" in response.text
