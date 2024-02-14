from dataclasses import dataclass
from typing import Optional, Protocol

from cloudengine.google import GoogleAuth

QueryResult = dict[str, dict[str, list[str]]]

class Provider(Protocol):

    def find_files(self, bucket: str, query: str, max: int) -> QueryResult:
      ...

class FilterByQuery:
    def find_files(self, query: str, max_result: int) -> QueryResult:
        return {"result": {"data": ["some data"]}}

@dataclass
class ACCloud:
    region: str
    bucket_name: str
    http_auth: GoogleAuth = GoogleAuth("service_key.json")
    secure: bool = True
    find_files_method: Optional[Provider] = None
        

    def find_files(self, query: str, max_result: int) -> list[str]:
        if self.find_files_method:
            return self.find_files_method.find_files(query, max_result)['result']['data']
        return []

video_storage = ACCloud(bucket_name="video-backup.arjancodes.com", region="eu-west-1c")
video_storage.find_files('cat', 10)
