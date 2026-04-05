from pathlib import Path

def test_hpa_exists():
    assert Path("k8s/hpa.yml").exists()
def test_locustfile_exists():
    assert Path("loadtest/locustfile.py").exists()