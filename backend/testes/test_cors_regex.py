import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from app.configuracao import Configuracoes

def test_cors_regex_allows_vercel_domains():
    # Setup a dummy app with the middleware configured as in principal.py
    app = FastAPI()
    
    # Simulate the configuration with the regex
    regex = r"https://.*\.vercel\.app"
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_origin_regex=regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    client = TestClient(app)
    
    # Test with a valid Vercel domain
    origin = "https://portfolio-jinnkb4tw-argenis1412s-projects.vercel.app"
    response = client.get("/", headers={"Origin": origin})
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == origin
    
    # Test with another valid Vercel domain
    origin2 = "https://any-other-random-domain.vercel.app"
    response2 = client.get("/", headers={"Origin": origin2})
    assert response2.status_code == 200
    assert response2.headers.get("access-control-allow-origin") == origin2
    
    # Test with an invalid domain
    invalid_origin = "https://hackersite.com"
    response3 = client.get("/", headers={"Origin": invalid_origin})
    assert response3.status_code == 200
    assert response3.headers.get("access-control-allow-origin") is None

def test_cors_preflight_vercel_origin():
    # Setup a dummy app with the middleware configured as in principal.py
    app = FastAPI()
    
    # Simulate the configuration with the regex
    regex = r"https://.*\.vercel\.app"
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_origin_regex=regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    @app.get("/api/v1/stack")
    def read_stack():
        return {"status": "ok"}
    
    client = TestClient(app)
    
    # Test preflight request (OPTIONS)
    origin = "https://portfolio-random-123.vercel.app"
    response = client.options(
        "/api/v1/stack",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "GET",
        },
    )
    
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == origin
    assert "GET" in response.headers.get("access-control-allow-methods", "")
