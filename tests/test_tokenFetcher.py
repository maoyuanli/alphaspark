from utils.fetch_token import TokenFetcher


class TestTokenFetcher():
    def test_fetch_token(self):
        fetcher = TokenFetcher('token.json')
        token = fetcher.fetch_token('quandl_cmhc')
        assert token[-4:] == 'jKZU'
