class UrlNotValidException(Exception):
    def __init__(self) -> None:
        super().__init__("The provided URL is not valid.")