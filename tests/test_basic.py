def test_basic(client):
    response = client.get('/')
    assert b'Basic CRUD App with Python Flask' in response.data
    assert b"Nothing yet..." in response.data
    assert b'Delete' not in response.data
    assert b'Update' not in response.data


def poster(client, content: str):
    return client.post('/', data=dict(content=content), follow_redirects=True)


def deleter(client, id_: int):
    return client.get('/delete/{0}'.format(id_), follow_redirects=True)


def updater(client, id_: int, content: str):
    return client.post('/update/{0}'.format(id_),
                       data=dict(content=content), follow_redirects=True)


def test_create_task(client):
    response = poster(client, "Yolo")
    assert response.status_code == 200
    response = client.get('/')
    assert b"Yolo" in response.data
    response = deleter(client, 1)
    assert response.status_code == 200
    response = deleter(client, 1)
    assert response.status_code == 404
    response = client.get('/')
    assert b"Yolo" not in response.data


def test_update(client):
    response = poster(client, "Yolo")
    assert response.status_code == 200
    response = updater(client, 1, "Yolo_modified")
    assert response.status_code == 200
    response = client.get('/')
    assert b"Yolo_modified" in response.data
