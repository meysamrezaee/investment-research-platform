import backend.services.market_data as market_data


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_fmp_endpoints_cache_for_24_hours(monkeypatch):
    calls = []
    cache = {}
    mocked_time = [0]

    def fake_get(url, params=None, timeout=None):
        calls.append((url, params, timeout))
        return FakeResponse([{"symbol": params["symbol"]}])

    monkeypatch.setattr(market_data.requests, "get", fake_get)
    monkeypatch.setattr(market_data, "_CACHE", cache)
    monkeypatch.setattr(market_data.time, "time", lambda: mocked_time[0])

    first = market_data.get_company_profile("AAPL")
    assert first["symbol"] == "AAPL"
    assert len(calls) == 1

    mocked_time[0] = 60 * 60 * 12
    second = market_data.get_company_profile("AAPL")
    assert second["symbol"] == "AAPL"
    assert len(calls) == 1

    mocked_time[0] = 24 * 60 * 60 + 1
    third = market_data.get_company_profile("AAPL")
    assert third["symbol"] == "AAPL"
    assert len(calls) == 2
